from operator import itemgetter

class Computer():
    def __init__(self, id, name, cost, class_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.class_id = class_id

class DisClass():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class CompDC():
    def __init__(self, class_id, comp_id):
        self.class_id = class_id
        self.comp_id = comp_id

comps = [
    Computer(1, 'A123', 100, 1),
    Computer(2, 'B123', 200, 2), 
    Computer(3, 'A233', 150, 3),
    Computer(4, 'D123', 200, 4),
    Computer(5, 'E123', 300, 5),]

dis_classes = [
    DisClass(1, '312л'),
    DisClass(2, '313л'), 
    DisClass(3, '314л'),
    DisClass(4, '315л'),
    DisClass(5, '316л'),]

comp_dc = [
    CompDC(1, 1),
    CompDC(2, 2), 
    CompDC(3, 3),
    CompDC(3, 4),
    CompDC(3, 5),
    CompDC(4, 1),
    CompDC(4, 2),
    CompDC(4, 3),
    CompDC(5, 4),
    CompDC(5, 5),]

def main():
    one_to_many = [(c.name, c.cost, dc.name)
                   for dc in dis_classes
                   for c in comps
                   if c.class_id == dc.id]
    
    many_to_many_temp = [(dc.name, co.class_id, co.comp_id)
                    for dc in dis_classes
                    for co in comp_dc
                    if dc.id == co.class_id]
    
    many_to_many = [(c.name, c.cost, class_name)
                    for class_name, class_id, comp_id in many_to_many_temp
                    for c in comps if c.id == comp_id]

    print('Задание B1') 
    '''
    «дисплейный класс» и «компьютер» связаны соотношением один-ко-многим. Выведите список всех компьютеров, у которых название начинается с буквы «А», и названия их дисплейных классов.
    '''
    resultB1 = sorted(x for x in one_to_many if x[0].startswith('A'))
    for i in resultB1:
        print(f'Название: {i[0]}, класс: {i[2]}')

    print('\nЗадание B2')
    '''
    «дисплейный класс» и «компьютер» связаны соотношением один-ко-многим. Выведите список классов с минимальной ценой за компьютер в каждом дисплейном классе, отсортированный по минимальной цене.
    '''
    resultB2 = {}
    for class_name in set(x[2] for x in one_to_many):
        min_cost = min(x[1] for x in one_to_many if x[2] == class_name)
        resultB2[class_name] =  min_cost
    resultB2 = sorted(resultB2.items(), key=itemgetter(1))
    for i in resultB2:
        print(f'Класс: {i[0]}, минимальная стоимость: {i[1]}')

    print('\nЗадание B3')
    '''
    «дисплейный класс» и «компьютер» связаны соотношением многие-ко-многим. Выведите список всех связанных компьютеров и дисплейных классов, отсортированный по компьютерам, сортировка по дисплейным классам произвольная.
    '''
    resultB3 = sorted(many_to_many, key=itemgetter(0))
    for i in resultB3:
        print(f'Название: {i[0]}, класс: {i[2]}')
main()