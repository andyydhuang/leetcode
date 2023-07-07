class Solution {
    public String mergeAlternately(String word1, String word2) {
        int N1 = word1.length();
        int N2 = word2.length();
        char[] charArray = new char[N1+N2];
        
        int i1 = 0, i2 = 0, k = 0;
        while (i1 < N1 || i2 < N2) {
            if (i1 < N1)
                charArray[k++] = word1.charAt(i1++);
            if (i2 < N2)
                charArray[k++] = word2.charAt(i2++);
        }
        return new String(charArray);
    }
}