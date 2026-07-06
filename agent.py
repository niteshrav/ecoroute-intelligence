from google.adk import Agent

data_analyst = Agent(
    name="TransitAnalyst",
    model="gemini-2.5-flash",
    instruction="""
    Analyze the traffic dataset.
    Always call query_community_transit_data first.
    Return structured findings.
    """,
    tools=[query_community_transit_data],
)

policy_director = Agent(
    name="EcoRouteDirector",
    model="gemini-2.5-flash",
    instruction="""
    Review TransitAnalyst findings.
    Produce policy recommendations.
    """,
    tools=[evaluate_antigravity_aerodynamics],
)

root_agent = Agent(
    name="EcoRoute_Intelligence_Network",
    model="gemini-2.5-flash",
    instruction="""
    Coordinate the specialist agents.

    First ask TransitAnalyst to analyze the data.

    Then use EcoRouteDirector to produce recommendations.

    Return the final report.
    """,
    sub_agents=[
        data_analyst,
        policy_director,
    ],
)