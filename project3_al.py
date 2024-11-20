# requirements 1 and 2

class Caregivers:
  def __init__(self, name, phone, email, pay_rate = 20):
    self.name = name
    self.phone = phone
    self.email = email
    self.pay_rate = pay_rate # paid caregivers are paid weekly at $20/hr
    self.hours = 0 # care is required 12 hours per day, 7 days a week (84 hours)
    self.availability = {}

  def schedule_availability(self, availability, shift):
    # each caregiver should have their own availability schedule where they can indicate their availability for each shift
    # availability categories are 'preferred', 'available' (default), and 'unavailable'
    # indicates AM or PM shifts
    pass

class Schedule:
  def __init__(self):
    pass

  

