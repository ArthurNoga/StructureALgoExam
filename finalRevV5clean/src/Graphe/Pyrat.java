package Graphe;

import java.util.*;

public class Pyrat {

    // Création de variable d'instance pour éviter de passer ces paramètres partout
    private Map<Point, List<Point>> laby;
    private List<Point> fromages;


    // pour stocker la liste des passages (pour pouvoir les retrouver rapidement), création d'une classe Passage
    private class Passage {
        private Point de, a;
        public Passage(Point de, Point a) { this.de=de; this.a=a; }
        public boolean equals(Object obj) { return this.de.equals(((Passage)obj).de) && this.a.equals(((Passage)obj).a); }
        public int hashCode() { return de.hashCode() + a.hashCode(); }
        public String toString() { return "{"+de+"-"+a+"}"; }
    }

    // création de variables permettant un accès direct (complexité O(1)) aux données
    private boolean[][] tabFromages;
    private Set<Passage> passages;

    int labyWidth,labyHeight=0;

    public void preprocessing() {
        this.laby=laby; this.fromages=fromages;
        // fromageIci_EnOrdreConstant: crée une matrice, initialisée à false, et met la position des fromages de la liste à true
        tabFromages = new boolean[labyWidth][labyHeight];
        for (int x=0; x<tabFromages.length; x++) { for (int y=0; y<tabFromages[x].length; y++) { tabFromages[x][y]=false; } }
        for (Point pos : fromages) { tabFromages[pos.getX()][pos.getY()] = true; }

        // passagePossible_EnOrdreConstant: crée un HashSet contenant tous les passages possibles existants
        passages = new HashSet<>();
        for (Point de : laby.keySet()) { for (Point a : laby.get(de)) { passages.add(new Passage(de,a)); } }
    }

    private boolean fromageIci(Point pos) {
        return fromages.contains(pos);			// effectue une boucle de parcours des fromages O(n), appel equals n fois
    }

    private boolean fromageIci_EnOrdreConstant(Point pos) {
        return tabFromages[pos.getX()][pos.getY()];		// accès direct au boolean O(1)
    }

    private boolean passagePossible(Point de, Point a) {
        return (laby.get(de) != null) && laby.get(de).contains(a);	// ce contains effectue une boucle de parcours dans List
    }

    private boolean passagePossible_EnOrdreConstant(Point de, Point a) {
        return passages.contains(new Passage(de,a));		// ce contains effectue un accès constant dans HashSet grâce au hashCode
    }




    Stack<Point>chemin = new Stack<>();
   ArrayList<Point>lstDesNoeudsVisités = new ArrayList<>();
    private void parcours(Point pos) {
        // Algo de parcours d'un Graphe / d'un Arbre :
        // 1) traiter le noeud courant
        // 2) boucle de parcours de toutes ses relations (Graphe) / de tous ses fils (Arbre) / de ses 2 fils (ArbreBinaire)
        // 3)    appel récursif de parcours pour chaque relation/fils

        System.out.println(pos);					// 1) traiter
        for (Point voisin : laby.get(pos)) {	// 2) boucle
            parcours(voisin);							// 3) appel récursif
        }

        // Dans le cas des Graphe, risque de "tourner en rond, boucle sans fin" !
        // ==> gérer les noeuds visités

        // Méthode 2: conserver la liste des noeuds visités
        if (lstDesNoeudsVisités.contains(pos)) { return; }
        lstDesNoeudsVisités.add(pos);

        // Méthode 3: conserver le chemin parcouru
        if (chemin.contains(pos)) { return; }
        for (Point voisin : laby.get(pos)) {
            chemin.push(voisin);
            parcours(voisin);
            chemin.pop();
        }
        // Méthode 4: créer une nouvelle classe NoeudVisité étant un wrapper de Noeud avec un nouvel attribut visit
        // Méthode 5: créer une nouvelle classe NoeudVisité extends Noeud implements Visitable


        // Problème principal à gérer :
        // Gestion de la valeur de retour de parcours, savoir quoi retourner, comment traiter ce retour au point 3), quand s'arrêter ...
    }



     class Point {
        private int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public List<Point> getVoisins() {
            return voisins;
        }

        private List<Point> voisins;
        public void addVoisin(Point p){
            voisins.add(p);
        }
        public boolean equals(Object obj) {
            return this.x == ((Point) obj).x && this.y == ((Point) obj).y;
        }

        public String toString() {
            return "<" + x + ";" + y + ">";
        }


        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}
