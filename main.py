from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import os


app = FastAPI()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



class EchoItem(BaseModel):
    text: str

class SummarizeRequest(BaseModel):
    text: str

    
@app.get("/")
async def root():
    return "hello"


@app.post("/echo")
async def echo_back(item: EchoItem):
    return item.text


@app.post("/summarize")
async def summarize_text(item: SummarizeRequest):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"summarize THIS: {item.text}",
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return {"summary":chat_completion.choices[0].message.content}

    except Exception as e:  
        raise HTTPException(status_code=500, detail=f"LLM CALL FAILED: {str(e)}")



    


