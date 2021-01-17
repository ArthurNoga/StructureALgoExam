package metier;

import javax.swing.*;
import java.util.*;

public class PyRat {
    Map<Point, Set<Point>> labySet = new HashMap<>();
    Map<Point, List<Point>> labyList = new HashMap<>();
    List<Point> cheeses = new LinkedList<>();
    Set<Point> cheeseSet = new HashSet<>();


    /* Méthode appelée une seule fois permettant d'effectuer des traitements "lourds" afin d'augmenter la performace de la méthode turn. */
    public void preprocessing(Map<Point, List<Point>> laby, int labyWidth, int labyHeight, Point position, List<Point> fromages) {
        for (Map.Entry<Point, List<Point>> map : laby.entrySet()) {
            Set<Point> pointSet = new HashSet<>();
            for (Point p : map.getValue()) {
                pointSet.add(p);
            }
            labySet.put(map.getKey(), pointSet);


        }

        for (Point cheese : fromages) {
            cheeseSet.add(cheese);
        }

        labyList = laby;

        cheeses = fromages;
    }

    /* Méthode de test appelant les différentes fonctionnalités à développer.
        @param laby - Map<Point, List<Point>> contenant tout le labyrinthe, c'est-à-dire la liste des Points, et les Points en relation (passages existants)
        @param labyWidth, labyHeight - largeur et hauteur du labyrinthe
        @param position - Point contenant la position actuelle du joueur
        @param fromages - List<Point> contenant la liste de tous les Points contenant un fromage. */
    public void turn(Map<Point, List<Point>> laby, int labyWidth, int labyHeight, Point position, List<Point> fromages) {
        Point pt1 = new Point(2, 1);
        Point pt2 = new Point(3, 1);

        System.out.println((fromageIci(pt1) ? "Il y a un" : "Il n'y a pas de") + " fromage ici, en position " + pt1);
        System.out.println((fromageIci_EnOrdreConstant(pt2) ? "Il y a un" : "Il n'y a pas de") + " fromage ici, en position " + pt2);
        System.out.println((passagePossible(pt1, pt2) ? "Il y a un" : "Il n'y a pas de") + " passage de " + pt1 + " vers " + pt2);
        System.out.println((passagePossible_EnOrdreConstant(pt1, pt2) ? "Il y a un" : "Il n'y a pas de") + " passage de " + pt1 + " vers " + pt2);
        System.out.println("Le fromage le plus proche est en position " + fromageLePlusProche(position));
        System.out.println("Liste des points inatteignables depuis la position " + position + " : " + pointsInatteignables(position));
        System.out.println("Liste des fromages inatteignables depuis la position " + position + " : " + fromagesInatteignables(position));
        System.out.println("Nombre de fromages à moins de 6 pas de la position " + position + " : " + nbFromagesAMoinsDeNbPas(position, 6));
        afficherLabyrinthe();
    }

    /* Regarde dans la liste des fromages s’il y a un fromage à la position pos.
        @return true s'il y a un fromage à la position pos, false sinon. */
    private boolean fromageIci(Point pos) {
        return cheeses.contains(pos);
    }

    /* Regarde de manière performante (accès en ordre constant) s’il y a un fromage à la position pos.
        @return true s'il y a un fromage à la position pos, false sinon. */
    private boolean fromageIci_EnOrdreConstant(Point pos) {
        return cheeseSet.contains(pos);
    }

    /* Indique si le joueur peut passer de la position (du Point) « de » au point « a ».
        @return true s'il y a un passage depuis  « de » vers « a ». */
    private boolean passagePossible(Point de, Point a) {
        return labyList.get(de).contains(a);
    }

    /* Indique si le joueur peut passer de la position (du Point) « de » au point « a »,
        mais sans devoir parcourir la liste des Points se trouvant dans la Map !
        @return true s'il y a un passage depuis  « de » vers « a ». */
    private boolean passagePossible_EnOrdreConstant(Point de, Point a) {
        return labySet.get(de).contains(a);
    }

