def decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

# func : 원래 함수
# wrapper : 원래 함수를 감싸는 내 함수
# retrun wrapper : 감싼 결과를 반환


def hello():
    print("안녕하세요")

hello = decorator(hello)
hello()

@decorator
def hello2():
    print("안녕하쇼!")

hello2()

# decorator add
def decorator2(func):
    def wrapper(a, b):
        print("계산 시작")
        func(a, b)
        print("계산 끝")
    return wrapper

@decorator2
def add(a, b):
    print(a + b)

add(3, 5)


# *args : positional arguments 
# : 갯수가 정해지지 않은 위치 인자를 받음 / 튜플 형태
# **kwargs : Named Argument
# : 갯수가 정해지지 않은 키워드 인자를 받음 / 딕셔너리 형태

# 어떤 인자든 받을 수 있도록 진행
def decorator3(func):
    def wrapper(*args, **kwargs):
        print("실행 전")
        func(*args, **kwargs)
        print("실행 후")
    return wrapper

@decorator3
def introduce(name, age):
    print(f"이름: {name}, 나이: {age}")

introduce("민수", 30)


# 반환값이 있는 함수에 decorator 적용하기
def decorator(func):
    def wrapper(*args, **kwargs):
        print("실행 전")
        result = func(*args, **kwargs)
        print("실행 후")
        return result
    return wrapper

@decorator
def multiply(a, b):
    return a * b

value = multiply(4, 5)
print(value)


# functools.wraps를 사용하는 이유??
from functools import wraps

def decorator5(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator5
def hello2():
    """인사 함수"""
    print("hello")

print(hello2.__name__)
print(hello2.__doc__)

# 자주 사용하는 decorator 예제
# 1. 실행 시간 측정 decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"실행 시간: {end - start:.6f}초")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("작업 완료")

slow_function()


# 2. 로그인이 필요한 예제
is_logged_in = False

def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("로그인이 필요합니다.")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
def my_page():
    print("마이페이지입니다.")

my_page()


'''
py decorator_more.py
'''