import unicodedata
c=0
name=[]
decform=[]
count=[]
j=input("Enter the effing stuff:")
for i in j:
    c+=1
    names=unicodedata.name(i)
    name.append(names)
    decforms=ord(i)
    decform.append(decforms)
    count.append(c)
if c>1:
    print("\nNo of Characters:",c)
else:
    print("\nNo of Character:",c) 
for z in range(0,c,1):
    print(name[z],decform[z],"Character No:",count[z])
