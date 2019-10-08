import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	
    	Scanner scanner = new Scanner(System.in);
    	
    	Integer N = scanner.nextInt();
    	Integer[] A = new Integer[N];
    	
    	int i = 0;
    	while(scanner.hasNext()){
    		A[i] = scanner.nextInt();
    		i += 1;
    	}
    	
    	for (i = A.length-1; i >= 0; i--) {
			System.out.print(A[i] + " ");
		}
    }
}
