
import os
import json
from ratings import get_ratings
with open("./movie_year.json") as f:
  years = json.load(f)
ratings = get_ratings()
decade_ratings = {}
decade_count = {}
count = 0

for movie in years.keys():
  decade = (int(years[movie]) // 10)
  decade = decade * 10
  for user in ratings[movie].keys():
    if decade in decade_count:
      decade_count[decade] += 1
    else:
      decade_count[decade] = 1

    if decade in decade_ratings:
      decade_ratings[decade] += int(ratings[movie][user])
    else:
      decade_ratings[decade] = int(ratings[movie][user])

  count += 1
  if count % 100 == 0:
    print(count)
print("saving")

for decade in decade_ratings:
  decade_ratings[decade] /= (decade_count[decade] * 1.0)

out = open("decade_avg_rating", "w")
for decade in decade_ratings.keys():
  out.write(str(decade) + ": " + str(decade_ratings[decade]) + "\n")

with open("decade_avg.json", "w") as out2:
  json.dump(decade_ratings, out2)

out.close()
