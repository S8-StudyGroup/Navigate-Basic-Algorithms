## <br><b>정렬(Sort)</b>

  <br>정렬이란, 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순), 혹은 그 반대의 순서대로(내림차순) 재배열하는 것을 의미합니다.

  <br><b>대표적인 정렬 방식의 종류</b>

- 버블 정렬(Bubble Sort)
- 카운팅 정렬(Counting Sort)
- 선택 정렬(Selection Sort)
- 퀵 정렬(Quick Sort)
- 삽입 정렬(Insertion Sort)
- 병합 정렬(Merge Sort)

<br> 이번 회의에서는 이전에 학습하였던 버블 정렬과 카운팅 정렬, 그리고 내장 함수인 sort에 대해 알아보았습니다.

<br><b>버블 정렬</b>

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식입니다.
- 정렬 과정
  1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동합니다.
  2. 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬됩니다.
  3. 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 합니다.
- 시간 복잡도(O(n^2))
- 구현 방법

<br>

```python
T = int(input())

for tc in range(1, T + 1):
  N = int(input())
  numbers = list(map(int, input().split()))

  for j in range(N - 1, 0, -1):
      for i in range(j):
          if numbers[i] > numbers[i + 1]:
              numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

  print(f"#{tc}", *numbers)
```

<br>

  <br><b>카운팅 정렬(Counting Sort)</b>

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- <b>제한 사항</b>
  
  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스되는 카운트들의 배열을 사용하기 때문입니다.
    - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 합니다.

- 시간 복잡도(O(n + k))

- 구현 방법
  
  <br>
  
  ```python
  T = int(input())
  
  for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = max(numbers)
    c = [0] * (max_num + 1)
    sorted_numbers = []
  
    for number in numbers:
        c[number] += 1
  
    for i in range(len(c)):
        while c[i]:
            sorted_numbers.append(i)
            c[i] -= 1
  
    print(f"#{tc}", *sorted_numbers)
  ```
  
  <br>
  
  <br><b>sort(), sorted()</b>

- sort, sorted는 내장함수이며, 내부적으로 병합 정렬을 적용하고 있습니다. 병합 정렬을 이용할 시 최악의 경우에도 O(NlogN)의 시간복잡도를 보장해준다는 장점이 있습니다.

<br>

<b>배열 회전에 관한 zip 활용 예시</b>

```python
# 2차원 리스트 다루기

a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# 90도 회전
rotated_a = list(zip(*a[::-1]))
# [
# [7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]
# ]

# 행과 열 바꾸기
change_row_and_col_a = list(zip(*a))
# [
# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]
# ]
```

<br>