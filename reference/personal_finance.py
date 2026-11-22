#!/usr/bin/env python3
"""Reference CLI formulas for the FinWise browser calculators.
Run: python3 personal_finance.py
The website itself runs in the browser and does not require Python.
"""
def emi(principal, annual_rate, years):
    months = years * 12
    monthly_rate = annual_rate / 1200
    if months <= 0: return 0.0
    if monthly_rate == 0: return principal / months
    return principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

def sip(monthly_investment, annual_return, years):
    n, r = years * 12, annual_return / 1200
    if r == 0: return monthly_investment * n
    return monthly_investment * (((1 + r) ** n - 1) / r) * (1 + r)

def gst(amount, rate_percent, inclusive=False):
    rate = rate_percent / 100
    base = amount / (1 + rate) if inclusive else amount
    tax = amount - base if inclusive else amount * rate
    return base, tax, base + tax

def fd(principal, annual_rate, years, compounds_per_year=4):
    return principal * (1 + annual_rate / (100 * compounds_per_year)) ** (compounds_per_year * years)

def rd(monthly_deposit, annual_rate, years):
    months = int(years * 12)
    monthly_rate = (1 + annual_rate / 100) ** (1 / 12) - 1
    if monthly_rate == 0: return monthly_deposit * months
    return monthly_deposit * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)

def main():
    print("FinWise reference calculator")
    print("1 EMI  2 SIP  3 GST  4 FD  5 RD")
    choice = input("Choose: ").strip()
    if choice == "1":
        p=float(input("Loan amount: ")); r=float(input("Annual rate (%): ")); y=float(input("Years: "))
        value=emi(p,r,y); print(f"Monthly EMI: ₹{value:,.2f}; total repayment: ₹{value*y*12:,.2f}")
    elif choice == "2":
        p=float(input("Monthly SIP: ")); r=float(input("Annual expected return (%): ")); y=float(input("Years: "))
        value=sip(p,r,y); print(f"Future value: ₹{value:,.2f}; invested: ₹{p*y*12:,.2f}")
    elif choice == "3":
        a=float(input("Amount: ")); r=float(input("GST rate (%): ")); inclusive=input("Amount already includes GST? (y/n): ").lower()=="y"
        base,tax,total=gst(a,r,inclusive); print(f"Base: ₹{base:,.2f}; GST: ₹{tax:,.2f}; total: ₹{total:,.2f}")
    elif choice == "4":
        p=float(input("Principal: ")); r=float(input("Annual rate (%): ")); y=float(input("Years: "))
        print(f"FD maturity: ₹{fd(p,r,y):,.2f}")
    elif choice == "5":
        p=float(input("Monthly deposit: ")); r=float(input("Annual rate (%): ")); y=float(input("Years: "))
        print(f"RD maturity estimate: ₹{rd(p,r,y):,.2f}")
    else: print("Invalid choice")
if __name__ == "__main__": main()
