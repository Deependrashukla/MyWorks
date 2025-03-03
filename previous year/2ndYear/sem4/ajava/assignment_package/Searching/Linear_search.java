package Searching;

public class Linear_search{

    public int linear_search(int[] arr, int target){
        int steps = 0;
        for (int i = 0; i < arr.length; i++){
            steps++;
            if (arr[i] == target){
                System.out.println("Total no. of steps : " + steps);
                System.out.print("target found at index : ");
                return i;
            }
        }
        System.out.println("Total no. of steps : " + steps);
        System.out.print("Target is not present in given array");
        return -1;
    }

}