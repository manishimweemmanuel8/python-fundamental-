# Conditions & control flow

numbers=[1,4,9,16,25]
is_even=[]
is_odd=[]

# for else if in python we use elif

for num in numbers:
    if num % 2 ==0:
        print(num, 'is even')
        is_even.append(num)
    else:
        print(num, 'is odd')
        is_odd.append(num)


print(is_even, is_odd)

  
# while loop 
x=10
i=0
z=12
while i < x:
    print(i)
    i=i+1

x=10
i=0
z=12
while i < x:
    z=z*2
    if z > 342900:
        break
    print(z,i)
    i=i+ .000000000001

x=10
i=0
while i < x:
    if i % 2==0:
        print("even")
    else:
        continue
    i += 1

