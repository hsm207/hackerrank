import sys

N = ['riya riya@gmail.com',
     'julia julia@julia.me',
     'julia sjulia@gmail.com',
     'julia julia@gmail.com',
     'samantha samantha@gmail.com',
     'tanya tanya@gmail.com']

names = []
for a0 in N:
    firstName, emailID = a0.split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    if emailID.endswith('gmail.com'):
       names.append(firstName)


print(*sorted(names), sep='\n')
