import argparse
from table import Table
from quality import Quality
from subgroup import Subgroup

class Discovery():

    def __init__(self):
        """
        target -> number
        data -> file
        """
        self.parser = argparse.ArgumentParser(description='Python Subgroup Discovery Tool')
        self.parser.add_argument('target', metavar='t',
                            help='target column')
        self.parser.add_argument('data', metavar='f',
                                 help='data file')
        self.args = self.parser.parse_args()
        self.data = self.args.data
        self.target = self.args.target
        self.quality = Quality()
        self.table = Table(self.data, self.target)
        self.target_index = self.table.index_column(self.target)

        
    def SD(self):
      for column in self.table.columns:
        for value in column.domain:
          subgroup = Subgroup(self.target_index)
          subgroup.binary_set_column(column, value)
          subgroup.print_subgroup()
          subgroup.generate_items(self.table.data)
          subgroup.compute_quality()



if __name__ == "__main__":
    discovery = Discovery()
    discovery.SD()


