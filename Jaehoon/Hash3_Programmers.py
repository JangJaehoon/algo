def solution(clothes):
    closet = dict()
    num_category = []
    choice = 1
    
    for name, category in clothes:
        if category in closet:
            closet[category].append(name)
        else:
            closet[category] = [name]
    
    for key in closet.keys():
        num_category.append(len(closet[key]))
    
    for i in num_category:
        choice += i + 1
    choice -= 1
    
    return choice