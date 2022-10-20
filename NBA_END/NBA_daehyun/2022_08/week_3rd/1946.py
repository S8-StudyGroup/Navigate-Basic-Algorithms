# 간단한 압축풀기

## 아이디어 : 일단 입력받은 모든 알파벳을 한줄로 다 붙여서 받은 다음에 10개씩 출력하는 방식

tc = int(input())

for i in range(tc):

    N = int(input())

    result_tmp = ''  ##임시 결과를 담을 변수

    for j in range(N):  ## 줄의 개수 N만큼 입력을 받는다
        a, b = input().split()  # a에는 알파벳  b에는 알파벳의 개수를 받는다
        result_tmp += a * int(b)  ## 전부 한줄로 더한다

    print(f'#{i + 1}')
    for k in range(1, len(result_tmp) + 1):  ## 한줄로 받은 변수  result_tmp의 길이만큼 프린트 반복, 1부터 시작하도록 했음
        if k % 10 != 0:  ## 10으로 나눈 나머지가 0이 아니면 줄을 바꾸지 않고 프린트 하는걸로 한다.
            print(result_tmp[k - 1],
                  end='')  ## 처음부터 줄을 바꾸지 않고 10개를 채워야하기때문에 인덱스 k는 1부터 시작한다. 그러면 첫번째부터 9번째까지는 줄을 바꾸지않고 출력된다.
        else:  ## 그게 아니면 프린트
            print(result_tmp[k - 1])

    print()  ## 이걸 추가 안하면 마지막 직전 프린트가 end='' 일경우 테스트 케이스 번호가 붙어서 나옴








