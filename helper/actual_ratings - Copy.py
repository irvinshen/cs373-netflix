
import os
# import cPickle as pickle
import json

ratings = {}
root = "./training_set/"
count = 0
for file in os.listdir(root):
  with open(root + file, "r") as f:
    # Skip first line (contains movie#)
    movie = f.readline().rstrip(":\n")
    ratings[movie] = {}
    for line in f:
      user, rating, date = line.split(",")
      # ratings[(movie, user)] = rating
      ratings[movie][user] = rating
    
    count += 1
    if count % 100 == 0:
      print(count)

    """
    if count % 2000 == 0:
      with open("user_ratings_" + str(count/2000), "w") as out:
        json.dump(ratings, out)
        ratings = {}
    """

with open("user_ratings", "w") as out:
  json.dump(ratings, out)
