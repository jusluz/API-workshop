from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Requets 
def old_home(): #Response
    return {
        "message": "Hello World"
    }
