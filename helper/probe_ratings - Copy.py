
import os
# import cPickle as pickle
import json
from ratings import get_ratings

ratings = get_ratings()
out = open("probe_ratings", "w")
  
movie = "0"
count = 0
with open("./probe.txt") as probe:
  for line in probe:
    l = line.rstrip("\n")
    # movie
    if l.endswith(":"):
      movie = l.rstrip(":")
      out.write(line)
    else:
      out.write(str(ratings[movie][l]) + "\n")
    
    count += 1
    if count % 100 == 0:
      print(count)

out.close()
