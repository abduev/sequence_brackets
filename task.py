class Stack:
    def __init__(self) -> None:
        # Инициализация стека как пустого списка
        self.items = []

    def push(self, item) -> None:
        # Добавление элемента в стек
        self.items.append(item)

    def pop(self) -> None:
        # Удаление верхнего элемента из стека
        self.items.pop()


class SequenceBracketsValidator:
    def __init__(self, sequence: str) -> None:
        # Инициализация SequenceBracketsValidator с заданной последовательностью скобок
        self.sequence = sequence
        self.stack = Stack()

    def check_sequence(self) -> bool:
        # Проверка корректности последовательности скобок
        for elem in self.sequence:
            if elem == '(':
                # Если встречена открывающая скобка, добавляем ее в стек
                self.stack.push(elem)
            elif elem == ')':
                # Если встречена закрывающая скобка, проверяем соответствие с верхним элементом стека
                if len(self.stack.items) > 0 and self.stack.items[-1] == '(':
                    # Если соответствие есть, удаляем верхний элемент стека
                    self.stack.pop()
                else:
                    # Если соответствия нет или стек пуст, последовательность некорректна
                    return False

        # После обхода всей последовательности, стек должен быть пустым для корректной последовательности
        return len(self.stack.items) == 0


if __name__ == '__main__':
    sequence = input("Введите последовательность скобок: ")
    validator = SequenceBracketsValidator(sequence)
    if validator.check_sequence():
        print("Последовательность скобок корректна.")
    else:
        print("Последовательность скобок некорректна.")
