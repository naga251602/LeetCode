class Solution {
public:
    int reverse(int x) {

        if (x > INT_MAX || x < INT_MIN) return 0;
        int neg_flag = -1;

        if ( x < 0 ) {
            neg_flag = 1;
            if (x < INT_MAX * -1) return 0;
            x *= -1;
        } 

        int rev = 0;
        while ( x > 0 ) {

            if (rev > INT_MAX/10) return 0;
            rev = rev * 10 + (x%10);
            x /= 10;
        }

        if (neg_flag == 1) return rev * -1;
        else return rev;
    }
};