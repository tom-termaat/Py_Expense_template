from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":[],
    },
]

involved_questions = [
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - Involved",
        "choices":[],
    }
]


def new_expense(*args):
    user_choices = []

    with open('users.csv', 'r') as file:
        data = csv.reader(file)

        for line in data:
            user_choices.append(line[0])

    expense_questions[2]['choices'] = user_choices
    infos = prompt(expense_questions)

    involved_choices = []
    for user in user_choices:
        choice = { "name": user, "checked": False }
        if user == infos["spender"]:
            choice["checked"] = True
        involved_choices.append(choice)
            

    involved_questions[0]["choices"] = involved_choices
    infos_involved = prompt(involved_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    f = open('expenses.csv', 'a')
    writer = csv.writer(f)

    delim = ";"
    data = [
            infos["amount"],
            infos["label"],
            infos["spender"],
            delim.join(infos_involved["involved"])
           ]
    writer.writerow(data)
    f.close()

    print("Expense Added !")
    return True
