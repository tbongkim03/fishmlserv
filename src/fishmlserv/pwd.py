from typing import Union
#from fastapi import FastAPI
from fishmlserv.model.manager import get_model_path
import pickle
import sys
import typer
import sklearn

def main():
    print(get_model_path())

def run():
    typer.run(main)