    /* Recherche le fromage le plus proche de la position « pos ».
        @return le point où se trouve le fromage le plus proche de « pos ».
                   BFS               */
    private Point fromageLePlusProche(Point pos) {
        Queue<Point> q = new LinkedList<>();
        List<Point> marked = new ArrayList<>();
        q.add(pos);
        while (!(q.isEmpty())) {
            Point p = q.remove();
            if (cheeseSet.contains(p)) {
                return p;
            }
            for (Point point : labyList.get(p)) {
                if (!(marked.contains(point))) {
                    q.add(point);
                }
            }
            marked.add(p);
        }
        return null;
    }

    List<Point> marked = new ArrayList<>();

    /* Retourne la liste des points qui ne peuvent pas être atteints depuis la position « pos ».
        @return la liste des points qui ne peuvent pas être atteints depuis la position « pos ». */
    private List<Point> pointsInatteignables(Point pos) {

        List<Point> marqué = pacours(pos);
        List<Point> inatenaible = new ArrayList<>();

        for (Point p : labyList.keySet()) {
            if (!(marqué.contains(p))) {
                inatenaible.add(p);
            }
        }


        return inatenaible;
    }

    private List<Point> pacours(Point pos) {
        if (pos == null) {
            return null;
        }
        if (marked.contains(pos)) {
            return null;
        }
        marked.add(pos);
        for (Point p : labyList.get(pos)) {
            pacours(p);
        }
        return marked;
    }

    /* Retourne la liste des fromages qui ne peuvent pas être atteints depuis la position « pos ».
        @return la liste des fromages qui ne peuvent pas être atteints depuis la position « pos ». */
    private List<Point> fromagesInatteignables(Point pos) {
        marked.clear();
        List<Point> inatenaible = pointsInatteignables(pos);
        List<Point> cheeseInateniale = new ArrayList<>();
        for (Point p : inatenaible) {
            if (cheeseSet.contains(p)) {
                cheeseInateniale.add(p);
            }
        }

        return cheeseInateniale;

    }

    /* Retourne le nombre de fromages se trouvant à moins de « nb » pas de « pos ».
        @return le nombre de fromages se trouvant à moins de « nb » pas de « pos ». */
    private int nbFromagesAMoinsDeNbPas(Point pos, int nb) {
        Map<Point, Integer> dist = dfs(labyList, pos);
        List<Point> cheeseAMoinsDeXpas = new ArrayList<>();
        Map<Integer, Point> map = new HashMap<>();
        for (Map.Entry<Point, Integer> m : dist.entrySet()) {
            map.put(m.getValue(), m.getKey());
        }
        for (Map.Entry<Integer, Point> M : map.entrySet()) {
            if (M.getKey() <= nb) {
                cheeseAMoinsDeXpas.add(map.get(M));
            }
        }
        return cheeseAMoinsDeXpas.size();
    }

    Map<Point, Integer> distance = new HashMap<>();

    private Map dfs(Map<Point, List<Point>> laby, Point _from) {

        List<Point> marqueé = new ArrayList<>();
        distance.put(_from, 0);
        /*CHEMIN  */
        return dfs(laby, _from, marqueé);
    }

    private Map dfs(Map<Point, List<Point>> laby, Point from, List marquée) {
        marquée.add(from);
        for (Point p : laby.get(from)) {
            if (!(marquée.contains(p))) {
                 /*routage.put(p,from)*/
                distance.put(p, distance.get(from) + 1);
                dfs(laby, p, marquée);
            }
        }
        /*return routage*/
        return distance;
    }


    } public List path_to(Map:routage,Point de, Point a){
     if (routage.keySet().contains(de) & routage.keySet().contains(a) & routage.get(de) != null) {
            Point current = a;
            while (current != null) {
                path_list.add(0, current);
                current = routage.get(current);
            }

        }return path_list;

    }

    /* Affiche le labyrinthe. */
    private void afficherLabyrinthe() {
    }

}