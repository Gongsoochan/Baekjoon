scorelist = []
for i in range(5):
    score=int(input())
    if score<40:
        score=40
    scorelist.append(score)
print(sum(scorelist)//5)