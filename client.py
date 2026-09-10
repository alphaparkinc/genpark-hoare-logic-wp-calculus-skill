import re

class HoareWPCalculus:
    """
    Dijkstra's Weakest Precondition (WP) Calculus.
    Computes precondition requirements backwards through imperative assignment sequences.
    """
    def wp_assign(self, var, expr, post_condition):
        pattern = rf'\b{re.escape(var)}\b'
        return re.sub(pattern, f"({expr})", post_condition)

    def wp_seq(self, stmts, post):
        curr = post
        for var, expr in reversed(stmts):
            curr = self.wp_assign(var, expr, curr)
        return curr
