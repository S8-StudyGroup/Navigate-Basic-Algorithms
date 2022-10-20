# [Programmers] 67256. 키패드 누르기
# Guest - 장현혁


def solution(numbers, hand):
    answer = ''
    # 휴대폰 키패드
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    # 왼손, 오른손 엄지의 좌표 정의
    left_thumb, right_thumb = (3, 0), (3, 2)

    # numbers의 길이만큼 반복
    for i in range(len(numbers)):
        # 시간 줄이기용 flag
        flag = False
        for r in range(4):
            for c in range(3):
                # 누르려는 번호 탐색
                if numbers[i] == phone[r][c]:

                    # 1. (1, 4, 7) 일때
                    if c == 0:
                        left_thumb = (r, c)
                        answer += 'L'
                        flag = True
                        break

                    # 2. (3, 6, 9) 일때
                    elif c == 2:
                        right_thumb = (r, c)
                        answer += 'R'
                        flag = True
                        break

                    # 3. (2, 5, 8, 0)일때
                    else:
                        # 거리가 더 작은 값 비교
                        l_dist = abs(left_thumb[0] - r) + abs(left_thumb[1] - c)
                        r_dist = abs(right_thumb[0] - r) + abs(right_thumb[1] - c)

                        # 거리가 더 작은 손으로 눌러준다
                        if l_dist < r_dist:
                            left_thumb = (r, c)
                            answer += 'L'
                            flag = True
                            break

                        elif l_dist > r_dist:
                            right_thumb = (r, c)
                            answer += 'R'
                            flag = True
                            break
                        # 거리가 같을 때는 밥 먹는손으로~
                        else:
                            if hand == 'left':
                                left_thumb = (r, c)
                                answer += 'L'
                                flag = True
                                break

                            else:
                                right_thumb = (r, c)
                                answer += 'R'
                                flag = True
                                break
            if flag:
                break

    return answer
