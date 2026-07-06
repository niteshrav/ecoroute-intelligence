import os
from google.adk.agents import LlmAgent, SequentialAgent
from .data_engine import compute_urban_metrics


def validate_secure_bounds(target_file: str) -> str:
    """Restrict file access to the current project folder."""
    base_directory = os.getcwd()
    absolute_path = os.path.abspath(target_file)

    if not absolute_path.startswith(base_directory):
        raise PermissionError("Security violation: path escapes project folder.")

    return absolute_path


def query_community_transit_data(dataset_name: str = "urban_traffic.csv") -> dict:
    """Analyze community traffic data and return congestion and emissions metrics."""
    try:
        safe_path = validate_secure_bounds(dataset_name)
        return compute_urban_metrics(safe_path)
    except Exception as error:
        return {"status": "error", "message": str(error)}


def evaluate_antigravity_aerodynamics() -> str:
    """Return futuristic routing recommendation concept for the demo."""
    return (
        "Antigravity simulation layer enabled. "
        "For demo purposes, high-congestion routes should be converted into "
        "priority public-transit and low-emission corridors."
    )


data_analyst = LlmAgent(
    name="TransitAnalyst",
    model="gemini-2.5-flash",
    instruction="""
You are TransitAnalyst.

Always call query_community_transit_data first.
Then summarize:
- congestion bottlenecks
- estimated emissions
- most affected routes
- acceleration layer used
""",
    tools=[query_community_transit_data],
    output_key="traffic_analysis",
)


policy_director = LlmAgent(
    name="EcoRouteDirector",
    model="gemini-2.5-flash",
    instruction="""
You are EcoRouteDirector.

Use the previous traffic analysis from state key: traffic_analysis.

Create clear community recommendations:
- short-term actions
- long-term policy changes
- emission reduction ideas
- public transport improvements
- final decision summary
""",
    tools=[evaluate_antigravity_aerodynamics],
    output_key="policy_recommendations",
)


root_agent = SequentialAgent(
    name="EcoRoute_Intelligence_Network",
    description="Sequential multi-agent decision intelligence system for smarter communities.",
    sub_agents=[data_analyst, policy_director],
)
