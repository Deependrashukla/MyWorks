
import java.util.*;


// class Employee implements Comparable<Employee>{
//     int id;
//     int salary;
//     Employee(int id, int salary){
//         this.id = id;
//         this.salary = salary;
//     }

//     @Override 
//     public int compareTo(Employee o){
//         return this.id - o.id;
//     }
// }

// class IDCompare implements Comparator<Employee>{

//     @Override 
//     public int compare(Employee o1, Employee o2){
//         return o1.id - o2.id;
//     }

// }

// class SalaryCompare implements Comparator<Employee>{

//     @Override 
//     public int compare(Employee o1, Employee o2){
//         return o1.salary - o2.salary;
//     }

// }

// public class comparableComparator {
//     public static void main(String[] args) {
//         // ArrayList<Integer> list = new ArrayList<Integer>();
//         // list.add(3);
//         // list.add(1);
//         // list.add(5);
//         // list.add(7);
//         // Collections.sort(list);
//         // System.out.println(list);

//         ArrayList<Employee> lst = new ArrayList<Employee>();
//         lst.add(new Employee(1,200));
//         lst.add(new Employee(3,400));
//         lst.add(new Employee(7,800));
//         lst.add(new Employee(5,1200));
        
//         // Collections.sort(lst);

//         SalaryCompare sc = new SalaryCompare();
//         Collections.sort(lst, sc);

//         for (Employee o : lst){
//             System.out.println(o.id+ " " + o.salary);
//         }

//     }
    
// }





// class emp{
//     int age;
//     int salary;
//     emp(int age, int salary){
//         this.age = age;
//         this.salary = salary;
//     }

// }

// class agecomparator implements Comparator<emp>{
//     @Override
//     public int compare(emp o1, emp o2){
//         return o1.age - o2.age;
//     }
// }

// public class comparableComparator{
//     public static void main(String[] args) {
//         ArrayList<emp> al = new ArrayList<>();
//         al.add(new emp(12,600 ));
//         al.add(new emp(13,700 ));
//         al.add(new emp(14,500 ));
//         agecomparator a = new agecomparator();
//         Collections.sort(al, a);
//         for (emp o : al){
//             System.out.println(o.age+" "+ o.salary);
//         }
//     }
// }



// class someclass<t1, t2>{
//     t1 element1;
//     t2 element2;
//     void setvalue(t1 a, t2 b){
//         element1 = a;
//         element2 = b;
//     }
//     void showvalue(){
//         System.out.println(element1+" "+ element2);
//     }
// }

// public class comparableComparator{
//     public static void main(String[] args) {
//         someclass<Double, String> sc = new someclass<>();
//         sc.setvalue(1.2, "deep");
//         sc.showvalue();
        
//         // agar koi data ni define h ....
//         ArrayList al = new ArrayList();
//         al.add(1);
//         al.add("dg");
//         al.add(3.2);
//         System.out.println(al);
        
//     }
// }



// #################################################################################################



class student implements Comparable<student>{
    int id;
    String fname, lname;

    student(int id, String fname, String lname){
        this.id = id;
        this.fname = fname;
        this.lname = lname;
    }
    @Override
    public int compareTo(student o){
        return this.id - o.id;
    }

}

class fnamecompare implements Comparator<student>{
    public int compare(student o1, student o2){
        return o2.fname.compareTo(o1.fname);
    }
}

public class comparableComparator{
    public static void main(String[] args){
        ArrayList<student> al = new ArrayList<>();
        al.add(new student(3, "deep", "sh"));
        al.add(new student(1, "ani", "aw"));
        al.add(new student(2, "sha", "ra"));

        fnamecompare fc = new fnamecompare();
        Collections.sort(al,fc);
     
        for (student i : al){
            System.out.println(i.id+ " " +i.fname+ " "+ i.lname);
        }
    }
}









// class movie{
//     String name; int rating;

//     movie(String m, int r){
//         this.name = m;
//         this.rating = r;

//     }
//     public String getname(){return name;}
//     public int getrating(){return rating;}
// }

// class namecompare implements Comparator<movie>{
//     @Override
//     public int compare(movie m1, movie m2){
//         return m2.getname().compareTo(m1.getname());
//     }
// }

// class ratingcompare implements Comparator<movie>{
//     @Override
//     public int compare(movie m1, movie m2){
//         return m1.rating - m2.rating;
//     }
// }

// public class comparableComparator{
//     public static void main(String[] args) {
//         movie m1 = new movie("deep", 1);
//         movie m2 = new movie("ank", 3);
//         movie m3 = new movie("shad", 2);

//         ArrayList<movie> al = new ArrayList<>();
//         al.add(m1);
//         al.add(m2);
//         al.add(m3);
//         namecompare nc = new namecompare();
//         Collections.sort(al,nc);
//         for (movie i : al){
//             System.out.println("name: "+ i.getname() + "\trating: "+ i.getrating());
//         }
//         System.out.println();
//         ratingcompare rc = new ratingcompare();
//         Collections.sort(al, rc);
//         for (movie i : al){
//             System.out.println("name: "+ i.getname() + "\trating: "+ i.getrating());
//         }
//     }
// }



