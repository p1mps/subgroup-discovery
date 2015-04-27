


class Column():
    def __init__(self, name, domain):
      self.name = name
      self.domain = domain
      self.values = list()

    def add_value(self, value):
      self.values.append(value)


    def print_column(self):
      print "column: " + self.name
      for value in self.values:
          print value

    
