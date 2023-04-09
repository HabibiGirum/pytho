tuition = 10000    # tuition this year
increase = 0.05    # 5% increase each year

# calculate tuition in 10 years
tuition_10_years = tuition * (1 + increase) ** 10
print("Tuition in 10 years:", tuition_10_years)

# calculate total cost of 4 years starting 10 years from now
total_cost = 0
for i in range(10, 14):
    total_cost += tuition * (1 + increase) ** i
print("Total cost of 4 years' tuition starting 10 years from now:", total_cost)
