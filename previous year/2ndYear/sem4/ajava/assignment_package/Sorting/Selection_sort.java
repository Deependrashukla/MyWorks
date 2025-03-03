package Sorting;

public class Selection_sort {

    public void selection(int[] arr){
        int j = 0;
        while (j != arr.length-1){
            int min = j;
            for (int i = j; i < arr.length; i++){
                if (arr[i] < arr[j]){
                    int temp = arr[j];
                    min = i;
                    arr[j] = arr[min];
                    arr[min] = temp;    
                }}
            j++;
    }}

    
}
