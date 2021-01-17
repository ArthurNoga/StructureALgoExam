from queue import Queue


class BinaryTree:

    def __init__(self, data: object):
        """
        Base de la création d'un arbre : Root avec la data, pointe vers du None pour la gauche et la droite
        :param data:
        """
        self.__data = data
        self.__left = None
        self.__right = None

    def insert_left(self, new_node: object):
        """
        insert a node in the left branch
        :param new_node: object of the node
        :return:
        """
        if self.__left is None:
            self.__left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.__left = self.__left
            self.__left = t

    def insert_right(self, new_node: object):
        """
        insert a node in the right branch
        :param new_node: object of the node
        :return:
        """
        if self.__right is None:
            self.__right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.__right = self.__right
            self.__right = t

    def insert(self, new_node: object):
        """
        insert a node in the next branch available (from left to right)
        :param new_node: object of the node
        :return:
        """
        q = Queue()
        q.put(self)     # add the tree to a queue
        # do level order traversal until we find an empty place
        while not q.empty():
            _temp = q.get()
            if _temp.left() is None:
                _temp.insert_left(new_node)
                break
            else:
                q.put(_temp.left())
            if _temp.right() is None:
                _temp.insert_right(new_node)
                break
            else:
                q.put(_temp.right())

    def right(self):
        """
        return right branch
        :return:
        """
        return self.__right

    def left(self):
        """
        return left branch
        :return:
        """
        return self.__left

    def root(self) -> object:
        """
        return node data
        :return:
        """
        return self.__data

    def is_empty(self) -> bool:
        """
        is node empty
        :return:
        """
        return self.__data is None

    def preorder(self):
        """
        -> Parcours en profondeur, mais on commence par la racine, puis le sous-arbre de gauche et enfin le sous-arbre de droite
        -> Root -> Gauche -> Droite
        :return:
        """
        #la racine de l'arbre est ainsi affiché, au début ça sera root, puis à chaque appel récursive, le nouveau root sera son gauche ou son droite, que l'on affiche à leur tour
        print(self.__data)
        #parcours du sous-arbre de gauche à partir de root
        if self.__left is not None:
            # on continue recommence avec l'arbre à partir de la valeur gauche de root, puis etc...
            self.__left.preorder()
        #après avoir parcouru tout à gauche, on fait la partie de droite
        if self.__right is not None:
            #etc...
            self.__right.preorder()


    def inorder(self):
        """
        -> Parcous en profondeur, mais on parcoure le sous arbre de gauche, puis le noeud racine, et enfin le sous-arbre de droit
        -> Gauche -> Root -> Droite
        :return:
        """
        #contrairement à preorder, on parcourt d'abord toute la partie de droit avant d'afficher la valeur
        if self.__left is not None:
            self.__left.inorder()
        print(self.__data)
        if self.__right is not None:
            self.__right.inorder()


    def postorder(self):
        """
        -> Parcous en profondeur, mais on parcoure le sous arbre de gauche, puis le sous-arbre de droite, et enfin la racine
        -> Gauche -> Droite -> Root
        :return:
        """

        #içi, la valeur de la racine sera affiché après le parcours complet de gauche et droite
        if self.__left is not None:
            self.__left.postorder()

        if self.__right is not None:
            self.__right.postorder()
        print(self.__data)


    def bfs(self):
        """
        ->  Parcours en largeur, on va procéder de façon à parcours chaque noeuds du même niveau avant de descendre au niveau en dessous
            en gros :
            on ajoute le Binary tree dans la queue, le premier get va ajouter donc root dans notre variable st
            à chaque get, prends la première valeur et la retire de la queue
            après le premier affichage, on ajoute les éléments de gauche et de droite à partir de root dans la queue
        :return:
        """
        # Création de la queue dans laquelle on ajoute la valeur de la racine de notre binary tree
        q: Queue = Queue()
        q.put(self)
        #tant que la queue n'est pas vide, il reste des éléments à afficher donc :
        while not q.empty():
            #création d'un 2ème BinaryTree qui reçoit root et toutes les données liées à root (au deuxième tour de boucle, recevra le sous-arbre de gauche comme racine, puis droite, etc...)
            st : BinaryTree = q.get()
            # si l'élément ne pointe pas sur None (donc qu'il ne s'agit pas du bout de l'arbre), on affiche le root
            # et on place dans la queue les 2 sous-arbres de root, etc...
            if st is not None and not st.is_empty():
                print(st.root())
                q.put(st.left())
                q.put(st.right())
        """
        
        """

    def height(self) -> int:
        """
        -> On va déteminer la hauteur de l'arbre
        :return:
        """
        #création d'une methode privé prenant comme param self, ainsi qu'un arbre binaire (içi il prendra self lorsque la methode est appelé la premiere fois)
        return self.__height(self)

    def __height(self, node: 'BinaryTree') -> int:
        """
        -> Va renvoyer un int correspondant à la hauteur max de notre arbre (si le sous-arbre de gauche est plus grand, c'est cette valeur qui sera retournée)
        :param node:
        :return:
        """
        #si aucun élément dans notre arbre, on retourne -1
        if node is None:
            return -1
        else:
            # on parcourt de façon récursive la partie de gauche et droite, on fait + 1 à chaque fois
            # la hauteur max sera donné par la valeur max(gauche ou droite)
            #h_left et h_right sont les hauteurs des sous-arbres à partir du root
            h_left:int = self.__height(node.left())
            h_right: int = node.__height(node.right())
            return 1 + max(h_left, h_right)
        #le +1 s'effectue à chaque récursivité (compense ainsi le -1 à chaque fois que la récursivité atteint le bout du noeud
        # quand le noeud sera None(donc le bout de la branche, on est à -1, ensuite à chaque fois qu'on remonte on fait +1 pour arriver jusqu'à root



    def depth(self, key:object) -> int:
        """
        -> va calculer la longeur du chemin reliant un noeud à la racine

        :param key:
        :return:
        """
        return self.__depth(key, self, 0)

    def __depth(self, key:object, node: 'BinaryTree', max_distance: int) -> int:
        """
        -> va calculer la longeur du chemin reliant un noeud à la racine
        :param key: l'élément visé
        :param node: le noeud sur lequel on travaille
        :param max_distance: valeur 0 au départ
        :return: la profondeur à partir d'un noeud
        """

        #lorsque le noeud est vide, on doit retourner -1
        if node is None:
            return -1
        #si le noeud cherché est la racine : alors la distance vaut 0
        elif node.root() == key:
            return max_distance
        #sinon, on descend d'un niveau, la distance augmente ainsi +1, et on parcours à gauche avec node.left() comme étant le nouvel arbre
        # ainsi qu'à droit avec node.right()
        else:
            max_distance += 1
            d1:int = node.__depth(key, node.left(), max_distance)
            d2: int = -1
            #en gros, si l'élément est trouvé à gauche, bah pas besoin de le chercher à droite
            if d1 == -1:
                d2:int = node.__depth(key, node.right(), max_distance)
            return max(d1, d2)

