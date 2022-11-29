"""
zoulou
"""
import math
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """
    test
    """
    return "Hello World"


@app.get("/{number}")
def return_square(number: int):
    """
    test
    """
    return get_square(number)


@app.get("/twice/{number}")
def return_square_twice(number: int):
    """
    test
    """
    return get_square(number) + get_square(number)


def get_square(number: int):
    """
    test
    """
    return math.floor(math.pow(number, 2))
