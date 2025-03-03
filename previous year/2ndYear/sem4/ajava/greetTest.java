import org.junit.*;
public class greetTest {
    @Test
    public void test(){
        greet gre = new greet();
        Assert.assertEquals("hello",gre.says());    
    }
    @Test
    public void test1(){
        greet vot = new greet();
        Assert.assertEquals("eligible",vot.voter(24));    
    }
}




// import java.util.*;
// class greetTest{
// public static void main(String args[]){
// Hashtable<Integer,String> map=new Hashtable<Integer,String>();
// map.put(100,"Amit");
// map.put(102,"Ravi");
// map.put(101,"Vijay");
// map.put(103,"Rahul");
// //Here, we specify the if and else statement as arguments of the method
// System.out.println(map.getOrDefault(101, "Not Found"));
// System.out.println(map.getOrDefault(105, "Not Fond"));
// }
// }


// class Parrot{
//     String name;
//     }
//     public abstract class greetTest {
//     public static void main(String[] args) {
//     Parrot obj1 = new Parrot();
//     Parrot obj2 = new Parrot();
//     obj1.name="Amazon";
//     obj2.name="Amazon";
    
//     System.out.println(obj1.name+"\t"+obj2.name);
//     Parrot obj3=obj1;
//     System.out.println(obj1.equals(obj2));
//     System.out.println(obj1.equals(obj3));
//     }
//     }