import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Map.Entry;
public class Solution {
    public static int numberNeeded(String first, String second) {
        
        Map<Character, Integer> string1Map = new HashMap<Character, Integer>();
		Map<Character, Integer> string2Map = new HashMap<Character, Integer>();
		
		for (int i=0; i<first.length(); i++){
			string1Map.put(first.charAt(i), string1Map.getOrDefault(first.charAt(i), 0)+1);
		}
		
		for (int i=0; i<second.length(); i++){
			string2Map.put(second.charAt(i), string2Map.getOrDefault(second.charAt(i), 0)+1);
		}
		
		Integer counter = 0;
		
		for (Entry<Character, Integer> entry : string1Map.entrySet()) {
			Integer value2 = string2Map.get(entry.getKey());
			if( value2 != null){
				counter +=  Math.abs(entry.getValue() - value2);
			}
			else{
				counter += entry.getValue();
			}
		}
		
		for (Entry<Character, Integer> entry : string2Map.entrySet()) {
			Integer value1 = string1Map.get(entry.getKey());
			if( value1 == null){
				counter += entry.getValue();
			}
		}
        
        return counter;
      
    }
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String first = in.next();
        String second = in.next();
        System.out.println(numberNeeded(first, second));
    }
}

