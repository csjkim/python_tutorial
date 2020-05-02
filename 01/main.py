# print
print("안녕하세요")
print("Hello")
print("Bonjour")
print("你好")
print("こんにちは")
print("오늘의 기분은", "어때?")
print(2020, "년", 1, "월", "21일")

# input
input("당신만의 최고의 여행지는?")
input("ID를 입력해주세요")
input("Password를 입력해주세요")

# variable
address = "대한민국 서울특별시 강남구"
education = '컴퓨터공학 석사과정'
height = 182

# number
gate =  129 # integer
weight = 74.5 # float
complex_number = -1j # complex
sum = 1 + 2 # 덧셈
subtract = 1 - 2 # 뺄셈
multiply = 1 * 3 # 곱셈
divide = 1 / 3 # 나눗셈
mod = 3 % 2 # 나머지
minute = 370
hours = minute // 60 # 몫
squared = 2 ** 10 # 제곱

# math
import math # math 모듈을 가져옵니다
math.ceil(weight) # 반올림
math.gcd(10, 12) # 최대공약수
math.log(99) # 로그값
math.cos(90) # 삼각함수 코싸인
print(math.pi) # pi 원주율

# range
print(list(range(10))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(2, 5))) # 2, 3, 4
print(list(range(1, 10, 2))) # 1, 3, 5, 7, 9
print(list(range(1, -4, -1))) # 1, 0, -1, -2, -3

# random
import random # random 모듈을 가져옵니다.
print(random.randint(1, 10))  # a <= N <= b 랜덤 정수값
print(random.uniform(-1, 1)) # 랜덤 소수값

# lotto
lotto = random.sample(range(1, 46), 6)
print(lotto)
lotto = random.sample(range(1, 46), 6)
print(lotto)
lotto = random.sample(range(1, 46), 6)
print(lotto)