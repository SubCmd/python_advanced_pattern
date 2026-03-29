import numpy as np

# list [] : 중복 가능 / 순서 있음 / 수정 가능 / 인덱싱 가능
# tuple () : 중복 가능 / 순서 있음 / 수정 불가능 / 인덱싱 가능
# dictionary {key:value} : 중복 가능 / 순서 있음 / 수정 가능 (key : value 구조) / 인덱싱 가능
# set {}: 중복 불가능 / 순서 없음 / 수정 가능 / 인덱싱 불가능

# 1단계 : 기본 구조 익히기
nums = [1, 2, 3, 4, 5]

numb = [x*2 for x in nums ]
print(numb)

numb1 = [str(x) for x in nums]
print(numb1)

words = ["apple", "banana", "cherry"]
numb2 = [len(x) for x in words]
print(numb2)

# 2단계 : 조건문 포함
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)

odds = [x for x in nums if x % 2 == 1]
print(odds)

words = ["apple", "banana", "kiwi", "grape"]
word = [x for x in words if len(x) >= 5]
print(word)

# 3단계
nums = [1, 2, 3, 4, 5]
what = ["Even" if n % 2 == 0 else 'Odd' for n in nums]
print(what)

nums = [10, 55, 32, 87, 100]
pf = ["pass" if x >= 50 else "fail" for x in nums]
print(pf)

# 4단계
list1 = [1, 2, 3]
list2 = [10, 20, 30]

pairs = [(x, y) for x in list1 for y in list2]
print(pairs)

matrix = [[1, 2], [3, 4], [5, 6]]
flatten = [item for row in matrix for item in row]
print(flatten)


# 5단계 실전
sentence = "hello world"
ls = [str(x) for x in sentence if x != " "]
print(ls)


words = ["apple", "banana", "cherry"]
first = [char[0] for char in words]
print(first)

nums = [1, 2, 3, 4, 5]
pairs = [(x, x**2) for x in nums]
print(pairs)

matrix = [[1, 2, 3], [4, 5, 6]]
flatten = [item for row in matrix for item in row if item % 2 == 0 ]
print(flatten)


'''
python comprehension.py
'''