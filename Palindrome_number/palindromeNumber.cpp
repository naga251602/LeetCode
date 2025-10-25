class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;

        int temp = x, rev = 0;

        while ( x != 0) {
            if (rev < INT_MAX / 10) rev = rev * 10 + (x%10);
            x /= 10;
        }

        return rev == temp;
    }
};