// public class functionalInterface {
//     public static void main(String[] args) {
//         inf o = () -> {
//             System.out.println("show");
//         };   
//         o.show();

//         rectarea o1 = (x,y) -> {
//             System.out.println("area of rect: "+ x*y);
//         };
//         o1.area(2,5);

//     }


// }
// // have only one abstract method and no. of default methods
// interface inf{
//     void show();
//     default void show1(){
//         System.out.println("show1");
//     }
// }


// interface rectarea{
//     void area(int x, int y);
// }

import java.util.*;

public class functionalInterface {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<String>();
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");
        list.forEach((o)-> System.out.println(o));

    }
}