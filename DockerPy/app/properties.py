from jproperties import Properties


class AppProperties:
        

    def __init__(self):
    
        self.p = Properties()
        self._read_from_file('application.properties')
        

    def _read_from_file(self, path):

        with open(path, 'rb') as f:
            self.p.load(f)

        

