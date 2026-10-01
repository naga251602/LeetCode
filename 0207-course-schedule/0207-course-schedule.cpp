class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0), res;
        vector<vector<int>> adj(numCourses);

        for (auto e: prerequisites) {
            adj[e[1]].push_back(e[0]);
            indegree[e[0]] ++;
        }

        queue<int> q;

        for (int i = 0; i < numCourses; i ++) {
            if (indegree[i] == 0) q.push(i);
        }

        while (! q.empty()){
            int u = q.front();
            q.pop();

            res.push_back(u);

            for (int v: adj[u]) {
                indegree[v] --;
                if (indegree[v] == 0) q.push(v);
            }
        }

        return res.size() == numCourses;
    }
};