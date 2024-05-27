a=input("Enter a name without spaces:")
b=input("Enter another name without spaces:")
c=a+b
d="FLAMESflames"
q="FLAMES"
e=""
for i in c:
    if i not in d:
        e+=i
f=len(e)%6
g=""
h=""
z=""
y=""
s=""
##if x==1:
##    print("F"
##elif x==2:
##    print("L"
##elif x==3:
##    print("A"
##elif x==4:
##    print("M")
##elif x==5:
##    print("E"
##elif x==0:
##    print("S"
#aj
#pri
for j in range(1,f+1):
    if j!=f:
        g+=q[j]
print(g)
for k in range(1,f+1):
    if k!=f:
        h+=g[k]
print(h)
for l in range(1,f+1):
    if l!=f:
        z+=h[l]
print(z)
for m in range(1,f+1):
    if m!=f:
        y+=z[m]
print(y)
for n in range(1,f+1):
    if n!=f:
        s+=y[n]
print(s)

    
    
    
