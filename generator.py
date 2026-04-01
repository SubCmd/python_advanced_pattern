# 제너레이터 (Generator)
# : yield 키워드를 사용해 값을 하나씩 생산하는 함수 (메모리 효율성 & 성능 향상)
# lazy evaluation(지연평가) -> 호출할 때 코드를 실행하지 않고, 실제 값을 필요로 할 때 값을 하나씩 생산.

# === 기본 제너레이터 ===
def count_up(start, end):
    """start부터 end까지 숫자를 생산하는 제너레이터"""
    current = start
    while current <= end:
        yield current
        current += 1

# 사용법 1: for 루프
for num in count_up(1, 5):
    print(num)  # 1 2 3 4 5

# 사용법 2: next()로 수동 제어
gen = count_up(1, 3)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # StopIteration 예외 발생

# === 실무 예시: 대용량 CSV 파일 처리 ===
import csv

def read_csv_chunks(filepath, chunk_size=1000):
    """대용량 CSV를 chunk 단위로 읽는 제너레이터"""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:  # 마지막 남은 chunk
            yield chunk

# 10GB 파일도 메모리 부족 없이 처리 가능
# for chunk in read_csv_chunks('huge_data.csv', chunk_size=5000):
#     process(chunk)  # chunk 단위로 처리


# === 제너레이터 표현식 (Generator Expression) ===
# 리스트 컴프리헨션 vs. 제너레이터 표현식
import sys

# 리스트 : 메모리에 모든 값을 저장
squares_list = [x**2 for x in range(1_000_000)]
print(sys.getsizeof(squares_list))  # ~8Mbytes

# 제너레이터 : 값을 하나씩 생산
squares_gen = (x**2 for x in range(1_000_000))
print(sys.getsizeof(squares_gen))  # 200 bytes

# 합계 구할 때 제너레이터가 효율적
total = sum(x**2 for x in range(1_000_000))  # 괄호 생략 가능


# === yield from : 제너레이터 위임 ===
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)    # 재귀적으로 위임
        else:
            yield item

data = [1, [2, 3, [4, 5]], 6, [7]]
print(list(flatten(data))) # [1, 2, 3, 4, 5, 6, 7]

## 대용량 데이터 처리, 스트리밍 파이프라인에 필수
## yield from -> 다른 제너레이터에 위임 (코드 간결화)


# === 컨텍스트 매니저 (Context Manager) ===
# : with문과 함께 사용 / 리소스의 획득과 해제를 자동으로 관리

# === contextlib로 간편하게 만들기 ===
from contextlib import contextmanager

@contextmanager
def timer_context(label):
    """코드 블록의 실행 시간을 측정"""
    start = time.perf_counter()
    try:
        yield  # 여기서 with 블록 내부 코드가 실행됨
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] {elapsed:.4f}초")

with timer_context("데이터 전처리"):
    data = [x**2 for x in range(1_000_000)]
    filtered = [x for x in data if x % 2 == 0]
# [데이터 전처리] 0.1823초


'''
py generator.py
'''