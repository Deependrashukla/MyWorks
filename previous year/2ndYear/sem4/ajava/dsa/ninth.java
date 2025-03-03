// class Student {
//     int id;
//     void show() {
//         System.out.println("I am show method");
//     }
// }

// public class ninth {
//     public static void main(String[] args) {
//         Student s1 = new Student();
//         System.out.println(s1);
//         System.out.println(s1.toString()); 
//     }
// }

public class ninth {
    public static class Node {
        int data;
        Node left, right;

        Node(int data) {
            this.data = data;
        }
    }

    public static Node insertNode(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            if (data < root.data) {
                root.left = insertNode(root.left, data);
            } else if (data > root.data) {
                root.right = insertNode(root.right, data);
            }
        }
        return root;
    }

    public static void inorderTraversal(Node root) {
        if (root == null) {
            return;
        } else {
            inorderTraversal(root.left);
            System.out.print(root.data + " ");
            inorderTraversal(root.right);
        }
    }

    public static boolean searchTree(Node root, int key) {
        if (root == null) {
            return false;
        } else {
            if (root.data == key) {
                return true;
            } else if (key < root.data) {
                return searchTree(root.left, key);
            } else {
                return searchTree(root.right, key); 
            }
        }

    }

    public static Node deletNode(Node root, int key) {
        if (root == null) {
            return root;
        } else {
            if (key < root.data) {
                root.left = deletNode(root.left, key);
            } else if (key > root.data) {
                root.right = deletNode(root.right, key);
            } else {
                if (root.left == null && root.right == null) {
                    return null;
                } else if (root.left == null) {
                    return root.right;
                } else if (root.right == null) {
                    return root.left;
                } else {
                    Node temp = root.right;
                    while (temp.left != null) {
                        temp = temp.left;
                    }
                    root.data = temp.data;
                    root.right = deletNode(root.right, temp.data);
                }
            }
        }
        return root;
    }

    public static void main(String[] args) {
        int arr[] = { 20, 15, 38, 7, 92, 69, -3 };
        Node root = null;
        for (int n : arr) {
            root = insertNode(root, n);
        }
        System.out.println("Inorder Traversal..");
        inorderTraversal(root);

        System.out.println("\nSearching..");
        searchTree(root, 15);

    }
}