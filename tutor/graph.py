from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from tutor.state import TutorState
from tutor.solver import sympy_solver
from tutor.visualize import graph_plotter
from tutor.explain import teacher_persona

graph = StateGraph(TutorState)
graph.add_node("solve", sympy_solver)
graph.add_node("visualize", graph_plotter)
graph.add_node("explain", teacher_explainer)

graph.set_entry_point("solve")
graph.add_edge("solve", "visualize")
graph.add_edge("visualize", "explain")
graph.add_edge("explain", END)

app = graph.compile(checkpointer=MemorySaver())
