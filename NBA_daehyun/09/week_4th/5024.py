# 파일 이름을 문제 번호로 수정해주신 뒤 발표할 문제에 대한 풀이를 작성해주세요!
# 여러 개의 문제를 가져오셨다면 파일을 복사해서 추가로 작성해주시기 바랍니다!
# 5024 병합정렬 swea
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    merged_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_0 = merge_sort(arr[:middle])
    right_0 = merge_sort(arr[middle:])

    return merge(left_0, right_0)



tc = int(input())

for n in range(tc):
    N = int(input())
    arrr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arrr)
    print(f'#{n + 1} {result[N//2]} {cnt}')