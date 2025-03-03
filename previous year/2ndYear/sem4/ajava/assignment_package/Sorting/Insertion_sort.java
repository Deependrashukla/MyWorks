package Sorting;

public class Insertion_sort {

    public void insertion(int[] arr){
        int j = 1;
        while (j != arr.length){
            for (int i = j; i > 0; i--){
                if (arr[i] < arr[i-1]){
                    int temp = arr[i];
                    arr[i] = arr[i-1];
                    arr[i-1] =  temp;
                }
            }
            j++;
        }}
    
}
