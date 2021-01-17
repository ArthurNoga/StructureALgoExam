package Arbre; /**
 * Structures de données : Les Arbres n-aires
 *    Version : fils implémentés dans un ArrayList
 * @author Ch. Stettler - HEG-Genève
 */
import java.util.ArrayList;

public class ArbreNrFils {

	private Noeud racine;

	public ArbreNrFils() { racine=null; }

	class Noeud {
		private int contenu;
		private ArrayList<Noeud> fils;

		public Noeud(int contenu) { this(contenu, new ArrayList<>()); }
		public Noeud(int contenu, ArrayList<Noeud> fils) { this.contenu=contenu; this.fils=fils; }
	}

	public Noeud inserer(int x, Noeud pere) {
		Noeud n = new Noeud(x); 
		if (pere == null) { return racine = n; }
		pere.fils.add(n);
		return n;
	}

	public  void parcoursPrefixe() { parcoursPrefixe(racine); }
	private void parcoursPrefixe(Noeud n) {
		if (n == null) { return; }
		System.out.print(n.contenu + " ");
		for (Noeud f : n.fils) { parcoursPrefixe(f); }
	}
	public  void parcoursPostfixe() { parcoursPostfixe(racine); }
	private void parcoursPostfixe(Noeud n) {
		if (n == null) { return; }
		for (Noeud f : n.fils) { parcoursPostfixe(f); }
		System.out.print(n.contenu + " ");
	}

	public  Noeud chercher(int x) { return chercher(x, racine); }
	private Noeud chercher(int x, Noeud n) {
		if (n == null || x == n.contenu) { return n; }
		for (Noeud f : n.fils) { 
			Noeud tmp = chercher(x, f); if (tmp != null) { return tmp; }
		}
		return null;
	}

	public  boolean supprimer(int x) { return supprimer(x, racine); }
	private boolean supprimer(int x, Noeud n) {
		if (n == null) { return false; }
		if (x == n.contenu) { racine=null; return true; }
		for (int i=0; i<n.fils.size(); i++) { 
			Noeud f = n.fils.get(i);
			if (x == f.contenu) { n.fils.remove(i); return true; }
			if (supprimer(x, f)) { return true; }
		}
		return false;
	}

	public  int taille() { return taille(racine); }
	private int taille(Noeud n) {
		if (n == null) { return 0; }
		int t=1;
		for (int i=0; i<n.fils.size(); i++) { t += taille(n.fils.get(i)); }
		return t;
	}

	public String toString() { return racine.toString(); }


	public static void main (String[] args) {
		ArbreNrFils a = new ArbreNrFils();
		a.inserer(0, null); a.inserer(1, a.chercher(0)); a.inserer(2, a.chercher(0)); a.inserer(3, a.chercher(0)); a.inserer(4, a.chercher(0));
		a.inserer(11, a.chercher(1)); a.inserer(12, a.chercher(1)); a.inserer(13, a.chercher(1)); a.inserer(14, a.chercher(1)); 
		a.inserer(121, a.chercher(12)); a.inserer(122, a.chercher(12)); a.inserer(123, a.chercher(12)); 
		a.inserer(1221, a.chercher(122)); 
		a.inserer(31, a.chercher(3)); a.inserer(32, a.chercher(3)); 
		a.inserer(311, a.chercher(31)); a.inserer(312, a.chercher(31)); a.inserer(313, a.chercher(31)); 
		a.inserer(41, a.chercher(4));

		a.parcoursPrefixe();  System.out.println();
		a.parcoursPostfixe(); System.out.println();

		System.out.println("Chercher 12: " + a.chercher(12));
		System.out.println("Taille: " + a.taille());

		System.out.println("Supprimer 12: " + a.supprimer(12));
		a.parcoursPrefixe(); System.out.println();
	}
}