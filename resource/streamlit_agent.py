import os
import certifi
import requests
import streamlit as st
from dotenv import load_dotenv

from langsmith import Client
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools.tavily_search import TavilySearchResults


# Load env variables
os.environ["SSL_CERT_FILE"] = certifi.where()
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


search_tool = TavilySearchResults(max_results=2) # max results means how many of website (link) will return.

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY
)

@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather information for a given city."""
    try:
        url = "https://api.weatherapi.com/v1/current.json"

        response = requests.get(
            url,
            params={
                "key": WEATHER_API_KEY,
                "q": city
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return (
            f"City: {data['location']['name']}\n"
            f"Temperature: {data['current']['temp_c']}°C\n"
            f"Condition: {data['current']['condition']['text']}"
        )

    except requests.RequestException as e:
        return f"Weather API Error: {str(e)}"

# Corrected: Pass the tool object reference (without parentheses or arguments)
tools = [search_tool, get_weather_data]


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


# Page config
st.set_page_config(
    page_title="Agentic AI Assistant",
    page_icon= "🤖",
    layout="centered"
)

st.title("Agentic AI Assistant")
st.markdown("Search + Weather AI Agent using Langchain")

# UI input
user_query = st.text_input(
    "Enter your query:",
    placeholder="Example: Find the capital of Bangladesh and current weather"
)

# Run agent
if st.button("Run Agent"):
    if user_query:
        with st.spinner("Agent is thinking..."):
            
            try:
                response = agent_executor.invoke({
                    "input": user_query
                })
                
                st.success("Response Generated")
                st.markdown("###### Final Response")
                st.write(response["output"])
            
            except Exception as ex:
                st.error(f"Error: {str(ex)}")
    else:
        st.warning("Please enter a query.")
