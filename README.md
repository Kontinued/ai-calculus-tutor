# ai-calculus-tutor

This project is an AI-powered calculus tutor that explains concepts
and encourages conceptual understanding rather than straight memorization.

Large Language Models are unreliable (at best) at solving symbolic math
problems, so I separated the code into three stages:

1. Mathematical computation (SymPy)
2. Visualization (numerical evaluation and plotting)
3. Explanation (LLM based on a teacher persona)

A LangGraph graph properly integrates each step and ensures smooth user interaction.

Most AI tutors give answers that may not be correct.
My program will not explain anything until it ensures that it is correct.
