/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    void bfs(Node *root) {
        queue<Node *> q;
        q.push(root);

        while (!q.empty()) {
            Node *prev = nullptr;
            int n = q.size();

            for (int i = 0; i < n; i ++) {
                Node *r = q.front();
                q.pop();
                
                if (prev != nullptr) {
                    prev->next = r;
                }
                
                prev = r;
                

                if (r->left) q.push(r->left);
                if (r->right) q.push(r->right);
            }

        }
    }

    Node* connect(Node* root) {
        if (!root) return nullptr;
        bfs(root);

        return root;
    }
};