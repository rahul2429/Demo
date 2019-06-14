"""a=eval(input("Enter a number"))
b=eval(input("Enter another number"))
c=a>b
d= a==b
print("a>b is ",c)
print("a==b is",d)

a=eval(input("Enter a number"))
b=eval(input("Enter another number"))
c=input("Enter arithmetic operators")
if(c=="+"):
    print("a+b is",a+b)
elif(c=="-"):
    print("a-b is",a-b)
elif(c=="*"):
    print("a*b is",a*b)
elif(c=="/"):
    print("a/b is",a/b)
count = 5
s=0
while count!=0:
    num=eval(input("Enter a number"))
    s=s+num
    count=count-1
avg=s/5
print("The average is",avg)

s1="Orange"
s2="Banana"
for letter in s1:
    if letter in s2:
        print(s1,"and",s2,"share the letter",letter)

c=0
s1="aeiouAEIOU"
s2=input("Enter a word")
for letter in s1:
    if letter in s2:
        c+=1
print(c)

name="Rahul"
print(name[:])
print(name[0:])
print(name[:6])
print(name[:100])
print(name[:len(name)])
print(name[1:-1])
print(name[2],name[1:4])

name="rahul    "
name1="RAHUL"
print(name.upper())
print(name1.lower())
print(name.strip())
print(name.find("hul"))
print(name.replace("hul","luh"))

lst=[2,-3,0,4,-1]
print(lst[1])
lst[3]=2
lst[-2]=1
print(lst)

a=[2,4,6,8]
b=[1,3,5,7]
print(a+b)
print(a+[10,12,14,16])
a=list(range(-10,10))
print(a)
print(a is b)


a=list(range(0,20,1))
print(a[-10:-1])
a[2:5]=[20,21,22]
print(a)

fruits=["banana","apple","mango","guava","pineapple"]
fruits.append("papaya")
fruits.extend(["jackfruit","grapes","litchi"])
fruits.insert(2,"orange")
fruits.remove("apple")
print(fruits.pop(2))
print(fruits.index("guava"))
print(fruits)

s1=[x*x for x in range(1,26)if x%10!=5]
print(s1)"""

