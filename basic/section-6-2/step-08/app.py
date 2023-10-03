# https://stepik.org/lesson/265115/step/8?unit=246063

city_with_min_len, city_with_max_len = str(), str()

city = input()

city_with_min_len = city
city_with_max_len = city

city = input()

if len(city) < len(city_with_min_len):
    city_with_min_len = city
if len(city) > len(city_with_max_len):
    city_with_max_len = city

city = input()

if len(city) < len(city_with_min_len):
    city_with_min_len = city
if len(city) > len(city_with_max_len):
    city_with_max_len = city

print(city_with_min_len)
print(city_with_max_len)
