import io
import sys

_INPUT = """\
6
3
30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  print(2**int(input()))