package Graphe;

import java.awt.*;
import java.util.*;
import java.util.List;

public class Graphe {
    private Map<Noeud, Set<Noeud>> lstNoeuds;
    private List<Noeud> lstDesNoeudsDejaVisites = new ArrayList<>();

    public Graphe() {
        lstNoeuds = new HashMap<>();
    }


    public void addRelation(Noeud source, Noeud dest) {
        Set<Noeud> relations = lstNoeuds.get(source);
        if (relations == null) {
            relations = new HashSet<>();
        }
        relations.add(dest);
        lstNoeuds.put(source, relations);

        relations = lstNoeuds.get(dest);
        if (relations == null) {
            relations = new HashSet<>();
        }
        relations.add(source);
        lstNoeuds.put(dest, relations);
    }


    public boolean existeRelation(Noeud source, Noeud dest) {
        return lstNoeuds.get(source).contains(dest);
    }

    public boolean existeChemin(Noeud source, Noeud dest) {
        return parcourirProfondeurUntilDest(source, dest);
    }


    public boolean parcourirProfondeurUntilDest(Noeud noeud, Noeud dest) {
        //      if (noeud.isVisit()) { return; }
//      noeud.setVisit(true);
        if (lstDesNoeudsDejaVisites.contains(noeud)) { return false; }
        lstDesNoeudsDejaVisites.add(noeud);

        if (noeud.equals(dest)) { return true; }

        for (Noeud rel : lstNoeuds.get(noeud)) {
            if (parcourirProfondeurUntilDest(rel, dest)) { return true; }
        }
        return false;
    }


    public void parcourirProfondeur(Noeud noeud) {

        if (lstDesNoeudsDejaVisites.contains(noeud)) {
            return;
        }
        lstDesNoeudsDejaVisites.add(noeud);

        System.out.print(noeud);
        for (Noeud rel : lstNoeuds.get(noeud)) {
            parcourirProfondeur(rel);
        }
    }

    public List bfs(Noeud pos) {

            ArrayList<Noeud> marked = new ArrayList<>();
            Queue<Noeud> queue = new LinkedList<>();

            queue.add(pos);
            while (!(queue.isEmpty())) {
                Noeud tmp = queue.remove();

                /* effectuer le check ou return ici ex:si contenue dans liste de fromage = fromage le plus proche*/

                for (Noeud p : lstNoeuds.get(tmp)) {
                    if (!marked.contains(p)) {
                        queue.add(p);
                    }
                }
                /*marquage après*/
                marked.add(tmp);
            }
            return marked;
    }
    public List dfs(Noeud pos) {
        ArrayList<Noeud> marked = new ArrayList<>();
        Stack<Noeud> list = new Stack<>();

        list.add(pos);
        while (!(list.isEmpty())) {
            Noeud tmp = list.pop();
            /* effectuer le check ou return ici*/
            if (!(marked.contains(tmp))) {
                System.out.print(tmp);
                /*marquage avant*/
                marked.add(tmp);
                for (Noeud p : lstNoeuds.get(tmp)) {
                    if (!marked.contains(p)) {
                        list.add(p);
                    }
                }
            }

        }
        return marked;
    }


    /* GrAPH MATRICE */
    class GrapheMatrice {
        private boolean[][] matrice;

        public GrapheMatrice(int nbNoeuds) {
            this.matrice = new boolean[nbNoeuds][nbNoeuds];
        }


        public void addRelation(int source, int destination) {
            matrice[source][destination] = true;
            matrice[destination][source] = true;	// si graphe non-orienté, donc relation dans les 2 sens
        }


        public boolean existeRelation(int source, int destination) {
            return matrice[source][destination];
        }


        public void affiRelations() {
            for (int i=0; i<matrice.length; i++) {
                System.out.print(i + " a des relations avec : ");
                for (int j=0; j<matrice[i].length; j++) {
                    if (matrice[i][j]) { System.out.print(j + " "); }
                }
                System.out.println();
            }
        }

        public void printMatrice() {
            for (int i=0; i<matrice.length; i++) {
                for (int j=0; j<matrice[i].length; j++) {
                    if (matrice[i][j]) { System.out.print("   X"); } else { System.out.print("   -"); }
                }
                System.out.println();
            }
        }
    }

    private class Noeud {

    }
    }
