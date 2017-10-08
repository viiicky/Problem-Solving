package test;

import java.util.*;

/**
 * This is an extension of {@link Question1}, where the constraint that:
 * For any given index i where 2 <= i < SIZE,
 * the formulae will depend upon either constant values or on the values present at the index k where 0 <= k < i
 * HAS BEEN REMOVED
 * <p>
 * It means the formulae at any given index i where 2 <= i < SIZE
 * may depend upon either constant values or values present at index k where 0 <= k < SIZE
 * <p>
 * Some extra dependencies has been added here with the help of {@link #initializeDependencyTable()}
 * to have some dependencies in such a way that for a given index the formulae not only depends upon the values to the left of it,
 * but also on the values to the right of it.
 * <p>
 * Our good old implementation in {@link Question1} will throw an {@link IllegalArgumentException} here,
 * because there is no guarantee that all the dependencies of the current i are already solved.
 * <p>
 * So here we will change the implementation in {@link #main(String[])} to use recursion instead.
 */
public class Question2 {
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
        dependencyTable.get(2).add(0);
        dependencyTable.get(2).add(1);

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

    private static int solve(int i) {
        if (getDependencies(i) == null) {   // base case for constant values
            return formulaeArray[i];
        }

        // find dependencies of formulae at i
        Set<Integer> dependencies = getDependencies(i);

        // create value list by solving for above dependencies, as execute() requires actual values to work upon
        List<Integer> values = new ArrayList<>();
        dependencies.forEach(dep -> values.add(solve(dep)));    // there is no guarantee at this point that all the dependencies of i is already solved, so lets dive inside using recursion

        return execute(i, values);
    }

    public static void main(String[] args) {
        initializeConstants();
        initializeDependencyTable();

        System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        for (int i = 2; i < SIZE; i++) {
            formulaeArray[i] = solve(i);
            System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        }
    }
}
