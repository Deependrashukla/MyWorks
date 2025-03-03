package Assignment.assignment1;

import java.io.*;
import java.util.*;

public class readDirectory {
    private static final Set<String> ignoredWords = new HashSet<>(Arrays.asList(
            "the", "and", "is", "in", "it", "of", "to", "for", "with", "on"
    ));

    public static void main(String[] args) {
        String folderPath = "/home/deependra/Documents/ajava/txtFiles";
        File folder = new File(folderPath);
        File[] fileList = folder.listFiles();

        if (fileList != null) {
            System.out.println("Total number of files: " + fileList.length);

            for (File textFile : fileList) {
                if (textFile.isFile()) {
                    displayFileContent(textFile);
                    displayWordFrequency(textFile);
                    displayContentWithoutIgnoredWords(textFile);
                    System.out.println("\n ");
                }
            }
        } else {
            System.out.println("The specified directory does not exist.");
        }
    }

    private static void displayFileContent(File textFile) {
        System.out.println("\nFile name is: " + textFile.getName());
        System.out.println("The above file's content: ");
        try (BufferedReader reader = new BufferedReader(new FileReader(textFile))) {
            String line;
            int totalWords = 0;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                totalWords += line.split("\\s+").length;
            }
            System.out.println();
            System.out.println("Total words: " + totalWords);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void displayWordFrequency(File textFile) {
        System.out.println("\nWord frequency in file " + textFile.getName() +":");
        try (Scanner scanner = new Scanner(textFile)) {
            Map<String, Integer> wordCountMap = new HashMap<>();
            while (scanner.hasNext()) {
                String word = scanner.next().toLowerCase();
                wordCountMap.put(word, wordCountMap.getOrDefault(word, 0) + 1);
            }
            for (Map.Entry<String, Integer> entry : wordCountMap.entrySet()) {
                System.out.print(entry.getKey() + ": " + entry.getValue()+", ");
            }
            System.out.println();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private static void displayContentWithoutIgnoredWords(File textFile) {
        System.out.println("\nFile content without stopwords in file " + textFile.getName() + ":");
        try (BufferedReader reader = new BufferedReader(new FileReader(textFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] words = line.split("\\s+");
                for (String word : words) {
                    if (!ignoredWords.contains(word.toLowerCase())) {
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
