def solution(participant, completion):
    compare = {}
    for i in participant:
        if i in compare:
            compare[i] += 1
        else:
            compare[i] = 1
    for i in completion:
        if compare[i] == 1:
            del compare[i]
        else:
            compare[i] -= 1
    failure = list(compare.keys())[0]
    return failure