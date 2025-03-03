class leap {
    boolean isLeap(int a){
        if (a%400 == 0 || (a%4) == 0 && a%100 != 0){
            return true;
        }return false;       
    }
}

public class LeapYear{
    public static void main(String[] args){
        leap o = new leap();
        System.out.println(o.isLeap(45));
        System.out.println();
        
    }
}

