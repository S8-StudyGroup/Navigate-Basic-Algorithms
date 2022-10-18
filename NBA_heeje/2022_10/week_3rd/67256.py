# [Programmers] 67256. 키패드 누르기

# 키패드를 2차원 리스트로 변환(*와 #은 사용 안하므로 생략)
number_list = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


# 맨헤튼 거리 구하는 함수
def cal_distance(arr1, arr2):
    return abs(arr1[0] - arr2[0]) + abs(arr1[1] - arr2[1])


def solution(numbers, hand):
    answer = ''
    left_finger = [3, 0]
    right_finger = [3, 2]
    
    for number in numbers:
        
        if number in [1, 4, 7]:     # 숫자가 1, 4, 6이면
            temp = "left"           # 왼손 이용
            
        elif number in [3, 6, 9]:   # 숫자가 3, 6, 9이면
            temp = "right"          # 오른손 이용

        else:                       # 숫자가 2, 5, 8, 0이면

            # 해당 위치와 양손가락의 위치를 비교하여 더 가까운 손을 이용
            if cal_distance(number_list[number], left_finger) < cal_distance(number_list[number], right_finger):
                temp = "left"
            elif cal_distance(number_list[number], left_finger) > cal_distance(number_list[number], right_finger):
                temp = "right"

            # 거리마저 같다면 왼손잡이, 오른손잡이에 맞추기!
            else:
                temp = hand

        # answer에 이용한 손 넣고 해당 손 위치 이동
        if temp == "left":
            answer += "L"
            left_finger = number_list[number]
        else:
            answer += "R"
            right_finger = number_list[number]

    return answer
