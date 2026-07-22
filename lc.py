from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
from scraper import fetch_website_contents


prompt = ChatPromptTemplate.from_template(
    "Give a short, friendly summary of the website: \n \n {website}"
)

model = ChatOpenAI(model='gpt-4o-mini', temperature = 0.5)

parse = StrOutputParser()

chain = prompt | model | parse

def summarize(url):
    return chain.invoke({'website': fetch_website_contents(url)})

print(summarize("https://anthropic.com"))
