from flask import Flask, request, jsonify
import random

app = Flask(__name__)


# Mock Salary Verification API
@app.route('/api/salary-verification', methods=['POST'])
def salary_verification():
    """Mock API to verify salary"""
    data = request.json
    national_id = data.get('national_id')

    # Simulate salary verification
    mock_salaries = {
        '12345678': 5000,
        '87654321': 3000,
        '11111111': 8000,
    }

    salary = mock_salaries.get(national_id, random.randint(2000, 10000))

    return jsonify({
        'national_id': national_id,
        'monthly_salary': salary,
        'verified': True
    })


# Mock Credit Bureau API
@app.route('/api/credit-bureau', methods=['POST'])
def credit_bureau():
    """Mock API to check credit history"""
    data = request.json
    national_id = data.get('national_id')

    # Simulate credit bureau response
    mock_credit_data = {
        '12345678': {'score': 650, 'active_defaults': 0, 'active_loans': 2},
        '87654321': {'score': 580, 'active_defaults': 1, 'active_loans': 1},
        '11111111': {'score': 720, 'active_defaults': 0, 'active_loans': 1},
    }

    credit_data = mock_credit_data.get(
        national_id,
        {
            'score': random.randint(500, 800),
            'active_defaults': random.randint(0, 2),
            'active_loans': random.randint(0, 4)
        }
    )

    return jsonify({
        'national_id': national_id,
        'credit_score': credit_data['score'],
        'active_defaults': credit_data['active_defaults'],
        'active_loans': credit_data['active_loans']
    })


# Main Loan Eligibility API
@app.route('/api/loan-eligibility', methods=['POST'])
def loan_eligibility():
    """
    Main API to check loan eligibility
    """
    try:
        data = request.json

        # Validate input
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        national_id = data.get('national_id')
        loan_amount = data.get('loan_amount')
        term_months = data.get('term_months')

        if not all([national_id, loan_amount, term_months]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Check salary
        salary_response = app.test_client().post('/api/salary-verification',
                                                 json={'national_id': national_id})
        salary_data = salary_response.get_json()
        monthly_salary = salary_data.get('monthly_salary', 0)

        # Check credit history
        credit_response = app.test_client().post('/api/credit-bureau',
                                                 json={'national_id': national_id})
        credit_data = credit_response.get_json()
        credit_score = credit_data.get('credit_score', 0)
        active_defaults = credit_data.get('active_defaults', 0)
        active_loans = credit_data.get('active_loans', 0)

        # Calculate monthly repayment
        monthly_repayment = loan_amount / term_months

        # Apply eligibility rules
        reasons = []
        eligible = True

        if monthly_salary < (3 * monthly_repayment):
            eligible = False
            reasons.append(f'Salary ${monthly_salary} < 3x repayment ${monthly_repayment * 3}')

        if credit_score < 600:
            eligible = False
            reasons.append(f'Credit score {credit_score} < 600')

        if active_defaults > 0:
            eligible = False
            reasons.append(f'{active_defaults} active default(s)')

        if active_loans > 3:
            eligible = False
            reasons.append(f'{active_loans} active loans > 3')

        # Build response
        response = {
            'national_id': national_id,
            'loan_amount': loan_amount,
            'term_months': term_months,
            'monthly_repayment': round(monthly_repayment, 2),
            'eligible': eligible,
            'applicant_details': {
                'monthly_salary': monthly_salary,
                'credit_score': credit_score,
                'active_defaults': active_defaults,
                'active_loans': active_loans
            }
        }

        if not eligible:
            response['decline_reasons'] = reasons
        else:
            response['message'] = 'Loan approved'

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    print("Loan Eligibility API running on http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)