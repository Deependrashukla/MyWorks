
class Sample1{
    static int a;
    void show(){
        System.out.println("sample 1");
    }
}

class Sample2 extends Sample1{
    static int a;
    void show(){
        System.out.println("sample 2");
    }
}



public class SampleMain extends Sample2{
    public static void main(String[] args) {
        Sample1 s1 = new Sample1();
        Sample1 s2 = new Sample1();
        s1.a = 1;
        s2.a = 2;
        System.out.println(s1.a);
        System.out.println(s2.a);
        System.out.println(Sample1.a);
    }
    
}
