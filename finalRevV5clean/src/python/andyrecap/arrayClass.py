import ctypes
import math


class DynamicArray(object):

    def __init__(self, capacity: int = 10):
        self.n: int = 0  # by default
        self.capacity: int = capacity  # by default
        self.A = self.__make_array(self.capacity)

    def __str__(self):
        """
        return the array representation
        :return: str of the array
        """
        return str([self.A[i] for i in range(self.n)])

    def __len__(self):
        """
        return number of elements in the array
        :return: n size of the array
        """
        return self.n

    def __getitem__(self, k: int):
        """
        return the element at the index k
        :param k: int index
        :return: element
        """
        if not 0 <= k < self.n:
            return IndexError('index k is out of bounds')
        return self.A[k]

    def __setitem__(self, k: int, element: object):
        """
        set the element at index k
        :param k: index
        :param element:
        :return:
        """
        if not 0 <= k < self.n:
            return IndexError('index k is out of bounds')
        self.A[k] = element

    def __resize(self, new_cap: int):
        """
        internal method to resize the array
        :param new_cap: new capacity
        :return:
        """
        # declare array B with the new capacity
        B = self.__make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]  # referencing the elements from array A to B
        self.A = B  # A is now the array B
        self.capacity = new_cap  # resets the capacity

    def __make_array(self, new_cap: int):
        """
        make a new array using ctypes
        :param new_cap: array capacity
        :return:
        """
        return (new_cap * ctypes.py_object)()

    def append(self, element: object):
        """
        append element to array
        :param element: element to append
        :return:
        """
        # checking the capacity
        if self.n == self.capacity:
            # double the capacity for the new array i.e
            self.__resize(2 * self.capacity)
        # add element ot the end of the array
        self.A[self.n] = element
        self.n += 1

    # Algorithmes de tri : À CONNAITRE POUR LE CC

    def tri_tres_simple(self):
        """
        -> Supposons que nous savons que notre tableau n'est composé que de deux valeurs : 1 ou 2 (par exemple) !
           Ce tri sera plus performant que le tri linéaire si l'on connait nos valeur stockées dans notre liste

        -> On considère une clé k = 0
        -> Complexité : elle sera toujours dans n'importe cas de : T = O(n)
        :return:
        """
        k: int = 0

        # On cherche les éléments avec la valeur 1, on incrémente k à chaque fois que c'est le cas
        for i in range(0, self.n):
            if self.A[i] == 1:
                k = k + 1
        # Ensuite, on remplit tout simplement notre liste avec des 1 de l'indice 0 à k
        for i in range(0, k):
            self.A[i] = 1

        # le reste de notre liste (donc de k+1 à n) sera rempli de valeur 2
        for i in range(k + 1, self.n):
            self.A[i] = 2

        # on a ainsi notre liste qui au départ vaut par exemple : [1,2,1,2,1] -> [1,1,1,2,2]

    def tri_par_selection(self, reverse: bool = False):
        """
        On parcourt toute la liste en recherchant à chaque fois le i'ème plus petit élément
        -> Principe du reverse : si on veut que le tri soit inversé en descendant
        -> Complexité : T = O(n^2) (toujours)
        :return:
        """
        # première boucle : compare chaque élément avec le reste des éléments dans la liste
        for i in range(0, self.n - 1):
            #
            key = self.A[i]
            minimum: int = i
            # on compare le minimum définit plus haut
            for j in range(i + 1, self.n):
                if reverse:
                    if self.A[minimum] < self.A[j]:
                        minimum = j
                else:
                    # On définit le minimum après avoir testé tout le reste de la liste
                    if self.A[minimum] > self.A[j]:
                        minimum = j
            # on place pour finir le minimum à la position i (dans le premier tour de boucle, le plus petit élément sera ainsi le premier, etc...)
            self.A[i] = self.A[minimum]
            self.A[minimum] = key

    def tri_par_insertion(self, reverse: bool = False):
        """
        sort array using the insertion sort algorithm
        -> Complexité T = O(n) dans le meilleur des cas, sinon dans le pire : T = O(n^2)
        :param reverse: on peut décider si l'on veut trier les éléments dans l'ordre décroissant lorsque le param reverse est précisé TRUE
        :return:
        """
        # On commence la boucle à partir du deuxième élément (à la pos 1)
        for i in range(1, self.n):
            # la clé sera l'élément i
            key = self.A[i]
            # j vaut i - 1
            j: int = i - 1
            if reverse:
                # cas REVERSE : si la clé est plus grande, on veut la déplacer à gauche pour avoir : 5 4 3 2 1 par exemple
                while j >= 0 and key > self.A[j]:
                    self.A[j + 1] = self.A[j]
                    j = j - 1
            else:
                # cas NORMAL : si la clé est plus petite, on veut la repositionner vers la gauche pour avoir : 1 2 3 4 5 par exemple
                while j >= 0 and key < self.A[j]:
                    self.A[j + 1] = self.A[j]
                    j = j - 1
            # ne pas oublier de changer la valeur de la clé
            self.A[j + 1] = key

    def tri_par_fusion(self, reverse: bool = False):
        """
        sort array using the merge sort algorithm
        :param reverse: reverse sort
        :return:
        """
        p = 0  # le premier élément
        r = self.n - 1  # le dernier élément
        # appel d'une méthode privé __tri_par_fusion
        self.__tri_par_fusion(p, r)

    def __tri_par_fusion(self, p: int, r: int):
        """
        -> Methode : on divise le tableau à trier en deux partie, que l'on trie, puis on fusionne les tableaux triés entre eux
        -> Complexité : T = O(n * log(n))
        :param p: premier élément
        :param r: dernier élément
        :return: le tableau entiérement trié
        """

        # Si le param p est plus grand ou égal à r, c'est que l'entiéreté de la liste a été parcouru et trié, on peut donc retourner simplement la liste elle-même
        if p >= r:

            return self
        else:
            # Sinon : on définit le milieu comme étant q la division modulaire de (p + r)
            q = (p + r) // 2
            # on trie la partie de Gauche :
            self.__tri_par_fusion(p, q)

            # On trie la partie de droite :
            self.__tri_par_fusion(q + 1, r)

            # on fusionne les deux parties ensembles
            self.__fusion(p, q, r)

    def __fusion(self, p: int, q: int, r: int):
        """

        :param p: premier élément de la liste
        :param q: milieu de la liste
        :param r: dernier élément de la liste
        :return:
        """
        # Avec n1 = taille de la liste Left ... et n2 = taille de la liste Right
        n1 = q - p + 1
        n2 = r - q
        # On crée nos 2 listes, ajout d'éléments vide dedans
        # On attribue ensuite à la partie de gauche les éléments de p à q de notre liste, puis à la partie de droite les éléments de q à r de notre liste
        Left: list = [None] * (n1 + 1)
        Right: list = [None] * (n2 + 1)
        Left[:n1] = self.A[p:q + 1]
        Right[:n2] = self.A[q + 1:r + 1]

        # ajout d'un sentinelle à la fin de notre liste de droite et gauche pour s'assurer que notre dernier élément soit forcement le plus grand
        Left[n1] = Right[n2] = math.inf

        # Partie de la fusion des deux listes en une (Polymérisation !)
        i: int = 0
        j: int = 0
        for k in range(p, r + 1):
            # si le premier élément de la liste de gauche est plus petit/egal à celui de la droite, notre liste à la position k aura pour valeur Lef[i]
            # exemple :
            # i et j = 0
            # premier tour de boucle :
            # Left[0] est plus petit que Right[0]
            # donc self.A[0] = Left[0]
            # on incrémente i += 1
            # deuxième tour de boucle :
            # Left[1] est plus grand que Right[0] (j étant toujours egal à 0)
            # donc self.A[1] = Right[0] (car on est au deuxième tour de boucle)
            # on incrémente j += 1
            # etc....jusqu'à r + 1 éléments
            if Left[i] <= Right[j]:
                self.A[k] = Left[i]
                i += 1
            else:
                self.A[k] = Right[j]
                j += 1

    # Algorithmes de Recherches : À CONNAITRE POUR LE CC
    def recherche_lineraire(self, x: object) -> int:
        """

        A CONNAITRE POUR LE CC !!!!!!!!!!!!!!!!!

        sera plus rapide avec un "return i" directement lorsque x est trouvé
        complexité : T = O(n) (dans le meilleur des cas : T = O(1)
        (si on fait la même chose pour une valeur x dans 2 tableau, le code est pareil, mais complexité : T = O(n^2)
        :param self: la liste
        :param x: la valeur recherchée
        :return: l'indice pour lequel liste[i] = x
        """
        for i in range(0, self.n):
            if self.A[i] == x:
                return i
        return -1

    def recherche_dichotomique_iterative(self, x: object):
        """
        ->  principe de la recherche du dictionnaire : on examine l'élément du milieu, on élimine la moitié qui ne nous intéresse plus,
            puis on refait une recherche du milieu, etc....jusqu'à trouver notre élément
            ATTENTION : LA LISTE DOIT ÊTRE TRIÉ AVANT DE FAIRE CETTE RECHERCHE
        -> Complexité : pire des cas : T = O(log^2 * n) ... meilleur des cas : T = O(1)
        :param x: l'élement à trouver
        :return:
        """
        # p = indice du premier élément , r = indice du dernier élément
        p: int = 0
        r: int = self.n - 1

        # tant qu'il reste plus d'un élément à parcourir dans notre liste :
        while p <= r:
            # on définit le milieu avec q
            q: int = (p + r) // 2

            # Si notre milieu correspond à x : jackpot, on a trouvé l'élément x et on retourne l'indice
            if self.A[q] == x:
                return q

            # si l'élément se trouve dans la partie inférieur du milieu, notre nouveau dernier correspond au milieu - 1
            # (on ne prend ainsi en compte que la partie de gauche pour continuer notre recherche)
            elif self.A[q] > x:
                r = q - 1
            # sinon, c'est l'inverse, et notre nouveau premier correspond au milieu + 1 (on se débarasse de la partie de gauche)
            else:
                p = q + 1
        # Si l'élément x n'a pas été retrouvé, on retourne -1 par convention
        return -1

    def recherche_dichotomique_recursive(self, p: int, r: int, x: object):
        """
        ->  même principe que précédement, mais cette fois on va le faire de façon récursive les gars (et il faut changer les params de la fonction)
            ATTENTION : LA LISTE DOIT ÊTRE TRIÉ AVANT DE FAIRE CETTE RECHERCHE
        -> Complexité reste la même
        :param x: l'élement à trouver
        :param p: l'indice du premier élément
        :param r: l'indice du dernier élément
        :return:
        """

        # dans le cas ou p est plus grand que r, c'est que notre recherche n'a pas trouvé l'élément x, on renvoit ainsi - 1
        if p > r:
            return -1
        else:
            q = (p + r) // 2
            # Si notre milieu correspond à x : on retourne l'indice
            if self.A[q] == x:
                return q
            # si l'élément se trouve dans la partie inférieur du milieu, notre nouveau dernier correspond au milieu - 1
            # (on ne prend ainsi en compte que la partie de gauche pour continuer notre recherche)
            elif self.A[q] > x:
                return self.recherche_dichotomique_recursive(p, q - 1, x)
            # sinon, c'est l'inverse, et notre nouveau premier correspond au milieu + 1 (on se débarasse de la partie de gauche)
            else:
                return self.recherche_dichotomique_recursive(q + 1, r, x)
