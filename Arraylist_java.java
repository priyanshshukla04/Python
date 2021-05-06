import java.util.ArrayList;

public class Arraylist_java {
    public static void main(String[] args) {
        ArrayList<Integer> arr1 = new ArrayList<>();
        ArrayList<Integer> arr2 = new ArrayList<>(10);
        arr1.add(1);
        arr1.add(2);
        arr1.add(4);
        arr1.add(6);
        arr1.add(4);
        arr1.add(0,9);
        arr1.add(0,8);

        arr2.add(12);
        arr2.add(14);
        arr2.add(13);
        arr2.add(18);
//        arr1.addAll(arr2);
        arr1.addAll(3,arr2);
//        arr1.clear();
//        for (Integer integer : arr1) {
//            System.out.println(integer);
//        }
        System.out.println(arr1.contains(4));
//        ArrayList<Integer> arr3 = (ArrayList<Integer>) arr1.clone();
        ArrayList arr3 = (ArrayList) arr1.clone();

//        System.out.println(arr3);
//        System.out.println(arr1.isEmpty());
//        System.out.println(arr1.indexOf(4));
//        System.out.println(arr1.lastIndexOf(4));
        for (Integer integer : arr2) {
            System.out.println(integer);
        }
        arr2.trimToSize();
        System.out.println(arr2.size());

    }
}
