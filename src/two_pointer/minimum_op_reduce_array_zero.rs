//! 1658. Minimum Operations to Reduce X to Zero

struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let subarray_sum = nums.iter().sum::<i32>() - x;
        let mut curr_sum = 0;
        let mut max_length = -1;

        while right < nums.len() {
            curr_sum += nums[right];
            // Now advance left pointer and see where we get the currSum to be equal
            // to subarray sum. Then, as we want the maximum subarray record the size of this subarray
            while left <= right && curr_sum > subarray_sum {
                curr_sum -= nums[left];
                left += 1;
            }
            if curr_sum == subarray_sum {
                max_length = std::cmp::max(max_length, right as i32 - left as i32 + 1);
            }
            right += 1;
        }

        if max_length == -1 {
            -1
        } else {
            nums.len() as i32 - max_length
        }
    }
}

#[cfg(test)]
mod tests {
    use std::vec;

    use super::*;

    #[test]
    fn test1() {
        let x = Solution::min_operations(vec![1, 1, 4, 2, 3], 5);
        assert_eq!(2, x);
    }

    #[test]
    fn test2() {
        let x = Solution::min_operations(vec![5, 6, 7, 8, 9], 4);
        assert_eq!(-1, x);
    }
}
