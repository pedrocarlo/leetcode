struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

#[allow(dead_code)]
impl Solution {
    pub fn remove_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut stack = Vec::new();
        let mut curr_head = &head;
        while let Some(node) = curr_head {
            while !stack.is_empty() && *stack.last().unwrap() < node.val {
                stack.pop();
            }
            stack.push(node.val);
            curr_head = &node.next;
        }
        stack
            .into_iter()
            .rev()
            .map(|x| ListNode::new(x))
            .reduce(|acc, mut node| {
                node.next = Some(acc.into());
                node
            })
            .map(|list| Box::new(list))
    }
}
