print("Voting system")
# to enter the number of people 
num_people = int(input("Enter the number of people you want to see"))
# array to store names and ages
names = []
ages = []
# loop to take input 
for v in range(num_people):
    print(f"\nPerson  {i + 1}")
    name = input("Enter your name")
    age = int(input("Enter your age"))

    names.append(name)
    ages.append(age)

print("\n -------VOTING ELIGIBILITY RESULTS--------")
# loop in check eligibility 
for i in range(num_people):
    if ages[i] >= 18:
          print(f"{names[i]} (Age: {ages[i]}) is eligible for voting ✅")
    else:
        print(f"{names[i]} (Age: {ages[i]}) is underage for voting ❌")