# https://stepik.org/lesson/327221/step/4?unit=310520

phone = input()
phone_parts = phone.split('-')

if len(phone_parts) == 3:
    if not phone_parts[0].isdigit() or not phone_parts[1].isdigit() or not phone_parts[2].isdigit():
        print('NO')
    elif len(phone_parts[0]) != 3 or len(phone_parts[1]) != 3 or len(phone_parts[2]) != 4:
        print('NO')
    else:
        print('YES')
elif len(phone_parts) == 4:
    if phone_parts[0] != '7' or not phone_parts[1].isdigit() or not phone_parts[2].isdigit() \
            or not phone_parts[3].isdigit():
        print('NO')
    elif len(phone_parts[1]) != 3 or len(phone_parts[2]) != 3 or len(phone_parts[3]) != 4:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
