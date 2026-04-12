from sys import argv
if len(argv) >= 2:
    print(f"Hello ,{argv[1]}")#بيطبع بس الاسم الاول
else:
    print("Hello ,World")

for i in argv[1:]:#حيطبع كل الاسماء الي دخلتها
    print(i)






