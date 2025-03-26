//! 11. Container With Most Water

struct Solution;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut max = 0;
        let mut right = height.len() - 1;
        let mut left = 0;
        while left != right {
            let min = std::cmp::min(height[left], height[right]);
            max = std::cmp::max(max, min * (right - left) as i32);
            if height[left] > height[right] {
                right -= 1;
            } else {
                left += 1;
            }
        }

        max
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]);
        assert_eq!(x, 49)
    }
}
