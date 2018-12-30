import re

class Function:
    def validemail(self, email):
        if re.match("[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False

    def ToSeoFriendly(self, s, maxlen):
        t = '-'.join(s.split()) # join words with dashes
        u = ''.join([c for c in t if c.isalnum() or c=='-']) # remove punctation   
        return u[:maxlen].rstrip('-').lower() # clip to maxlen
