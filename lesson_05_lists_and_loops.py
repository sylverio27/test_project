numbers = [3, 12, 7, 25, 4, 18, 9, 30]

result = []
for res in numbers:
    if res > 10:
        result.append(res)

print(result)



numbers = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)



films = ['Tron Legacy', 'Taxi 2', 'Taxi', 'Naruto', 'One Piece']

long_films = []
for film in films:
    if len(film) > 5:
        long_films.append(film)

print(long_films)