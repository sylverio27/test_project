number = 1

while number <= 5:
    print(number)
    number = number + 1


number = 10

while number >= 5:
    print(number)
    number = number - 1


password = input('Введите пароль ')

while password != 'python123':
    print('Неверный пароль')
    password = input('Попробуйте еще раз ')

print('Доступ разрешен!')


number = int(input('Введите число '))

while number != 0:
    number = int(input('Введите снова '))

print('Программа завершена')