package test;

import java.util.*;

/**
 * This is an extension of {@link Question2}.
 * <p>
 * We solved the problem where dependencies can be present on either side of the given index using recursion.
 * But if we see the console we can find that a lot of repeated calculation is taking place here.
 * <p>
 * We can optimize this by maintaining a record where we will save the intermediate calculation results,
 * so that if similar sub problem ever occurs, we just get the value from the record,
 * instead of solving the same problem again (Memoization/Caching/Whatever)
 * <p>
 * The console output for this implementation will not have same calculations repeated.
 */
public class Question3 {

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
        dependencies.forEach(dep -> {
            if (formulaeArray[dep] != null) {
                values.add(formulaeArray[dep]);   // if you can remember the past, use it
            } else {
                values.add(solve(dep));    // there is no guarantee at this point that all the dependencies of i is already solved, so lets dive inside using recursion
            }
        });

        int solution = execute(i, values);
        formulaeArray[i] = solution;
        return solution;
    }

    public static void main(String[] args) {
        initializeConstants();
        initializeDependencyTable();

        System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        for (int i = 2; i < SIZE; i++) {
            if (formulaeArray[i] == null) {
                formulaeArray[i] = solve(i);
            }
            System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        }
    }
}
