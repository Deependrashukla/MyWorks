import java.util.*;

class Employee{
    String name;
    int age;

    Employee(String name, int age){
        this.name = name;
        this.age = age ;
        // both will work..........
        // this.show();
        show();
    }

    void show(){
        System.out.println("Name: " + name + "\tAge: "+ age);
    }
}



public class testing{
    public static void main(String[] args) {

        // Employee o = new Employee("deep", 19);
        new Employee("deep", 19);


        ArrayList<Employee> lst = new ArrayList<>();
        lst.add(new Employee("deep", 19));
        lst.add(new Employee("akan", 18));

        for (Employee i : lst){
            System.out.println("name : "+i.name+"\t age: "+i.age);
        }
    }
}