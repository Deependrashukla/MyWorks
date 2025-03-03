package Linked_List;

public class Linked_list {

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

    public void addFirst(int data) {
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

    public void show() {
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

    public int getSize(){
        return size;
    }

    public void addLast(int data){
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

    public void deleteFirst(){
        if (head == null){
            System.out.println("cant delete: ");
        }
        else{
            head = head.next;
            size--;
        }
    }
    public void deleteLast(){
        Node tempNode = head;
            while (tempNode.next.next != null) {
                tempNode = tempNode.next;
            }
            tempNode.next = null;
    }
}
