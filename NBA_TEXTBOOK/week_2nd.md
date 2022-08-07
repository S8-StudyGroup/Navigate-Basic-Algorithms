# 2주차 회의 내용 관련 개념 정리

## <br>List Comprehension

<br>표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

<br>

- List Comprehension의 과정


```python
a = []
# List Comprehension의 과정을 제어문으로 만들어 보면..
for i in range(5):
    if i % 2 == 1:
        a.append(i)

# 마법의 복사 붙여넣기
# for문 그대로 들고가서 가운데, if문을 그 오른쪽에, 출력할 값을 왼쪽에!
a = [i for i in range(5) if i % 2 == 1]
```

<br>

- 알고리즘 문제 풀 때 많이 활용됨!!

```python
[code for 변수 in iterable]

[code for 변수 in iterable if 조건식]
# [1, 2, 3, 4, ...] 에서 [2, 4, 6, 8...] 뽑아낼 떄 등 많이 사용됨!
```

<hr>

출처 : [GangYunGit_TIL](https://github.com/GangYunGit/TIL/blob/master/python/2022_07_20_TIL.md)

