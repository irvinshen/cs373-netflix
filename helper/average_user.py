
import os
import json
from ratings import get_ratings

ratings = get_ratings()
count = 0
user_count = {}
user_ratings = {}

for movie in ratings.keys():
  m_ratings = ratings[movie]
  for user in m_ratings.keys():
    if user in user_count:
      user_count[user] += 1
    else:
      user_count[user] = 1

    if user in user_ratings:
      user_ratings[user] += int(m_ratings[user])
    else:
      user_ratings[user] = int(m_ratings[user])
  count += 1
  if count % 100 == 0:
    print(count)

out = open("user_avg_ratings", "w")
for user in user_count.keys():
  total = user_ratings[user] * 1.0
  num = int(user_count[user]) * 1.0
  user_ratings[user] = total/num
  out.write(str(user) + ": " + str(total/num) + "\n")

with open("user_avg_json", "w") as out2:
  json.dump(user_ratings, out2)

out.close()
