def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def compound_interest(principal, rate, time):
    interest = principal * ((1 + rate / 100) ** time - 1)
    return interest