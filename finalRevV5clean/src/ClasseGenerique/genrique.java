package classeGenrique;

public class genrique
{/** Langage Java : Généricité – classes paramétrées
 @author Ch. Stettler - HEG-Genève
 */
public static class Generic {

    private static class MyClass<T> {
        private int no;
        private T valeur;

        public MyClass(int no, T valeur) { this.no=no; this.valeur=valeur; }

        public T getValeur() { return valeur; }
        public void setValeur(T valeur) { this.valeur=valeur; }
    }

    private static class MyClass2<T1, T2> {
        private T1 val1;
        private T2 val2;

        public MyClass2(T1 val1, T2 val2) { this.val1=val1; this.val2=val2; }

        public T1 getVal1() { return val1; }
        public T2 getVal2() { return val2; }
        public void setVal1(T1 val1) { this.val1=val1; }
        public void setVal2(T2 val2) { this.val2=val2; }

        public String toString() { return "val1=" + val1 + " val2=" + val2; }
    }

    private static class MyClassNum0<T> {
        private T valeur;
        public MyClassNum0(T valeur) { this.valeur=valeur; }
//		public double inverse() { return 1 / valeur.doubleValue(); }	// erreur à la compilation
    }

    private static class MyClassNum<T extends Number> {
        private T valeur;
        public MyClassNum(T valeur) { this.valeur=valeur; }
        public double inverse() { return 1 / valeur.doubleValue(); }
    }

    private static class MyClassComp<T extends Comparable> { }

    private static class MyClassEtSubclass<T1, T2 extends T1> {
        private T1 val1;
        private T2 val2;
        public MyClassEtSubclass(T1 val1, T2 val2) { this.val1=val1; this.val2=val2; }
    }

    private static class MyClassWildcard<T extends Number> {
        private T valeur;
        public MyClassWildcard(T valeur) { this.valeur=valeur; }
        public boolean idem(MyClassWildcard<?> obj) { return valeur.intValue() == obj.valeur.intValue(); }
    }

    private static <T> boolean estDans(T[] tab, T val) { // méthode générique
        for (T t : tab) {
            if (t.equals(val)) { return true; }
        }
        return false;
    }

    public static void main (String[] args) {
        MyClass<Double> maClasse = new MyClass<>(123, new Double(45.67));
        maClasse.setValeur(7.8);	// auto-boxing
        Double dbl = maClasse.getValeur();
        System.out.println(dbl);

        MyClass<String> maClasseStr = new MyClass<>(123, "Texte");
        maClasseStr.setValeur("Hello");
        System.out.println(maClasseStr.getValeur());

        MyClass2<String, Integer> maClasse2 = new MyClass2<>("Texte", 123);
        maClasse2.setVal1("Hello");
//		maClasse2.setVal2("Hello");	// erreur à la compilation
        System.out.println(maClasse2);

        MyClassNum<Integer> maClasseNum = new MyClassNum<>(5);
        System.out.println(maClasseNum.inverse());

        MyClassNum<Float> maClasseF = new MyClassNum<>((float)2.5);
        System.out.println(maClasseF.inverse());

        MyClassEtSubclass<Integer, Integer> maClasseSubc1 = new MyClassEtSubclass<>(123, 45);
        MyClassEtSubclass<Number,  Integer> maClasseSubc2 = new MyClassEtSubclass<>(1.2, 45);
//		MyClassEtSubclass<Integer, Number>  maClasseSubc3 = new MyClassEtSubclass<>(123, 45);

        MyClassWildcard<Double> maClasseWildcard1 = new MyClassWildcard<>(5.1);
        MyClassWildcard<Double> maClasseWildcard2 = new MyClassWildcard<>(5.1);
        if (maClasseWildcard1.idem(maClasseWildcard2)) { System.out.println("Idem"); }
        MyClassWildcard<Integer> maClasseWildcard3 = new MyClassWildcard<>(5);
        if (maClasseWildcard1.idem(maClasseWildcard3)) { System.out.println("Idem"); }

        Integer[] tab1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        String[]  tab2 = { "AA", "BB", "CC", "DD", "EE" };
        if (estDans(tab1, 3)) { System.out.println("3 estDans tab1"); }
        if (estDans(tab2, "CC")) { System.out.println("CC estDans tab2"); }
    }
}
}
