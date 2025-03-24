//! 1673. Find the Most Competitive Subsequence
//!

#[allow(dead_code)]
struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn most_competitive(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut stack = Vec::new();

        for (i, x) in nums.iter().enumerate() {
            while !stack.is_empty()
                && nums[*stack.last().unwrap()] > *x
                && stack.len() + nums.len() - i > k as usize
            {
                stack.pop();
            }

            if stack.len() < k as usize {
                stack.push(i);
            }
        }

        Vec::from_iter(stack.into_iter().map(|i| nums[i]))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::most_competitive(vec![3, 5, 2, 6], 2);
        assert_eq!(x, vec![2, 6])
    }

    #[test]
    fn test2() {
        let x = Solution::most_competitive(vec![2, 4, 3, 3, 5, 4, 9, 6], 4);
        assert_eq!(x, vec![2, 3, 3, 4])
    }
}
