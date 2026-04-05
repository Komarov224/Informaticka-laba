import json

# TODO решите задачу
def task() -> float:
    with open("input.json", 'r', encoding='utf-8') as f:
        data = json.load(f) #специальный метод, превращение в списки
    sum = 0.0

    for i in data: # так как вложенные словари в одном списке
        score = i.get("score")
        weight = i.get("weight")
        sum += score * weight

    return round(sum, 3) #округление

print(task())
