package com.company;

/**
 * Maximum consecutive repeating character in string:
 *
 * Given a string, the task is to find maximum consecutive repeating character in string.
 * Examples:
 *
 * Input : str = "geeekk"
 * Output : e
 *
 * Input : str = "aaaabbcbbb"
 * Output : a
 *
 * Problem Link: http://www.geeksforgeeks.org/maximum-consecutive-repeating-character-string/
 */
public class MaxConsecutiveCharacter {
    
    public static void main (String[] args) {
        //code
        MaxConsecutiveCharacter.findMaxConsecutiveCharTest();
    }

    /**
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * This approach is same as the below approach except that it doesn't use any sentinel to take the last character of string into account.
     * To handle the last character it repeats the same check which is present inside the loop, once it comes outside of the loop.
     */
    private static char findMaxConsecutiveChar(String string){
        char maxChar = 0;
        int maxCharCount = 0;

        char previousChar = string.charAt(0);
        int previousCharCount = 1;

        char currentChar;
        for (int i=1; i<string.length() && previousCharCount + (string.length() - i+1) > maxCharCount; i++){  // if the remaining string length added with the current streak value cannot beat maxCharCount, no sense to traverse anymore
            currentChar = string.charAt(i);

            if (currentChar == previousChar){   // keep counting
                previousCharCount += 1;
            } else {    // streak ended
                if (previousCharCount > maxCharCount){  // this streak breaks previous record?
                    maxCharCount = previousCharCount;
                    maxChar = previousChar;
                }
                previousCharCount = 1;  // reset the count
            }

            previousChar = currentChar;
        }

        return previousCharCount > maxCharCount ? previousChar : maxChar;    // to entertain the last character in string
    }

    /**
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * This approach is same as the above approach except that it uses a sentinel to consider the last character in the string.
     * i.e. It just appends a dummy character at the end of the string such that this character should never be same as the character present at the end in the actual string.
     */
    private static char findMaxConsecutiveCharUsingSentinel(String inputString){
        String string = inputString + "`"; // Place a sentinel at the end which will never be equal to the character before it
        char maxChar = 0;
        int maxCharCount = 0;

        char previousChar = string.charAt(0);
        int previousCharCount = 1;

        char currentChar;
        for (int i=1; i<string.length() && previousCharCount + (string.length() - i+1) > maxCharCount; i++){  // if the remaining string length added with the current streak value cannot beat maxCharCount, no sense to traverse anymore
            currentChar = string.charAt(i);

            if (currentChar == previousChar){   // keep counting
                previousCharCount += 1;
            } else {    // streak ended
                if (previousCharCount > maxCharCount){  // this streak breaks previous record?
                    maxCharCount = previousCharCount;
                    maxChar = previousChar;
                }
                previousCharCount = 1;  // reset the count
            }

            previousChar = currentChar;
        }
        // no need to entertain last character as we have kept sentinel at the end
        return maxChar;
    }

    /**
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     *
     * Inspired by method two of geeksforgeeks
     */
    private static char findMaxConsecutiveCharStartingLoopFrom0Index(String string){
        char maxChar = 0;
        int maxCharCount = 0;

        int currentCharCount = 1;

        for (int i=0; i<string.length() && currentCharCount + (string.length() - (i+1)) > maxCharCount; i++){
            if (i<string.length()-1 && string.charAt(i) == string.charAt(i+1)){   // keep counting  // the if condition here is smart bit(inspired from geeksforgeeks)
                currentCharCount += 1;
            } else {    // streak ended
                if (currentCharCount > maxCharCount){  // this streak breaks previous record?
                    maxCharCount = currentCharCount;
                    maxChar = string.charAt(i);
                }
                currentCharCount = 1;  // reset the count
            }
        }

        return maxChar;
    }

    private static void findMaxConsecutiveCharTest(){
        System.out.println("Testing findMaxConsecutiveChar()");
        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("geeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("aaaabbcbbb") == 'a' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("geeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("geeekkaa") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("geeekkk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("geeekkkk") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("g") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("gg") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggg") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeee") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekka") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekkaee") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekkaeekkkk") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekkaeekkkkc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekkaeekkkkcc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekkaeekkkkccc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveChar("ggeeekkaeekkkkcccc") == 'k' ? "PASS" : "FAIL");

        System.out.println("Testing findMaxConsecutiveCharUsingSentinel()");
        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("geeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("aaaabbcbbb") == 'a' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("geeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("geeekkaa") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("geeekkk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("geeekkkk") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("g") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("gg") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggg") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeee") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekka") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaee") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkk") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkkc") == 'k' || MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkkc") == 'e'? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkkcc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkkccc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkkcccc") == 'k' ? "PASS" : "FAIL");

        System.out.println("Testing findMaxConsecutiveCharStartingLoopFrom0Index()");
        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("geeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("aaaabbcbbb") == 'a' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("geeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("geeekkaa") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("geeekkk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("geeekkkk") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("g") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("gg") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggg") == 'g' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeee") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekk") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekka") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekkaee") == 'e' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekkaeekkkk") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekkaeekkkkc") == 'k' || MaxConsecutiveCharacter.findMaxConsecutiveCharUsingSentinel("ggeeekkaeekkkkc") == 'e'? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekkaeekkkkcc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekkaeekkkkccc") == 'k' ? "PASS" : "FAIL");

        System.out.println(MaxConsecutiveCharacter.findMaxConsecutiveCharStartingLoopFrom0Index("ggeeekkaeekkkkcccc") == 'k' ? "PASS" : "FAIL");
    }
}
