#r  only read
#r+ read and write
#w  only write      and create new file and clear old data
#w+ read and write and create new file and clear old data
#a  only write      and create new file and save old data
import csv
name = input("name: ")
number = input("number: ")

with open ("test.csv","a+") as file:
    writer= csv.writer(file)
    writer.writerow([name ,number])



# بتعمل close لحالها




