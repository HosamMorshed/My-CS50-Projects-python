#cs50 week 6-> 3 , 4
#from cs50 import get_string , get_int 
#لو بدنا كل الي جوا المكتبة بنحط نجمه *

answer = input("what is your name? ")
print(f"hello {answer}")

try:#هنا بنحدد البداية تعت الكود الي ممكن يصير في خطأ لدي المستخدم 
    x= int(input ("x: "))
    y= int(input ("y: "))
except ValueError:#في حال صار خطأ راح يصير الي جوا هاي
#ValueError هاي لو بنتوقع خطأ بنوع البيانات المدخله فقط
    print("invalid value")
    exit()#هنا يعني اطلع من الكود كله و ما تنزلش لباقي الكود

print ( x + y )

