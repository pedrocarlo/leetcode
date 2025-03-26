//! 15. 3sum

use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut set: HashSet<(i32, i32, i32)> = HashSet::new();

        for first in 0..nums.len() {
            let mut map = HashMap::new();
            let first_num = nums[first];

            for second in first + 1..nums.len() {
                let complement = 0 - (first_num + nums[second]);
                if map.contains_key(&complement) {
                    set.insert((first_num, nums[second], nums[map[&complement]] as i32));
                }
                map.insert(nums[second], second);
            }
        }

        Vec::from_iter(set.into_iter().map(|(x, y, z)| vec![x, y, z]))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::three_sum(vec![-1, 0, 1, 2, -1, -4]);
        assert_eq!(x, vec![[-1, -1, 2], [-1, 0, 1]])
    }
}
