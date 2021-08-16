src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

a = [num1 for num1, num2 in zip(src[1:], src[:-1]) if num1 > num2]
print(a)
