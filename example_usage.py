from client import HoareWPCalculus

def main():
    print("=== Testing Hoare Logic WP Calculus ===")
    wp = HoareWPCalculus()
    
    # Program: x = x + 1; y = x * 2; Postcondition: y > 10
    stmts = [('x', 'x + 1'), ('y', 'x * 2')]
    post = "y > 10"
    pre = wp.wp_seq(stmts, post)
    print(f"Postcondition: {post}")
    print(f"Computed WP Precondition: {pre}")
    assert "((x + 1) * 2) > 10" == pre
    print("=== Hoare WP Calculus Complete ===")

if __name__ == "__main__":
    main()
