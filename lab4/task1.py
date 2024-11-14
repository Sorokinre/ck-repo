# TODO решите задачу
def task() -> float:
    total_score = 0
    score = 0
    weight = 0
    with open("input.json", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "score" in line:
                score = float(line[line.find("score") + 8:line.rfind(",")])
            elif "weight" in line:
                weight = float(line[line.find("weight") + 9:line.rfind("}")])
            if score and weight:
                total_score += score * weight
                score, weight = 0, 0
    return round(total_score, 3)


print(task())
