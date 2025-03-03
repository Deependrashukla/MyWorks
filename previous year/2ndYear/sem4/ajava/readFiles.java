import java.io.*;
import java.util.*;

public class readFiles {
    private static final Set<String> stopwords = new HashSet<>(Arrays.asList(
            "the", "and", "is", "in", "it", "of", "to", "for", "with", "on"
    ));

    public static void main(String[] args) {
        // Set the directory path
        String directoryPath = "/home/ankita/Documents/Java/text_files";

        // Get the list of files in the directory
        File dir = new File(directoryPath);
        File[] files = dir.listFiles();

        if (files != null) {
            // 1) Total number of files
            System.out.println("Total number of files: " + files.length);

            for (File file : files) {
                if (file.isFile()) {
                    // 2) Content of each file and total number of words
                    printFileContent(file);

                    // 3) Word frequency
                    printWordFrequency(file);

                    // 4) Content of each file after removing stopwords
                    printFileContentWithoutStopwords(file);
		    System.out.println("\n ");
                }
            }
        } else {
            System.out.println("The specified directory does not exist.");
        }
    }

    private static void printFileContent(File file) {
        System.out.println("\nFile name is: " + file.getName());
	System.out.println("The above file's content: ");
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            int wordCount = 0;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
                wordCount += line.split("\\s+").length;
            }
	    System.out.println();
            System.out.println("Total words: " + wordCount);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void printWordFrequency(File file) {
        System.out.println("\nWord frequency in file " + file.getName() +":");
        try (Scanner scanner = new Scanner(file)) {
            Map<String, Integer> wordFrequency = new HashMap<>();
            while (scanner.hasNext()) {
                String word = scanner.next().toLowerCase();
                wordFrequency.put(word, wordFrequency.getOrDefault(word, 0) + 1);
            }
            for (Map.Entry<String, Integer> entry : wordFrequency.entrySet()) {
                System.out.print(entry.getKey() + ": " + entry.getValue()+", ");
            }
	    System.out.println();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private static void printFileContentWithoutStopwords(File file) {
        System.out.println("\nFile content without stopwords in file " + file.getName() + ":");
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] words = line.split("\\s+");
                for (String word : words) {
                    if (!stopwords.contains(word.toLowerCase())) {
                        System.out.print(word + " ");
                    }
                }
                System.out.println(); // Move to the next line after processing each line
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
