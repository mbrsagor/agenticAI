import os
import certifi
import requests
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langsmith import Client


from langchain.agents import create_react_agent, AgentExecutor


# Load env variables
os.environ["SSL_CERT_FILE"] = certifi.where()
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


search_tool = TavilySearchResults(max_results=2) # max results means how many of website (link) will return.
# result = search_tool.invoke("Give me a latest news on AI")
# result

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY
)

result = llm.invoke("Tell me joke about AI")
# result.content
# print(result.content)


@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather information for a given city."""
    url = (
        f"https://api.weatherapi.com/v1/current.json?"
        f"key={WEATHER_API_KEY}&q={city}"
    )
    
    response = requests.get(url)
    data = response.json()
    
    if "current" not in data:
        return f"Could not fetch weather data for {city}"
        
    return f"Current temperature: {data['current']['temp_c']}°C"

# Corrected: Pass the tool object reference (without parentheses or arguments)
tools = [search_tool, get_weather_data]
tools


client = Client()
prompt = client.pull_prompt("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


response = agent_executor.invoke({
    "input": (
        "Find the capital of India."
        "And then find its current weather."
    )
})

print(response["output"])
