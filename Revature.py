lst = ["very easy", "very easy", "easy", "easy", "medium", "medium", "hard", "hard"]
scores=[]
total_score =[]
student_scores = [[5, 5, 10, 10, 15, 15, 20, 20], 120]
value =0
result =""
def candidate_status(lst,total_score,Total,student_scores):
    for x in range(len(lst)):
        value = marks(lst[x])
        scores.append(value)
    total_score.append(scores)
    total_score.append(Total)
    #print(student_scores)
    #print(total_score)
    if student_scores[1] > total_score[1]:
        result="disqualified"
    
    else:
        if len(student_scores[0]) < len(lst):
            result="disqualified"
        else:
            for x in range(len(lst)):
                if student_scores[0][x] > scores[x]:
                    result ="disqualified"
                    break
                else:
                    result ="qualified"
    return result
    
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


print(candidate_status(lst,total_score,120,student_scores))