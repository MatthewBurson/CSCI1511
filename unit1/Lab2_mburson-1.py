# Lab2_mburson-1
# Matthew Burson
# 1/20/24
bill = input("Enter bill total: ")
bill = float(bill)
tip_15 = bill * 0.15
tip_20 = bill * 0.20
total_15 = bill + tip_15
total_20 = bill + tip_20
print(f"Your bill is ${bill:.2f}")
print(f"Tip suggesgtions: 15% (${tip_15:.2f}), 20% (${tip_20:.2f})")
print(f"Total with tip: 15% : ${total_15:.2f}, 20% : ${total_20:.2f}")