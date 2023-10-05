# https://stepik.org/lesson/265118/step/10?unit=246067

start_population, delta_per_day, days = int(input()), int(input()), int(input())

for i in range(days):
    actual_day = i + 1
    population = start_population * (1 + delta_per_day / 100) ** (actual_day - 1)
    print(actual_day, population)
