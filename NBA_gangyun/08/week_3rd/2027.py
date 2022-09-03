# 대각선 출력하기


my_text = "#++++"
print(my_text)
for i in range(4):
    my_text = my_text.replace("#+", "+#")
    print(my_text)
