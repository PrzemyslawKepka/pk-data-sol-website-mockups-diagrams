"""
Generate diagrams for the Streamlit to Flask migration blog post.
Uses graphviz for flowchart generation.

Usage:
    python generate_diagrams.py

Output:
    - traditional_vs_streamlit.png
    - streamlit_rerun_cycle.png
    - tech_stack_decision.png
"""

from graphviz import Digraph


def create_traditional_vs_streamlit():
    """Diagram 1: Traditional web dev vs Streamlit architecture"""

    dot = Digraph("traditional_vs_streamlit", format="png")
    dot.attr(rankdir="TB", bgcolor="white", pad="0.5")
    dot.attr(
        "node", shape="box", style="rounded,filled", fontname="Arial", fontsize="12"
    )
    dot.attr("edge", fontname="Arial", fontsize="10")

    # Traditional web dev subgraph
    with dot.subgraph(name="cluster_traditional") as c:
        c.attr(
            label="Traditional Web Development",
            style="rounded",
            bgcolor="#f0f4f8",
            fontname="Arial",
            fontsize="14",
        )
        c.node(
            "backend",
            "Backend\n(Python, Java, etc.)",
            fillcolor="#4a90a4",
            fontcolor="white",
        )
        c.node(
            "frontend",
            "Frontend\n(HTML, CSS, JS)",
            fillcolor="#e07b53",
            fontcolor="white",
        )
        c.edge("backend", "frontend", dir="both", color="#333333", penwidth="2")

    # Streamlit subgraph
    with dot.subgraph(name="cluster_streamlit") as c:
        c.attr(
            label="Streamlit",
            style="rounded",
            bgcolor="#f0f8f0",
            fontname="Arial",
            fontsize="14",
        )
        c.node("python", "Python\nCode", fillcolor="#4a90a4", fontcolor="white")
        c.node(
            "abstraction",
            "Streamlit\nAbstraction",
            fillcolor="#7c5caf",
            fontcolor="white",
        )
        c.node("webapp", "Web App", fillcolor="#5cb85c", fontcolor="white")
        c.edge("python", "abstraction", color="#333333", penwidth="2")
        c.edge("abstraction", "webapp", color="#333333", penwidth="2")

    # Force vertical layout
    dot.edge("frontend", "python", style="invis")

    dot.render("traditional_vs_streamlit", cleanup=True)
    print("Created: traditional_vs_streamlit.png")


def create_rerun_cycle():
    """Diagram 2: Streamlit re-run cycle"""

    dot = Digraph("streamlit_rerun_cycle", format="png")
    dot.attr(rankdir="LR", bgcolor="white", pad="0.5")
    dot.attr(
        "node", shape="box", style="rounded,filled", fontname="Arial", fontsize="12"
    )
    dot.attr("edge", fontname="Arial", fontsize="10")

    # Nodes
    dot.node("user", "User\ninteraction", fillcolor="#5cb85c", fontcolor="white")
    dot.node("rerun", "Full script\nre-runs", fillcolor="#f0ad4e", fontcolor="white")
    dot.node(
        "cached",
        "Cache/State?",
        shape="diamond",
        fillcolor="#d9edf7",
        fontcolor="#31708f",
    )
    dot.node("reload", "Data\nreloads", fillcolor="#d9534f", fontcolor="white")
    dot.node("skip", "Skip\nreload", fillcolor="#5cb85c", fontcolor="white")
    dot.node("ui", "UI\nrebuilds", fillcolor="#5bc0de", fontcolor="white")

    # Edges
    dot.edge("user", "rerun", penwidth="2", color="#333333")
    dot.edge("rerun", "cached", penwidth="2", color="#333333")
    dot.edge("cached", "reload", label="No", penwidth="2", color="#d9534f")
    dot.edge("cached", "skip", label="Yes", penwidth="2", color="#5cb85c")
    dot.edge("reload", "ui", penwidth="2", color="#333333")
    dot.edge("skip", "ui", penwidth="2", color="#333333")
    dot.edge("ui", "user", style="dashed", penwidth="2", color="#999999")

    dot.render("streamlit_rerun_cycle", cleanup=True)
    print("Created: streamlit_rerun_cycle.png")


def create_tech_stack_decision():
    """Diagram 3: Tech stack decision flowchart"""

    dot = Digraph("tech_stack_decision", format="png")
    dot.attr(rankdir="TB", bgcolor="white", pad="0.5")
    dot.attr(
        "node", shape="box", style="rounded,filled", fontname="Arial", fontsize="12"
    )
    dot.attr("edge", fontname="Arial", fontsize="10")

    # Decision nodes (diamonds)
    dot.node(
        "seo",
        "Need SEO +\ndynamic pages?",
        shape="diamond",
        fillcolor="#d9edf7",
        fontcolor="#31708f",
    )
    dot.node(
        "interactive",
        "High\ninteractivity?",
        shape="diamond",
        fillcolor="#d9edf7",
        fontcolor="#31708f",
    )
    dot.node(
        "complex",
        "Complex features?\n(users, auth)",
        shape="diamond",
        fillcolor="#d9edf7",
        fontcolor="#31708f",
    )

    # Outcome nodes
    dot.node(
        "streamlit", "Stay with\nStreamlit/Dash", fillcolor="#5cb85c", fontcolor="white"
    )
    dot.node("react", "React/Vue\n+ API", fillcolor="#5bc0de", fontcolor="white")
    dot.node("django", "Django", fillcolor="#f0ad4e", fontcolor="white")
    dot.node("flask", "Flask", fillcolor="#5cb85c", fontcolor="white", penwidth="3")

    # Edges
    dot.edge("seo", "streamlit", label="No", penwidth="2", color="#5cb85c")
    dot.edge("seo", "interactive", label="Yes", penwidth="2", color="#333333")
    dot.edge("interactive", "react", label="Yes", penwidth="2", color="#333333")
    dot.edge("interactive", "complex", label="No", penwidth="2", color="#333333")
    dot.edge("complex", "django", label="Yes", penwidth="2", color="#333333")
    dot.edge("complex", "flask", label="No", penwidth="2", color="#5cb85c")

    dot.render("tech_stack_decision", cleanup=True)
    print("Created: tech_stack_decision.png")


if __name__ == "__main__":
    create_traditional_vs_streamlit()
    create_rerun_cycle()
    create_tech_stack_decision()
    print("\nAll diagrams generated!")
