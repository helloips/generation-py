# https://stepik.org/lesson/284816/step/10?unit=266160

number_of_seats_in_the_compartments = 4
seat = int(input())
actual_compartment = ((seat - 1) // number_of_seats_in_the_compartments) + 1
print(actual_compartment)
