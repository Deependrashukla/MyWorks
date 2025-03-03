import java.util.*;

public class arraylist {
    public static void main(String[] args) {
        ArrayList<Integer> al1 = new ArrayList<>();
        al1.add(1);al1.add(2);
        al1.add(3);al1.add(4);
        al1.add(5);
        System.out.println(al1);

        ArrayList<Integer> al2 = new ArrayList<>();
        al2.add(4);al2.add(6);
        al2.add(5);
        System.out.println(al2);

        al1.retainAll(al2);
        System.out.println(al1.retainAll(al2));

        for (int a : al1){
            System.out.println(a);
        }

    }
    
}
