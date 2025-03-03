package Sorting;

public class Bubble_sort {
    
    public void bubble (int[] arr){
        int j = arr.length;
        while (j != 1){
            for (int i = 0; i < j-1; i++){
                if (arr[i] > arr[i+1]){
                    int element = arr[i+1];
                    arr[i+1] = arr[i];
                    arr[i] = element;
                }}j--;
    }}

}
