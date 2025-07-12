from fastapi import  FastAPI
from langserve import add_routes
from dotenv import  load_dotenv
from langchain_openai import ChatOpenAI
from  langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import  ChatPromptTemplate

load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

system_promt = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_promt), ("user", "{text}")]
)

parser = StrOutputParser()
chain = prompt_template | model | parser
app=FastAPI(
    title="Translate App",
    version="1.0.0"
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
