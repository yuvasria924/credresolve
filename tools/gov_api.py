import random, time

def apply_scheme_api(scheme, data):
    time.sleep(1)
    if random.random() < 0.2:
        return {"status": "FAILED", "reason": "Server Timeout"}
    return {"status": "SUCCESS", "application_id": "TN-" + str(random.randint(10000,99999))}
