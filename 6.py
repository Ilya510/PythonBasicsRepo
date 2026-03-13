a = int(input())
b = int(input())

max_sum = -1
result_number = -1

for num in range(a, b + 1):
    current_sum = 0
    # Находим все делители числа num
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            current_sum += i
            if i*i != num:
                current_sum += num // i
    
    # Если текущая сумма больше или равна максимальной, обновляем результат
    # Равенство (>=) обеспечивает выбор наибольшего числа при одинаковых суммах
    if current_sum >= max_sum:
        max_sum = current_sum
        result_number = num

print(result_number, max_sum)