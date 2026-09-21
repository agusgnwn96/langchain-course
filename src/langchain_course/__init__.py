from dotenv import load_dotenv
# from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

information = """
Ada Lovelace (born December 10, 1815) was an English mathematician and writer
chiefly known for her work on Charles Babbage's proposed mechanical
general-purpose computer, the Analytical Engine. She was the first to
recognize that the machine had applications beyond pure calculation, and
published what is now considered the first algorithm intended to be carried
out by such a machine, earning her recognition as the first computer
programmer.
"""

summary_template = """
given the information {information} about a person, I want you to create:
1. A short summary
2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

# llm = ChatAnthropic(model="claude-sonnet-5", temperature=0)
llm = ChatOllama(model="gemma3:270m", temperature=0)

chain = summary_prompt_template | llm
response = chain.invoke({"information": information})
print(response.content)

def main() -> None:
    print("Hello from langchain-course!")
