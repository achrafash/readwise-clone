class Book:
    def __init__(self, title, author, highlights):
        self._title = title
        self._author = author
        self._highlights = highlights

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_highlights(self):
        return self._highlights

    def set_title(self, new_title):
        self._title = new_title
    
    def set_author(self, new_author):
        self._author = new_author
    
    def add_highlight(self, new_highlight):
        self._highlights.append(new_highlight)
