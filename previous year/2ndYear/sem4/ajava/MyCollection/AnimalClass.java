public class AnimalClass{
    public static void main(String[] args) {
        Birds b1 = new Birds("Parrot", 5);
        System.out.println(b1.numBirds);
        Birds b2 = new Birds("Crow", 10);
        Birds b3 = new Birds("Pigeon", 2);
        Birds b4 = new Birds("Sparrow",4);
        Birds b5 = new Birds("Peacock", 3);

        
        System.out.println(b2.numBirds);
        System.out.println(b3.numBirds);
        System.out.println(b4.numBirds);
        System.out.println(b5.numBirds);
    }
}

class Birds{
    String name;
    int age;
    static int numBirds = 0;
    Birds(String name, int age){
        this.name = name;
        this.age = age;
        numBirds++;
        show();
    }

    void show(){
        System.out.println("Bird: " + this.name + "\tage: "+ this.age+"\tnumber of words: " + this.numBirds);
    }
}