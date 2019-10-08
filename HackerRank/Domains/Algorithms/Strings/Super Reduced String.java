import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        String string = scanner.next();
        scanner.close();
        
        StringBuilder reducedString = new StringBuilder(string);
        
        int i = 0;
        while(i<reducedString.length()-1){
        	if(reducedString.charAt(i) == reducedString.charAt(i+1)){
        		reducedString.delete(i, i+2);
        		if(i > 0){
        			i -= 1;
        		}
        	}else{
        		i += 1;
        	}
        }
        
        if(reducedString.length()==0){
        	System.out.println("Empty String");
        }else{
        	System.out.println(reducedString);
        }
        
    }
}
