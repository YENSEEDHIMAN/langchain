from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template("Translate to Hindi: {text}")

llm = ChatGoogleGenerativeAI(
    temperature=0.3,
    model="gemini-1.5-flash-8b",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

chain = prompt | llm

response = chain.invoke(input("Enter the text : {text} "))
print(response.content)

# User Input → Prompt Template → Final Prompt → LLM → Output

