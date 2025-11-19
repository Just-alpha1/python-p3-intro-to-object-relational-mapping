from model import Model

class School(Model):
    table_name = 'schools'

    def __init__(self, name=None, location=None, **kwargs):
        super().__init__(name=name, location=location, **kwargs)
