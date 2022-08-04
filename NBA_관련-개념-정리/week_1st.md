# 1주차 회의 내용 관련 정리

## <br/>언패킹 연산자

  <br/>`packing`은 여러 개의 객체를 하나로 합쳐줄 때 사용하는 반면, 이와 반대되는 개념인 `unpacking`은 여러 개의 객체를 포함하고 있는 하나의 객체를 풀어줍니다.

  <br/>

  ```python
  # 예시

  numbers = [1, 2, 3]
  print(*numbers) # 1 2 3

  # 언패킹 되는 과정
  # 1. print(*numbers)
  # 2. print(*[1, 2, 3])
  # 3. print(1, 2, 3)
  # 4. 1 2 3이 출력됨
  ```

  ## <br>range(stop), range(start, stop[, step])
  
  <br/> range 함수는, 연속적인 숫자 객체를 만들어서 반환해주는 함수입니다. 불변형이고, 순서가 있는 시퀀스형입니다. 반복문 for와 함께 사용이 되기 때문에 알아둬야 할 필수 요소라고 생각하시면 되겠습니다.

  <br/>

  ```python
  # 예시

    for a in range(4):
      print(a, end=' ') # 0 1 2 3 (4는 출력되지 않습니다.)

    for b in range(1, 5):
      print(b, end=' ') # 1 2 3 4 (5는 출력되지 않습니다.)

    for c in range(1, 6, 2):
      print(c, end=' ') # 1 3 5

    for d in range(5, 2, -1):
      print(d, end=' ') # 5 4 3 (2는 출력되지 않습니다.)
  ```

  ## <br/> Pythonic swap

  <br/>프로그래밍 언어, 특히 c언어로 swap을 시도하면 이렇습니다.

  <br/>
  
  ```python
  a = 30
  b = 50

  temp = a
  a = b
  b = temp

  print(a, b) # 50 30
  ```

  <br/>하지만 파이썬에게는 파이써닉(pythonic)한 코드가 있습니다.

  <br>

  ```python
  a = 30
  b = 50

  a, b = b, a
  print(a, b) # 50 30
  ```

  <br/>물론 파이써닉한 코드도 좋은 코드이지만 회의에서도 말씀드렸다시피 가독성이 좋은 코드가 더 좋은 코드라고 할 수 있겠습니다!! 🙂

  ## <br/> f-string

  <br/>파이썬에서 문자열을 표현하는 방법은 여러 가지가 있지만, 그 중 가장 최근에 나왔으면서 깔끔한 표현방법이 f-string입니다. 다들 잘 사용하고 계셔서 다행입니다!

  <br/>

  ```python
  team_name = "NBA"
  count_members = 9

  print(f'저희 그룹스터디 이름은 {team_name}이며, 팀원은 총 {count_members}명입니다.')
  # 저희 그룹스터디 이름은 NBA이며, 팀원은 총 9명입니다.
  ```