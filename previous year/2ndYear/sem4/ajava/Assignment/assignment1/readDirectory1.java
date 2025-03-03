package Assignment;

import java.io.File;

public class readDirectory1 {
    public static void main(String[] args) {
        // Specify the directory path
        String directoryPath = "/home/deependra/Documents/ajava";

        // Create a File object
        File dir = new File(directoryPath);
        System.out.println(dir);
        // Get all the names of the files present in the directory
        String[] fileNames = dir.list();
        System.out.println("printing    fielslnadmnfalenl");
        System.out.println(fileNames);


        // If the directory is not empty
        if (fileNames != null) {
            // Print the names of the files
            for (String fileName : fileNames) {
                System.out.println(fileName);
            }
        } else {
            System.out.println("The directory is empty or does not exist.");
        }
    }
}
