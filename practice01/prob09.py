#문제9. 주어진 if 문을 dict를 사용해서 수정하세요.
menu = input('메뉴: ')

menu_dict = {'오뎅': 1000, '순대':500, '만두':400 }
print('가격: {0}'.format(menu_dict.get(menu)))