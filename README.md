

#  Loan Eligibility API


##  Overview

This project implements a **REST API** that determines whether a loan applicant is eligible based on salary verification, credit history checks, and predefined business rules.
The goal is to simulate how a financial institution like DRS Capital might automate loan decisioning using backend services.

---

##  Tech Choices & Rationale

### **Python 3.x**

Chosen for:

* Its readability and ease of use
* Strong adoption in finance, data analysis, and backend services
* A rich ecosystem for building APIs and automation tools

### **Flask Framework**

Selected because it is:

* Lightweight and minimalistic
* Ideal for small to medium REST APIs
* Easy to extend as the system grows
* Perfect for rapid prototyping during assessments

### **Mock External APIs**

Used to simulate:

* Salary verification
* Credit bureau scoring/history
  These make the project realistic without needing actual third-party integrations.

### **Modular Business Logic**

Rules such as credit score, salary checking, and loan limits are separated for maintainability and easy upgrades.

---
### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the API**

```bash
python app.py
```

API will be available at:
👉 `http://127.0.0.1:5000`

### **5. Run Tests**

```bash
python test_api.py
```

---

## 📡 API Endpoint

### **POST /api/loan-eligibility**

Checks whether the applicant qualifies for a loan.

#### **Request Example**

```json
{
  "national_id": "12345678",
  "loan_amount": 10000,
  "term_months": 12
}
```

#### **Response Example (Approved)**

```json
{
  "eligible": true,
  "monthly_repayment": 833.33,
  "message": "Loan approved"
}
```

---

## ✔ Eligibility Rules Implemented

1. **Income Rule:**
   Applicant salary must be at least **3× the monthly repayment**.

2. **Credit Score Rule:**
   Minimum credit score **≥ 600**.

3. **Defaults Rule:**
   Applicants with active defaults are automatically disqualified.

4. **Loan Count Rule:**
   Applicants may have at most **3 active loans**.

These rules simulate typical lending criteria in microfinance and retail credit lending.

---

##  What I Would Improve With More Time

### **1. Database Integration**

Use PostgreSQL or MongoDB to store:

* Applicants
* Loan applications
* Credit history
* Salary records

### **2. Real Third-Party Integrations**

Integrate actual:

* Credit bureau APIs
* Salary verification services
* Risk scoring systems

### **3. Security Enhancements**

Add:

* JWT authentication
* API key validation
* Advanced request validation and sanitisation

### **4. Deployment**

Deploy using:

* Render
* Railway
* AWS or GCP
  Include CI/CD pipelines using GitHub Actions.

### **5. Frontend Dashboard**

Build a minimal UI to:

* View applications
* Check eligibility
* Display analytics and risk summaries

---

## 👤 Author

**Nigel Kamufohoma**

