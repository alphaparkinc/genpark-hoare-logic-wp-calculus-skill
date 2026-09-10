from client import HoareWPCalculus
import json

def handle_request(req):
    wp = HoareWPCalculus()
    action = req.get("action")
    if action == "wp_seq":
        stmts = req.get("statements", [])
        post = req.get("postcondition", "")
        res = wp.wp_seq(stmts, post)
        return {"status": "ok", "precondition": res}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "wp_seq", "statements": [["x", "x+1"]], "postcondition": "x > 5"})))
