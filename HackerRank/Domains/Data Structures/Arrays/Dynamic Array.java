import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enteryour code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	
    	Scanner scanner = new Scanner(System.in);
    	
    	int N = scanner.nextInt();
    	int Q = scanner.nextInt();
    	
    	List<List<Long>> seqList = new ArrayList<List<Long>>(N);
    	
    	for(int i=0; i<N; i++){
    		List<Long> seq = new ArrayList<Long>();
    		seqList.add(seq);
    	}
    	
    	long lastAns = 0L;
    	
    	for(int i=0; i<Q; i++){
    		short queryType = scanner.nextShort();
    		
    		long x = scanner.nextLong();
    		long y = scanner.nextLong();
    		
    		if(queryType == 1){
    			seqList.get((int)((x ^ lastAns)%N)).add(y);
    			
    		}else if(queryType == 2){
    			List<Long> seq = seqList.get((int)(x ^ lastAns)%N);
    			lastAns = seq.get((int) (y%seq.size()));
    			System.out.println(lastAns);
    		}
    	}
    	
    }
}
