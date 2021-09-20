from datetime import datetime

class Destination():
    def __init__(self, name, description, currency, image):
        self.name = name
        self.description = description
        self.currency = currency
        self.image = image
        self.comments = list()
    
    def addComment(self, comment):
        self.comments.append(comment)




class Comment():
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.created_at = datetime.now()
