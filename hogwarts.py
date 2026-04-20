import csv
#1-score =0
houses ={
    "Gryffindor":0,
    "Ravenclaw":0,
    "Hufflepuff":0,
    "Slytherin":0
}
#2-open file 
file=open("hogwarts.csv","r")
#3-read house colume
reader=csv.DictReader(file)
#next(reader)
for row in reader:
    #4-add score
    houses[row["House"]] +=1
file.close()

#5-print score
for i in houses:
    print(f"{i} , {houses[i]}")