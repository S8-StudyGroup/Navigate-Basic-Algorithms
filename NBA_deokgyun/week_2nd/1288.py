# 새로운 불면증 치료법

Test_count = int(input())
for i in range(1, Test_count + 1):
    number_for_multiple = int(input())
    number_for_count = 1
    set_of_numbers = set()

    while True:
        set_of_numbers.update(set([int(j) for j in str(number_for_multiple * number_for_count)]))

        if set_of_numbers == set(range(10)):
            break
        number_for_count += 1

    print("#{} {}".format(i, number_for_count * number_for_multiple))
