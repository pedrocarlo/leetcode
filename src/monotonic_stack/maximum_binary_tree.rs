//! 654. Maximum Binary Tree

use std::cell::RefCell;
use std::rc::Rc;
struct Solution;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

#[allow(dead_code)]
impl Solution {
    pub fn construct_maximum_binary_tree(mut nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.is_empty() {
            return None;
        }
        let mut idx_max = 0;
        let mut max = 0;
        for (i, x) in nums.iter().enumerate() {
            if max < *x {
                max = *x;
                idx_max = i;
            }
        }
        let mut root = TreeNode::new(max);

        let left = nums.drain(..idx_max).collect();
        root.left = Solution::construct_maximum_binary_tree(left);
        let right = nums.drain(1..).collect();
        root.right = Solution::construct_maximum_binary_tree(right);

        Some(Rc::new(root.into()))
    }
}
