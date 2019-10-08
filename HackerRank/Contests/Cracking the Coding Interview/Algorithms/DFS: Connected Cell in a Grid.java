import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

	static Map<String, Boolean> vistedNodesPosition = new HashMap<String, Boolean>();
	static Integer maxRegionSize = -1;

	private static boolean isVisited(int i, int j){
		String key = String.valueOf(i) + String.valueOf(j);
		if (vistedNodesPosition.containsKey(key)){
			return true;
		}else{
			return false;
		}
	}

	private static List<Integer[]> getAdjacentNodeIndices(int i, int j, int n, int m){
		List<Integer[]> adjacentIndices = new ArrayList<Integer[]>();

		if(i > 0){
			if(j > 0){
				adjacentIndices.add(new Integer[] {i-1, j-1});
			}
			
			adjacentIndices.add(new Integer[] {i-1, j});
			
			if(j < m-1){
				adjacentIndices.add(new Integer[] {i-1, j+1});
			}
		}

		if(j > 0){
			adjacentIndices.add(new Integer[] {i, j-1});
		}
		
		if(j < m-1){
			adjacentIndices.add(new Integer[] {i, j+1});
		}

		if(i < n-1){
			if(j > 0){
				adjacentIndices.add(new Integer[] {i+1, j-1});
			}
			
			adjacentIndices.add(new Integer[] {i+1, j});
			
			if(j < m-1){
				adjacentIndices.add(new Integer[] {i+1, j+1});
			}
		}

		return adjacentIndices;
	}

	private static Integer getRegionSize(int i, int j, int n, int m, int[][] matrix){
		// mark the node's position as visited
		vistedNodesPosition.put(String.valueOf(i) + String.valueOf(j), true);

		// initialize the region size
		Integer regionSize = 1;

		// loop through adjacent connected nodes
		List<Integer[]> adjacentIndices = getAdjacentNodeIndices(i, j, n ,m);
		
		for (Integer[] index : adjacentIndices) {
			Integer x = index[0];
			Integer y = index[1];
			
			// if a node is filled and its still unvisited
			if (matrix[x][y] == 1 && !isVisited(x, y)){
				// mark it as visited
				vistedNodesPosition.put(String.valueOf(x) + String.valueOf(y), true);
				
				// and add up the region size
				regionSize += getRegionSize(x, y, n, m, matrix);
			}
		}

		// finally return the calculated region
		return regionSize;
	}

	public static int getBiggestRegion(int[][] matrix) {
		Integer numberOfRows = matrix.length;
		Integer numberOfCols = matrix[0].length;

		for(int grid_i=0; grid_i < numberOfRows; grid_i++){
			for(int grid_j=0; grid_j < numberOfCols; grid_j++){	// traverse each node in the matrix
				// set current region size to 0
				Integer currentRegionSize = 0;

				// if value of the current node is 0, do nothing
				// if value of the current node is 1, check whether its already visited,
				// if yes, do nothing
				if (matrix[grid_i][grid_j] == 1 && !isVisited(grid_i, grid_j)){
					// else get the region size of the region formed by the current node
					// and set the current region size to it
					currentRegionSize = getRegionSize(grid_i, grid_j, numberOfRows, numberOfCols, matrix);
				}

				// update the biggest region size
				if (currentRegionSize > maxRegionSize){
					maxRegionSize = currentRegionSize;
				}

			}
		}

		return maxRegionSize;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		int grid[][] = new int[n][m];
		for(int grid_i=0; grid_i < n; grid_i++){
			for(int grid_j=0; grid_j < m; grid_j++){
				grid[grid_i][grid_j] = in.nextInt();
			}
		}
		in.close();
		System.out.println(getBiggestRegion(grid));
	}
}
