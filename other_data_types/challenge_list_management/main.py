meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Chedder", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
deli_dept = [meat, cheese, condiment]
if "Ham" in meat[0] and meat[2] < 100:
    meat[2] = 100
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
print("Initial Deli List: ", deli_dept)
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()
print("Updated Deli List: ", deli_dept)