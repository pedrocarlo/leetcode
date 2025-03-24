use std::collections::{HashMap, HashSet};

struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn smallest_subsequence(s: String) -> String {
        let mut stack: Vec<char> = vec![];
        let mut map = HashMap::new();
        let mut set = HashSet::new();

        for (i, c) in s.chars().enumerate() {
            map.insert(c, i);
        }

        for (i, c) in s.chars().enumerate() {
            if set.contains(&c) {
                continue;
            }
            while !stack.is_empty()
                && *stack.last().unwrap() > c
                && i < *map.get(stack.last().unwrap()).unwrap()
            {
                let last_char = stack.pop().unwrap();
                set.remove(&last_char);
            }
            stack.push(c);
            set.insert(c);
        }

        let mut res = String::new();
        for ch in stack {
            res.push(ch);
        }
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::smallest_subsequence("bcabc".to_string());
        assert_eq!(x, "abc".to_string())
    }

    #[test]
    fn test2() {
        let x = Solution::smallest_subsequence("cbacdcbc".to_string());
        assert_eq!(x, "acdb".to_string())
    }

    #[test]
    fn test3() {
        let x = Solution::smallest_subsequence("cdadabcc".to_string());
        assert_eq!(x, "adbc".to_string())
    }

    #[test]
    fn test4() {
        let x = Solution::smallest_subsequence("baababaaaaababbbbbbaababaababa".to_string());
        assert_eq!(x, "ab".to_string())
    }

    #[test]
    fn test5() {
        let x = Solution::smallest_subsequence("cbaacabcaaccaacababa".to_string());
        assert_eq!(x, "abc".to_string())
    }
}
