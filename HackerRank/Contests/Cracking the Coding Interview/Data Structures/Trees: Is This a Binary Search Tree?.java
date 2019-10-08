/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/
    private List<Integer> nodeDataArrayList = new ArrayList<Integer>();

    void traverseInOrder(Node root){
        if(root != null){
            traverseInOrder(root.left);
            
            nodeDataArrayList.add(root.data);
            Integer length = nodeDataArrayList.size();
            if(length > 1){
                if(nodeDataArrayList.get(length-1) <= nodeDataArrayList.get(length-2)){
                    System.out.println("No");
                    System.exit(0);
                }
            }
            
            traverseInOrder(root.right);
        }
    }

    boolean checkBST(Node root) {
        traverseInOrder(root);
        System.out.println("Yes");
        System.exit(0);
        return false;
    }

