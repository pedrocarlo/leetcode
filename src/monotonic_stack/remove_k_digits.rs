struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn remove_kdigits(num: String, mut k: i32) -> String {
        let mut stack = Vec::new();

        for digit in num.chars() {
            while !stack.is_empty() && *stack.last().unwrap() > digit && k > 0 {
                stack.pop();
                k -= 1;
            }
            stack.push(digit);
        }

        if k > 0 {
            stack = stack[..stack.len() - k as usize].into()
        }

        let res = String::from_iter(stack.into_iter())
            .trim_start_matches('0')
            .to_string();

        if res.is_empty() { "0".into() } else { res }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::remove_kdigits("1432219".into(), 3);
        assert_eq!(x, "1219")
    }

    #[test]
    fn test2() {
        let x = Solution::remove_kdigits("10200".into(), 1);
        assert_eq!(x, "200")
    }

    #[test]
    fn test3() {
        let x = Solution::remove_kdigits("10".into(), 2);
        assert_eq!(x, "0")
    }

    #[test]
    fn test4() {
        let x = Solution::remove_kdigits("9".into(), 1);
        assert_eq!(x, "0")
    }
}
