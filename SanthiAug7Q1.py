#fujji_strings

a,b=input(),input()
c=set(a+b)
z=0
for i in c:
    if(a.count(i)!=b.count(i)):
        z+=(abs(a.count(i)-b.count(i)))
print(z)

"""
Sample:
Input: abc
        amnop
output:6
"""
