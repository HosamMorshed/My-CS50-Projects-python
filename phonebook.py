from cs50 import get_string
people ={
    "hossam":'0592976',
    'dived':'556644',
    "ahmed":'01002'
}

name=get_string("name: ")
if name in people:
    print( people[name] )
else:
    print("not found")