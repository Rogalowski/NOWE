from random import choice as c

def randPass(leng):
    all  = 'qwertyuiopasdfghjklzxcvbnm', 'QWERTYUIOPASDFGHJKLZXCVBNM', '!@#$%^&*()}{:"<>?[];",./|\'\\', '1234567890'

    pswd = { c(i) for i in all }
    while len(pswd) < leng: pswd.add(c(c(all)))
    txt = ''
    for i in pswd: txt += i

    return txt

print(randPass(int(input('Ile znaków: '))))



# from random import choice as c

# leng = int(input('Ile znaków: '))
# all  = 'qwertyuiopasdfghjklzxcvbnm', 'QWERTYUIOPASDFGHJKLZXCVBNM', '!@#$%^&*()}{:"<>?[];",./|\'\\', '1234567890'

# pswd = { c(i) for i in all }
# while len(pswd) < leng: pswd.add(c(c(all)))

# print(*pswd, sep='')