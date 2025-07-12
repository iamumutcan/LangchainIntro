from itertools import chain

from dotenv import  load_dotenv
from langchain.chains.question_answering.map_reduce_prompt import messages
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from  langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import  ChatPromptTemplate

load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

#messages=[
#    SystemMessage(content="Translate the following from Turkish to English"),
#    HumanMessage(content="Merhaba Dünya :D")
#]

system_promt = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_promt), ("user", "{text}")]
)

parser = StrOutputParser()

chain = prompt_template | model | parser


if __name__ == "__main__":
    print(chain.invoke({"language": "italian", "text": "Merhaba dünya"}))
