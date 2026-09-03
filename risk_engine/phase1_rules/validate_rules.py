"""
Phase 1 - validates underwriting_rules.json against the PRD's worked example.
Run: python validate_rules.py
Expected: DTI 18.75%, Decision APPROVE
"""
import json
import os

RULES_PATH = os.path.join(os.path.dirname(__file__), "underwriting_rules.json")

with open(RULES_PATH) as f:
    rules = json.load(f)


def decide(score: int, income: float, existing_emi: float):
    dti = existing_emi / income
    if score < rules["score_reject_below"] or dti > rules["dti_reject_above"]:
        return "REJECT", dti
    if score < rules["score_review_below"] or dti > rules["dti_review_above"]:
        return "REVIEW", dti
    return "APPROVE", dti


if __name__ == "__main__":
    
    decision, dti = decide(score=718, income=80000, existing_emi=15000)
    print(f"DTI: {dti:.2%}")
    print(f"Decision: {decision}")

    
    print(decide(score=520, income=50000, existing_emi=10000))   
    print(decide(score=700, income=50000, existing_emi=30000))   
    print(decide(score=600, income=50000, existing_emi=15000))   