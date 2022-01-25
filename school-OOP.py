class School:
  def __init__(self, name, level, numberOfStudents):
    self._name = name
    if level in ['primary', 'middle', 'high']:
      self._level = level
    else:
      raise Exception("level not one of 'primary', 'middle', or 'high'")
    self._numberOfStudents = numberOfStudents
  
  def __repr__(self):
    return f"A {self._level} school named {self._name} with {self._numberOfStudents} students"

  @property
  def name(self):
    return self._name
  
  @property
  def level(self):
    return self._level
  
  @property
  def numberOfStudents(self):
    return self._numberOfStudents

  @numberOfStudents.setter
  def numberOfStudents(self, newNumberOfStudents):
    self._numberOfStudents = newNumberOfStudents



class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self._pickupPolicy = pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return f"{parentRepr}, the pickup policy is {self._pickupPolicy}"

  @property
  def pickupPolicy(self):
    return self._pickupPolicy
  
  @pickupPolicy.setter
  def pickupPolicy(self, newPickupPolicy):
    self._pickupPolicy = newPickupPolicy



class MiddleSchool(School):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)



class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self._sportsTeams = sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    sportsTeams = ", ".join(self._sportsTeams)
    return f"{parentRepr} with the sportsteams: {sportsTeams}"

  @property
  def sportsTeams(self):
    return self._sportsTeams


mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.name)
print(mySchool.level)
mySchool.numberOfStudents = 200
print(mySchool.numberOfStudents)

testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool)
testSchool.pickupPolicy = 'not allowed'
print(testSchool.pickupPolicy)
print(testSchool)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.sportsTeams)
print(c)
