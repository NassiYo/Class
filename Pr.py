#Кондитерский магазин

#Головной класс
class Nyam_nyam:
    def Name(self,name):
        return name

#Подкласс головного класса
class Sweet(Nyam_nyam):
    def Kind(self,pf):
        return pf
        
x1 = Sweet()
x2 = Sweet()

#1 подкласс класса Sweet
class Sweet_1(Sweet):
    def Kinds_1(seld,knd_1):
        return knd_1
    
#2 подкласс класса Sweet
class Sweet_0(Sweet):
    def Kinds_0(self, knd_0):
        return knd_0

x2 = Sweet()
x1 = Sweet_1()
x0 = Sweet_0()

inp = input('Вывести таблицу вкусняшек? (Да/Нет)   ')
print('\n')
if inp == 'Да':
    while True:
        print('+'+'-'*41+'+')
        print('|{0:41}|'.format(x2.Name('Вкусняшка')))
        print('+'+'-'*41+'+')
        print('|{0:20}|{1:20}|'.format(x2.Kind('Сдадость'), x2.Kind('Несладость')))
        print('+'+'-'*41+'+')
        print('|{0:20}|{1:20}|'.format('   |   ', '   |   '))
        print('|{0:20}|{1:20}|'.format('   |   ', '   |   '))
        print('|{0:20}|{1:20}|'.format('   \/   ', '   \/   '))
        print('+'+'-'*41+'+')
        print('|{0:20}|{1:20}|'.format(x1.Kinds_1('Шоколадный кекс'), x0.Kinds_0('Пирожок с капустой')))
        print('|{0:20}|{1:20}|'.format(x1.Kinds_1('Яблочный пай'), x0.Kinds_0('Пирожок с мясом')))
        print('|{0:20}|{1:20}|'.format(x1.Kinds_1('Творожный пай'), x0.Kinds_0('Пицца')))
        print('|{0:20}|{1:20}|'.format(x1.Kinds_1('Ватрушка с творогом'), x0.Kinds_0('Курник')))
        print('|{0:20}|{1:20}|'.format(x1.Kinds_1('Молочный корж'), x0.Kinds_0('Слойка с сосиской')))
        print('+'+'-'*41+'+')
        print('\n')
        inp_1 = input('Вывести еще раз? (Да/Нет)   ')
        print('\n')
        if inp_1 == 'Нет': break
#print(x.f.cl())
#class Pies(nyam_nyam):
   # def __init__(self):
