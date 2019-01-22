logins = {'john':'john123','sue':'sue123'}
employees = {1:'john',2: 'sue'}

#print(logins.keys())
#print(employees.keys())

list_of_login_keys = list(logins.keys())
print(list_of_login_keys)
for k in list_of_login_keys:
 print(k,' is equal to ',logins[k])

