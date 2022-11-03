# SQLD

#### SQL 명령문 개괄

- From-where-groupby-having-select-orderby

- DML - select, insert, delete, update
  
  DDL - alter, create, modify, drop
  
  TCL - rollback, commit
  
  DCL - grant, revoke

#### select

- distinct (집약)
  
  - 중복된 값을 제거하고 집약
  
  - 예시)  DISTINCT depth,mgr -> (depth, mgr)에 대해 집약 == group by (depth,mgr)

- alias
  
  - AS 
    
    - select
      
      1) as 생략가능
      
      2) column명에 띄어쓰기 있는 경우, ex) "직원 번호"
    
    - from 
      
      1) as **사용불가!!!**

- concat 연산자 ( concat(().()) )
  
  - "+" : sql server
  
  - "=" : oracle
  
  - 인수가 반드시 **2개!**

#### 논리연산자

- 연산순위
  
  - not > and > or

- and
  
  - A and B

- or
  
  - A or B

- not
  
  - not A, B

#### SQL 연산자

- A **Between** B **and** C : B <= A <= C

- A **In** (1,2,3,) : A = 1 or A = 2 or A = 3

- <mark>LIKE</mark>
  
  - 와일드 카드
    
    - "\_" : 한 글자
    
    - "%" : 0개 이상의 글자
  
  - escape
    
    - ex) ename like 'A_A'
      
      LIKE escape 와일드카드(\_, %)를 문자로 취급!
      
      -> like 'A@\_A' ESCAPE '@' -> @는 아무문자나 가능!!

- Rownum(oracle)
  
  - where 조건절에서 Rownum = 1인 경우 포함
  
  - **select** empno, sal **from** emp **where** rownum <= 3 **order by** sal **desc**
    
    -> order by sal 이 가장 마지막
    
    -> 정렬 전에 rownum에 대해 먼저 실행 후 sal 순서로 정렬

- Top(sql server)
  
  - select top (n) <컬럼명> : 상위 n개

- <mark>Null</mark>
  
  - Null의 정의
    
    - 부재, 모르는값
    
    - null + 2, null - 4 **산술연산** => null
    
    - null == null, null == 2 등 **비교연산** => 알수없음(unknown) : where의 조건일시 false로 인식
    
    - 정렬상 의미
      
      - oracle : 무한대 -> 오름차순시 제일 마지막 나옴
      
      - SQLserver : 음의 무한대 -> 오름차순시 제일 먼저 나옴
  
  - NVL(값1, 값2) : 값1이 null이면 값2, 아니면 값1
  
  - NVL@(값1, 값2, 값3) : 값1이 null이면 값3, 아니면 값2
  
  - isnull(값1, 값2) : NVL과 동일
  
  - null if ( 값1, 값2) : 같으면 NULL, 다르면 값1
  
  - coaless -> 널아닌 첫번째 값(값1, 값2, ...) : 값1, 값2 순으로 보다가 null 아닌 첫번째 값

- 정렬
  
  - 정렬의 특성
    
    - **<mark>가장 마지막에 실행</mark>**
    
    - 성능이 느려질 수 있다.
    
    - null 값과의 관계
  
  - 컬럼번호정렬 : 출력되는 컬럼의 수보다 큰값 **불허**
  
  - 인수두개 정렬 : sal desc, ename asc -> sal이 같은 경우 ename 오름차순
  
  - select ename (a) orderby sal : (a) 자리에 sal가 없지만 orderby에 sal 사용가능

- 숫자 함수
  
  - round 자릿수 확인하기
    
    - round(138.94) -> 8은 0, 9는 1, 4는 2
  
  - ceil(oracle)/ceiling(sql server)

- 문자열 함수
  
  - upper/lower
  
  - Lpand, Rpad, Ltrim, Rtrim
  
  - substring,instring (실습)

- 날짜 함수
  
  - to_char/to_data (실습) -> 형변환 
  
  - sysdate(oracle), getdate(sql server)
  
  - 날짜데이터 + 100 -> 100일 이후 : 숫자 더하면 day로 인식

- DECODE/CASE
  
  - CASE!!!!
    
    - CASE WHEN    
    
    - CASE THEN
    
    - else : else가 없는 경우 위에 둘다 만족안하면 NULL 나옴
    
    - DECODE 실습

- 집계함수
  
  - NULL과의 관계
    
    - sum의 경우 null 빼고 샘
    
    - sum(A+B+C)의 경우 A+B+C 컬럼 만들고 계산

- GROUP BY
  
  - 집약기능
  
  - where 다음
  
  - 그룹수준으로 정보를 바꿈

- JOIN
  
  - natural join / using : 중복된 컴럼 하나로 줄임, 그리고 제일 앞에 등장, using은 table aliasing 사용 금지
  
  - A left outer join B => A  col 1 = b col 1 (+)
  
  - **FROM A, B, C  일 경우 : A, B JOIN 후 C와 JOIN**

- 서브쿼리
  
  - SELECT : scalar
  
  - FROM : inlineview -> 메인쿼리의 컬럼사용가능
  
  - WHERE -> 거의 모든 서브쿼리
  
  - ~~GROUP BY~~
  
  - HAVING -> 거의 모든 서브쿼리
  
  - ORDER BY : scalar
  
  - IN
  
  - ANY/SOME
  
  - ALL
  
  - EXIST

- (45,13)
