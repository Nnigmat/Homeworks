/**
 * Class AVLT which extend BST class
 */
public class AVLT extends BST {
    /**
     * Number of elements in AVLT
     */
    private int size = 0;

    /**
     * Insert element into tree and after balance all tree
     *
     * And also increase size of tree
     * @param key
     */
    @Override
    public void insert(int key) {
        super.insert(key, head);
        size++;
        balance();
    }

    /**
     * Remove element from tree
     *
     * After balance tree
     *
     * Also increase size of tree
     * @param key
     */
    @Override
    public void remove(int key) {
        super.remove(key);
        size--;
        balance();
    }

    /**
     * First recount height of each node
     *
     * After it find node where we have unbalancing(if no it's null)
     *
     * After use trinode method to current node
     */
    private void balance() {
        countHeight(head);
        Node unNode = findUnbalancedNode(head);
        trinode(unNode);
    }

    /**
     * We have some properties and based on it was created this method
     * It's too complicated part of all class and i think i'll can't
     * describe it in this comment
     *
     * To understand you need to see how it works in some examples on peace
     * of paper
     *
     * This method balance all tree
     * @param node
     */
    private void trinode(Node node) {

        /**
         * If node is equal null go out from this method
         */
        if (node == null) {
            return;
        }

        Node y, x;

        if (node.left.height < node.right.height) {
            y = node.right;

            if (y.left.height < y.right.height) {

                x = y.right;

                node.right = y.left;
                node.right.parent = node;

                y.left = node;

                if (node == head) {
                    head = y;
                } else {
                    y.parent = node.parent;
                    if (node.parent.value > y.value) {
                        node.parent.left = y;
                    } else {
                        node.parent.right = y;
                    }

                }

                node.parent = y;

            } else {

                x = y.left;

                y.left = x.right;
                y.left.parent = y;

                node.right = x.left;
                node.right.parent = node;

                if (node == head) {
                    head = x;
                } else {
                    x.parent = node.parent;
                    if (node.parent.value > x.value) {
                        node.parent.left = x;
                    } else {
                        node.parent.right = x;
                    }
                }

                x.left = node;

                node.parent = x;

                x.right = y;
                y.parent = x;

            }
        } else {

            y = node.left;

            if (y.left.height < y.right.height) {
                x = y.right;

                y.right = x.left;
                y.right.parent = y;
                y.parent = x;

                if (head == node) {
                    head = x;
                } else {
                    if (node.parent.value > x.value) {
                        node.parent.left = x;
                    } else {
                        node.parent.right = x;
                    }
                    x.parent = node.parent;
                }

                node.left = x.right;
                node.left.parent = node;
                node.parent = x;

                x.left = y;
                x.right = node;
            } else {

                node.left = y.right;
                node.left.parent = node;

                x = y.left;

                y.right = node;

                if (node == head) {
                    head = y;
                } else {
                    if (node.parent.value > x.value) {
                        node.parent.left = x;
                    } else {
                        node.parent.right = x;
                    }
                    y.parent = node.parent;
                }

                node.parent = y;
            }

        }

    }

    /**
     * This method find unbalanced node into tree if it has it or
     * return null
     * @param node
     * @return
     */
    private Node findUnbalancedNode(Node node) {
        if ((node.left != null && node.left.value != null) || (node.right != null && node.right.value != null)) {

            if ((node.left != null && node.left.value != null) && (node.right != null && node.right.value != null)) {
                if (Math.abs(node.left.height - node.right.height) > 1) {
                    return node;
                } else {
                    Node left = findUnbalancedNode(node.left);
                    Node right = findUnbalancedNode(node.right);

                    if (left != null) {
                        return left;
                    } else if (right != null) {
                        return right;
                    } else {
                        return null;
                    }
                }
            } else if (node.left == null || node.left.value == null) {

                if (node.right.height > 1) {
                    return node;
                }

                return findUnbalancedNode(node.right);
            } else {

                if (node.left.height > 1) {
                    return node;
                }

                return findUnbalancedNode(node.left);
            }

        } else {
            return null;
        }
    }

    /**
     * Sum of smaller element
     * @return
     */
    public int sumOfSmaller() {
        return size * (size - 1) / 2;
    }

    /**
     * This method count height of each node
     * @param node
     * @return
     */
    private int countHeight(Node node) {
        if ((node.left == null || node.left.value == null) && (node.right == null || node.right.value == null)) {
            node.height = 1;
            return 1;
        } else if (node.left == null || node.left.value == null) {
            node.height = countHeight(node.right) + 1;
            return node.height;
        } else if (node.right == null || node.right.value == null) {
            node.height = countHeight(node.left) + 1;
            return node.height;
        } else {
            node.height = Math.max(countHeight(node.left) + 1, countHeight(node.right) + 1);
            return node.height;
        }
    }
}
