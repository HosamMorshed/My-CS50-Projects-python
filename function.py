# week [6 - 5] functions in python

#بنكتب ديف (def)
#مش بيتم تنفيذها غير لازم نستدعيها
def hello(name):
    print(f"Hello {name}")
    print("in the function")

def sum(num1 , num2):
    return num1 + num2

answer = input("whats your name? ")
hello(answer)
result =sum(3 ,2)
print(result + 3)
