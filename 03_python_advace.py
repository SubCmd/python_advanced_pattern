# === 기본 데코레이터 ===

# 데코레이터 (Decorator)
# : 함수를 인자로 받아 새로운 기능을 추가한 함수를 반환하는 패턴.
# -> 원본 함수를 수정하지 않고 기능을 확장한다.

import time
import functools

def timer(func):
    """함수 실행 시간을 측정하는 데코레이터"""
    @functools.wraps(func)  # 원본 함수의 메타데이터 보존
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] 실행 시간: {elapsed:.4f}초")
        return result
    return wrapper    




'''
python 03_python_advace.py
'''