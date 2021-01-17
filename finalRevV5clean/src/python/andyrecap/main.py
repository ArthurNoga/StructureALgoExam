#Revision CC : algorithmes de tri et de recherches, récursivité, noeuds, binary-tree

from random import randint

from arrayClass import DynamicArray
from bintreeClass import BinaryTree
from LinkedList import LinkedList

def melange_liste() -> 'DynamicArray':
    """

    """
    _arr: DynamicArray = DynamicArray(10)
    for i in range(10):
        rand_int: int = randint(1, 100)
        _arr.append(rand_int)

    return _arr

def melange_linkedlist() -> 'LinkedList':
    """
    """
    _lk = LinkedList()
    # Ajouter des nombres aléatoires dans la liste
    for i in range(0, 10):
        _lk.add(randint(0, 100))
    return _lk

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Partie avec liste normale")
    arr = melange_liste()

    print("Les trois tri : ")

    arr.tri_par_selection()
    print("Tri par séléction : " + str(arr))
    arr = melange_liste()

    arr.tri_par_insertion()
    print("Tri par insertion : " + str(arr))
    arr = melange_liste()

    arr.tri_par_fusion()
    print("Tri par fusion : " + str(arr))

    print("Recherche dichotomique : \n" + str(arr.recherche_dichotomique_iterative(20)) +
          "\nRecherche dichotomique mais Récursive :\n" + str(arr.recherche_dichotomique_recursive(0, arr.n-1, 50)))

    arr = melange_liste()

    print("Recherche linéaire : \n" + str(arr.recherche_lineraire(25)))
    print()



    print("Partie avec liste doublement chaînée")
    """
    [None, 5, next] <---> [Prev, 10, Next] <---> [Prev, 15, Next] <---> [Prev, 20, None]
    pas besoin de savoir comment construire une LinkedList, juste comprendre comment ça fonctionne et comment
    les methodes de tri et de recherches fonctionnent sur les LinkedList
    """
    lk = melange_linkedlist()
    print("Tri par insertion")
    lk.insertion_sort()
    print(lk)
    print()

    lk = melange_linkedlist()
    print("Tri par merge_sort")
    lk.merge_sort()
    print(lk)
    print()

    print("Recherche dichotomique :")
    print(lk)
    print(lk.dichotomic_search(50))
    print()




    print("Partie des arbres binaires :")
    """
                   root
                /        \  
               a          d 
             /   \      /   \
             b   c      e    f

    Quelques définitions :
    
    - chemin : suite de noeuds donc chacun est le fils du précédent
    - racine : noeud qui n'a pas de parent (ici : root)
    - profondeur : longeur du chemin reliant un noeud à la racine (pour 'a' par exemple, ça sera 1)
    - hauteur : la profondeur maximale des noeuds (içi, ça sera 2)
    
    """
    # Création de notre arbre binaire avec comme valeur à la racine : 'root'
    r = BinaryTree('root')
    #on voit bien que les valeur de droite et gauche sont None, pas encore été attribués
    print(r.root())
    print(r.left())
    print(r.right())

    r.insert('a')
    r.insert('d')
    print()

    # on affiche les 2 sous-arbres à partir de root :
    print(r.left().root())
    print(r.right().root())

    r.insert('b')
    r.insert('c')
    r.insert('e')
    r.insert('f')

    print()
    print("Les methode de parcours en profondeur/largeur")
    print()

    print("preorder")
    r.preorder()
    print()

    print("inorder")
    r.inorder()
    print()

    print("postorder")
    r.postorder()
    print()

    print("bfs")
    r.bfs()
    print()

    print("la hauteur de notre arbre vaut : " + str(r.height()))
    print("La hauteur de l'élément 'root' vaut : " + str(r.depth('root')))
    print("La hauteur de l'élément 'f' vaut : " + str(r.depth('f')))