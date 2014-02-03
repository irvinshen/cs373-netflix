
import os
import cPickle as pickle

with open("ratings", "rb") as f:
  ratings = pickle.load(f)

out = open("probe_ratings", "wb")

movie = "0"
count = 0
with open("/u/downing/cs/netflix/probe.txt") as probe:
  for line in probe:
    l = line.chomp
    # movie
    if l.endsWith(":"):
      movie = l.rstrip(":")
      out.write(line)
    else:
      out.write(str(ratings[(movie, l)]) + "\n")
    
    count += 1
    if count % 100 == 0:
      print(count)

out.close()
