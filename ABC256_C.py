import io
import sys

_INPUT = """\
6
3 4 6 3 3 7
3 4 5 6 7 8
5 13 10 6 13 9
20 25 30 22 29 24
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  h1,h2,h3,w1,w2,w3=map(int,input().split())
  ans=0
  for i in range(1,h1):
    for j in range(1,h1-i):
      for k in range(1,h2):
        for l in range(1,h2-k):
          if w1>i+k and w2>j+l and w3-(h1-i-j+h2-k-l)>0 and w3-(h1-i-j+h2-k-l)==h3-(w1-i-k+w2-j-l):
            ans+=1
  print(ans)