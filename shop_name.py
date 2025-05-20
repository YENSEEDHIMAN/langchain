from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
prompt_shop_name = ChatPromptTemplate.from_template(
    "Suggest 5 creative shop names for a business selling '{product}'."
)

prompt_related_items = ChatPromptTemplate.from_template(
    "Tell me 5 related items or con0.cepts to '{product}'."
)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b",
    temperature=0.9,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

chain_shop = prompt_shop_name | llm
chain_related = prompt_related_items | llm

product = input("Enter a product name: ")

response_shop = chain_shop.invoke({"product": product})
response_related = chain_related.invoke({"product": product})

print("Suggested Shop Names:")
print(response_shop.content)

print("Related Items or Ideas:")
print(response_related.content)
