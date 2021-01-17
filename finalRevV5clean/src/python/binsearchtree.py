class BST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, item: object, left=None, right=None, parent=None):
            self.item: object = item
            self.left = left
            self.right = right
            self.parent = parent

    def is_empty(self) -> bool:
        """
        retourne True si T est vide et False sinon
        :return: bool
        """
        return self.root is None

    def node(self, item, parent=None) -> Node:
        """
        retourne un objet du type Node
        :param item:
        :param parent:
        :return:
        """
        if item is not None:
            return self.Node(item, parent=parent)

    def print(self, mode: str = 'infixe'):
        """
        affiche les valeurs de T selon le type de parcours précisé par le paramètre mode,
        où mode est une chaîne de caractères qui peut prendre les valeurs prefixe, infixe, postfixe
        :param mode: type de parcours
        :return:
        """
        return self.__print(self.root, mode)

    def __print(self, node: Node, mode: str):
        if node is None:
            return
        else:
            if mode != 'prefixe':
                self.__print(node.left, mode)
            else:
                print(str(node.item), end=' ')

            if mode == 'prefixe':
                self.__print(node.left, mode)
            elif mode == 'postfixe':
                self.__print(node.right, mode)
            else:
                print(str(node.item), end=' ')

            if mode != 'postfixe':
                self.__print(node.right, mode)
            else:
                print(str(node.item), end=' ')

    def search_rec(self, item: object) -> Node:
        """
        retourne Node si item figure dans T et None sinon
        :param item: la valeur du nœud recherche
        :return:
        """
        return self.__search_rec(item, self.root)

    def __search_rec(self, item: object, node: Node) -> Node:
        if node is None:
            return None
        elif item == node.item:
            return node
        else:
            if item < node.item:
                return self.__search_rec(item, node.left)
            else:
                return self.__search_rec(item, node.right)

    def search_iter(self, item: object) -> Node:
        """
        retourne Node si item figure dans T et None sinon
        :param item: la valeur du nœud recherche
        :return:
        """
        node = None
        stack = list()
        stack.append(self.root)
        while len(stack) > 0 and node is None:
            cur = stack.pop()
            if cur is not None:
                if cur.item == item:
                    node = cur
                stack.append(cur.right)
                stack.append(cur.left)
        return node

    def insert(self, item: object):
        """
        insère la valeur item dans T si elle n’y figure pas et ne fait rien sinon
        :param item: la valeur à être inserée
        :return:
        """
        self.root = self.__insert(None, self.root, item)

    def __insert(self, parent: Node, node: Node, item: object) -> Node:
        if node is None:
            node = self.node(item, parent=parent)
            return node
        else:
            if item < node.item:
                node.left = self.__insert(node, node.left, item)
            elif item > node.item:
                node.right = self.__insert(node, node.right, item)
            return node

    def insert_list(self, items: list):
        """
        insère les valeurs de la liste items dans T qui n’y figurent pas déjà
        :param items:
        :return:
        """
        for item in items:
            self.insert(item)

    def delete(self, item: object) -> Node:
        """
        supprime le noeud de T portant la valeur item, s’il en existe un
        :param item:
        :return:
        """
        node = self.search_rec(item)
        if node is not None:
            self.__delete(node)
        return node

    def __delete(self, node: Node):
        """
        supprime le noeud node de T
        :param node: un nœud à supprimer
        :return:
        """
        if node.left is None:
            self.transplante(node, node.right)
        elif node.right is None:
            self.transplante(node, node.left)
        else:
            # node with two children: get the successor
            y = self.successor(node)
            if y.parent != node:
                self.transplante(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplante(node, y)
            y.left = node.left
            y.left.parent = y

    def transplante(self, u: Node, v: Node):
        """
        transplante le nœud v vers le nœud u
        :param u:
        :param v:
        :return:
        """
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        elif u.parent.right == u:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def successor(self, node: Node) -> Node:
        if node is not None:
            if node.right is not None:
                return self.__minimum(node.right)
            else:
                cur = node.parent
                while cur is not None and node == cur.right:
                    node = cur
                    cur = node.parent
                return cur

    def delete_all(self):
        """
        garbage collector will do this for us
        :return:
        """
        self.root = None

    def minimum(self) -> Node:
        """
        retourne la valeur la plus à gauche
        :return:
        """
        return self.__minimum(self.root)

    def __minimum(self, node) -> Node:
        if node.left is None:
            return node
        else:
            return self.__minimum(node.left)

    def maximum(self) -> Node:
        """
        retourne la valeur la plus à droite
        :return:
        """
        return self.__maximum(self.root)

    def __maximum(self, node) -> Node:
        if node.right is None:
            return node
        else:
            return self.__maximum(node.right)


def create_tree():
    tree = BST()
    tree.insert(3)
    tree.insert(4)
    tree.insert(0)
    tree.insert(8)
    tree.insert(2)
    return tree

def main():
    #     3
    # 0     4
    #   2      8
    modes = ['prefixe', 'infixe', 'postfixe']

    # create
    tree = create_tree()
    print('tree')
    tree.print(modes[1])
    print()

    # delete
    tree.delete(2)
    print('tree without 2')
    tree.print(modes[1])
    print()

    # search
    print('search_rec 4:', tree.search_rec(4).item)
    print('search_rec 10:', tree.search_rec(10))

    print('search_iter 4:', tree.search_iter(4).item)
    print('search_iter 10:', tree.search_iter(10))

    # successor
    print('successor 3:', tree.successor(tree.search_rec(3)).item)
    print('successor 4:', tree.successor(tree.search_rec(4)).item)

    # insert
    new_items = [21, 5, 4, 17, 3, 17, 33]
    tree.insert_list(new_items)
    print('new tree')
    tree.print(modes[0])
    print()

    # delete
    for i in new_items:
        tree.delete(i)
    print('tree without new items')
    tree.print(modes[0])


if __name__ == '__main__':
    main()
