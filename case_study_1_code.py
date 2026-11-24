"""
Case Study 1: Progressive Electricity Billing

Slab rates:
    First 100 units: Rs. 2 per unit
    Next 100 units:  Rs. 3 per unit
    Next 100 units:  Rs. 5 per unit
    Above 300 units: Rs. 7 per unit
Fixed charge: Rs. 50
"""

def calculate_bill(units):
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    remaining = units
    energy_charge = 0

    # First 100 units
    slab_units = min(remaining, 100)
    energy_charge += slab_units * 2
    remaining -= slab_units

    # Next 100 units
    slab_units = min(remaining, 100)
    energy_charge += slab_units * 3
    remaining -= slab_units

    # Next 100 units
    slab_units = min(remaining, 100)
    energy_charge += slab_units * 5
    remaining -= slab_units

    # Units above 300
    energy_charge += remaining * 7

    fixed_charge = 50
    total_bill = energy_charge + fixed_charge
    return energy_charge, fixed_charge, total_bill


def main():
    print("===== PROGRESSIVE ELECTRICITY BILLING =====")

    try:
        units = float(input("Enter electricity units consumed: "))

        if not units.is_integer():
            print("Please enter a whole number of units.")
            return

        energy, fixed, total = calculate_bill(int(units))

        print("\n----- BILL DETAILS -----")
        print(f"Units consumed : {int(units)}")
        print(f"Energy charge  : Rs. {energy:.2f}")
        print(f"Fixed charge   : Rs. {fixed:.2f}")
        print("------------------------")
        print(f"Total bill     : Rs. {total:.2f}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
