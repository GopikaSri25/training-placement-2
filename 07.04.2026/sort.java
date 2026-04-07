import java.util.*;

class Student {
    int id;
    String fname;
    double cgpa;

    Student(int id, String fname, double cgpa) {
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());

        List<Student> students = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            students.add(new Student(id, fname, cgpa));
        }

        Collections.sort(students, new Comparator<Student>() {
            public int compare(Student s1, Student s2) {
                if (s1.cgpa != s2.cgpa) {
                    return Double.compare(s2.cgpa, s1.cgpa); // descending CGPA
                } else if (!s1.fname.equals(s2.fname)) {
                    return s1.fname.compareTo(s2.fname); // ascending name
                } else {
                    return s1.id - s2.id; // ascending ID
                }
            }
        });

        for (Student s : students) {
            System.out.println(s.fname);
        }
    }
}
