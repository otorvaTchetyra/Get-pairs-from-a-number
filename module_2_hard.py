def find_pairs(n):
    #Используем множество (set) для хранения уникальных пар. Множество автоматически удаляет дубликаты одинаковых пар
    #Генерируем список для создания пар
    unique_pairs = set()
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                unique_pairs.add((i, j))
    return list(unique_pairs)
    #Далее создаём цикл While, где он завершится, если ввести установленное число.  В противном случаее попросит заново написать число.
while True:
    try:
        n = int(input("Введите число от 3 до 20: "))
        if 3 <= n <= 20:
            break
        else:
            print("Число должно быть от 3 до 20.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

result = find_pairs(n)
print("Пароль: ", end='')
for pair in result:
    print(pair[0], pair[1], end=' ')