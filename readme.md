
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
| `simplemessage.py` | One-shot prompt → LLM → output (translate CLI demo). |
| `serve.py` | Same chain exposed as `/chain` via FastAPI & LangServe. |
| `messageshistory.py` | Console chatbot that remembers the conversation. |
| `messageshistorywithstreaming.py` | Same bot, but streams tokens as they arrive. |
| `vectorestoreintro.py` | Load docs into Chroma and run similarity search. |