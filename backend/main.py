from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import get_db, get_engine
import schemas
import crud
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Root"}

@app.get("/orders", response_model=List[schemas.Order])
def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), conn = Depends(get_engine)):
    try:
        orders = crud.get_orders(db, skip=skip, limit=limit)
        return orders

    except SQLAlchemyError as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
    
@app.get("/recommended/{product_id}", response_model=schemas.RecommendedProduct)
def get_recommended(product_id: int, limit: int = 1, conn = Depends(get_engine)):
    try:
        result = crud.get_recommended_product(product_id, conn)
        
        return schemas.RecommendedProduct(id=result[0], product_name=result[1],
                                          product_description=result[2], image_path=result[3], 
                                          similarity_score=result[4])

    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=500, detail="Database error occurred")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)