# Task 1 description:
# 1. Make a script with the few variables and outputs
# 2. Add breakpoints to script
# 3. Run script via debugger
# 4. Execute it step by step
# Pay attention to the list of variables in the debugger.
# Pay attention to the notes that appear in the code.
# from datetime import datetime

due_date = '2024-01-01' # assign due date of the project completion
print ("Due Date:" , due_date) # show due date for the user

from datetime import datetime # import function to display today date from datetime module
today_date = datetime.now()
date2 = (today_date.strftime('%Y-%m-%d'))
print("Current Date:", date2) # display today date for the user

from datetime import date
date1 = date(2024, 1, 1)
date3 = date(2023, 11, 12) # ask how to use here date2 to calculate delta
delta = date1-date3
print('Remaining Days:', delta.days)









