instrument_familes = {
  'Strings': ['Guitar', 'Banjo', 'Sitar'],
  'Percussion': ['Conga', 'Cymbal', 'Cajon'],
  'woodwinds': ['Flute', 'Oboe', 'Clarinet']
}

class KeyError(Exception):
  def __init__(self, key):
    self.key = key
  
  def __str__(self) -> str:
      return f"Key {self.key} does not exist"

def print_instrument_families() -> None:
  # print out instrument families
  for family in ['Strings', 'Percussion', 'woodwinds']:
    try:
      print('Some instruments in the ' + family + 'family are: ' + ', '.join(instrument_familes[family]))
    except:
      raise KeyError(family)


print_instrument_families()
 