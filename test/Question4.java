package test;

import java.util.*;

/**
 * This is an extension of {@link Question3}
 * Here we are going to change the approach. Up until now, we have been following the procedure where
 * we were solving for each index sequentially, now we are going to create a graph based on the dependency information.
 * <p>
 * Each index will be a vertex in the graph, and each dependency will serve as the edge.
 * <p>
 * We will then start with the constants node, and will move our way forward solving each index exactly once.
 * Note: we have already assumed that there is not going to be any cyclic dependency.
 */

class Node {
    int value;  // this is the index number, can be called as id too
    Set<Node> incomingNodes = new HashSet<>();
    Set<Node> outgoingNodes = new HashSet<>();

    Node(int value) {
        this.value = value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Node node = (Node) o;

        return value == node.value;
    }

    @Override
    public int hashCode() {
        return value;
    }
}

class Graph {
    Map<Integer, Node> nodes = new HashMap<>();
}

public class Question4 {

    private static final int SIZE = 7;

    private static Integer[] formulaeArray = new Integer[SIZE];

    private static Map<Integer, Set<Integer>> dependencyTable = new HashMap<>();

    private static void initializeConstants() {
        formulaeArray[0] = 42;
        formulaeArray[1] = 42;
    }

    private static void initializeDependencyTable() {
        dependencyTable.put(0, null);   // constant

        dependencyTable.put(1, null);   // constant

        dependencyTable.put(2, new HashSet<>());
        dependencyTable.get(2).add(5);
        dependencyTable.get(2).add(6);

        dependencyTable.put(3, new HashSet<>());
        dependencyTable.get(3).add(2);
        dependencyTable.get(3).add(5);

        dependencyTable.put(4, new HashSet<>());
        dependencyTable.get(4).add(6);
        dependencyTable.get(4).add(1);

        dependencyTable.put(5, new HashSet<>());
        dependencyTable.get(5).add(4);

        dependencyTable.put(6, new HashSet<>());
        dependencyTable.get(6).add(0);
        dependencyTable.get(6).add(1);
    }

    private static Set<Integer> getDependencies(int i) {
        return dependencyTable.get(i);
    }

    /**
     * dummy method that returns 42 as all answers
     */
    private static int execute(int index, List<Integer> values) {
        if (values.contains(null)) {
            throw new IllegalArgumentException("I cannot work on formulae. Send me raw values.");   // null for us is the formulae, any value other than null is the value of that formulae
        }
        System.out.println(String.format("Solving for index[%d] using values[%s]", index, values));
        return 42;
    }

    public static void main(String[] args) {
        initializeConstants();
        initializeDependencyTable();

        Graph graph = new Graph();

        // create a set of SIZE number of nodes and put them in Graph by their id
        for (int i = 0; i < SIZE; i++) {
            graph.nodes.put(i, new Node(i));
        }

        // create links among the nodes
        for (int i = 2; i < SIZE; i++) {
            int finalI = i;
            getDependencies(i).forEach(dep -> {
                graph.nodes.get(finalI).outgoingNodes.add(graph.nodes.get(dep));
                graph.nodes.get(dep).incomingNodes.add(graph.nodes.get(finalI));
            });
        }

        // put constant terms in solved nodes set
        Set<Node> solvedNodes = new HashSet<>();
        solvedNodes.add(graph.nodes.get(0));
        solvedNodes.add(graph.nodes.get(1));

        System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        while (solvedNodes.size() != SIZE) {
            // accumulate all the incoming nodes for all the calculated nodes
            Set<Node> solvedNodesIncomingNeighbour = new HashSet<>();
            for (Node solvedNode : solvedNodes) {
                solvedNodesIncomingNeighbour.addAll(solvedNode.incomingNodes);
            }

            // solve for all the nodes present in solvedNodesIncomingNeighbour for which all the outgoing nodes are already solved
            for (Node neighbourNode : solvedNodesIncomingNeighbour) {
                if (!solvedNodes.contains(neighbourNode) && neighbourNode.outgoingNodes.stream().allMatch(solvedNodes::contains)) {  // solvable node
                    // create value list by solving for node's dependencies, as execute() requires actual values to work upon
                    List<Integer> depValues = new ArrayList<>();
                    neighbourNode.outgoingNodes.forEach(dep -> depValues.add(formulaeArray[dep.value]));

                    formulaeArray[neighbourNode.value] = execute(neighbourNode.value, depValues);
                    solvedNodes.add(neighbourNode);
                    System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
                }
            }
        }
    }
}
