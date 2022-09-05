# 대각선 출력하기
# 이차원 리스트를 활용하여 배열의 대각선에 접근 및 할당

# +로 채워진 2차원 리스트 생성
diagonal = list(['+'] * 5 for _ in range(5)) 

# 배열의 대각선에 접근하려면 행과 열의 index값이 똑같으므로 arr[i][i]로 접근
for i in range(len(diagonal)):
        diagonal[i][i] = '#'
        print(*diagonal[i], sep='') # sep='' : 원소 사이의 공백을 없앰

