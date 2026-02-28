# Design-patterns

## Strategy pattern

#### 🎯 When Do We Use Strategy Pattern?

We use Strategy Pattern when:

✅ We have multiple interchangeable algorithms
✅ The algorithm can change at runtime
✅ We want to avoid large if-elif chains
✅ We want to follow Open/Closed Principle

🔥 Real-World Scenarios (Senior-Level Thinking)


1️⃣ Payment Gateways (Classic Example)
```python

Different payment providers:

Stripe
Razorpay
PayPal
UPI
Crypto

Instead of:

if payment_type == "stripe":
    ...
elif payment_type == "razorpay":
    ...

We create strategies:

StripePayment()
RazorpayPayment()
UPIPayment()

👉 Clean, extendable, testable.

```

2️⃣ Authentication Mechanisms
```python
Login can be:

JWT
OAuth
Session-based
API Key

Each authentication method has different validation logic.

class AuthStrategy:
    def authenticate(self, request):
        pass

Used heavily in:
FastAPI backends
Django middleware
API gateways

```


3️⃣ File Processing / Parsers
```python
Suppose your system supports:

CSV
JSON
XML
Excel

Instead of messy conditionals:

if file_type == "csv":
    ...

You create:

CSVParser()
JSONParser()
XMLParser()

This is very common in data engineering systems.

```

4️⃣ Notification Systems

```python
Send notifications via:

Email
SMS
Push notification
WhatsApp API

Each has different sending logic but same interface:

send(message)

Used in:

E-commerce
Banking apps
SaaS products
```


5️⃣ Pricing / Discount Engines

```python
Different discount strategies:

Percentage discount
Flat discount
Seasonal discount
Buy 1 Get 1
Loyalty discount

Instead of deeply nested conditions, use:

class DiscountStrategy:
    def apply(cart):
        pass

Very common in:

E-commerce platforms
Subscription billing systems

```


6️⃣ Sorting or Filtering Algorithms
```python
Example:

Sort by price
Sort by date
Sort by rating
You inject sorting strategy dynamically.

Used in:

Search systems
E-commerce listings
Data dashboards

```


7️⃣ Machine Learning Model Selection

```python
Different models:

Linear regression
Random forest
XGBoost
Neural network
All implement:

train()
predict()

Production ML systems use this pattern heavily.
```

8️⃣ Retry / Backoff Policies
```python
Different retry strategies:
No retry
Fixed retry
Exponential backoff
Circuit breaker

Very important in:

Microservices
Distributed systems
API clients
```

🧠 When NOT To Use Strategy Pattern

Senior developers also know when NOT to use it:

❌ When there are only 2 small conditions
❌ When logic will never change
❌ When abstraction adds unnecessary complexity

Overengineering is also bad design.
```python
🚀 How Seniors Recognize Strategy Pattern

If you see code like this:

if type == "A":
    ...
elif type == "B":
    ...
elif type == "C":
    ...

And that block keeps growing…

💡 That’s a strong smell for Strategy Pattern.

🏗 In Python Specifically

In Python, Strategy Pattern can be:

Implemented using classes (like you did)
Using functions (first-class functions)
Using dictionaries of callables
Using dependency injection (FastAPI style)
Example Pythonic shortcut:

strategies = {
    "credit": credit_payment,
    "paypal": paypal_payment
}

strategies[payment_type](amount)
```

Senior Python developers often choose simpler approaches unless strict OOP is required.

🎯 What This Means For You

If you master Strategy Pattern, you improve:

Clean architecture skills
SOLID principles
Interview system design answers
Backend extensibility thinking
And this directly pushes you toward senior backend developer level.

