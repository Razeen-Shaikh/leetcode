/**
 * You are given a string s and an integer t, representing the number of
 * transformations to perform.
 * In one transformation, every character in s is replaced according to the
 * following rules:
 * 
 * If the character is 'z', replace it with the string "ab".
 * Otherwise, replace it with the next character in the alphabet.
 * For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
 * Return the length of the resulting string after exactly t transformations.
 * 
 * Since the answer may be very large, return it modulo 109 + 7.
 * 
 * Example 1:
 * Input: s = "a", t = 1
 * Output: 2
 * Explanation: The transformation is as follows:
 * "a" -> "b"
 * The length of the resulting string is 2.
 *
 */

public class TotalCharactersInStringAfterTransformationsI {
    private static final int MOD = 1_000_000_007;

    public int lengthAfterTransformations(String s, int t) {
        int[][] dp = new int[26][t + 1];

        for (int i = 0; i < 26; i++) {
            dp[i][0] = 1;
        }

        for (int step = 1; step <= t; step++) {
            for (int ch = 0; ch < 26; ch++) {
                if (ch == 25) {
                    dp[ch][step] = (dp[0][step - 1] + dp[1][step - 1]) % MOD;
                } else {
                    dp[ch][step] = dp[ch + 1][step - 1];
                }
            }
        }

        long result = 0;
        for (char c : s.toCharArray()) {
            int index = c - 'a';
            result = (result + dp[index][t]) % MOD;
        }

        return (int) result;
    }

    public static void main(String[] args) {
        TotalCharactersInStringAfterTransformationsI solver = new TotalCharactersInStringAfterTransformationsI();

        System.out.println(solver.lengthAfterTransformations("abcyy", 2));
        System.out.println(solver.lengthAfterTransformations("azbk", 1));
        System.out.println(solver.lengthAfterTransformations("v", 7));
    }
}