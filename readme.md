
## ⚡LangChain Quick-Start Snippets

⚙️Configuration  
Copy `.env.example` to `.env` and add your keys:

```
OPENAI_API_KEY=xxxKEYxxx
LANGCHAIN_API_KEY=xxxKEYxxx
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=_projectname_
```
### 📂 Files & What They Do
| File |💡 What it does |
|------|--------------|
| `simple_message.py` | One-shot prompt → LLM → output (translate CLI demo). |
| `serve.py` | Same chain exposed as `/chain` via FastAPI & LangServe. |
| `messages_history.py` | Console chatbot that remembers the conversation. |
| `messages_history_with_streaming.py` | Same bot, but streams tokens as they arrive. |
| `vector_store_intro.py` | Load docs into Chroma and run similarity search. |
| `vector_store_intro_with_llm.py	` | Combines vector search with an LLM to answer questions using context. |
| `rag_chain_with_web_loader.py`         | Fetches content from a webpage and uses RAG (retrieval-augmented generation) to answer questions. |
