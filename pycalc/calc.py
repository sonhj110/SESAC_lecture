def add(a, b) :
    return a+b

# print(add(1,2)) # 파이썬은 이게 됨. 다른언어는 대부분 안됨
# print(__name__) # 여기선 __main__이라고 뜸 test.py에선 calc(파일명)라고 뜸


if __name__ == '__main__' :
    print(add(1,2))
    print(__name__)

