
import os
# import cPickle as pickle
import json

ratings = {}
root = "./movie_titles.txt"
count = 0
with open(root, "r") as f:
  # Skip first line (contains movie#)
  for line in f:
    unpack = line.split(",")
    movie = unpack[0]
    year = unpack[1]
    # print(movie, year)
    if year == 'NULL':
      continue
    # ratings[(movie, user)] = rating
    ratings[movie] = year
  
  count += 1
  if count % 100 == 0:
    print(count)

with open("movie_year.json", "w") as out:
  json.dump(ratings, out)
