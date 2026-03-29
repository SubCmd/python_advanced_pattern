# 01. Stack
# LIFO(Last In, First Out) : 위에서만(push) 넣고, 위에서만 빼는(pop) (접시 쌓기)
# 핵심 연산 3가지 : push(삽입), pop(꺼내기), peek(맨 위 확인)
# 예시) 브라우저 뒤로가기, Ctrl + Z, 함수 호출 스택(재귀)

# 방법 1 : 리스트로 간단 구현 (실무 이용도 높음)
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)        # ['A', 'B', 'C']
print(stack.pop())  # 'C'
print(stack[-1])    # 'B'


# 방법 2 : 클래스로 구현 (구조를 이해하기 위한 학습용)
class Stack:
    def __init__(self):
        self._data = [] # 내부에서만 사용, 외부에서 직접 접근하지 말라
    
    def push(self, item):
        """스택 맨 위에 요소 추가"""
        self._data.append(item)
    
    def pop(self):
        """스택 맨 위 요소를 꺼내서 반환"""
        if self.is_empty():
            raise IndexError("빈 스택에서 pop 불가")    # 개발자가 의도적으로 일으키는 명령어
        return self._data.pop()

    def peek(self):
        """스택 맨 위 요소를 꺼내지 않고 확인"""
        if self.is_empty():
            raise IndexError("빈 스택에서 peek 불가")
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def size(self):
        return len(self._data)
    
    def __repr__(self):     # Representation : 개발자 관점에서 보여주는 공식적인 문자열 표현
        return f"Stack({self._data})"

# Class Stack 사용
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s)        # Stack([10, 20, 30])
print(s.peek()) # 30
print(s.pop())  # 30
print(s.pop())  # 20
print(s.size()) # 1


## 괄호 유효성 검사
def is_valid_parentheses(s: str) -> bool:
    """'(', ')', '{', '}', '[', ']' 로 이루어진 문자열의 유효성 검사"""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)        # 여는 괄호 → push
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()               # 짝 맞으면 → pop
    return len(stack) == 0

print(is_valid_parentheses("({[]})"))   # True
print(is_valid_parentheses("({[})"))    # False
print(is_valid_parentheses("(("))       # False


# 02. Queue (큐)
# FIFO(First In, First Out) : 먼저 넣은 것이 먼저 나오는 구조 (줄 서기)
# enqueue : 맨 뒤에 데이터 추가 / dequeue : 맨 앞에 데이터 꺼내고 제거
# 예시) 작업 대기열, 프린터 큐, BFS(너비 우선 탐색), 메시지 큐(Kafka, RabbitMQ)

from collections import deque

# 방법 1 : deque로 구현 (실무 정석)
queue = deque()
queue.append("1번 손님")    # enqueue (뒤로 입장)
queue.append("2번 손님")
queue.append("3번 손님")
print(queue)                   # deque(['1번 손님', '2번 손님', '3번 손님'])
print(queue.popleft())         # '1번 손님' — 먼저 온 사람이 먼저 나감
print(queue.popleft())         # '2번 손님'

# 방법 2 : 클래스로 구현
class Queue:
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item):
        """큐 뒤쪽에 요소 추가"""
        self._data.append(item)
    
    def dequeue(self):
        """큐 앞쪽에서 요소를 꺼내서 반환"""
        if self.is_empty():
            raise IndexError("빈 큐에서 dequeue 불가")
        return self._data.popleft()
    
    def front(self):
        if self.is_empty():
            """큐 맨 앞 요소를 꺼내지 않고 확인"""
            raise IndexError("빈 큐에서 front 불가")
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"
    
q = Queue()
q.enqueue("작업A")
q.enqueue("작업B")
q.enqueue("작업C")
print(q)              # Queue(['작업A', '작업B', '작업C'])
print(q.dequeue())    # '작업A'
print(q.front())      # '작업B'

## 변형 : 양방향 큐 (덱, Deque)
from collections import deque

# 덱은 양쪽 끝에서 삽입/삭제가 모두 (0, 1)
d = deque([1, 2, 3])

d.append(4)           # 오른쪽 추가    → [1, 2, 3, 4]
print(d)
d.appendleft(0)       # 왼쪽 추가      → [0, 1, 2, 3, 4]
print(d)
d.pop()               # 오른쪽 제거    → [0, 1, 2, 3]
print(d)
d.popleft()           # 왼쪽 제거      → [1, 2, 3]
print(d)

## maxlen 설정 -> 최근 N개만 유지 (로그, 히스토리에 유용)
recent_logs = deque(maxlen=3)
recent_logs.append("log1")
recent_logs.append("log2")
recent_logs.append("log3")
recent_logs.append("log4")   # log1이 자동으로 밀려남
print(recent_logs)             # deque(['log2', 'log3', 'log4'], maxlen=3)

