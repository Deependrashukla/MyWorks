class stack_class{
    Node head;

    class Node{
        int data;
        Node next;

        Node(int data){
            this.data = data;
            this.next = null;
        }
    }
    void push(int data){
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
    int pop(){

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

    int top(){
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

public class Stack {
    public static void main(String[] args) {
        stack_class o = new stack_class();
        // o.push(5);
        // o.push(2);
        // o.push(8);

        System.out.println(o.top());
        System.out.println(o.pop());
        o.pop();
        // o.pop();
        System.out.println(o.top());
    }
    
}
