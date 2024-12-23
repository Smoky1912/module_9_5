# зададим пользаковский класс искл-я, кот. наследуется
class StepValueError(ValueError):
    pass

class Iterator: # зададим класс Iterator
    # метод инициализации, приним. знач. старта, конца и шага итерации
    def __init__(self, start, stop, step=1):
        # проверка, что шаг не равен 0
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        # инициализируем атрибуты объекта
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # указатель на текущее число в итерации

    # метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора
    def __iter__(self):
        self.pointer = self.start
        return self

    # метод, увеличивающий атрибут pointer на step
    def __next__(self):
        # проверка усл. завершения итерации
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        # увеличиваем pointer на step и возвращаем его значение
        current_value = self.pointer
        self.pointer += self.step
        return current_value

# пример
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()