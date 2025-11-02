import csv, random

with open("turingbot_input.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])  # column headers
    for i in range(50):
        x = i / 50
        y = random.random()
        writer.writerow([x, y])

print("✅ Created turingbot_input.csv with x,y columns")
