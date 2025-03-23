//! 1248. Count Number of Nice Subarrays
//!
//!
//!

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut subarrays = 0;
        let mut curr_sum = 0;

        let mut prefix_sum = HashMap::new();
        prefix_sum.insert(curr_sum, 1);

        for x in nums {
            curr_sum += x % 2;
            println!("{curr_sum}");
            if prefix_sum.contains_key(&(curr_sum - k)) {
                subarrays += prefix_sum.get(&(curr_sum - k)).unwrap();
            }
            let x = prefix_sum.get(&curr_sum).map(|x| *x).unwrap_or(0);
            prefix_sum.insert(curr_sum, x + 1);
        }

        subarrays
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::number_of_subarrays(vec![1, 1, 1, 1, 1], 1);
        assert_eq!(5, x);
    }

    #[test]
    fn test2() {
        let x = Solution::number_of_subarrays(vec![2,2,2,1,2,2,1,2,2,2], 2);
        assert_eq!(16, x);
    }
}
