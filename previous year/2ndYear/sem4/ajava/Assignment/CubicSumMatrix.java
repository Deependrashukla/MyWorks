import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class CubicSumMatrix {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= 9; i++) {
            numbers.add(i);
        }

        List<List<Integer>> permutations = generatePermutations(numbers);
        
        List<int[][]> validMatrices = new ArrayList<>();
        
        for (List<Integer> perm : permutations) {
            int[][] matrix = new int[3][3];
            int index = 0;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    matrix[i][j] = perm.get(index++);
                }
            }
            if (checkSums(matrix)) {
                validMatrices.add(matrix);
            }
        }
        if (!validMatrices.isEmpty()) {
            int randomIndex = new Random().nextInt(validMatrices.size());
            int[][] selectedMatrix = validMatrices.get(randomIndex);
            printMatrix(selectedMatrix);
        } else {
            System.out.println("Not a valid  matrix matched.");
        }
    }
    
    private static boolean checkSums(int[][] matrix) {
        for (int i = 0; i < 3; i++) {
            int rowSum = 0;
            int colSum = 0;
            for (int j = 0; j < 3; j++) {
                rowSum += matrix[i][j];
                colSum += matrix[j][i];
            }
            if (rowSum != 15 || colSum != 15) {
                return false;
            }
        }
        return checkDiagonalSums(matrix);
    }
    
    private static boolean checkDiagonalSums(int[][] matrix) {
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < 3; i++) {
            sum1 += matrix[i][i];
            sum2 += matrix[i][2 - i];
        }
        return sum1 == 15 && sum2 == 15;
    }
    
    private static void printMatrix(int[][] matrix) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static List<List<Integer>> generatePermutations(List<Integer> numbers) {
        List<List<Integer>> permutations = new ArrayList<>();
        permute(numbers, 0, permutations);
        return permutations;
    }
    
    private static void permute(List<Integer> numbers, int start, List<List<Integer>> permutations) {
        if (start == numbers.size()) {
            permutations.add(new ArrayList<>(numbers));
            return;
        }
    
        for (int i = start; i < numbers.size(); i++) {
            swapElements(numbers, start, i);
            permute(numbers, start + 1, permutations);
            swapElements(numbers, start, i);
        }
    }

    private static void swapElements(List<Integer> list, int i, int j) {
        int temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }
}