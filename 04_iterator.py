# 이터레이터 (Iterator)
# : 값을 차례대로 꺼낼 수 있는 객체(object)
# for문 - 숫자가 많아질 때, 메모리를 많이 사용하게 됨.
# // 반복할 때마다 이터레이터에서 숫자를 한씩 꺼내서 반복
# 지연 평가(lazy evaluation) : 불필요한 계산을 방지해 성능을 최적화

## dir(객체)
it = [1, 2, 3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
## 한 번 더 사용시, StopIteration

'''
class 이터레이터 이름:
    def __iter__(self):
        코드
    def __next__(self):
        코드
'''

# iterator.py
class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')

'''
class 이터레이터 이름:
    def __getitem__(self, 인덱스):
        코드
'''

# iterator_getitem.py
class Counter:
    def __init__(self, stop):
        self.stop = stop
 
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
 
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
 
for i in Counter(3):
    print(i, end=' ')

# 제너레이터 (Generator)
# : 이러

'''
py 04_generator.py
'''