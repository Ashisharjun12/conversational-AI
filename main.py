from mem0 import Memory
from openai import OpenAI
import json



GEMINI_API_KEY="AIzaSyB1basgGEcbPEJ58AmQRuRuT1di-_iuj6g"
QDRANT_HOST="localhost"
NEO4J_URL="bolt://localhost:7687"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="reform-william-center-vibrate-press-5829"


config ={
    "version":"v1.1",
    "embedder":{
        "provider":"gemini",
        "config":{"api_key":GEMINI_API_KEY,"model":"gemini-embedding-exp-03-07"},
    },
    "llm":{"provider":"gemini","config":{"api_key":GEMINI_API_KEY,"model":"gemini-2.0-flash"}},
    "vector_store":{
        "provider":"qdrant",
        "config":{
            "host":QDRANT_HOST,
            "port":6333
        }
    },
    "graph_store":{
        "provider":"neo4j",
        "config":{
            "url":NEO4J_URL,
            "username":NEO4J_USERNAME,
            "password":NEO4J_PASSWORD
        }
    }
}

mem_client =Memory.from_config(config)


client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



# print(response.choices[0].message)

def chat(message):
    messages= [
        {"role":"user" , "content":message}
    ]
    result = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=messages
       
)
    messages.append({
        "role":"assistent" , "content":result.choices[0].message.content
    })
    # mem_client.add(messages , user_id="id_01")
   
    mem_client.add(messages,user_id="ashish")
    
    return result.choices[0].message.content


while True:
    message=input(">>")
    print("BOT :",chat(message=message))
    