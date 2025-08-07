from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = ""

items = [
    Item(id=1, name="Sample Item", description="This is a sample item.")
]

@app.get("/hello")
def read_hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items):
        if item.id == item_id:
            items[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(items):
        if item.id == item_id:
            del items[idx]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
