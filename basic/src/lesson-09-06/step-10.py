# https://stepik.org/lesson/1209103/step/10?unit=1289613

SUCCESS_MESSAGE = 'Все идет по плану'
ERROR_MESSAGE = 'Что-то пошло не так'

initial_weight = 100
reference_weight = 88
initial_days = 60
reference_weight_delta = (initial_weight - reference_weight) / initial_days

current_day = int(input())
current_weight = float(input())

reference_current_weight = initial_weight - (current_day * reference_weight_delta)

description = f'#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {reference_current_weight} кг'

if reference_current_weight >= current_weight:
    print(SUCCESS_MESSAGE)
else:
    print(ERROR_MESSAGE)

print(description)
