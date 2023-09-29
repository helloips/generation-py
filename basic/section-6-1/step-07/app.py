# https://stepik.org/lesson/265105/step/7?unit=246053

dog_years = int(input())

human_years = dog_years * 10.5 if dog_years <= 2 else (dog_years - 2) * 4 + 21

print(human_years)
