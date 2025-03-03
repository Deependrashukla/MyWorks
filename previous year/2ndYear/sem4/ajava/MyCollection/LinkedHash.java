// package MyCollection;
import java.util.*;

public class LinkedHash {
    public static void main(String[] args) {
        // HashSet<String> set1 = new HashSet<String>();

        // set1.add("Avinash");
        // set1.add("Ankita");
        // set1.add("Deependra");
        // set1.add("Devesh");
        // set1.add("Liyana");

        // for (String s:set1){
        //     System.out.print(s+" ");
        // }
        // System.out.println();
        
        // LinkedHashSet<String> set2 = new LinkedHashSet<String>();

        // set2.add("Loren");
        // set2.add("Ankita");
        // set2.add("Deependra");
        // set2.add("Devesh");
        // set2.add("Yoshita");

        // for (String s:set2){
        //     System.out.print(s+" ");
        // }
        // System.out.println();
        // System.out.println(set2.remove("Devesh"));
        // System.out.println(set2);

        TreeSet<String> set3 = new TreeSet<String>();

        set3.add("Vvinash");
        set3.add("Ankita");
        set3.add("Deependra");
        set3.add("Devesh");
        set3.add("Liyana");

        for (String s:set3){
            System.out.print(s+" ");
        }
        System.out.println();
        System.out.println(set3);
        System.out.println(set3.pollFirst());
        System.out.println(set3);
        System.out.println(set3.pollLast());
        System.out.println(set3);

        
    }
}

class Student{
    String name;
    int age;

    Student(String name, int age){
        this.name = name;
        this.age = age;
    }

    // @Override
    public int compareTo(Student o){
        return o.age - this.age;
    }
}

