import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
     public static boolean isBalanced(String expression) {
         expression = expression.trim();
         
         LinkedList<Character> stack = new LinkedList<Character>();
         
         for(int i=0; i<expression.length(); i++){
             Character bracket = expression.charAt(i);
             
             if (bracket.equals('{') || bracket.equals('(') || bracket.equals('[')){
                 stack.push(bracket);
                 continue;
             }
               
             Character topBracket = stack.peek();
             
             // stack prematurely empty, i.e. right bracket is trying to come before left
             if (topBracket == null){
                 return false;
             }
             
             // the brakcet doesnt match each other             
             if ((bracket.equals('}') &&  !topBracket.equals('{')) || (bracket.equals(']') &&  !topBracket.equals('[')) || (bracket.equals(')') &&  !topBracket.equals('('))){
                 return false;
             }
             
             stack.pop();
             
         }
         
         // there was/were extra left brackets
         if(stack.isEmpty()){
        	return true;
        }else{
        	return false;
        }
      
     }
  
   public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
             boolean answer = isBalanced(expression);
             if(answer)
              System.out.println("YES");
             else System.out.println("NO");
        }
    }
}

