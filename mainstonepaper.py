pc : str = str(input('ввод'))




player : str = str(input('ввод'))


if(pc=='ножницы' and player=='бумага'):
    print('pc won')
elif(pc=='бумага' and player=='ножницы'):
    print('player won')
elif(pc=='камень' and player=='бумага'):
    print('player won')
elif(pc=='бумага' and player=='камень'):
    print('pc won')
elif(pc=='ножницы' and player=='камень'):
    print('player won')
elif(pc=='камень' and player=='ножницы'):
    print('pc won')
elif(pc=='камень' and player=='камень'):
    print('nobody won')
elif(pc=='ножницы' and player=='ножницы'):
    print('nobody won')
elif(pc=='бумага' and player=='бумага'):
    print('nobody won')






