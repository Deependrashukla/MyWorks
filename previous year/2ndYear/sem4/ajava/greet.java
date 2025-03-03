public class greet {
    public String says(){
        return "hello";
    }

    public String voter(int age){
        if(age < 18){
            return "not eligible";
        }
        else{
            return "eligible";
        }
    }
    
}
