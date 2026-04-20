#r ->only read
#w ->only write "clear old data"
#a ->append "whise save to old data"

#open file 
file=open("file.txt","r")

#do what you want
data = file.read()#اقرأ الملف
print(data)
data = file.readable()#هل الملف قابل للقراءة او لا bool
print(data)
#close file
file.close()


