class MusicAlbum:
    def __init__(self, band="unknown band", title="unknown", year="unknown year"):
        self.band = band
        self.title = title
        self.year = year
    def set_album(self, band, title, year):
        if band != None:
            self.band = band
        if title != None:
            self.title = title
        if year != None:
            self.year = year
    def __str__(self):
        return "Album {} by {}, released in {}.".format(self.title, self.band, self.year)