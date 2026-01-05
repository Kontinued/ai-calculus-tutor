from typing import TypedDict
class TutorState(TypedDict):
    question: str
    math_output: str
    explanation: str
    student_level: str  # "beginner", "intermediate", "advanced"
