def sympy_solver(state: TutorState) -> TutorState:
    """
    Handles calculus questions using SymPy to ensure correctness.
    LLMs are deliberately excluded from mathematical computation.
    """
    question = state["question"]
    x = sp.Symbol("x")

    def parse(expr_str: str):
        expr_str = re.sub(r"x!", "factorial(x)", expr_str)
        return sp.sympify(
            expr_str,
            locals={
                "x": x,
                "sin": sp.sin,
                "cos": sp.cos,
                "tan": sp.tan,
                "log": sp.log,
                "sqrt": sp.sqrt,
                "e": sp.E,
                "factorial": sp.factorial,
            },
        )

    # Derivatives
    match = re.search(r"derivative of (.*)", question, re.IGNORECASE)
    if match:
        expr = parse(match.group(1))
        state["math_output"] = f"Derivative: {sp.diff(expr, x)}"
        return state

    # Indefinite integrals
    match = re.search(r"integral of (.*)", question, re.IGNORECASE)
    if match:
        expr = parse(match.group(1))
        result = sp.integrate(expr, x)
        state["math_output"] = (
            f"Integral: {result} + C"
            if not isinstance(result, sp.Integral)
            else "Integral: No closed-form solution."
        )
        return state

    state["math_output"] = "Unable to parse mathematical request."
    return state
