struct Solution;

impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let mut stack = Vec::new();

        for x in arr.iter() {
            if let Some(last) = stack.last().cloned() {
                if *x > last {
                    stack.push(*x);
                } else {
                    while !stack.is_empty() && x < stack.last().unwrap() {
                        stack.pop();
                    }
                    stack.push(last);
                }
            } else {
                stack.push(*x);
            }
        }

        stack.len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let x = Solution::max_chunks_to_sorted(vec![4, 3, 2, 1, 0]);
        assert_eq!(x, 1)
    }

    #[test]
    fn test2() {
        let x = Solution::max_chunks_to_sorted(vec![1, 0, 2, 3, 4]);
        assert_eq!(x, 4)
    }

    #[test]
    fn test3() {
        let x = Solution::max_chunks_to_sorted(vec![0, 1]);
        assert_eq!(x, 2)
    }

    #[test]
    fn test4() {
        let x = Solution::max_chunks_to_sorted(vec![2, 0, 1]);
        assert_eq!(x, 1)
    }
}
