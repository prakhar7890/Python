a=0
b=1
c=0
i=1
n=int(input("Enter a no :"))
print(a)
print(b)
while(i<=n-2):
    c=a+b
    a=b
    b=c
    print(c," ")
    i=i+1
