from fastapi import FastAPI

# import uvicorn
# uvicorn end_point_api:app --reload
app = FastAPI()


# http://127.0.0.1:8000/get-message
@app.get("/get-message")
async def read_root():
    return {"Message": "Congrats! This is your first API!"}


# Initial static string
static_string = "Initial text"


@app.post("/add")
async def add_text(text: str):
    global static_string
    static_string += text
    return {"message": "Text added", "curent_string": static_string}


@app.put("/change")
async def change_text(new_text: str):
    global static_string
    static_string = new_text
    return {"message": "Text changed", "curent_string": static_string}


@app.delete("/remove")
async def remove_text(new_text: str):
    global static_string
    static_string = ""
    return {"message": "Text removed"}
