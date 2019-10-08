import java.io.*;
import java.util.*;
import java.util.Map.Entry;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Node{
	private Map<Character, Node> childrenHashTable;
	private Integer count;	// just to maintain count, no other use
	
	Node(){
		this.childrenHashTable = new HashMap<Character, Node>();
	}
	
	Node(Integer count){
		this.count = count;
	}

	public Map<Character, Node> getChildrenHashTable() {
		return childrenHashTable;
	}
	
	public Integer getCount() {
		return count;
	}

	public Node increaseCount(){
		this.count += 1;
		return this;
	}
}

class Trie{
	Node rootNode;
	
	Trie(){
		// lets set the root as empty node
		// i.e. no keys present in its childrenHashTable
		this.rootNode = new Node();
	}
	
	public void addName(String name){
		// set the pointer at the root node's children table;
		Map<Character, Node> currentChildrenHashTable = this.rootNode.getChildrenHashTable();
		
		// traverse the input name string
		for (int i = 0; i < name.length(); i++) {
			Character letter = name.charAt(i);
			
			// if the current letter is not in the current children hash table, lets put it 
			// with its value as new empty node
			if(currentChildrenHashTable.get(letter) == null){
				Node newNode = new Node();
				currentChildrenHashTable.put(letter, newNode);
			}
			
			// whenever a letter is encountered at a position in trie
			// whether its for the first time put
			// or just a traversal as it was already present
			// increase the count for that letter in the trie at that position
			currentChildrenHashTable.get(letter).getChildrenHashTable().put(null,currentChildrenHashTable.get(letter).getChildrenHashTable().getOrDefault(null, new Node(0)).increaseCount());
			
			//update the pointer currentChildrenHashTable with the childrenNode's childrenHashTable present
			currentChildrenHashTable = currentChildrenHashTable.get(letter).getChildrenHashTable();
		}
	}
	
	public Integer countNames(String partialName){
		// set the pointer at the root node's children table;
		Map<Character, Node> currentChildrenHashTable = this.rootNode.getChildrenHashTable();
		
		// traverse the partial name string
		Integer partialNameLength = partialName.length();
		for (int i=0; i<partialNameLength; i++){
			Character letter = partialName.charAt(i);
			
			// if partialName string itself doesn't match, no need to go further
			if(! currentChildrenHashTable.containsKey(letter)){
				// no name matches, so return 0
				return 0;
			}else{
				// update the pointer
				currentChildrenHashTable = currentChildrenHashTable.get(letter).getChildrenHashTable();
			}
		}
		
		// if control reached here, it means we traversed the whole input partialName string
		// and we have the childrenHashTable, of the last letter in the input partial name, as the current pointer
		// where we have already stored the count (disguised in the form of a Node object) at 'null' key
		// so just return it
		return currentChildrenHashTable.get(null).getCount();
	}
}

public class Solution {

    public static void main(String[] args) {
    	
    	// create trie
    	Trie trie = new Trie();
    	
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        for(int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
            
            if(op.equals("add")){
            	 trie.addName(contact);
            }else if(op.equals("find")){
            	System.out.println(trie.countNames(contact));
            }
        }
        
        in.close();
        
    }
}
