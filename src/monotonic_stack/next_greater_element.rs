//! 496 Next Greater Element 1
//!

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn next_greater_element(mut nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::new();
        let mut map = HashMap::new();

        for x in nums2.iter() {
            while !stack.is_empty() && *stack.last().unwrap() < *x {
                let value = stack.pop().unwrap();
                map.insert(value, *x);
            }
            stack.push(*x);
        }

        for x in nums1.iter_mut() {
            if let Some(greater) = map.get(x) {
                *x = *greater;
            } else {
                *x = -1
            }
        }

        nums1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::next_greater_element(vec![4, 1, 2], vec![1, 3, 4, 2]);
        assert_eq!(x, vec![-1, 3, -1])
    }
}
