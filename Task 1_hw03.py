import datetime as dt
# Function to get the number of days from today to the indicated date
from datetime import datetime
def get_days_from_today(date):
  try:
    # Current date
    current_datetime = datetime.now()
    # Indicated date
    given_date = datetime(year=1991, month=8, day=24)
    # difference between dates
    difference = current_datetime.toordinal() - given_date.toordinal()
    return difference
    # error exeption
  except ValueError:
      return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

# sample of output
print(get_days_from_today("1991-08-24"))
