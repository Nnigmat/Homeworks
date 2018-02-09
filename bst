/**
 * Class BST - binary search tree.
 * <p>
 * This class implements features/methods of BTreeInterface class
 */
public class BST implements TreeInterface {

    /**
     * Root of tree
     * <p>
     * From it we'll always start any our action
     */
    protected Node head = new Node();

    /**
     * Queue for print() and traverse() methods
     */
    private LinkedQueue<Node> queue = new LinkedQueue<Node>();

    /**
     * Remove element from tree
     *
     * @param key
     */
    @Override
    public void remove(int key) {

        /**
         * Start function to find and delete element
         */
        removeHeadChecker(key);

    }

    /**
     * Start function which first check that key placed on head node
     * or not and if not starts recursive searching method
     *
     * @param key
     */
    protected void removeHeadChecker(int key) {
        /**
         * If key inside head delete head node with special method
         */
        if (head.value == key) {
            deleteHeadNode();
        }
        /**
         * Otherwise go deep in our tree
         */
        else {
            if (head.value > key) {
                remove(key, head.left);
            } else {
                remove(key, head.right);
            }
        }
    }

    protected void deleteHeadNode() {
        /**
         * If no children in head just make head node value equal null
         *
         * If have one of them, just up them to head
         *
         * If have two child refactor head node
         */
        if (head.left == null || head.left.value == null && head.right == null || head.right.value == null) {
            head.value = null;
        } else if (head.left == null || head.left.value == null) {
            head = head.right;
        } else if (head.right == null || head.right.value == null) {
            head = head.left;
        } else {

            /**
             * Refactoring of head node
             */
            if (head.right.left == null || head.right.left.value == null) {
                head.right.left = head.left;
                head = head.right;
            } else {
                Node tempNode = head.right;
                findLeft(tempNode);

                tempNode.parent.left = tempNode.right;

                head.value = tempNode.value;
            }
        }
    }

    /**
     * Delete node method
     *
     * @param node
     */
    protected void deleteNode(Node node) {

        /**
         * If no child go to parent of current node and create new node
         * at the place of current node
         *
         * If have one of child just make them up. Replace current node
         * to its child
         *
         * If we have two child then more complicated refactoring
         */
        if ((node.left == null || node.left.value == null) && (node.right == null || node.right.value == null)) {

            /**
             * Find where current node placed relative to its parent
             */
            if (node.parent.value >= node.value) {
                node.parent.left = new Node();
            } else {
                node.parent.right = new Node();
            }
        } else if (node.left == null || node.left.value == null) {
            /**
             * Find where current node placed relative to its parent
             */
            if (node.parent.value >= node.value) {
                node.parent.left = node.right;
            } else {
                node.parent.right = node.right;
            }
        } else if (node.right == null || node.right.value == null) {
            /**
             * Find where current node placed relative to its parent
             */
            if (node.parent.value >= node.value) {
                node.parent.left = node.left;
            } else {
                node.parent.right = node.left;
            }
        } else {
            if (node.right.left == null || node.right.left.value == null) {
                /**
                 * Find where current node placed relative to its parent
                 */
                if (node.parent.value >= node.value) {
                    node.parent.left = node.right;
                    node.right.left = node.left;
                } else {
                    node.parent.right = node.right;
                    node.right.left = node.right;
                }

            } else {
                Node tempNode = node.right;
                findLeft(tempNode);

                tempNode.parent.left = new Node();

                /**
                 * Find where current node placed relative to its parent
                 */
                if (node.parent.value >= node.value) {
                    node.parent.left = tempNode;
                    node.parent.left.left = node.left;
                    node.parent.left.right = node.right;
                } else {
                    node.parent.right = tempNode;
                    node.parent.right.left = node.left;
                    node.parent.right.right = node.right;
                }
            }
        }
    }

    /**
     * Recursive method to find node where value is equal key
     * @param key
     * @param node
     */
    private void remove(int key, Node node) {
        if (key < node.value) {
            remove(key, node.left);
        } else if (key > node.value) {
            remove(key, node.right);
        } else {
            deleteNode(node);
        }
    }

    /**
     * Find the leftest(if we may say that) element of particular node
     *
     * This method uses for refactoring in deleteNode method
     * @param node
     */
    private void findLeft(Node node) {
        if (node.left != null && node.left.value != null) {
            node = node.left;
            findLeft(node);
        } else {
            return;
        }
    }

