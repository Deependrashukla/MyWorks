import java.util.Scanner;
class Search{

    int linear_search(int[] arr, int target){
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

    int binary_search(int[] arr, int target){
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


public class SearchAlgo {
    public static void main(String[] args) {
	int[] arr;
	for (int i = 0; i < args.length; i++){
		arr[i] = Integer.parseInt(args[i]);
       	}
        int target = 5;
        Search o = new Search();
        System.out.println(o.linear_search(arr, target));
        System.out.println(o.binary_search(arr, target));

    }
}
