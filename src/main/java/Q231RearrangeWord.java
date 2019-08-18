/*
Challenge #231:
This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
 */

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.*;
import java.util.stream.Collectors;

public class Q231RearrangeWord {

    private String rearrange(String word) {
        List<Character> chars = word.chars().mapToObj(c -> (char) c ).collect(Collectors.toList());
        Map<Character, Long> charCounter = new TreeMap<>();
        for (char a : chars) {
            charCounter.put(a, chars.stream().filter(character -> character == a).count());
        }

        char nextChar = getNextChar(charCounter, '\0');
        StringBuilder out = new StringBuilder(Character.toString(nextChar));
        for (int i = 1; i < chars.size(); ++i){
            char prev = nextChar;
            nextChar = getNextChar(charCounter, prev);
            if (prev == nextChar)
                return "None";

            out.append(nextChar);
        }
        return out.toString();
    }

    private char getNextChar(Map<Character, Long> characterMap, char prev){
        long maxEntry = 0;
        char nextChar = '\0';
        for (Map.Entry<Character, Long> entry : characterMap.entrySet()){
            if (entry.getValue() > maxEntry && entry.getKey() != prev){
                maxEntry = entry.getValue();
                nextChar = entry.getKey();
            }
        }
        if (nextChar == '\0')
            nextChar = prev;
        characterMap.put(nextChar, maxEntry-1);
        if (characterMap.get(nextChar) == 0)
            characterMap.remove(nextChar);

        return nextChar;
    }

    @Test
    public void testWordRearrange(){
        Assert.assertEquals(rearrange("aabbv"), "ababv");
        Assert.assertEquals(rearrange("aabbb"), "babab");
        Assert.assertEquals(rearrange("aaaabb"), "None");
        Assert.assertEquals(rearrange("aaabbbccc"), "abcabcabc");
    }
}