    /**
     * Public method to insert the element into the tree
     * @param key
     */
    @Override
    public void insert(int key) {

        /**
         * Start protected recursive method for searching place for
         * our key
         */
        insert(key, head);
    }

    /**
     * Recursive method to find place where we can insert element and
     * to insert this element
     * @param key
     * @param node
     */
    protected void insert(int key, Node node) {
        /**
         * If free node, put element into it
         *
         * Otherwise continue your searching
         */
        if (node.value == null) {
            node.value = key;
            node.left = new Node();
            node.right = new Node();
            node.left.parent = node;
            node.right.parent = node;
            return;
        } else if (node.value <= key) {
            insert(key, node.right);
        } else {
            insert(key, node.left);
        }
    }

    /**
     * Integer for find method
     */
    private static int num = 0;

    /**
     * Public method to find elements
     *
     * It's return integer which equal how much time do we find element
     * @param key
     * @return
     */
    @Override
    public int find(int key) {
        num = 0;
        /**
         * Start recursive find method
         */
        find(key, head);
        return num;
    }

    /**
     * Method to count how much element placed into tree
     * @param key
     * @param node
     */
    private void find(int key, Node node) {
        if (node != null && node.value != null && key < node.value) {
            find(key, node.left);
        } else if (node != null && node.value != null && key > node.value) {
            find(key, node.right);
        } else if (node != null && node.value != null && key == node.value) {
            num++;
            find(key, node.right);
        }
    }

    /**
     * String for traverse method
     */
    private static String traverse = "";

    /**
     * Return traverse of tree
     * @return
     */
    @Override
    public String traverse() {
        traverse = "";

        /**
         * Start recursive method traverse
         */
        traverse(head);

        return traverse;
    }

    /**
     * Private method to write traverse of our tree
     * @param node
     */
    private void traverse(Node node) {

        /**
         * First goes to left
         */
        if (node.left != null && node.left.value != null) {
            traverse(node.left);
        }

        /**
         * After write element into traverse string
         */
        traverse += node.value + " ";

        /**
         * At the end goes to right node nad repeat all actions
         * again
         */
        if (node.right != null && node.right.value != null) {
            traverse(node.right);
        }
    }

    /**
     * Prints tree
     * @return
     */
    @Override
    public String print() {
        String print = "";

        /**
         * Push into queue head node(root)
         */
        queue.push(head);

        /**
         * It goes in all nodes in a tree and put child of this node
         * to queue and after add to string its value
         */
        while (queue.size() != 0) {

            Node tempNode = queue.dequeue();

            if (tempNode.left != null && tempNode.left.value != null && (tempNode.left.left != null && tempNode.left.left.value != null) || (tempNode.left.right != null && tempNode.left.right.value != null)) {
                queue.push(tempNode.left);
            }
            if (tempNode.right != null && tempNode.right.value != null && (tempNode.right.left != null && tempNode.right.left.value != null) || (tempNode.right.right != null && tempNode.right.right.value != null)) {
                queue.push(tempNode.right);
            }


            print += tempNode.value + " ";
            if (tempNode.left != null && tempNode.left.value != null) {
                print += tempNode.left.value + " ";
            }
            if (tempNode.right != null && tempNode.right.value != null) {
                print += tempNode.right.value + "\n";
            } else {
                print += "\n";
            }
        }

        return print;
    }

    /**
     * Method which do almost the same as print method.
     *
     * But it only change way(sounds not very understandable, i know)
     *
     * It just starts from right the first and left the second
     * @return
     */
    public String mirror() {
        String mirror = "";

        queue.push(head);

        while (queue.size() != 0) {

            Node tempNode = queue.dequeue();


            if (tempNode.right != null && tempNode.right.value != null && (tempNode.right.left != null && tempNode.right.left.value != null) || (tempNode.right.right != null && tempNode.right.right.value != null)) {
                queue.push(tempNode.right);
            }

            if (tempNode.left != null && tempNode.left.value != null && (tempNode.left.left != null && tempNode.left.left.value != null) || (tempNode.left.right != null && tempNode.left.right.value != null)) {
                queue.push(tempNode.left);
            }


            mirror += tempNode.value + " ";

            if (tempNode.right != null && tempNode.right.value != null) {
                mirror += tempNode.right.value + " ";
            }
            if (tempNode.left != null && tempNode.left.value != null) {
                if (queue.size() != 0)
                    mirror += tempNode.left.value + "\n";
                else
                    mirror += tempNode.left.value;
            } else {
                if (queue.size() != 0) {
                    mirror += "\n";
                }
            }

        }

        return mirror;
    }
}
