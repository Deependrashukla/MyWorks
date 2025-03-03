package stack;


public class Stack {

    Node head;

    class Node{
        int data;
        Node next;

        Node(int data){
            this.data = data;
            this.next = null;
        }
    }
    public void push(int data){
        Node newNode = new Node(data);
        if (head == null){
            head = newNode;   
        } else {
            Node tempNode = head;
            while (tempNode.next != null) {
                tempNode = tempNode.next;
            }
        tempNode.next = newNode;
        }
    }
    public int pop(){
        if (head == null){
            return -1;  
        } else {
            Node tempNode = head;
            while (tempNode.next.next != null) {
                tempNode = tempNode.next;
            }
            int data = tempNode.data;
            tempNode.next = null;
            return data;
        }
    }

    public int top(){
        if (head == null){
            return -1;
        }else {
            Node tempNode = head;
            while (tempNode.next != null) {
                tempNode = tempNode.next;
            }
            return tempNode.data;
    }

    }
}
