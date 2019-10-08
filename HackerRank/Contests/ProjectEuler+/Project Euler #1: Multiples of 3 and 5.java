import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
	public static Long sumToN(Long N){
		return N * (N+1) / 2;
	}
	
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            Long n = in.nextLong();
            
            n -= 1;
            System.out.println(3*sumToN(n/3) + 5*sumToN(n/5) - 15*sumToN(n/15));
        }
    }
}

