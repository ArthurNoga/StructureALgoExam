package pileFile;

public class pileFile {
    /**
     * Structures de données : PILE (FILO) & FILE (FIFO)
     * Version 1 : implémenté dans un tableau redimensionnable
     * @author Ch. Stettler - HEG-Genève
     */
    public static class TestPileEtFile_Version1 {

        public static void main(String[] args) {
            Pile p = new Pile();
            p.push( 2); p.push( 4); p.push( 6); p.push( 8); p.push(10);
            p.push(12); p.push(14); p.push(16); p.push(18); p.push(20);
            p.push(22); p.push(24); p.push(26); p.push(28); p.push(30);
            while (!p.isEmpty()) { System.out.print(p.pop()+" "); } System.out.println();

            File file = new File();
            file.add( 1); file.add( 3); file.add( 5); file.add( 7); file.add( 9);
            file.add(11); file.add(13); file.add(15); file.add(17); file.add(19);
            file.add(21); file.add(23); file.add(25); file.add(27); file.add(29);
            while (!file.isEmpty()) { System.out.print(file.remove()+" "); } System.out.println();
        }
    }
    // ==================================================================
    static class Pile { // FILO
        final static int SIZE_TAB_INIT = 10;
        private int size;
        private int[] tab;

        public Pile() { tab = new int[SIZE_TAB_INIT]; size = 0; }

        public void push(int val) {
//		if (size >= SIZE_TAB_INIT) { throw new RuntimeException("Push: pile pleine !"); }
            if (size >= tab.length) { resize(); }
            tab[size++] = val;
        }

        public int pop() {
            if (isEmpty()) { throw new RuntimeException("Pop: pile vide !"); }
            return tab[--size];
        }

        private void resize() {
            int[] newTab = new int[2*tab.length];					// Allouer le nouveau tableau
            for (int k=0; k<size; k++) { newTab[k] = tab[k]; }	// Recopier le contenu
            tab = newTab;													// Remplacer
        }

        public boolean isEmpty() { return size==0; }
        public int size() { return size; }
    }
    // ==================================================================
    static class File { // FIFO
        private final static int SIZE_TAB_INIT=10;
        private int in, out, nb;
        private int[] tab;

        public File() { tab = new int[SIZE_TAB_INIT]; in = out = nb = 0; }

        public void add(int val) {
            if (nb+1 >= tab.length) resize();
            tab[in] = val;
            in = incr(in); nb++;
        }

        public int remove() {
            if (isEmpty()) { throw new RuntimeException("File vide !"); }
            int val = tab[out];
            out = incr(out); nb--;
            return val;
        }

        /* Incrémente modulo la taille du tableau tab */
        private int incr(int i) { return (i+1) % tab.length; }

        private void resize() {
            int[] newTab = new int[2*tab.length];		// Allouer
            for (int k=0, i=out; k<nb; k++) { newTab[k]=tab[i]; i=incr(i); }
            tab=newTab; out=0; in=nb;						// Remplacer
        }

        public boolean isEmpty() { return nb==0; }
        public int size() { return nb; }
    }
}
