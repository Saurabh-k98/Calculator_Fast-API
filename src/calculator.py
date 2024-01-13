from fastapi import FastAPI

calci = FastAPI()

@calci.get("/")
def start():
    return {"Result": "Welcome"}

@calci.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"Result": num1 + num2}

@calci.get("/sub/{num1}/{num2}")
def sub(num1: int, num2: int):
    return {"Result": num1 - num2}

@calci.get("/div/{num1}/{num2}")
def div(num1: int, num2: int):
    return {"Result": num1 / num2}

@calci.get("/mul/{num1}/{num2}")
def mul(num1: int, num2: int):
    return {"Result": num1 + num2}
