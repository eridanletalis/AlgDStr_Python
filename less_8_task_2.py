from collections import Counter


class Node:
    def __init__(self, freq, val=None, left=None, right=None):
        self.freq = int(freq)
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, node):
        self.root = node

    def return_code(self, letter):

        def walk(node, acc, letter):
            flag = 0
            if node.left and flag == 0:
                return walk(node.left, acc + "0", letter)
            if node.right and flag == 0:
                return walk(node.right, acc + "1", letter)
            if str(node.val) == str(letter):
                flag = 1
                return acc

        acc = ""
        return walk(self.root, "", letter)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1

        return max_wdth

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
        self.get_width(root.right, level - 1)

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.val, end='')
        elif level > 1:
            self.print_given_level(node.left, level - 1)
            self.print_given_level(node.right, level - 1)

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1

def huffman(_string):
    counts = Counter(_string)  # получаем коллекцию с частотой
    Nd = []
    # преобразуем в массив листьев. Каждый дист имеет left и right=0
    while len(counts) > 0:
        val, freq = counts.popitem()
        Nd.append(Node(freq, val))

    # Обеспечиваем порядок по возрастанию переворачиваем для удобства работы с извлечением
    Nd.sort(key=lambda node: node.freq, reverse=1)
    while len(Nd) > 1:  # пока в массиве больше одного элемента
        node_left = Nd.pop()  # первый наименьший
        node_right = Nd.pop()  # второй наименьший
        # создаём узел из двух листьев.
        Nd.append(Node(node_left.freq + node_right.freq, left=node_left, right=node_right))
        # Обеспечиваем порядок по возрастанию переворачиваем для удобства работы с извлечением
        Nd.sort(key=lambda node: node.freq, reverse=1)

    tree = Tree(Nd[0])
    print(tree.height(tree.root))
    tree.print_level_order(tree.root)
    code = ""
    for letter in _string:
        code += tree.return_code(letter)
    return code

s = "beep boop beer!"
code = huffman(s)
print(code)
