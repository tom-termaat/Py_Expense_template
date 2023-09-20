from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"checkbox",
        "name":"user_debt",
        "message":"Expense Report",
        "choices":[]
    }
]

def show_expense_report(*args):
    expense_report_choices = []

    user_list = []

    with open('users.csv', 'r') as file:
        data = csv.reader(file)

        for line in data:
            user_list.append(line[0])

    user_debt_report = []

    for user in user_list:
        user_debt_report.append({
            "user": user,
            "debt": list(map(lambda x: { "user": x, "amount":0 }, user_list))
        })

    print(user_debt_report)

    with open('expenses.csv', 'r') as file:
        data = csv.reader(file) 

        for line in data:
            amount = line[0]
            spender = line[2]
            involved = line[3].split(';')

            print(int(amount)/len(involved))
            
