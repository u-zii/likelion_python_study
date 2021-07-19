from random import *

print("주사위 던지기")
a = randint(1,6)
b = randint(1,6)
print("주사위 1:" + str(a))
print("주사위 2:" + str(b)+ "\n")

kind = input("""실행할 연산의 종류를 입력하세요.
1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 나머지 구하기
연산종류 : """)

if kind == "1":
    result=a+b
    print("덧셈 결과 : " + str(result) + "\n")
    print("별찍기")
    for i in range(1, result+1):
        print("*"*i)
    
elif kind=="2":
    result=a-b
    print("뺄셈 결과 : " + str(result) + "\n")
    print("별찍기")
    for i in range(1, result+1):
        print("*"*i)

elif kind=="3":
    result=a*b
    print("곱셈 결과 : " + str(result) + "\n")
    print("별찍기")
    for i in range(1, result+1):
        print("*"*i)

elif kind=="4":
    result=a/b
    print("나눗셈 결과 : " + str(result) + "\n")
    print("별찍기")
    for i in range(1, int(result)+1):
        print("*"*i)

elif kind=="5":
    result=a%b
    print("나머지 구하기 결과 : " + str(result) + "\n")
    print("별찍기")
    for i in range(1, result+1):
        print("*"*i)

else:
    print("오류")