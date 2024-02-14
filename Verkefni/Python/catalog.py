class Catalog:
    def __init__(self, name):
        self.name = name
        self.catalog = []

    def add(self, item):
        ''' Add the item if it's not already in the catalog '''
        if item not in self.catalog:
            self.catalog.append(item)

    def remove(self, item):
        ''' Remove's the inputted item if it's in the list '''
        if item in self.catalog:
            self.catalog.remove(item)

    def set_name(self, new_name):
        ''' Set's the name of the catalog as the inputted string '''
        self.name = new_name

    def clear(self):
        ''' Clears the list '''
        self.catalog = []
    def __str__(self) -> str:
        format_str = "Catalog {}:".format(self.name)
        for item in self.catalog:
            format_str += "\n\t{}".format(item)
        return format_str
