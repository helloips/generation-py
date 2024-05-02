# https://stepik.org/lesson/303084/step/7?unit=284991

ERROR_MESSAGE = 'COMMENT SHOULD BE DELETED'


def is_correct_comment(comment_for_checking):
    return not comment_for_checking.isspace() and comment_for_checking != ''


comments = list()
n = int(input())

for _ in range(n):
    comments.append(input())

index = 1

for comment in comments:
    print(index, ': ', comment if is_correct_comment(comment) else ERROR_MESSAGE, sep='')
    index += 1
