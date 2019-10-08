import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextLong();
            
            Long a = 1L;
            Long b = 2L;
            Long c = 0L;
            Long sum = 0L;
            
            while(b <= n){
            	c = a + b;
            	if(b % 2 == 0){
            		sum += b;
            	}
            	a = b;
            	b = c;
            }
            
            System.out.println(sum);
            
        }
    }
}
