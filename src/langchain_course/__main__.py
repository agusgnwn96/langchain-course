from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

# tavily = TavilyClient()


# @tool
# def search(query: str) -> dict:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-5")
# llm = ChatOllama(model="qwen3:0.6b")
# llm = ChatAnthropic(model="claude-opus-5-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")})
    print(result)


if __name__ == "__main__":
    main()
