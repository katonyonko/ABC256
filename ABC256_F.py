import io
import sys

_INPUT = """\
6
3 3
1 2 3
2 3
1 2 0
2 3
2 1
998244353 998244353
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    #合計にはrを含まない
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
  N,Q=map(int,input().split())
  A=list(map(int,input().split()))
  bit1,bit2,bit3=BIT(N),BIT(N),BIT(N)
  for i in range(N):
    bit1.add(i,(A[i]*(i+1)**2)%mod)
    bit2.add(i,(A[i]*(i+1))%mod)
    bit3.add(i,A[i])
  for _ in range(Q):
    query=input().split()
    if query[0]=='1':
      x,v=map(int,query[1:])
      a=bit1.sum(x-1,x)%mod
      bit1.add(x-1,(v*x**2-a)%mod)
      b=bit2.sum(x-1,x)%mod
      bit2.add(x-1,(v*x-b)%mod)
      c=bit3.sum(x-1,x)%mod
      bit3.add(x-1,v-c)
    else:
      x=int(query[1])
      print((bit1.sum(0,x)-bit2.sum(0,x)*(2*x+3)+bit3.sum(0,x)*(x**2+3*x+2))*pow(2,mod-2,mod)%mod)