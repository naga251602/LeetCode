class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n == 1) return x;

        if ( n > 0 ) {
            double temp = myPow(x, n/2);

            if (n%2 == 0) {
                return temp * temp;
            } else {
                return temp * temp * x;
            }
        } else {
            if (n == INT_MIN) {
                return 1 /  (myPow(x, (n + 1) * -1) * x);
            };
            return 1 / myPow(x, n * -1);
        }   

    }
};