import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	static boolean isPalindrome(Integer number){
		StringBuilder originalNumberString = new StringBuilder(String.valueOf(number));
		StringBuilder reversedNumberString = new StringBuilder(String.valueOf(number));
		reversedNumberString.reverse();
		
		return originalNumberString.toString().equals(reversedNumberString.toString());
	}

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            
            int a = 999;
            int b = a;
            
            int answer = 9999;
            
            while(a>99){
            	while(b>99){
                	int p = a*b;
                	if(p<n && isPalindrome(p)){
                		if(p>answer){
                			answer = p;
                		}
                		break;
                	}
                	b -= 1;
                }
            	a -= 1;
            	b = a;
            }
            
            System.out.println(answer);
        }
        
        in.close();
    }
}
