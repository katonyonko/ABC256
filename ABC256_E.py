import io
import sys

_INPUT = """\
6
3
2 3 2
1 10 100
8
7 3 5 5 8 4 1 2
36 49 73 38 30 85 27 45
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappush, heappop
  N=int(input())
  X=list(map(lambda x:int(x)-1,input().split()))
  C=list(map(int,input().split()))
  ans=0
  inter,out=[0]*N,[set() for _ in range(N)]
  edge=[set() for _ in range(N)]
  for i in range(N):
    inter[X[i]]+=C[i]
    edge[X[i]].add(i)
    out[i].add((X[i],C[i]))
  h=[]
  for i in range(N):
    heappush(h,(inter[i],i))
  while h:
    x,i=heappop(h)
    if x==inter[i]:
      ans+=x
      for v,c in out[i]:
        inter[v]-=c
        heappush(h,(inter[v],v))
      for v in edge[i]:
        if (i,C[v]) in out[v]: out[v].remove((i,C[v]))
  print(ans)