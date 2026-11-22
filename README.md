# FinWise — Personal Finance Calculator Website

A responsive, static personal-finance calculator website built with **HTML, CSS and JavaScript**.

## Included calculators
- EMI calculator
- SIP calculator
- GST calculator (add GST / extract GST)
- Indian income-tax estimator (new and old regimes)
- FD calculator
- RD calculator
- Loan eligibility estimator

## Run locally
Open `index.html` in a browser. For a more reliable local preview, open Terminal in this folder and run:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

Python is only used here as an optional local static-file preview and in `reference/personal_finance.py` as a command-line formula example. `reference/finance_calculators.cpp` is an optional C++17 command-line formula example. Neither Python nor C++ is required to run or host the website.

## Deploy free with GitHub Pages
1. Create a GitHub repository, for example `finwise-calculators`.
2. Upload `index.html`, `style.css`, `script.js`, and the `assets` folder to the repository root.
3. In repository Settings → Pages, select deploy from the `main` branch and `/ (root)`.
4. For `tools.nishublogs.online`, add that custom domain in GitHub Pages settings, then add the DNS record GitHub specifies at your domain provider. For a subdomain this is usually a CNAME to `<your-github-username>.github.io`. Wait for DNS and HTTPS provisioning.

## Important notes
- Calculations run in the visitor's browser; this project has no backend, login, database or file upload.
- Google Fonts are loaded from Google Fonts. The site otherwise uses local files.
- The income-tax tool is an indicative estimate for India, tax year 2026–27. The new regime calculation applies a ₹75,000 salary standard deduction, section 87A rebate up to ₹12 lakh and basic marginal relief between ₹12 lakh and ₹12.75 lakh. Old-regime mode uses basic slab estimates and entered deductions. It does not model every exemption, surcharge, special-rate income, deduction condition or tax-specific adjustment. Verify using the official Income Tax Department portal or a tax professional before filing.
- SIP returns are not guaranteed. FD/RD compounding may differ from bank-specific rules. Loan eligibility depends on lender underwriting, credit score, age, employment and other conditions.
- Review all formulas and tax assumptions before public launch.

## Optional command-line references
Python:
```bash
python3 reference/personal_finance.py
```
C++17:
```bash
g++ -std=c++17 reference/finance_calculators.cpp -o finance
./finance
```
