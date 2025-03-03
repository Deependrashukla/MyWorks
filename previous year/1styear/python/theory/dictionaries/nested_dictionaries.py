Employee = { 'emp1': {'name': 'Hameed', 'age': 29, 'Designation':'CR', 'Salary':5000  }, 'emp2': {'name': 'Gurjeet', 'age': '45', 'Designation':'HR', 'Salary':30000 }, 'emp3': {'name': 'Madhav', 'age': '35', 'Designation':'Admin', 'Salary':40000 } } 

def update_dic(Employee, d, s):
    for employee in Employee :
        # print(employee,1)
        # for designation in Employee[employee] :
            # print(designation)
        if  Employee[employee]['Designation'] == d :
            Employee[employee]['Salary'] = s
                # print(employee[designation ]) 

update_dic(Employee, 'CR', 5)
print(Employee)
