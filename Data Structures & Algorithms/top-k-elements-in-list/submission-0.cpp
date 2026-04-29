class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count_map;
        vector<vector<int>> freq_arr(nums.size()+1);
        for(int n:nums ) {
            count_map[n]++;
        }      
        for(const auto& count_entry : count_map) {
            freq_arr[count_entry.second].push_back(count_entry.first);
        }
        vector<int> res;
        for ( int i = freq_arr.size()-1; i > 0; --i ) {
            for ( const auto& n : freq_arr[i] ) {
                res.push_back(n);
                if (res.size()==k) return res;
            }
        }
        return res;
    }
};