# https://stepik.org/lesson/415553/step/4?unit=405082

COST_IN_CENTS = 60
CENTS_IN_UNIT = 100

text = input()
total_cost_in_cents = len(text) * COST_IN_CENTS

print('{} р. {} коп.'.format(total_cost_in_cents // CENTS_IN_UNIT, total_cost_in_cents % CENTS_IN_UNIT))
