from config import koneksi

# inisialisasi database
db = koneksi.connections()
cur = db.cursor()

class Beranda:

    # create post
    def createpost(self, judul, url, isi, kategori, id_user):

        cur.execute('INSERT INTO post(judul, url, isi, kategori, id_user) VALUES (%s, %s, %s, %s, %s)', \
        (judul, url, isi, kategori, id_user,))
        db.commit()

    # show post
    def showpost(self):
        query = cur.execute('SELECT * FROM post ORDER BY id DESC')
        result = cur.fetchall()

        return result

    # show post per id
    def showpostperid(self, id_post):
        query = cur.execute('SELECT * FROM post WHERE id = %s', (id_post,))
        result = cur.fetchall()

        return result

    # show post per url
    def showpostperurl(self, url):
        query = cur.execute('SELECT * FROM post WHERE url = %s', (url,))
        result = cur.fetchall()

        return result

    def editpost(self, judul, kategori, isi, id_post):
        cur.execute('UPDATE post SET judul = %s, kategori = %s, isi = %s WHERE id = %s', (judul, kategori, isi, id_post,))
        db.commit()

    # upload cover post
    def upload_cover(self, cover, id_post):
        cur.execute('UPDATE post SET cover = %s WHERE id = %s', (cover, id_post,))
        db.commit()

    # delete post
    def deletepost(self, id_post):
        cur.execute('DELETE FROM post WHERE id = %s', (id_post,))
        db.commit()

    # function check pass for used in edit password
    def check_pass(self, user):
        query = cur.execute('SELECT email, password FROM user WHERE email = %s', (user,))
        result = cur.fetchall()

        return result

    def change_pass(self, password, user):
        cur.execute('UPDATE user SET password = %s WHERE email = %s', (password, user,))
        db.commit()