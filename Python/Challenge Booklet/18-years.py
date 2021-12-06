#Years in a Range
start_year = int(input("Enter a starting year: "))
end_year = int(input("Enter a ending year: "))
selected_years = []
for i in range(start_year, end_year):
    counts = {}
    for j in str(i):
        if j in counts:
            counts[j] += 1
        else:
            counts[j] = 1
    for k in counts.values():
        if k >= 2:
            selected_years.append(i)
print(selected_years)