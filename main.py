import uvicorn
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates") 

app = FastAPI()


# class Item(BaseModel):
#     content: str
#     img: bytes


@app.post("/add")
async def post_textarea(option: str = Form(...), img: UploadFile = File(...)):
    # print(data.dict())
    return {"option": option, "file name": img.filename}


@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)