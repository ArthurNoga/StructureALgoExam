from nodeClass import Node


class LinkedList():

    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.taille: int = 0

    def __str__(self):
        n: Node = self.first
        affichage: str = ""
        for i in range(0, self.taille):
            if n.get_value() is None:
                break
            else:
                res = str(n.get_value())
                affichage += res
                n = n.get_next()
            if i != self.taille - 1:
                affichage += " <-> "
        return affichage

    def add(self, element, index: int = None) -> None:
        """

        """
        if index is None:
            # on ajoute à la fin
            self.__addLast__(element)
        else:
            if index == 0:
                self.__addFirst__(element)

            elif index == self.taille:
                self.__addLast__(element)

            elif 0 < index < self.taille:
                newnode = Node(None, element, None)
                nodeindex: Node
                # celui précédant l'index dois rediriger vers notre newNode
                nodeindex = self.__getNode__(index)
                newnode.set_prev(nodeindex.get_prev())
                nodeindex.get_prev().set_next(newnode)

                # celui après l'index dois rediriger vers notre newNode
                newnode.set_next(nodeindex)
                nodeindex.set_prev(newnode)


            else:
                raise IndexError("L'index est incorrect")

    def __addFirst__(self, element) -> None:
        # Créer un noveau noeud contenant ta valeur et que son next = self.first
        # self.first => next = nouveau noeud
        # self.first = nouveau noeud
        newnode = Node(None, element, self.first)

        if self.first is None:
            self.first = self.last = newnode
        else:
            self.first.set_prev(newnode)
            self.first = newnode

        self.taille += 1

    def __addLast__(self, element) -> None:
        # Créer un noveau noeud contenant ta valeur et que son prev = self.last
        # self.last => next = nouveau noeud
        # self.last = nouveau noeud
        newnode = Node(self.last, element, None)

        if self.first is None:
            self.first = self.last = newnode
        else:
            self.last.set_next(newnode)
            self.last = newnode

        self.taille += 1

    def __getNode__(self, index: int) -> Node:
        indexnode: Node = self.first
        for i in range(0, index):
            indexnode = indexnode.get_next()

        return indexnode

    def get(self, index: int):
        if 0 <= index < self.taille:
            indexnode: Node = self.first
            for i in range(0, index):
                indexnode = indexnode.get_next()
            return indexnode.get_value()
        else:
            raise IndexError("Erreur d'index")

    def set(self, element, index: int) -> None:
        if 0 <= index < self.taille:
            indexnode: Node = self.first
            for i in range(0, index):
                indexnode = indexnode.get_next()
            indexnode.set_value(element)
        else:
            raise IndexError("Erreur d'index")

    def remove(self, element=None, index: int = None) -> None:
        if element is None and index is None:
            raise IndexError("Il faut au moins 1 paramètre")
        elif element is not None:
            f: Node = self.first
            for i in range(0, self.taille):
                if f.__eq__(element):
                    # on supprime l'élement et on réajuste notre collection
                    self.__deleteNode__(i)
                    self.taille -= 1
                    break
                f = f.get_next()
        else:

            self.__deleteNode__(index)
            self.taille -= 1

    def __deleteNode__(self, index):
        """

        """

        n: Node = self.__getNode__(index)
        if index == 0:
            self.first = self.first.get_next()
            if self.first is None:
                self.last = None
            else:
                self.first.set_prev(None)

        elif index == self.taille - 1:
            self.last = self.last.get_prev()
            if self.last is None:
                self.first = None
            else:
                self.last.set_next(None)

        elif 0 < index < self.taille:
            n.get_prev().set_next(n.get_next())
            n.get_next().set_prev(n.get_prev())
        else:
            raise IndexError("Erreur d'index")

    def clear(self) -> None:
        for i in range(0, self.taille):
            self.__deleteNode__(0)
        self.taille = 0

    def size(self) -> int:
        return self.taille

    def is_empty(self) -> bool:
        return self.first is None

    def contains(self, element) -> bool:
        f: Node = self.first
        for i in range(0, self.taille):
            if f.__eq__(element):
                return True
            f = f.get_next()
        return False

    def index_of(self, element) -> int:
        n: Node = self.first
        for i in range(0, self.taille):
            if n.__eq__(element):
                return i
            n = n.get_next()
        return -1

    def bad_insertion_sort(self):
        # Ne pas utiliser les méthodes self.get() et self.set() => uniquement les fonctions de Node (get_prev, get_next, ...)
        #node: Node = self.first.get_next()
        for i in range(1, self.taille):
            k: int = self.get(i)
            #k = node.get_value()
            j = i - 1
            while j >= 0 and self.get(j) > k:
                n: Node = self.__getNode__(j + 1)
                n.set_value(self.get(j))
                j -= 1
            self.set(k, j + 1)

    def insertion_sort(self):
        # Ne pas utiliser les méthodes self.get() et self.set() => uniquement les fonctions de Node (get_prev, get_next, ...)
        node: Node = self.first.get_next()
        while node.get_next() is not None:
            k = node.get_value() # 1
            j = node.get_prev() # None
            while j is not None and j.get_value() > k:
                n: Node = j.get_next() # Node(4)
                n.set_value(j.get_value()) # Node(4) = 2
                j = j.get_prev()

            # j = None || j = Node
            # Si j = Node => faire traitement normal
            # Si j = None => remplacer le premier element

            if j is not None:
                j.get_next().set_value(k) # Node(4) = 4
            else:
                self.first.set_value(k)
            node = node.get_next()



    def merge_sort(self):

        #création d'une LinkedList contenant nos résultats, on pointe ainsi juste le premier et dernier vers ceux du res (=> self = res)
        res = self.__triFusion__(self)
        self.first = res.first
        self.last = res.last

    def __triFusion__(self, lk: 'LinkedList'):
        """
        Au lieu de travailler avec des listes gauche et droite, on crée des LinkedList gauche et LinkedList droite
        Dans ce cas-là, __triFusion__ retourne une LinkedList trié (c'est comme ça que l'on aura notre Lk resultat
        """
        if lk.size() == 1:
            return lk
        else:
            q: int = lk.size() // 2
            L: LinkedList = LinkedList()
            R: LinkedList = LinkedList()
            n: Node = lk.first
            for i in range(0, q):
                L.add(n.get_value())
                n = n.get_next()
            for i in range(q, lk.size()):
                R.add(n.get_value())
                n = n.get_next()

            # Aouter dans L => toutes les valeurs de 0 à q
            # Ajputer  dans R => toutes les valeurs de q+1 a lk.size()
            L = self.__triFusion__(L)
            R = self.__triFusion__(R)
            res = self.__fusionner__(L, R)
            return res

    def __fusionner__(self, L: 'LinkedList', R: 'LinkedList'):
        """

        """

        res: LinkedList = LinkedList()

        # Boucler sur L n'est pas vide et R n'est pas vide
        # Si L[k] <= R[k] => res.append(L[k])
        # Sinon => res.append(R[k])
        # Supprimer L[k] ou R[k]
        while L.is_empty() == False and R.is_empty() == False:
            if L.get(0) <= R.get(0):
                res.add(L.get(0))
                L.remove(None, 0)
            else:
                res.add(R.get(0))
                R.remove(None, 0)

        # Soit R soit L est vide
        if L.is_empty():
            n: Node = R.first
            while n is not None:
                res.add(n.get_value())
                n = n.get_next()
        else:
            n: Node = L.first
            while n is not None:
                res.add(n.get_value())
                n = n.get_next()

        return res

    def dichotomic_search(self, element) -> int:
        """
        Ne change pas grande chose comparé à une recherche sur une liste
        """
        p: int = 0
        r: int = self.taille - 1
        while p <= r:
            q: int = (p + r) // 2
            if self.get(q) == element:
                return q
            elif self.get(q) > element:
                r = q - 1
            else:
                p = q + 1
        return -1
