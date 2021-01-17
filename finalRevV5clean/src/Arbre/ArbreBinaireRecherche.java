package Arbre;

import java.util.LinkedList;
import java.util.Queue;

public class ArbreBinaireRecherche {

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
        public ArbreBinaireRecherche() {

        }


        public void insert(Node node, int value) {
            if (value < node.value) {
                if (node.left != null) {
                    insert(node.left, value);
                } else {
                    node.left = new Node(value);
                }
            } else if (value > node.value) {
                if (node.right != null) {
                    insert(node.right, value);
                } else {
                    node.right = new Node(value);
                }
            }
        }

        public boolean containsNode(Node current, int value) {
            if (current == null) {
                return false;
            }
            if (value == current.value) {
                return true;
            }
            return value < current.value
                    ? containsNode(current.left, value)
                    : containsNode(current.right, value);
        }


        public Node deleteNode(Node current, int value) {
            if (current == null) {
                return null;
            }
            if (current.left == null && current.right == null) {
                return current;
            }
            if (current.right == null) {
                return current.left;
            }

            if (current.left == null) {
                return current.right;
            }

            if (value < current.value) {
                current.left = deleteNode(current.left, value);
                return current;
            }
            current.right = deleteNode(current.right, value);
            return current;


        }


        public int findSmallestValue(Node root) {
            return root.left == null ? root.value : findSmallestValue(root.left);
        }

        public int findBiggestValue(Node root) {
            return root.right == null ? root.value : findBiggestValue(root.right);
        }


        public void traverseInOrder(Node node) {
            if (node != null) {
                traverseInOrder(node.left);
                System.out.print(" " + node.value);
                traverseInOrder(node.right);
            }
        }


        public void traversePreOrder(Node node) {
            if (node != null) {
                System.out.print(" " + node.value);
                traversePreOrder(node.left);
                traversePreOrder(node.right);
            }
        }


        public void traversePostOrder(Node node) {
            if (node != null) {
                traversePostOrder(node.left);
                traversePostOrder(node.right);
                System.out.print(" " + node.value);
            }
        }


        public void bfs(Node root) {
            if (root == null) {
                return;
            }

            Queue<Node> nodes = new LinkedList<>();
            nodes.add(root);

            while (!nodes.isEmpty()) {

                Node node = nodes.remove();

                System.out.print(" " + node.value);

                if (node.left != null) {
                    nodes.add(node.left);
                }

                if (node.right != null) {
                    nodes.add(node.right);
                }
            }
        }

        /* Function to get the maximum width of a binary tree*/

        public int getMaxWidth(Node node) {
            int maxWidth = 0;
            int width;
            int h = height(node);
            int i;

        /* Get width of each level and compare
           the width with maximum width so far */
            for (i = 1; i <= h; i++) {
                width = getWidth(node, i);
                if (width > maxWidth)
                    maxWidth = width;
            }

            return maxWidth;
        }

        /* Get width of a given level */

        public int getWidth(Node node, int level) {
            if (node == null)
                return 0;

            if (level == 1)
                return 1;
            else if (level > 1)
                return getWidth(node.left, level - 1)
                        + getWidth(node.right, level - 1);
            return 0;
        }
        /* UTILITY FUNCTIONS */

    /* Compute the "height" of a tree -- the number of
     nodes along the longest path from the root node
     down to the farthest leaf node.*/

        public int height(Node node) {
            if (node == null)
                return 0;
            else {
                /* compute the height of each subtree */
                int lHeight = height(node.left);
                int rHeight = height(node.right);

                /* use the larger one */
                return (lHeight > rHeight) ? (lHeight + 1)
                        : (rHeight + 1);
            }
        }
    }
