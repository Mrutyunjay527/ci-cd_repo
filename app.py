
def calculate_total(amount):
    if amount > 300:
        amount = amount * 0.90

    total = amount * 1.05
    return round(total, 2)


if __name__ == "__main__":
    print("Total for ₹200:", calculate_total(200))
    print("Total for ₹300:", calculate_total(300))
    print("Total for ₹400:", calculate_total(400))
