import numpy as np

# 주어진 배열
A = np.arange(1, 101, 2)
B = np.arange(1, 101)
B.resize(10, 10)

'''
    함수명 : min()
    해당 함수의 역할 : min()함수는 주어진 배열에서의 최솟값을 반환한다.
    - A는 1차원 배열이고 B는 2차원 배열이다.
    1. 1차원 배열의 경우 np.min(A)를 사용하거나 A.min()을 사용할 수 있다.
    두 함수 형태의 차이점은 괄호안에 인자를 넣을수 있는지 없는지이다.
    2. 2차원 배열의 경우 np.min(A, axis=0) 또는 np.min(A, axis=1)을 통해서 각 행, 열의 최솟값을 반환하고
    A.min(axis=0) 또는 A.min(axis=1)을 사용하면 된다.
'''
print(np.min(A))
print(np.min(B))
print(np.min(A, axis=0))
print(np.min(B, axis=0))
print(np.min(B, axis=1))
print(A.min(axis=0))
print(B.min(axis=0))
print(B.min(axis=1))

'''
    함수명 : max()
    해당 함수의 역할 : max()함수는 주어진 배열에서의 최댓값 반환한다.
    - A는 1차원 배열이고 B는 2차원 배열이다.
    1. 1차원 배열의 경우 np.max(A)를 사용하거나 A.max()을 사용할 수 있다.
    두 함수 형태의 차이점은 괄호안에 인자를 넣을수 있는지 없는지이다.
    2. 2차원 배열의 경우 np.max(A, axis=0) 또는 np.max(A, axis=1)을 통해서 각 행, 열의 최솟값을 반환하고
    A.max(axis=0) 또는 A.max(axis=1)을 사용하면 된다.
'''
print(np.max(A))
print(np.max(B))
print(np.max(A, axis=0))
print(np.max(B, axis=0))
print(np.max(B, axis=1))
print(A.max(axis=0))
print(B.max(axis=0))
print(B.max(axis=1))

'''
    함수명 : argmin()
    해당 함수의 역할 : 해당 리스트에서 가장 작은 값의 위치(인덱스)를 반환한다.
'''
print(np.argmin(A))
print(np.argmin(B, axis=0))
print(np.argmin(B, axis=1))

'''
    함수명 : argmax()
    해당 함수의 역할 : 해당 리스트에서 가장 큰 값의 위치(인덱스)를 반환한다.
'''
print(np.argmax(A))
print(np.argmax(B, axis=0))
print(np.argmax(B, axis=1))

'''
    함수명 : mean()
    해당 함수의 역할 : 해당 리스트의 평균값을 반환한다.
'''
print(np.mean(A))
print(np.mean(B))
print(np.mean(B, axis=0))
print(np.mean(B, axis=1))

'''
    함수명 : sum()
    해당 함수의 역할 : 해당 리스트의 총 합을 반환한다.
'''
print(np.sum(A))
print(np.sum(B))
print(np.sum(B, axis=0))
print(np.sum(B, axis=1))

'''
    함수명 : cumsum()
    해당 함수의 역할 : 해당 리스트의 누적합 반환한다.
'''
print(np.cumsum(A))
print(np.cumsum(B))
print(np.cumsum(B, axis=0))
print(np.cumsum(B, axis=1))

'''
    함수명 : prod()
    해당 함수의 역할 : 해당 리스트의 곱 반환한다.
'''
print(np.prod(A))
print(np.prod(B))
print(np.prod(B, axis=0))
print(np.prod(B, axis=1))

'''
    함수명 : cumprod()
    해당 함수의 역할 : 해당 리스트의 누적곱 반환한다.
'''
print(np.cumprod(A))
print(np.cumprod(B))
print(np.cumprod(B, axis=0))
print(np.cumprod(B, axis=1))