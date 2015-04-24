from column import Column
import arff


class Table():

    def __init__(self, fileData, target):
      self.arffFile = arff.load(open(fileData,'rb'))
      self.target = target
      self.columns = list()
      for attribute in self.arffFile['attributes']:
        print 'attribute ' +  attribute[0]
        print 'domain ' + str(attribute[1])
        self.columns.append(Column(attribute[0], attribute[1]))
        
