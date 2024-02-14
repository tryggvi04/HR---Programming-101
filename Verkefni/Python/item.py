class Item:
    def __init__(self, title, category):
        self.title = title
        self.category = category

    def set_category(self, new_category):
        ''' Change the name of the category by the input '''
        self.category = new_category

    def set_name(self, new_name):
        ''' Change the name of the film based on the input '''
        self.title = new_name

    def __str__(self) -> str:
        return "Name: {}, Category: {}".format(self.title, self.category)
 