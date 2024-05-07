# https://stepik.org/lesson/415554/step/8?unit=405083

USER_1_NAME = 'Тимур'
USER_2_NAME = 'Руслан'
DRAW_NAME = 'ничья'

choice_1 = input()
choice_2 = input()

winner_name = ''
if choice_1 == choice_2:
    winner_name = DRAW_NAME
elif choice_1 == 'камень' and choice_2 == 'ножницы':
    winner_name = USER_1_NAME
elif choice_1 == 'камень' and choice_2 == 'ящерица':
    winner_name = USER_1_NAME
elif choice_1 == 'бумага' and choice_2 == 'камень':
    winner_name = USER_1_NAME
elif choice_1 == 'бумага' and choice_2 == 'Спок':
    winner_name = USER_1_NAME
elif choice_1 == 'ножницы' and choice_2 == 'бумага':
    winner_name = USER_1_NAME
elif choice_1 == 'ножницы' and choice_2 == 'ящерица':
    winner_name = USER_1_NAME
elif choice_1 == 'ящерица' and choice_2 == 'Спок':
    winner_name = USER_1_NAME
elif choice_1 == 'ящерица' and choice_2 == 'бумага':
    winner_name = USER_1_NAME
elif choice_1 == 'Спок' and choice_2 == 'ножницы':
    winner_name = USER_1_NAME
elif choice_1 == 'Спок' and choice_2 == 'камень':
    winner_name = USER_1_NAME
else:
    winner_name = USER_2_NAME

print(winner_name)
