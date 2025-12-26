from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os

load_dotenv()

def main():
    print("Hello from langchain-course!")
    # print(os.environ.get("OPENAI_API_KEY"))
    information = """"
    Expedia Group, Inc. is an American travel technology company that owns and operates travel fare aggregators and travel metasearch engines, including Expedia, Hotels.com, Vrbo, Travelocity, Hotwire.com, Orbitz, Ebookers, CheapTickets, CarRentals.com, Expedia Cruises, Wotif, and Trivago.[1] Over 3.5 million lodging facilities and flights on over 500 airlines are bookable on the company's websites.[1] It has 16,500 employees, and its headquarters are located in Seattle, Washington.

    The word "Expedia" is derived from a combination of "exploration" and "speed".[2] The company is listed on Nasdaq under the ticker symbol EXPE.
    """
    summary_template="""
    given the infomration {information} about company I want you to create
    1. A short summary
    2. One interesting fact about it
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
        )
    
    llm = ChatOpenAI(temperature=0, model="gpt-5")
    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)

if __name__ == "__main__":
    main()
