class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for ( int i = 0; i < nums.size(); i++ ) {
            map[nums[i]] = i;
        }
        for ( int i = 0; i < nums.size(); i++ ) {
            int difference = target - nums[i];
            if (map.count(difference) && map[difference] != i ) {
                return {i, map[difference]};
            }
        }
        return {};
    }
};
