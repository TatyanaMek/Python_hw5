# Игра против бота




from email import message
from random import choice, randint

from task1 import player_vs_player

player_vs_player()


def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nВаше имя: ')
    player_2 = 'Я Робот,у меня нет сердца'
    players = [player_1, player_2]
    print(f'\nВнимание {player_1} и  {player_2} игра началась!\n')
    print('\nКто первый начнет игру?\n')

    lucky = randint(-1, 0)

    print(f'Ура, {players[lucky+1]} Вы ходите первым!')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Я Робот,у меня нет сердца':
            print(
                f'\nХодит {players[lucky%2]} \nВ игре {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХодите,пожалуйста,  {players[lucky%2]} \nВ игре {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nИзвините,можно взять только {max_take} конфет, попробуйте еще раз: '))
        candies_total = candies_total - step

    print(f'В игре осталось {candies_total} \nПобеда за {players[lucky%2]}')

player_vs_bot()