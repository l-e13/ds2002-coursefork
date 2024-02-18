#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

# Ask for input
ANIMAL = input('What is your favorite animal? ')
BODOS = input('What is your Bodos Bagels order? ')
SEASON = input('What is your favorite season? ')

# env variables
os.environ["ANIMAL"] = ANIMAL
os.environ["BODOS"] = BODOS
os.environ["SEASON"] = SEASON

# fetch and print
ANIMAL_ENV = print(os.getenv("ANIMAL"))
BODOS_ENV = print(os.getenv("BODOS"))
SEASON_ENV = print(os.getenv("SEASON"))


