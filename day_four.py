# Iteration & loop

my_list=[1,2,3,4,5]
# for loop
for my_var in my_list:
    print(my_var)

print(my_var)


for x in range (0,10):
    print(x)


users=[{"username":"python", "id":1 },{"username":"typescript", "id":2,'email':"email.gmail.com" }]

for user in users:
    print(user['username'])
    if 'email' in user:
        print(user['email'])


for x in range(0,10):
    for user in users:
        if user['id']==x:
            print(user)

