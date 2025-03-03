class LinkedList {
    Node head;
    int size = 0;

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    void addFirst(int data) {
        Node newNode = new Node(data);
        System.out.println("adding node at first: " + newNode.data);
        if (head == null) {
            head = newNode;

        } else {
            newNode.next = head;
            head = newNode;
        }
        size++;
    }

    void show() {
        if (head == null) {
            System.out.println("List is empty");
        } else {
            Node tempNode = head;
            while (tempNode != null) {
                System.out.print(tempNode.data+ "-->");
                tempNode = tempNode.next;
            }
            System.out.print(tempNode);
            System.out.println();
        }
    }

    int getSize(){
        return size;
    }

    void addLast(int data){
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        }else{
            Node tempNode = head;
            while (tempNode.next != null) {
                tempNode = tempNode.next;
            }
            tempNode.next = newNode;
        }
        size++;
    }

    void deleteFirst(){
        if (head == null){
            System.out.println("cant delete: ");
        }
        else{
            head = head.next;
            size--;
        }
    }
    void deleteLast(){
        Node tempNode = head;
            while (tempNode.next.next != null) {
                tempNode = tempNode.next;
            }
            tempNode.next = null;
    }
}



public class Linked_list {
    public static void main(String[] args) {
        // System.out.println("I am going to create Linked List");
        LinkedList mylist = new LinkedList();
        mylist.show();
        mylist.addFirst(5);
        mylist.show();
        mylist.addFirst(6);
        mylist.show();
        mylist.addLast(8);
        mylist.show();
        mylist.deleteFirst();
        mylist.show();
        mylist.addLast(2);
        mylist.show();
        mylist.deleteLast();
        mylist.show();
        mylist.getSize();
    }
}