def evaluate(result):
    if result["status"] in ["FAILED", "INCOMPLETE"]:
        return False
    return True

