print(' ---Перед вами появились ворота с двумя каменными вставками для чисел.---')
print('---Подберите пароль для второй каменной вставки, чтобы выйти из ловушки---')
print('')
def password(num):
     stone_insert = ''
     for i in range(1, num):
         for j in range(2, num):
             if i >= j:
                 continue
             if num % (i + j) == 0:
                 stone_insert += str(i) + str(j)
     return stone_insert

n = int(input('Напишите во втором поле камня число от 3 до 20: '))


result = password(n)
print('Верный пароль от второй каменной вставки: ', result)



