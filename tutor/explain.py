TEACHER_PERSONA = """
You are an AP Calculus AB/BC teacher.
Explain solutions concisely and step-by-step.
Emphasize conceptual understanding over memorization.
"""
def teacher_explainer(state: TutorState) -> TutorState:
    """
    Uses an LLM only after correct math is established.
    """
    prompt = (
        TEACHER_PERSONA
        + f"\n\nStudent question: {state['question']}"
        + f"\nMath result: {state['math_output']}"
        + "\nExplain clearly and concisely:"
    )
    state["explanation"] = llm.invoke(prompt).content
    return state
