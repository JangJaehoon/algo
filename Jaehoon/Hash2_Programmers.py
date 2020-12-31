def solution(phone_book):
    answer = True
    finish = False
    phone_book = sorted(phone_book, key=len)
    for i in range(0, len(phone_book)):
        if finish:
            break
        current = phone_book[i]
        for j in range(i+1, len(phone_book)):
            match = phone_book[j]
            if len(current)<len(match) and current == match[0:len(current)]:
                answer = False
                finish = True
                break
    return answer