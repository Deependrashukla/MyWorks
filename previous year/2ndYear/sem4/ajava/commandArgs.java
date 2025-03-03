public class commandArgs {
    public static void main(String args[]) {
        // System.out.println(args[]);
        System.out.println(" the command lines args are:");
        if (args.length>0){
            // System.out.println("argss are");
            for(String val : args)
                System.out.println(val);
        }
        else{
            System.out.println("no args given");
        }
    }
}
