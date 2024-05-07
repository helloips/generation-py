# https://stepik.org/lesson/415554/step/9?unit=405083

TAIL_OF_COIN = 'Р'
FACE_OF_COIN = 'O'

max_seq_len = 0
current_seq_len = 0

for side in input() + FACE_OF_COIN:
    if side == TAIL_OF_COIN:
        current_seq_len += 1
    else:
        max_seq_len = max(max_seq_len, current_seq_len)
        current_seq_len = 0

print(max_seq_len)
