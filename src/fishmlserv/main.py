from typing import Union
from fastapi import FastAPI
from fishmlserv.model.manager import get_model_path, pp
#import pickle
app = FastAPI()


@app.get("/")
def read_root():
    pkl = get_model_path()
    #return {"Hello": "World"}
    return pkl

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


### 모델 불러오기
#pkl = get_model_path()
#with open(pkl, "rb") as f:
#    fish_model = pickle.load(f)

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기 종류 판별기
    
    Args:
        length (float): 물고기 길이 (cm)
        weight (float): 물고기 무게 (g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    return pp(length, weight)
#    prediction = fish_model.predict([[length, weight]])

#    fish_class = "빙어"
#    if prediction[0] == 1:
#        fish_class = "도미"

    #return fish_model
#    return {
#                "prediction": fish_class,
#                "length": length,
#                "weight": weight
#            }
