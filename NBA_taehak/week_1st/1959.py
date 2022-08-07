# 두 개의 숫자열
'''
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
두 번째 줄에는 Ai,
세 번째 줄에는 Bj 가 주어진다.
'''


def max_product(A_count, B_count, A, B):
    # A가 B보다 개수가 더 많은 상황 만들기
    if B_count >= A_count:
        B_count, A_count = A_count, B_count
        A, B = B, A

    products = []
    for move in range(A_count - B_count + 1):
        product_sum = 0
        for i in range(B_count):
            product_sum += A[i + move] * B[i]
        products.append(product_sum)
    return max(products)


cases = int(input())
result = dict()
for case in range(cases):
    A_count, B_count = map(int, input().split())
    A, B = map(int, input().split()), map(int, input().split())
    result[case + 1] = max_product(A_count, B_count, list(A), list(B))

for case, product in result.items():
    print(f'#{case} {product}')
