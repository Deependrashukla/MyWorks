
// import java.util.*;
// class student {
//     int id;
//     String name;

//     student(int id, String name) {
//         this.id = id;
//         this.name = name;
//     }
// }

// // class idcomparator implements Comparator<student> {
// //     @Override
// //     public int compare(student s1, student s2) {
// //         return Integer.compare(s1.id, s2.id);
// //     }
// // }

// class idcomparator implements Comparator<student> {
//     @Override
//     public int compare(student s1, student s2) {
//         return s1.id - s2.id;
//     }
// }

// class namecomparator implements Comparator<student> {
//     @Override
//     public int compare(student s1, student s2) {
//         return s1.name.compareTo(s2.name);
//     }
// }

// public class sixth {
//     public static void main(String[] args) {
//         ArrayList<student> list = new ArrayList<>();
//         list.add(new student(1, "bohn"));
//         list.add(new student(6, "cohn"));
//         list.add(new student(3, "dhn"));
//         list.add(new student(2, "aohn"));
//         idcomparator idc = new idcomparator();
//         Collections.sort(list, idc);
//         for (student i : list) {
//             System.out.println("id-" + i.id + " name-" + i.name);
//         }

//         namecomparator n = new namecomparator();
//         Collections.sort(list, n);
//         for (student i : list) {
//             System.out.println("id-" + i.id + " name-" + i.name);
//         }
//     }
// }


import java.util.*;

class Movie {
    String name;
    double rating;

    Movie(String name, double rating) {
        this.name = name;
        this.rating = rating;
    }
}

class NameComparator implements Comparator<Movie> {
    @Override
    public int compare(Movie m1, Movie m2) {
        return m1.name.compareTo(m2.name);
    }
}

class RatingComparator implements Comparator<Movie> {
    @Override
    public int compare(Movie m1, Movie m2) {
        return Double.compare(m1.rating, m2.rating);
    }
}

public class sixth {
    public static void main(String[] args) {
        ArrayList<Movie> movies = new ArrayList<>();
        movies.add(new Movie("Inception", 6.8));
        movies.add(new Movie("The Shawshank Redemption", 9.3));
        movies.add(new Movie("Pulp Fiction", 8.9));
        movies.add(new Movie("The Godfather", 9.2));

        // Sort movies by name
        NameComparator nameComparator = new NameComparator();
        Collections.sort(movies, nameComparator);
        System.out.println("Sorted by movie name:");
        for (Movie movie : movies) {
            System.out.println(movie.name + " - Rating: " + movie.rating);
        }

        // Sort movies by rating
        RatingComparator ratingComparator = new RatingComparator();
        Collections.sort(movies, ratingComparator);
        System.out.println("\nSorted by movie rating:");
        for (Movie movie : movies) {
            System.out.println(movie.name + " - Rating: " + movie.rating);
        }
    }
}

