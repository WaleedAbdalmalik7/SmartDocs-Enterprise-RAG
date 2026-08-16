"""Query router deciding internal vs web LLMs and handlers."""


def route_query(query: str, source: str = "web"):
    # Inspect query and route accordingly
    return {"routed_to": "local"}
