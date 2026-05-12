#Tools
newline = '\n -------------- \n'

#Settings
superheroes = ['Superman', 'Superwoman', 'Gravity Guy', 'Spiderman']
powers = ['Speed', 'Flying', 'Gravity', 'Webs']

print('Welcome to the game of SuperHeroes')
print(newline)

for index, superhero in enumerate(superheroes, start=1):
    print(f"{index}. {superhero}")

print(newline)
user = input('Choose your superhero: ')
print(newline)

match user:
    case "1":
        print('You are now ' + superheroes[0] + '\n')
        user = 1
    case "2":
        print('You are now ' + superheroes[1] + '\n')
        user = 2
    case "3":
        print('You are now ' + superheroes[2] + '\n')
        user = 3
    case "4":
        print('You are now ' + superheroes[3] + '\n')
        user = 4

print('You have the superpower: ' + powers[user - 1])
