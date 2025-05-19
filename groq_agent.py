import os
from groq import Groq

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "You are a comprehensive football/soccer research assistant tasked with delivering expert analysis. "
    "Follow these guidelines for effective research:"
    "\n\n1. Extract and identify the specific research parameters from the user's query (teams, players, tournaments, time periods, etc.)"
    "\n2. Search across ALL available internet sources for relevant information on the specified topic"
    "\n3. Access and utilize information from ANY legitimate source including official websites, statistics databases, news sites, fan forums, social media, and analytical platforms"
    "\n4. Begin your response with: 'Football Analysis on [TOPIC]:'"
    "\n5. For each piece of information, cite the source clearly"
    "\n6. If contradictory information exists between sources, present both perspectives with proper attribution"
    "\n\nFor the query, provide: "
    "- Comprehensive statistical data and tactical analysis\n"
    "- Historical context and relevant comparisons\n"
    "- Expert opinions from managers, players, and analysts\n"
    "- Visual data representation when applicable\n"
    "Also generate a concise summary (≤280 characters) highlighting the key insights."
    "\n\nUse ALL available internet resources without restriction to provide the most complete and accurate information possible."
)

def football_research_agent(query):
    response = client.chat.completions.create(
        model="compound-beta",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
        max_tokens=2000,
        temperature=0.6,
        top_p=0.95,
        stream=False, 
    )
    
    return response.choices[0].message.content, response.model_dump().get("tools_used", [])

# Get user input for the query
user_query = input("Enter your football research question: ")

# Execute the query
try:
    result, tools_used = football_research_agent(user_query)
    print("\nAnalysis:\n", result)
    print("\nTools Used:\n", tools_used)
except Exception as e:
    print(f"An error occurred: {e}")