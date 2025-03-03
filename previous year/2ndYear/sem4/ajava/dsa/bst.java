// public class bst {
//     static Node root = null;

//     public static class Node {
//         int data;
//         Node left, right;

//         Node(int data) {
//             this.data = data;
//         }
//     }

//     public static Node insertNode(Node root, int data) {
//         if (root == null) {
//             root = new Node(data);
//         } else {
//             if (data < root.data) {
//                 root.left = insertNode(root.left, data);
//             } else {
//                 root.right = insertNode(root.right, data);
//             }
//         }
//         return root;
//     }

//     public static void inorderTraversal(Node root) {
//         if (root == null) {
//             return;
//         } else {
//             inorderTraversal(root.left);
//             System.out.print(root.data + " ");
//             inorderTraversal(root.right);
//         }
//     }

//     public static boolean search(Node root, int key) {
//         if (root == null) {
//             return false;
//         } else {
//             if (root.data == key) {
//                 return true;
//             } else if (key < root.data) {
//                 return search(root.left, key);
//             } else {
//                 return search(root.right, key);
//             }
//         }
//     }

//     public static Node deleteNode(Node root, int data) {
//         if (root == null) {
//             return null;
//         } else {
//             if (data < root.data) {
//                 root.left = deleteNode(root.left, data);
//             } else if (data > root.data) {
//                 root.right = deleteNode(root.right, data);
//             } else {
//                 if (root.left == null && root.right == null) {
//                     return null;
//                 } else if (root.left == null) {
//                     return root.right;
//                 } else if (root.right == null) {
//                     return root.left;
//                 } else {
//                     Node insc = inOrderSuccessor(root.right);
//                     root.data = insc.data;
//                     root.right = deleteNode(root.right, insc.data);
//                 }
//             }
//             return root;
//         }
//     }

//     public static Node inOrderSuccessor(Node root) {
//         while (root.left != null) {
//             root = root.left;
//         }
//         return root;
//     }

//     public static void main(String[] args) {
//         int arr[] = { 20, 5, 8, 3, 4, -6 };

//         for (int i : arr) {
//             root = insertNode(root, i);
//         }

//         System.out.println("Inorder traversal:");
//         inorderTraversal(root);
//         System.out.println();

//         // Example usage of deletion
//         root = deleteNode(root, 8);
//         System.out.println("Inorder traversal after deletion:");
//         inorderTraversal(root);

//         insertNode(root, 6);
//         System.out.println("inorder:");
//         inOrderSuccessor(root);
//     }
// }


// import java.util.*;
// public class bst{
// public static void main(String args[]){
// //Creating Array
// String[] array={"Java","Python","PHP","C++"};
// System.out.println(Arrays.toString(array));
// System.out.println("Printing Array: "+Arrays.toString(array));
// //Converting Array to List
// List<String> list=new ArrayList<String>();
// for(String lang:array){
// list.add(lang);
// }
// System.out.println(list);
// System.out.println("Printing List: "+list);
// }
// }
