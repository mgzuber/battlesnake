from sanic import Sanic
from sanic.response import json

app = Sanic("Battlesnake app")

@app.get("/")
async def root(request):
  return json({
    "apiversion": "1",
    "author": "mgzuber",
    "color" : "#4D7FE4",
    "head" : "default",
    "tail" : "default",
    "version" : "0.0.1-beta"
  })

@app.post("/start")
async def start_game(request):
  return json({})

@app.post("/move")
async def make_move(request):
  return json({
    "move": "up",
    "shout": "I am moving up!"
  })

@app.post("/end")
async def make_move(request):
  return json({})