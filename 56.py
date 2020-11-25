airtime_minutes = 50
text_message = 50
cost_month = 15

ADD_AIRTIME = 0.25
ADD_TEXT = 0.15

ADD_CHARGE_911 = 0.44
SALES_BILL = 0.05

number_minutes = int(input("Enter the number minutes used in a month: "))
number_text = int(input("Enter the text messages used in a month: "))

if number_minutes > airtime_minutes and number_text > text_message:
    total_minutes = (number_minutes - airtime_minutes) * ADD_AIRTIME
    total_text = ( number_text - text_message) * ADD_TEXT
    print("The extra minutes used are: ",total_minutes)
    print("The extra text messages used are: ",total_text)
    
    total_amount = cost_month + total_minutes + total_text
    print("The total amount is: ",total_amount)
elif number_minutes > airtime_minutes and number_text <=text_message:
    total_minutes = (number_minutes - airtime_minutes) * ADD_AIRTIME
    print("The extra minutes used are: ",total_minutes)

    total_amount = cost_month + total_minutes
    print("The total amount is: ",total_amount)
elif number_minutes <= airtime_minutes and number_text > text_message:
    total_text = (number_text - text_message) * ADD_TEXT
    print("The extra text messages used are: ",total_text)

    total_amount = cost_month + total_text
    print("The total amount is: ",total_amount)
else: 
    print("The base charge is", cost_month, "$ a month.")
