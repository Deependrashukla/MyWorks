class compiletime{
    int sum(int a, int b){
        System.out.println("from int sum");
        return a+b;
    }
    double sum(int a, double b){
        System.out.println("from double sum");
        return a + b;

    }
}



class parent{
    void conversion(int a){
        System.out.println("convert prent class" + a);
    }
}

class binDeci extends parent{
    void conversion(int a){
        System.out.println("convert binDeci" + a) ;
    }
}

class deciBin extends parent{ 
    void conversion(int a){
        System.out.println("convert deciBin" + a);
    }
}

public class Polymorphism {
    public static void main(String[] args) {
        parent o;
        o = new parent();
        o.conversion(5);
        o = new binDeci();
        o.conversion(6);
        o = new deciBin();
        o.conversion(5);

        compiletime a;
        a = new compiletime();
        int s = a.sum(1,20);
        System.out.println(s);
        double p = a.sum(5, 7.5);
        System.out.println(p);
        
    }
    
}
