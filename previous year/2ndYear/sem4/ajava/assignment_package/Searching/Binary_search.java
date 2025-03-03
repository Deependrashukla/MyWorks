package Searching;

public class Binary_search{

    public int binary_search(int[] arr, int target){
        int steps = 0;
        int left = 0;
        int right = arr.length - 1;
        int mid = (left + right)/2;
        while (left <= right){
            steps++;
            if (arr[mid] == target){
                System.out.println("Total no. of steps : " + steps);
                return mid;
            }
            else if (target > arr[mid]){
                left = mid + 1;  
            }
            else if (target < arr[mid]){
                right = mid - 1;
            }
        }
        System.out.println("Total no. of steps : " + steps);
        System.out.print("Target is not present in given array");
        return -1;
    }
}
