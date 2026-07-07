class Solution {
public:
    unordered_map<char, string> digitToChar = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},  // 注意：这里 'qprs' 改为 'pqrs'
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};  // 处理空输入
        dfs(digits, 0);
        return result;
    }

private:
    vector<string> result;
    string path;
    
    void dfs(const string& digits, int start) {
        if (start >= digits.size()) {
            result.push_back(path);
            return;
        }
        
        char digit = digits[start];
        string str = digitToChar[digit];
        for (char c : str) {
            path.push_back(c);
            dfs(digits, start + 1);
            path.pop_back();
        }
    }
};