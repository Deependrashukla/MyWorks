import java.util.*;

public class Set {
    public static void main(String[] args) {
        LinkedHashSet<String> set = new LinkedHashSet<String>();
        set.add("azi");
        set.add("akank");
        set.add("shuk");
        set.add("deep");
        
        Iterator<String> itr = set.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}
