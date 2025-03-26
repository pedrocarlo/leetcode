//! 2571. Minimum Operations to Reduce an Integer to 0

struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn min_operations(mut n: i32) -> i32 {
        let mut count = 0;
        while n > 0 {
            if n & 3 == 3 {
                n += 1;
                count += 1;
            } else {
                count += n & 1;
                n >>= 1;
            }
        }
        count
    }
}
