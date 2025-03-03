import package1.*;
import package2.*;
import package3.*;

class PackageTesting{
    public static void main(String[] args) {
        ClassOne a = new ClassOne();
        ClassTwo b = new ClassTwo();
        ClassThree c = new ClassThree();
        a.methodClassOne();
        b.methodClassTwo();
        c.methodClassThree();
    }
}
