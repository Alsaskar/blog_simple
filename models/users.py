from config import koneksi

# inisialisasi database
db = koneksi.connections()
cur = db.cursor()

class Users:

    def __init__(self):
        # protected (for object register)
        self._firstname = None
        self._lastname = None
        self._email = None
        self._password = None
    
    def register(self, firstname, lastname, email, password):
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password

        cur.execute('INSERT INTO user(firstname, lastname, email, password) VALUES (%s, %s, %s, %s)', (\
                    self._firstname, self._lastname, self._email, self._password,))
        db.commit()

    def login(self, email):
        self._email = email

        query = cur.execute('SELECT email, password FROM user WHERE email = %s', (self._email,))
        result = cur.fetchall()

        if query > 0: # if data exists in database, then
            # return variabel result for get data in database
            return result
        else:
            # return value True for check condition (used for get callback message to user)
            return True

    def userLogged(self, loggedIn):
        query = cur.execute('SELECT * FROM user WHERE email = %s', (loggedIn,))
        result = cur.fetchall()

        return result
