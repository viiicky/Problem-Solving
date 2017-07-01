import java.util.Arrays;

/**
 * Segregate 0s and 1s in an array
 * You are given an array of 0s and 1s in random order.
 * Segregate 0s on left side and 1s on right side of the array. Traverse array only once.
 *
 * If Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
 * then Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
 *
 * Problem link: http://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
 */
public class Segregator {
    public void segregate(int[] array) {
        int start = 0;
        int end = array.length - 1;

        while (start < end) {
            if (array[start] == 0) {
                start += 1;
            }

            if (array[end] == 1) {
                end -= 1;
            }

            if (array[start] != 0 && array[end] != 1) {
                this.swap(array, start, end);
                start += 1;
                end -= 1;
            }
        }
    }

    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] args) {
        int[] array = {0, 1, 0, 1, 0, 0, 1, 1, 1, 0};
        Segregator segregator = new Segregator();
        System.out.println(Arrays.toString(array));
        segregator.segregate(array);
        System.out.println(Arrays.toString(array));
    }
}