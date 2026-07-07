class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // 把 wordList 转换为 unordered_set，方便快速查找
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0; // 如果 endWord 不在 wordList 中，直接返回 0
        }

        // 构建邻接表
        unordered_map<string, vector<string>> adjList;
        for (const string& word : wordSet) {
            for (int i = 0; i < word.size(); ++i) {
                string pattern = word;
                pattern[i] = '*'; // 用 '*' 替换一个字符
                adjList[pattern].push_back(word);
            }
        }

        // BFS 初始化
        queue<pair<string, int>> q; // 队列保存单词和当前路径长度
        q.push({beginWord, 1});
        unordered_set<string> visited; // 记录已访问过的单词
        visited.insert(beginWord);

        while (!q.empty()) {
            auto [currentWord, length] = q.front();
            q.pop();

            // 遍历当前单词的所有邻接单词
            for (int i = 0; i < currentWord.size(); ++i) {
                string pattern = currentWord;
                pattern[i] = '*';

                for (const string& neighbor : adjList[pattern]) {
                    if (neighbor == endWord) {
                        return length + 1; // 找到目标单词，返回路径长度
                    }
                    if (visited.find(neighbor) == visited.end()) {
                        visited.insert(neighbor);
                        q.push({neighbor, length + 1});
                    }
                }
            }
        }

        return 0; // 如果未找到路径，返回 0
    }
};