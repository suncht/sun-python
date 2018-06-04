from python_learning.models.user import User


list = []
for i in range(100):
    user = User(i)
    user.userName = 'name_' + str(i)
    user.age = 20 + i
    user.idcode = 'X100' + str(i)
    list.append(user)

for u in list:
    print(u)


str = ','.join(str(v.userName) for v in list)
print(str)
