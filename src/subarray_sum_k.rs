use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut subarrays = 0;
        let mut curr_sum = 0;
        let mut prefix_sum = HashMap::new();
        prefix_sum.insert(curr_sum, 1);

        for x in nums {
            curr_sum += x;
            dbg!(&prefix_sum, &curr_sum);
            if let Some(&encounters) = prefix_sum.get(&(curr_sum - k)) {
                subarrays += encounters;
            }
            *prefix_sum.entry(curr_sum).or_insert(0) += 1;
        }

        subarrays
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::subarray_sum(vec![1, 1, 1], 2);
        assert_eq!(2, x);
    }

    #[test]
    fn test2() {
        let x = Solution::subarray_sum(vec![1, 2, 3], 3);
        assert_eq!(2, x);
    }
}
