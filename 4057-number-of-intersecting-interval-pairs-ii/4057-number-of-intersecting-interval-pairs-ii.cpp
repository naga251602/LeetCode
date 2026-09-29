class Solution {
public:
    long long countIntersectingIntervals(vector<vector<int>>& intervals) {
        priority_queue<int, vector<int>, greater<int>> pq;
        ranges::sort(intervals);

        long long count = 0;
        pq.push(intervals[0][1]);

        for (int i = 1; i < intervals.size(); i ++) {
            while (!pq.empty() && pq.top() < intervals[i][0]) {
                pq.pop();
            }

            count += pq.size();
            pq.push(intervals[i][1]);     
        }

        return count;
    }
};