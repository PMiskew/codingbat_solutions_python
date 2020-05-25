'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
'''


def alarm_clock(day, vacation):
  
  #Approach 1: Using Standard If statement approach
  '''
  if day == 0 or day == 6:
    if vacation:
      return "off"
    return "10:00"
    
  if vacation:
    return "10:00"
  return "7:00"
  '''
  
  #Approach 2: Using the MOD operator
  '''
  weekend = "off"
  weekday = "10:00"
  
  if (not(vacation)):
    weekend = "10:00"
    weekday = "7:00"
    
  if day % 6 == 0:
    return weekend
  return weekday
  '''
  
  #Approach 3: Using the lists and day as an index. 
  normalDay = ["10:00","7:00","7:00","7:00","7:00","7:00","10:00"]
  vacationDay = ["off","10:00","10:00","10:00","10:00","10:00","off"]
  
  if (vacation):
    return vacationDay[day]
  return normalDay[day]
  
  
  
  
  
  
  