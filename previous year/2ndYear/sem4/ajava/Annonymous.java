class add{
    void show(){
        System.out.println("from add class");
    }
}



public class Annonymous {
    public static void main(String[] args) {
    add o = new add(){
        void show(){
            System.out.println("from Annonymous");
        }
    };
    o.show();
    }
}
