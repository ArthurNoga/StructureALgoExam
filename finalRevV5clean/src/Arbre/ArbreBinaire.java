package Arbre;

public class ArbreBinaire {
    ArbreBinaire root;
    ArbreBinaire left;
    ArbreBinaire right;
    int equilibre;
    int Hauteur;

    public ArbreBinaire() {
        root = null;
        left = null;
        right = null;
        equilibre = 0;
        Hauteur = 0;

    }
     class Node {
        int value;
        Node left;
        Node right;

        Node(int value) {
            this.value = value;
            right = null;
            left = null;
        }
    }



    ArbreBinaire rotationVersDroite(ArbreBinaire a) {
        ArbreBinaire result = a;
        if ((a != null) && (a.left != null)) {
            ArbreBinaire filsGauche = a.left;
            a.left = filsGauche.right;
            filsGauche.right = a;
            result = filsGauche;
        }
        return result;
    }

    ArbreBinaire rotationVersGauche(ArbreBinaire a) {
        ArbreBinaire result = a;
        if ((a != null) && (a.right != null)) {
            ArbreBinaire filsDroit = a.right;
            a.right = filsDroit.left;
            filsDroit.left = a;
            result = filsDroit;
        }
        return result;
    }

    ArbreBinaire reequilibre(ArbreBinaire a) {
        if (a != null) {
            while (a.equilibre < -1 || a.equilibre > 1) {
                a.left = reequilibre(a.left);
                a.right = reequilibre(a.right);
                /*si branche droite trop longue*/
                if (a.equilibre <= -2)
                    a = rotationVersGauche(a);
                /*si branche gauche trop longue*/
                if (a.equilibre >= 2)
                    a = rotationVersDroite(a);
                getHauteur(a);
                getEquilibre(a);

            }
        }
        return a;
    }

    /* retourne la hauteur de l'arbre */
    int getHauteur(ArbreBinaire a) {
        int result = 0;
        if (a != null) {
            int hauteurG = getHauteur(a.left);
            int hauteurD = getHauteur(a.right);
            int maxHauteurFils = (hauteurG > hauteurD ? hauteurG : hauteurD);
            result = 1 + maxHauteurFils;
            a.Hauteur = result;
        }
        return result;
    }

    public int getEquilibre(ArbreBinaire a) {
        int result = 0;
        if (a != null) {
            ArbreBinaire filsDroit = a.right;
            int hauteurDroit = (filsDroit != null ? filsDroit.Hauteur : 0);
            ArbreBinaire filsGauche = a.left;
            int hauteurGauche = (filsGauche != null ? filsGauche.Hauteur : 0);
            result = hauteurGauche - hauteurDroit;
            a.equilibre = result;
        }
        return result;
    }

    public void inserer(Node node, int value) {
        if (value < node.value) {
            if (node.left != null) {
                inserer(node.left, value);
            } else {
                node.left = new Node(value);
            }
        } else if (value > node.value) {
            if (node.right != null) {
                inserer(node.right, value);
            } else {
                node.right = new Node(value);
            }
        }
    }
}
