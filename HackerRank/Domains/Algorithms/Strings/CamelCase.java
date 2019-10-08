import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        in.close();
        
        Integer count = 1;
        for(int i=1; i<s.length(); i++){
            Integer asciiValue = (int) s.charAt(i);
            if(asciiValue >= 65 && asciiValue <= 90){
                count += 1;
            }
        }
        
        System.out.println(count);
        
    }
}
