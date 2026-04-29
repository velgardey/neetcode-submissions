class Solution {
public:
    //Quick check to eliminate obvious non anagrams
    bool isAnagram(string s, string t) {
        if ( s.length() != t.length() ) {
            return false;
        }
        //Create a hashmap to keep track of the frequencies
        unordered_map<char, int> charFreq;

        //Populate the frequencies of each character of string s
        for ( char c : s ) {
            charFreq[c]++;
        }
        
        //Checks if each char of t is present in s, and decrement the freq of the common characters
        for ( char c : t ) {
            if ( charFreq.find(c) == charFreq.end() || --charFreq[c] < 0 ) {
                return false;
            }
        }
        return true;
    }
};