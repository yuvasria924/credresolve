from tools.eligibility import check_eligibility
from tools.scheme_db import get_scheme
from tools.gov_api import apply_scheme_api

def run_agent(memory):
    age = memory.get("age")
    income = memory.get("income")
    category = memory.get("category")

    if None in [age, income, category]:
        return {"status": "INCOMPLETE"}

    if not check_eligibility(age, income, category):
        return {"status": "NOT_ELIGIBLE", "scheme": None}

    scheme = get_scheme(category)
    memory.update("scheme", scheme)

    res = apply_scheme_api(scheme, memory.dump())
    if res["status"] == "FAILED":
        return {"status": "FAILED"}
    return {"status": "SUCCESS", "scheme": scheme, "app_id": res["application_id"]}

