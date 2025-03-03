class Concrete1{
    public void show(){
        System.out.println("from concrete1");
    }
    void display(){
        System.out.println("display from concrete1 ");
    }
}

class Concrete2 extends Concrete1{
    public void show(){
        System.out.println("show from concrete2");
    }
    // void display(){
    //     System.out.println("display from concrete2 ");
    // }   
}

public class Selection {
    public static void main(String[] args) {
        Concrete1 c1 = new Concrete2();
        c1.show();
        c1.display();
    }
}
