//! 901. Online Stock Span

struct StockSpanner {
    stack: Vec<(i32, i32)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
#[allow(dead_code)]
impl StockSpanner {
    fn new() -> Self {
        StockSpanner { stack: Vec::new() }
    }

    fn next(&mut self, price: i32) -> i32 {
        let mut span = 1;
        while !self.stack.is_empty() && self.stack.last().unwrap().0 <= price {
            let last = self.stack.pop().unwrap();
            span += last.1;
        }
        self.stack.push((price, span));
        span
    }
}
