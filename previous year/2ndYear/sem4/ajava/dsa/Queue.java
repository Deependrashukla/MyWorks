import java.util.*;

public class Queue {
    public static void main(String[] args) {
        PriorityQueue<String> queue = new PriorityQueue<String>();
        queue.add("apple");
        queue.add("ball");
        queue.add("cat");
        queue.add("axlo");
        System.out.println("head element : " + queue.element()); //give error if head element is not there
        System.out.println("head peek : " + queue.peek()); // give null
        PriorityQueue<Integer> queue2 = new PriorityQueue<Integer>();
        queue2.add(4);
        queue2.add(1);
        queue2.add(2);
        queue2.add(6);
        System.out.println("head element : " + queue2.element());
        System.out.println("head peek : " + queue2.peek());

        Iterator<Integer> itr = queue2.iterator();
        while( itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}
