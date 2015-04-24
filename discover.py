import argparse
from table import Table
from quality import Quality

class Discovery():

    def __init__(self):
        """
        target -> number
        data -> file
        """
        self.parser = argparse.ArgumentParser(description='Python Subgroup Discovery Tool')
        self.parser.add_argument('target', metavar='t', type=int,
                            help='target column')
        self.parser.add_argument('data', metavar='f',
                                 help='data file')
        self.args = self.parser.parse_args()
        self.data = self.args.data
        self.target = self.args.target
        self.table = Table(self.data, self.target)
        self.quality = Quality()

        
    def load_data(self):
        pass

    def SD(self):
        pass







if __name__ == "__main__":
    discovery = Discovery()