# 03. Linked List (연결 리스트)
# 각 요소(노드)가 데이터 + 다음 노드의 참조(포인터)를 갖는 구조
# 메모리에 연속적으로 저장되지 않음 / 장점 : 위치를 알고 있을때, 중간 삽입, 삭제가 O(1) / 인덱스 접근은 O(n)
# 파이썬 자체에서 list를 제공해서 큰 문제는 없지만, 개념을 알아둬야 함!
'''
[데이터|다음] → [데이터|다음] → [데이터|다음] → None
   Head                                Tail
'''

class Node:
    """연결 리스트의 각 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None    # 다음 노드에 대한 참조

    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        """리스트 끝에 노드 추가 — O(n)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:       # 끝까지 순회
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, data):
        """리스트 맨 앞에 노드 추가 — O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def delete(self, data):
        """값으로 노드 삭제 — O(n)"""
        if self.head is None:
            return

        # head가 삭제 대상인 경우
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next   # 건너뛰기로 삭제
                self._size -= 1
                return
            current = current.next

    def search(self, data) -> bool:
        """값이 존재하는지 검색 — O(n)"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self):
        """파이썬 리스트로 변환"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self._size

    def __repr__(self):
        return " → ".join(str(d) for d in self.to_list()) + " → None"

# 사용
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
print(ll)              # 5 → 10 → 20 → 30 → None
print(ll.search(20))   # True
ll.delete(20)
print(ll)              # 5 → 10 → 30 → None
print(len(ll))         # 3


# 04. Tree (트리)
# 계층 구조를 표현하는 자료구조
# 하나의 루트(root)에서 시작해 자식 노드들로 분기 
# 이진 트리(Binary Tree)와 이진 트리 탐색(BST)

'''
        8          ← 루트(root)
       / \
      3   10       ← 자식 노드
     / \    \
    1   6    14    ← 리프(leaf) 노드 (자식 없음)
       / \
      4   7
'''
# root (최상위), parent(부모), child(자식), leaf(잎, 자식 없는 노드), depth(깊이), height(높이)
# BST 규칙 : 왼쪽 자식 < 부모 < 오른쪽 자식 -> 이 규칙 덕분에 탐색 평균이 O(log n)
# 실제 사용 사례 : 파일 시스템, HTML DOM, 데이터베이스 인덱스(B-Tree), 의사결정 트리(ML)

class TreeNode:
    """이진 트리의 노드"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """BST 규칙에 따라 삽입 — 평균 O(log n)"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value) -> bool:
        """값 검색 — 평균 O(log n)"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # === 트리 순회 (3가지 핵심 순회) ===

    def inorder(self, node=None, first_call=True):
        """중위 순회: 왼쪽 → 루트 → 오른쪽 (BST에서 정렬된 순서)"""
        if first_call:
            node = self.root
        result = []
        if node:
            result += self.inorder(node.left, False)
            result.append(node.value)
            result += self.inorder(node.right, False)
        return result

    def preorder(self, node=None, first_call=True):
        """전위 순회: 루트 → 왼쪽 → 오른쪽 (트리 복사에 유용)"""
        if first_call:
            node = self.root
        result = []
        if node:
            result.append(node.value)
            result += self.preorder(node.left, False)
            result += self.preorder(node.right, False)
        return result

    def postorder(self, node=None, first_call=True):
        """후위 순회: 왼쪽 → 오른쪽 → 루트 (삭제에 유용)"""
        if first_call:
            node = self.root
        result = []
        if node:
            result += self.postorder(node.left, False)
            result += self.postorder(node.right, False)
            result.append(node.value)
        return result

# 사용
bst = BinarySearchTree()
for val in [8, 3, 10, 1, 6, 14, 4, 7]:
    bst.insert(val)

print(bst.search(6))      # True
print(bst.search(9))      # False

print(bst.inorder())      # [1, 3, 4, 6, 7, 8, 10, 14] ← 정렬됨!
print(bst.preorder())     # [8, 3, 1, 6, 4, 7, 10, 14]
print(bst.postorder())    # [1, 4, 7, 6, 3, 14, 10, 8]


### 트리 순회 시각화
'''
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7

중위(Inorder)  : 1 → 3 → 4 → 6 → 7 → 8 → 10 → 14  (정렬!)
전위(Preorder) : 8 → 3 → 1 → 6 → 4 → 7 → 10 → 14
후위(Postorder): 1 → 4 → 7 → 6 → 3 → 14 → 10 → 8
'''

'''
python 02_structure.py
'''