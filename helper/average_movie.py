
import os
import json
from ratings import get_ratings

ratings = get_ratings()
count = 0
movie_ratings = {}

for movie in ratings.keys():
  m_ratings = ratings[movie]
  for user in m_ratings.keys():
    if movie in movie_ratings:
      movie_ratings[movie] += int(m_ratings[user])
    else:
      movie_ratings[movie] = int(m_ratings[user])
    count += 1
  movie_ratings[movie] /= (count * 1.0)
  count = 0

out = open("movie_avg_rating", "w")
for movie in movie_ratings.keys():
  out.write(str(movie) + ": " + str(movie_ratings[movie]) + "\n")

with open("movie_avg_json", "w") as out2:
  json.dump(movie_ratings, out2)

out.close()
