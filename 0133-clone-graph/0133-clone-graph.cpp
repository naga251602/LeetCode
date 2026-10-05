/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<int, Node *> ht;

    void dfs(Node *node, vector<Node *> &neighbors, unordered_set<int> &visited) {
        for (Node *v: node->neighbors) {
            if (visited.count(v->val) == 0) {
                Node *n = new Node(v->val);
                neighbors.push_back(n);
                ht.insert({n->val, n});
                
                visited.insert(v->val);
                dfs(v, n->neighbors, visited);
            } else {
                neighbors.push_back(ht.at(v->val));
            }
        }

        return;
    }
    Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;

        Node *copy = new Node(node->val);
        unordered_set<int> visited;
        visited.insert(node->val);
        ht.insert({node->val, copy});

        dfs(node, copy->neighbors, visited);
        
        visited.clear();
        visited.insert(node->val);

        return copy;
    }
};