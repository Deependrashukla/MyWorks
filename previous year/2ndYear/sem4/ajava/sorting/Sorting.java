
import java.util.Random;
class Diff_sort{
    
        void bubble (int[] arr){
            int j = arr.length;
            while (j != 1){
                for (int i = 0; i < j-1; i++){
                    if (arr[i] > arr[i+1]){
                        int element = arr[i+1];
                        arr[i+1] = arr[i];
                        arr[i] = element;
                    }}j--;
        }}
        
        void selection(int[] arr){
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


        void insertion(int[] arr){
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
    


public class Sorting{
    public static void main(String[] args) {
        int[] arr = new int[10];
        Random rd = new Random();
        System.out.print("given array: ");
        for (int i = 0; i < arr.length; i++){
            arr[i] = rd.nextInt(10);
            System.out.print(arr[i]+ " ");
        }

        long start = System.currentTimeMillis();
        Diff_sort b = new Diff_sort();
        b.insertion(arr);
        long end = System.currentTimeMillis();
        System.out.println();
        System.out.print("sorted array: ");
        for(int num:arr){
            System.out.print(num + " ");   
        }
        System.out.println();
        System.out.println("Time taken: " + (end-start));
    
    }

}


