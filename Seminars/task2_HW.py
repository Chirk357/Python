# Задача 2: 

# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = 123
sum = 0

while(a > 0):
    b = a % 10
    a = a // 10
    sum = sum + b
print(sum)
