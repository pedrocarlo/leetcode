//! 26. Remove Duplicates from Sorted Array

struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut k = 0;
        let mut first = 0;
        let mut second = 0;

        while second < nums.len() {
            while second < nums.len() && nums[second] == nums[first] {
                second += 1;
            }
            if second > first {
                if first < nums.len() - 1 {
                    first += 1;
                }
                if second == nums.len() {
                    nums[first] = nums[second - 1];
                } else {
                    nums[first] = nums[second];
                }
                k += 1;
            }
        }

        nums.drain(first + 1..);
        k
    }
}

#[cfg(test)]
mod tests {}
