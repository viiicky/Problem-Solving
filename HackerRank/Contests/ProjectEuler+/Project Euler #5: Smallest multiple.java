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
            int n = in.nextInt();
            
            BigInteger lcm = BigInteger.ONE;
            for(int i=2; i<=n; i++){
            	BigInteger b = BigInteger.valueOf(i);
            	lcm = (lcm.multiply(b)).divide(lcm.gcd(b));
            }
            
            System.out.println(lcm);
        }
    }
}

