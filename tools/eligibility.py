def check_eligibility(age, income, category):
    if category == "student":
        return age >= 17 and income < 200000
    if category == "woman":
        return age >= 18 and income < 250000
    if category == "farmer":
        return age >= 18 and income < 300000
    return False



