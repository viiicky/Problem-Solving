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
            int m = in.nextInt();
            int n = in.nextInt();
            // int a[] = new int[n];
            Map<Integer, Stack<Integer>> costIndexHashTable = new HashMap<Integer, Stack<Integer>>();
            for(int a_i=0; a_i < n; a_i++){
                // a[a_i] = in.nextInt();
                Integer cost = in.nextInt();
                Stack<Integer> indexStack = costIndexHashTable.get(cost);
                if (indexStack == null){
                    indexStack = new Stack<Integer>();
                    indexStack.push(a_i);
                    costIndexHashTable.put(cost, indexStack);
                }else{
                    indexStack.push(a_i);
                }
            }
            
            Integer money = m;
            Integer m1 = 0;
            Integer m2 = 0;
            
            while(money > 0){
                money -= 1;
                Stack<Integer> indexArray1 = costIndexHashTable.get(money);
                
                if(indexArray1 != null && indexArray1.size() > 0){
                    m1 = indexArray1.pop();
                    
                    Stack<Integer> indexArray2 = costIndexHashTable.get(m - money);
                    if(indexArray2 != null && indexArray2.size() > 0){
                        m2 = indexArray2.pop();
                        break;
                    }
                }
            }
            
            if(m1 < m2){
            	System.out.print(m1+1+" ");
                System.out.println(m2+1);
            }else{
            	System.out.print(m2+1+" ");
                System.out.println(m1+1);
            }
        }
    }
}
