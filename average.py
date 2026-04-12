from cs50 import get_int

#core =[21,33,44]
#print(f"average: {(core[0]+core[1]+core[2])/3}")
#print (f"average: {sum(core)/len(core)}")

scores=[]
for i in range(3):
    score=get_int(f"enter your number {i +1}:")
    #scores.append(score)
    scores += [score]



print (f"average: {sum(scores)/len(scores)}")
