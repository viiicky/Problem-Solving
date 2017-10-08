package test;

import java.util.*;

/**
 * A {@code SIZE} length array {@code formulaeArray} is given with constant values on the initial two positions.
 * All other index values need to be calculated by the formulae present at that index.
 * <p>
 * For any given index i where 2 <= i < SIZE,
 * the formulae will depend upon either constant values or on the values present at the index k where 0 <= k < i
 * <p>
 * Two methods are provided, which performs the following tasks:
 * - {@link #getDependencies(int)}: returns the set of indices of dependencies of the given index
 * - {@link #execute(int, List)}: calculates the answer for index position
 * using the formulae present in the formulaeArray and the values passed to be used in the formulae
 * <p>
 * For the sake of simplicity we are not having any actual formulae here,
 * the dependencies are defined manually in the beginning of the program using the method {@link #initializeDependencyTable()}
 * And the method {@link #execute(int, List)} returns dummy fixed answer for any index which is 42.
 * And we assume that there are no cyclic dependencies
 * <p>
 * So the array will have values filled for the initial two position and all other position's value will be null.
 * As we move further each null value will be replaced by the calculated answer.
 */
public class Question1 {

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
        dependencyTable.get(2).add(0);
        dependencyTable.get(2).add(1);

        dependencyTable.put(3, new HashSet<>());
        dependencyTable.get(3).add(2);

        dependencyTable.put(4, new HashSet<>());
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

        System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        for (int i = 2; i < SIZE; i++) {
            // find dependencies of formulae at i
            Set<Integer> dependencies = getDependencies(i);

            // create value list by solving for above dependencies, as execute() requires actual values to work upon
            List<Integer> values = new ArrayList<>();
            dependencies.forEach(dep -> values.add(formulaeArray[dep]));    // at this point we know all indices to the left of i are already solved

            formulaeArray[i] = execute(i, values);
            System.out.println(String.format("Formulae array: %s", Arrays.toString(formulaeArray)));
        }
    }
}
