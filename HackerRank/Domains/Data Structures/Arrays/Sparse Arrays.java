import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        
        Map<String, Integer> wordsFrequencyHashTable = new HashMap<String, Integer>(N);
                
        for(int i=0; i<N; i++){
            String key = scanner.next().trim();
            wordsFrequencyHashTable.put(key, wordsFrequencyHashTable.getOrDefault(key, 0) + 1);
        }
        
        int Q = scanner.nextInt();
        
        for(int i=0; i<Q; i++){
            System.out.println(wordsFrequencyHashTable.getOrDefault(scanner.next().trim(), 0));
        }
    }
}
