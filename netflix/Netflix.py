#!/usr/bin/env python3

# -------------
# collatz_solve
# -------------

def neflix_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
  for line in probe:
    l = line.rstrip("\n")
    # movie
    if l.endswith(":"):
      movie = l.rstrip(":")
      out.write(line)
    else:
      out.write(str(ratings[movie][l]) + "\n")
