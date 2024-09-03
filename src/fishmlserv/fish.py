from typing import Union
#from fastapi import FastAPI
from fishmlserv.model.manager import get_model_path
import pickle
import sys
import typer
import sklearn
#app = FastAPI()

#def get-model-path():
#    print(get_model_path())

def prediction(length, weight):
    """ 
    물고기 종류 판별기
    
    Args:
        length (float): 물고기 길이 (cm)
        weight (float): 물고기 무게 (g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    ### 모델 불러오기
    pkl = get_model_path()
    with open(pkl, "rb") as f:
        fish_model = pickle.load(f)

    prd = fish_model.predict([[length, weight]])

    fish_class = "빙어"
    if prd[0] == 1:
        fish_class = "도미"

    #return fish_model
    return {
                "prediction": fish_class,
                "length": length,
                "weight": weight
            }

def main(length: int, weight: int):
    fish_dict = prediction(length, weight)
    print(fish_dict)
    
def run():
    typer.run(main)
        
