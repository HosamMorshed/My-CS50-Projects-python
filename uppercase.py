from cs50 import get_string

before =get_string("before: ")
print(f"after: {before.upper()}")#بتخليها كابيتل
print(f"after: {before.lower()}")#بتخليها سمول 
print(f"after: {before.capitalize()}")#اول حرف كبير و الباقي صغير


#for c in before:
#    print(c.upper(), end="")
