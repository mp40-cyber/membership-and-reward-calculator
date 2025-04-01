# membership-and-reward-calculator
# PacECommerce Membership and Reward Calculator

## Overview
PacECommerce Membership and Reward Calculator is a Python-based program designed to predict user membership tiers and calculate discounts and rewards based on spending and income levels.

## Features
- Predicts membership tier based on user expenses and income.
- Displays membership benefits and tier requirements.
- Calculates discounts and potential rewards for purchases.
- Supports three membership tiers: Platinum, Gold, and Silver.

## Membership Benefits
| Tier | Discount | Rewards |
|------|---------|---------|
| Platinum | 15% | Food Voucher, Gold 0.5g, Travel Voucher, Cashback up to 30% |
| Gold | 10% | Food Voucher, Ride-hailing Voucher |
| Silver | 8% | Food Voucher |

## Tier Requirements
| Tier | Minimum Expense (Mil/Month) | Minimum Income (Mil/Month) |
|------|---------------------------|---------------------------|
| Platinum | 8 | 17 |
| Gold | 6 | 10 |
| Silver | 5 | 7 |

## How It Works
1. Create a `MembershipUser` instance with a username, expense, and income.
2. Call `user_prediction()` to predict the membership tier.
3. Call `calculate_price(total_spent)` to determine the final amount after discount and display potential rewards.

## Example Usage
```python
from membership import MembershipUser

# Create a user instance
user1 = MembershipUser("HeraMaulana", 7000000, 9000000)
user1.user_prediction()
user1.calculate_price(750000)
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/mp40-cyber/membership-and-reward-calculator.git
   ```
2. Install dependencies:
   ```sh
   pip install tabulate
   ```
3. Run the program:
   ```sh
   python main.py
   ```

## License
This project is open-source and available under the MIT License.

