# https://stepik.org/lesson/327221/step/2?unit=310520

result = list()
l_numbers = [int(i) for i in input().split()]
m_numbers = [int(i) for i in input().split()]

for i in range(min(len(l_numbers), len(m_numbers))):
    result.append(l_numbers[i] + m_numbers[i])

print(*result)
