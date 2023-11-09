import calc
print(calc.add(1,2))

from calc import add
print(add(3,4))

# 둘다 가능



import bs4 
import sys

print(sys.path) # 이 경로안에 있는 모듈은 import 가능, 앞에 있는게 우선순위 높음

