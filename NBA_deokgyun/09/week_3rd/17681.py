# [Programmers] 17681. [1차] 비밀지도


def solution(n, arr1, arr2):
    maze_string = ""
    answer = []
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if arr1[i] & 1 << j or arr2[i] & 1 << j:
                maze_string += "#"
            else:
                maze_string += " "
        answer.append(maze_string)
        maze_string = ""
    return answer
