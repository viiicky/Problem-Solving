import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Map.Entry;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        String magazine[] = new String[m];
        for(int magazine_i=0; magazine_i < m; magazine_i++){
            magazine[magazine_i] = in.next();
        }
        String ransom[] = new String[n];
        for(int ransom_i=0; ransom_i < n; ransom_i++){
            ransom[ransom_i] = in.next();
        }
        
        Map<String, Integer> magazineHash = new HashMap<String, Integer>();
        for(String word : magazine){
            magazineHash.put(word, magazineHash.getOrDefault(word, 0) + 1);
        }
        
        Map<String, Integer> ransomHash = new HashMap<String, Integer>();
        for(String word : ransom){
            ransomHash.put(word, ransomHash.getOrDefault(word, 0) + 1);
        }
        
        for(Entry<String, Integer> entry : ransomHash.entrySet()){
            if(magazineHash.get(entry.getKey()) == null){
                System.out.println("No");
                System.exit(1);
            }
            
            if(magazineHash.get(entry.getKey()) < entry.getValue()){
                System.out.println("No");
                System.exit(1);
            }
            
        }
        System.out.println("Yes");
    }
}

