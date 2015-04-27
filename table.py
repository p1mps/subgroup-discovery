from column import Column
import arff


class Table():

    def __init__(self, fileData, target):

      #reading arff file
      self.arffFile = arff.load(open(fileData,'rb'))

      #target is the column's name target
      self.target = target

      #list of table's columns
      self.columns = list()
      self.column_names = list()
      
      #loading columns descriptions
      for attribute in self.arffFile['attributes']:
        self.columns.append(Column(attribute[0], attribute[1]))
        self.column_names.append(attribute[0])
        
      #loading data into columns
      for d in self.arffFile['data']:
        for idx,value in enumerate(d):
            self.columns[idx].add_value(value)

      #self.data is the "real" data
      self.data = self.arffFile['data']
                  
        
    def index_column(self, column_name):
      return self.column_names.index(column_name)
        
