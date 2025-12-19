import requests
import json

BASE_URL = "http://127.0.0.1:5000"


def test_loan_eligibility():
    """Test the loan eligibility endpoint"""

    print("=" * 60)
    print("Testing Loan Eligibility API")
    print("=" * 60)

    # Test Case 1: Approved Application
    print("\n1. Testing APPROVED application...")
    data1 = {
        "national_id": "12345678",
        "loan_amount": 10000,
        "term_months": 12
    }

    response1 = requests.post(f"{BASE_URL}/api/loan-eligibility", json=data1)
    print(f"Status Code: {response1.status_code}")
    print(f"Response: {json.dumps(response1.json(), indent=2)}")

    # Test Case 2: Declined Application
    print("\n2. Testing DECLINED application...")
    data2 = {
        "national_id": "87654321",
        "loan_amount": 15000,
        "term_months": 6
    }

    response2 = requests.post(f"{BASE_URL}/api/loan-eligibility", json=data2)
    print(f"Status Code: {response2.status_code}")
    print(f"Response: {json.dumps(response2.json(), indent=2)}")

    # Test Case 3: Missing Fields
    print("\n3. Testing INVALID request (missing fields)...")
    data3 = {
        "national_id": "11111111"
    }

    response3 = requests.post(f"{BASE_URL}/api/loan-eligibility", json=data3)
    print(f"Status Code: {response3.status_code}")
    print(f"Response: {json.dumps(response3.json(), indent=2)}")

    print("\n" + "=" * 60)
    print("Testing Complete!")
    print("=" * 60)


if __name__ == "__main__":
    test_loan_eligibility()