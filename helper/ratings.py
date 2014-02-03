import json
import os

def get_ratings():
  with open("user_ratings_1.0", "r") as f:
    ratings = json.load(f)
  print(1)
  with open("user_ratings_2.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
  print(2)
  with open("user_ratings_3.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
  print(3)
  with open("user_ratings_4.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
    print(4)
  with open("user_ratings_5.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
    print(5)
  with open("user_ratings_6.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
    print(6)
  with open("user_ratings_7.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
    print(7)
  with open("user_ratings_8.0", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
    print(8)
  with open("user_ratings_10", "r") as f:
    temp = json.load(f)
    ratings.update(temp)
    print(9)
  return ratings