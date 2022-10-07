lst = ["very easy", "very easy", "easy", "easy", "medium", "medium", "hard", "hard"]
scores=[]
total_score =[]


def marks(difficulty):
    mark=0
    if difficulty == "very easy":
        mark =5
    elif difficulty =="easy":
        mark =10
    elif difficulty =="medium":
        mark =15 
    elif difficulty == "hard":
        mark =20
    return mark


def interview(student_scores,Time):
    for x in range(len(lst)):
        value = marks(lst[x])
        scores.append(value)
    total_score.append(scores)
    total_score.append(120)

    if Time > total_score[1]:
        result="disqualified"
    
    else:
        if len(student_scores) < len(lst):
            result="disqualified"
        else:
            for x in range(len(lst)):
                if student_scores[x] > scores[x]:
                    result ="disqualified"
                    break
                else:
                    result ="qualified"
    return result

    

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64)) 
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120)) 
print(interview([5, 5, 10, 10, 15, 15, 20], 120)) 
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 150)) 

