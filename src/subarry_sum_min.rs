//! 907. Sum of Subarray Minimums

use std::{cmp::min, collections::HashMap};

struct Solution;

impl Solution {
    pub fn subarray_mins(mut arr: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut new_arr = vec![-1];
        new_arr.append(&mut arr);
        new_arr.push(-1);

        let mut stack: Vec<usize> = Vec::new();
        for (i, x) in new_arr.iter().enumerate() {
            while !stack.is_empty() && new_arr[*stack.first().unwrap()] > *x {
                let smaller_idx = stack.pop().unwrap();
                // let larger_idx = 
            }
        }

        0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::subarray_mins(vec![3, 1, 2, 4]);
        assert_eq!(17, x);
    }
}
