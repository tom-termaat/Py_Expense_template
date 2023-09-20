from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import user_questions,add_user
from expense_report import show_expense_report

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()

    if (option['main_options']) == "New User":
        add_user()

    if (option['main_options']) == "Show Status":
        show_expense_report()

def main():
    ask_option()

main()
