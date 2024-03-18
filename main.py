from app.interest import simple_interest, compound_interest

simple_value = simple_interest(100, 1.05, 3)
compound_value = compound_interest(100,1.05, 3)

print(f"Simple Interest: {simple_value}")
print(f"Compound Interest: {compound_value}")

negative_value = simple_interest(100,-1.05,3)

print(f"Simple Negative: {negative_value}")