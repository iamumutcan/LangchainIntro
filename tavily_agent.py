from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()
model = ChatOpenAI(model="gpt-4")
search = TavilySearch(max_results=2)
tools = [search]

config = {"configurable": {"thread_id": "4a288b9d-19a9-4b41-b62c-15a30c0f466f"}}

if __name__ == "__main__":
    with SqliteSaver.from_conn_string(":memory:") as memory:
        agent_executor = create_react_agent(model, tools, checkpointer=memory)

        while True:
            user_input = input("> ")
            for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}, config
            ):
                print(chunk)
                print("-----")
