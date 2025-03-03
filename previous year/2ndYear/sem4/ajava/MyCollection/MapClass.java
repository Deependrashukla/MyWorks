// package MyCollection;

import java.util.*;

public class MapClass {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "deep");
        map.put(2, "akan");
        map.put(3, "push");
        // double inf = Double.POSITIVE_INFINITY;
        
        // for (Map.Entry m : map.entrySet()){
        //     System.out.println(m);
        // }

        // for (int i : map.keySet()){
        //     System.out.println(i + " " + map.get(i));
        // }
        HashMap<Integer, String> map1 = new HashMap<Integer, String>();
        map.put(4, "jeep");
        map.put(2, "akan");
        map.put(3, "kush");
        map.put(5, "kush");

        map.putAll(map1);
        
        map.remove(1);
        map.values().remove("kush");

        for (int i : map.keySet()){
            System.out.println(i + " " + map.get(i));
        }


    }
}