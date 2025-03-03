
import Sorting.*;
import Searching.*;
import queue.*;
import stack.*;
import Linked_List.*;

import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose what you want to perform.");
        System.out.println("1. Sorting");
        System.out.println("2. Searching");
        System.out.println("3. Queue");
        System.out.println("4. Stack");
        System.out.println("5. Linked_list");
        System.out.print("Enter your choice from (1-5). ");

        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                performSortingOperations();
                break;
            case 2:
                performSearchingOperations();
                break;
            case 3:
                performQueueOperations();
                break;
            case 4:
                performStackOperations();
                break;
            case 5:
                performLinkedListOperations();
                break;           
            default:
                System.out.println("It is invlaid select any one 1, 2, 3, 4 or 5.");
        }

        scanner.close();
    }

    // Define methods for each activity
    private static void performSortingOperations() {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter the array elements:");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }

        System.out.println("Choose any sorting method ");
        System.out.println("1. Bubble Sort");
        System.out.println("2. Insertion Sort");
        System.out.println("3. Merge Sort");
        System.out.println("4. Quick Sort");
        System.out.println("5. Selection Sort");
        System.out.print("Enter your choice (1-5): ");
        int sortChoice = scanner.nextInt();

        switch (sortChoice) {
            case 1:
                Bubble_sort bubbleSort = new Bubble_sort();
                bubbleSort.bubble(arr);
                break;
            case 2:
                Insertion_sort insertionSort = new Insertion_sort();
                insertionSort.insertion(arr);
                break;
            case 3:
                Merge_sort mergeSort = new Merge_sort();
                mergeSort.mergeSort(arr, 0, arr.length - 1);
                break;
            case 4:
                Quick_sort quickSort = new Quick_sort();
                quickSort.quickSort(arr, 0, arr.length - 1);
                break;
            case 5:
                Selection_sort selectionSort = new Selection_sort();
                selectionSort.selection(arr);
                break;
            default:
                System.out.println("Itis invalid select from 1, 2, 3, 4, or 5.");
        }

        System.out.println("Sorted array is ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        scanner.close();
    
    }


    private static void performSearchingOperations() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose any one search method");
        System.out.println("1. Binary Search");
        System.out.println("2. Linear Search");
        System.out.print("Enter your choice in (1 or 2) ");
        int searchChoice = scanner.nextInt();

        // Create an example array (you can replace this with your actual array)
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter the array elements");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }

        System.out.print("Enter the target value ");
        int target = scanner.nextInt();

        switch (searchChoice) {
            case 1:
                Binary_search binarySearch = new Binary_search();
                int binaryResult = binarySearch.binary_search(arr, target);
                if (binaryResult != -1) {
                    System.out.println("Target  index is : " + binaryResult);
                }
                break;
            case 2:
                Linear_search linearSearch = new Linear_search();
                int linearResult = linearSearch.linear_search(arr, target);
                if (linearResult != -1) {
                    System.out.println("Target  index is : " + linearResult);
                }
                break;
            default:
                System.out.println("It is invalid select from 1 or 2.");
        }
        scanner.close();
        
    }


    private static void performQueueOperations() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();
        Queue myQueue = new Queue(size);

        while (true) {
            System.out.println("\nChoose an operation:");
            System.out.println("1. Enqueue (Insert an element)");
            System.out.println("2. Dequeue (Delete an element)");
            System.out.println("3. Display Queue");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the element to enqueue: ");
                    int element = scanner.nextInt();
                    System.out.println(element);
                    myQueue.enQueue(element);
                    break;
                case 2:
                    int dequeuedElement = myQueue.deQueue();
                    if (dequeuedElement != -1) {
                        System.out.println("Dequeued element: " + dequeuedElement);
                    }
                    break;
                case 3:
                    myQueue.display();
                    break;
                case 4:
                    System.out.println("Exiting the program.");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("It is invalid select  from ,1 2, 3, or 4.");
            }
        }
    }

    private static void performStackOperations() {

            Scanner scanner = new Scanner(System.in);
            Stack myStack = new Stack();
    
            while (true) {
                System.out.println("\nChoose a stack operation:");
                System.out.println("1. Push (Insert an element)");
                System.out.println("2. Pop (Remove the top element)");
                System.out.println("3. Top (Get the top element)");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();
    
                switch (choice) {
                    case 1:
                        System.out.print("Enter the element to push: ");
                        int element = scanner.nextInt();
                        myStack.push(element);
                        break;
                    case 2:
                        int poppedElement = myStack.pop();
                        if (poppedElement != -1) {
                            System.out.println("Popped element: " + poppedElement);
                        } else {
                            System.out.println("Stack is empty.");
                        }
                        break;
                    case 3:
                        int topElement = myStack.top();
                        if (topElement != -1) {
                            System.out.println("Top element: " + topElement);
                        } else {
                            System.out.println("Stack is empty.");
                        }
                        break;
                    case 4:
                        System.out.println("Exiting the program.");
                        scanner.close();
                        System.exit(0);
                    default:
                        System.out.println("It is invaklid select from 1, 2, 3, or 4.");
                }
        }
        
    }

    private static void performLinkedListOperations() {

            Scanner scanner = new Scanner(System.in);
            Linked_list myLinkedList = new Linked_list();
    
            while (true) {
                System.out.println("\nChoose a linked list operation:");
                System.out.println("1. Add First (Insert an element at the beginning)");
                System.out.println("2. Add Last (Insert an element at the end)");
                System.out.println("3. Delete First (Remove the first element)");
                System.out.println("4. Delete Last (Remove the last element)");
                System.out.println("5. Show Linked List");
                System.out.println("6. Exit");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();
    
                switch (choice) {
                    case 1:
                        System.out.print("Enter the element to add at the beginning: ");
                        int elementToAddFirst = scanner.nextInt();
                        myLinkedList.addFirst(elementToAddFirst);
                        break;
                    case 2:
                        System.out.print("Enter the element to add at the end: ");
                        int elementToAddLast = scanner.nextInt();
                        myLinkedList.addLast(elementToAddLast);
                        break;
                    case 3:
                        myLinkedList.deleteFirst();
                        break;
                    case 4:
                        myLinkedList.deleteLast();
                        break;
                    case 5:
                        System.out.println("Linked List:");
                        myLinkedList.show();
                        break;
                    case 6:
                        System.out.println("Exiting the program.");
                        scanner.close();
                        System.exit(0);
                    default:
                        System.out.println("It is invalid select from 1, 2, 3, 4, 5, or 6.");
                }
            }
        
    }

}


