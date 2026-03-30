# 제너레이터와 yield 알아보기
# : 이터레이터를 생성해주는 함수

# yield.py
def number_generator():
    yield 0
    yield 1
    yield 2
 
for i in number_generator():
    print(i)


g = number_generator()
print(g.__next__())
print(g.__next__())
print(g.__next__())

# yield_next.py
def number_generator():
    yield 0    # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1    # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 2    # 2를 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
 
g = number_generator()
 
a = next(g)    # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)       # 0
 
b = next(g)
print(b)       # 1
 
c = next(g)
print(c)       # 2


'''
py 05_generator.py
'''