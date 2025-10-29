

#



import random

figures: list[str] = ('камень','ножницы','бумага')


while True:
    u_c:str = input('ввод')
    c_c:str = random.choice('камень','ножницы','бумага')
    print('выбор пк',c_c)



    if (u_c == 'камень' and c_c =='ножницы') \
        or (u_c=='ножницы' and c_c=='бумага')\
            or (u_c =='бумага' and c_c=='камень'):
            print('win')
    elif(u_c ==c_c):
            print('tie')
    elif u_c not in ('камень','ножницы','бумага'):
            print('whaaaat?')
    else:
            print('lose')

    user_break: str = input('continue? (y/n):')


    if user_break =='y':
        continue
    elif user_break not in ('y','n'):
        print('dont understand')
        break
    

