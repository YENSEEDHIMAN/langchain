#LangChain LLM Chain with PromptTemplate using Google Gemini

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
prompt_quotes = ChatPromptTemplate.from_template(
    "Give me 3 inspirational or meaningful quotes related to the word: '{word}'."
)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b",
    temperature=0.8,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

chain = prompt_quotes | llm

word = input("Enter a word to get related quotes: ")

response = chain.invoke({"word": word})
print("Quotes related to:", word)
print(response.content)
