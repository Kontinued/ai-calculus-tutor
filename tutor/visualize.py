def graph_plotter(state: TutorState) -> TutorState:
    """
    Converts symbolic expressions into numerical plots
    to support conceptual understanding.
    """
    try:
        match = re.search(r": (.*)", state["math_output"])
        if not match:
            return state

        expr = sp.sympify(match.group(1))
        x = sp.Symbol("x")
        f = sp.lambdify(x, expr, "numpy")

        X = np.linspace(-5, 5, 400)
        Y = f(X)
        Y = np.where(np.isfinite(Y), Y, np.nan)

        plt.figure(figsize=(4, 3))
        plt.plot(X, Y)
        plt.axhline(0)
        plt.axvline(0)
        plt.title("Function Visualization")
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()

        img_b64 = base64.b64encode(buf.getvalue()).decode()
        state["math_output"] += f"\n[Graph: data:image/png;base64,{img_b64}]"

    except Exception:
        pass

    return state
