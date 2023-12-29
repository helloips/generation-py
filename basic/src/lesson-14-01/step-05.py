# https://stepik.org/lesson/334152/step/5?unit=317561

# объявление функции
def get_shipping_cost(quantity):
    return 1000 * 1 + 120 * (quantity - 1)


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
