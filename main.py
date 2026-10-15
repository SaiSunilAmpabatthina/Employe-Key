def func():
    name = ["vijay", "ajay", "rani", "vinay", "mahesh", "sai", "chandu", "srinivas", "arun", "varsha"]
    salary = [10000, 20000, 12000, 55000, 45000, 20000, 26000, 60000, 17000, 25000]
    memo = [0, 1, 1, 1, 2, 3, 2, 0, 2, 2]
    fired = []

    for i in range(len(salary)):
        if salary[i] > 40000:
            fired.append(name[i])
            
    for i in range(len(memo)):
        if(salary[i]>20000 and memo[i]>=2):
            fired.append(name[i])

    return fired

fired_employees = func()
fired_employees = set(fired_employees)
print(fired_employees)
