import java.io.*;
import java.util.*;
import java.util.Map.Entry;

class Node{
	int id;
	List<Node> adjacentNodes;
	
	Node(int id){
		this.id = id;
		this.adjacentNodes = new LinkedList<Node>();
	}
}

class Graph{
	Map<Integer, Node> nodes;
	
	Graph(){
		this.nodes = new HashMap<Integer, Node>();
	}
}

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	Scanner scanner = new Scanner(System.in);
    	int q = scanner.nextInt();
    	
    	for (int i=0; i<q; i++){
    		// create an empty graph
    		Graph graph = new Graph();
    		
    		int n = scanner.nextInt();	// number of nodes
    		int m = scanner.nextInt();	// number of edges
    		
    		// create n nodes, and put them in the graph
    		for(int j=1;j<=n; j++){
    			Node node = new Node(j);
    			graph.nodes.put(j, node);
    		}
    		
    		// connect edges
    		for(int j=0; j<m; j++){
    			int u = scanner.nextInt();
    			int v = scanner.nextInt();
    			
    			// if the edges are not already connected, make connection
    			if(! graph.nodes.get(u).adjacentNodes.contains(graph.nodes.get(v))){
    				graph.nodes.get(u).adjacentNodes.add(graph.nodes.get(v));
        			graph.nodes.get(v).adjacentNodes.add(graph.nodes.get(u));
    			}
    		}
    		
    		//print graph
    		/*for (Entry<int, Node> node : graph.nodes.entrySet()) {
				System.out.println("key: " + node.getKey());
				System.out.println("id: " + node.getValue().id);
				for (Node x : node.getValue().adjacentNodes) {
					System.out.println("Adjacent Nodes: " + x.id);
				}
				System.out.println("---------------------------------------------------------");
			}*/
    		
    		int s = scanner.nextInt();	// starting node
    		Node startNode = graph.nodes.get(s);
    		
    		// start the BFS traversal for the graph from start node
    		Map<Integer, Node> visitedNodes = new HashMap<Integer, Node>();
    		
    		Queue<Node> nodesToBeVisited = new LinkedList<Node>();
    		nodesToBeVisited.add(startNode);
    		
    		Map<Integer, Integer> nodeLengthHashTable = new HashMap<Integer, Integer>();
    		nodeLengthHashTable.put(s, 0);
    		while(! nodesToBeVisited.isEmpty()){
    			// visit the node present at the head of the queue and remove it from the queue
    			Node currentNode = nodesToBeVisited.poll();
    			
    			// mark it as visited
    			visitedNodes.put(currentNode.id, currentNode);
    			
    			// add all its adjacent nodes in the queue to visit,
    			// if they are still unvisited
    			for (Node node : currentNode.adjacentNodes) {
    				if(visitedNodes.get(node.id) == null){
    					// mark the node as visited
    					nodesToBeVisited.add(node);
    				}
    				
    				// store the length
    				if(nodeLengthHashTable.get(node.id) == null){	// shortest distance should have already come, so dont override with longer distance
    					nodeLengthHashTable.put(node.id, nodeLengthHashTable.get(currentNode.id) + 6);
    				}
				}
    			
    		}
    		// BFS traversal ends here
    		
    		for(int j=1; j<=n; j++){
    			if(j != s){
    				System.out.print(nodeLengthHashTable.getOrDefault(j, -1) + " ");
    			}
    		}
    		System.out.println();
    	}
    	scanner.close();
    }
}
