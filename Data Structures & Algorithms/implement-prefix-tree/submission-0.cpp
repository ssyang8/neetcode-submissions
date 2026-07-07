class TrieNode{
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord = false;
};
class PrefixTree {
private:
public:
    TrieNode* root;
    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur = root;
        for(char c : word){
            if(cur->children.find(c) == cur->children.end()){
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
        }
        cur->endOfWord = true; // 标记单词结束
    }
    
    bool search(string word) {
        TrieNode* cur = root;
        for(char c : word){
            if(cur->children.find(c) == cur->children.end()){
                return false;
            }
            cur = cur->children[c];
        }
        return cur->endOfWord;
        
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;
        for(char c : prefix){
            if(cur->children.find(c) == cur->children.end()){
                return false;
            }
            cur = cur->children[c];

        }
        return true;
        
    }
};
