class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int l = 0, r = intervals.size() - 1;

        // 二分查找插入位置
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (intervals[mid][0] <= newInterval[0]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        // 插入新区间
        intervals.insert(intervals.begin() + l, newInterval);

        // 合并区间
        vector<vector<int>> res;
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] <= res.back()[1]) {  // 当前区间和上一个区间重叠
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            } else {  // 当前区间不重叠，直接加入结果
                res.push_back(intervals[i]);
            }
        }
        return res;
    }
};