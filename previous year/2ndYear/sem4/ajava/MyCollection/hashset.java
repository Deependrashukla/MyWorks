class book{
    int id;
    String name, author;
    book(int id, String author){
        this.id = id;
        this.author = author;
    }
}


public class hashset {
    public static void main(String[] args) {
        book s = new book(1, "deep");
        System.out.println(s);
        System.out.println(s.toString());
    }
}
