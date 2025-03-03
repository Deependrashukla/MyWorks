public class diff_method {
    public static void main(String[] args) {
        String a = "  hi   how are you     but.";
        String[] words = a.split(" "); // Split the string into an array of words
        for (String word : words) {
            System.out.println(word);
        }
    }
}
