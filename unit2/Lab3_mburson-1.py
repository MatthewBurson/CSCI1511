camping_items = ["tent", "sleeping bag", "sleeping pad", "camp stove", "fuel", "cooking pot", "utensils", "headlamp", "first-aid kit", "folding chairs"]

num_items = len(camping_items)
print(f"Number of items: {num_items}")

camping_items.sort()
print("\nSorted list of camping gear:")
for item in camping_items:
    print(item)