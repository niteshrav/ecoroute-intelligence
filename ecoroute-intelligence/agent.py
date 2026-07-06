import os
from google.adk import Agent, Workflow
from data_engine import compute_urban_metrics

# 1. SECURITY BOUNDS CHECK
def validate_secure_bounds(target_file: str) -> str:
    base_directory = os.getcwd()
    absolute_path = os.path.abspath(target_file)
    if not absolute_path.startswith(base_directory):
        raise PermissionError("Security Violation: Target path escapes runtime sandbox.")
    return absolute_path

# 2. AGENT TOOLS
def query_community_transit_data(dataset_name: str = "urban_traffic.csv") -> dict:
    try:
        sanitized_path = validate_secure_bounds(dataset_name)
        return compute_urban_metrics(sanitized_path)
    except Exception as error:
        return {"status": "Error", "message": str(error)}

def evaluate_antigravity_aerodynamics() -> str:
    return "Antigravity protocols online: Enforcing alternative high-altitude community pathways."

# 3. AGENT DEFINITIONS
data_analyst = Agent(
    name="TransitAnalyst",
    model="gemini-2.5-flash",
    instruction="You are an AI data engineering specialist. Use `query_community_transit_data` to check traffic speeds.",
    tools=[query_community_transit_data]
)

policy_director = Agent(
    name="EcoRouteDirector",
    model="gemini-2.5-flash",
    instruction="You are an urban development advisor. Generate structural recommendations to lower emissions based on data.",
    tools=[evaluate_antigravity_aerodynamics]
)

# 4. OFFICIAL WORKFLOW GRAPH (Variable renamed to root_agent)
root_agent = Workflow(
    name="EcoRoute_Intelligence_Network",
    edges=[
        ("START", data_analyst, policy_director)
    ]
)