import java.io.File;
import java.util.Scanner;


public class scrapDirectory {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Scraping to be done on directory :  ");
        String path = sc.nextLine();
        scrap(path);



    }
        static void scrap(String path){
            File dir = new File(path); 
            String[] filenames = dir.list();
            if(filenames == null){
                System.out.println("no files present in this directory");
                return;}
            String[] files;
            for(String file : filenames){
                System.out.println(file);
            }
        

        
    }
}
