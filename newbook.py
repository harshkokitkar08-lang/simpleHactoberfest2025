# Read inputs
X = int(input())      # Weekly rental cost
D = int(input())      # Number of days rented
S = input().lower()   # Staff status ("true" or "false")

# Base cost for up to 7 days
total_cost = X

# If rental exceeds 7 days and not a staff member, add extra charges
if D > 7 and S == "false":
    extra_days = D - 7
    total_cost += extra_days * 2  # Rs 2 per extra day

print(total_cost)
