



class Subgroup():

  def __init__(self, target_index):
    self.description = ""
    self.items = list()
    self.target_index = target_index
    self.binary_values = list()
    


  def binary_set_column(self, column, value):
    binary_set = ""
    for v in column.values:
      if(v == value):
        binary_set += "1"
      else:
        binary_set += "0"

    self.set_description(column.name, value)
    self.binary_set = binary_set

  def set_description(self, column_name, value):

    if(self.description != ""):
      self.description += "AND " + column_name + "=" + value

    self.description = column_name + "=" + value


  def print_subgroup(self):
    print self.description


  def generate_items(self, data):
    for idx,d in enumerate(data):
      if(self.binary_set[idx] == "1"):
        self.items.append(d)

  




  def compute_quality(self):
    positive = 0
    negative = 0
    for item in self.items:
      if(item[self.target_index] == "1"):
        positive = positive + 1
      else:
        negative = negative + 1

    print positive, negative
