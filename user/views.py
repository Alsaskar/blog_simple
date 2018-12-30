from flask import render_template, session, flash, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import user
from models import users, beranda
from config import function
import os, sys, re
from werkzeug.utils import secure_filename

datauser = users.Users()
fct = function.Function()
brd = beranda.Beranda()

UPLOAD_FOLDER = 'static/library/image/cover_post/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_CONFIG = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@user.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    # check, if the user hasn't logged in, then
    if 'user' not in session:
        # user can't access in page this
        flash("You must login.", 'error')
        return redirect('/login')

    # get data user who is logged in
    getuser = datauser.userLogged(session['user'])

    if request.method == 'POST':
        judul = request.form['judul']
        kategori = request.form['kategori']
        isi = request.form['isi']
        url = fct.ToSeoFriendly(judul, 200)
        id_user = getuser[0][0]

        if judul == '':
            flash('Judul cannot be empty', 'error')
        elif kategori == '':
            flash('Kategori cannot be empty', 'error')
        else:
            brd.createpost(judul, url, isi, kategori, id_user)
            flash('Post success create.', 'success')
        return redirect(url_for('user.dashboard'))
    else:
        return render_template('user/dashboard.html', title='Dashboard User', getuser=getuser)

@user.route('/data/post')
def data_post():
    # check, if the user hasn't logged in, then
    if 'user' not in session:
        # user can't access in page this
        flash("You must login.", 'error')
        return redirect('/login')

    # get data user who is logged in
    getuser = datauser.userLogged(session['user'])

    # show data post
    getpost = brd.showpost()

    return render_template('user/data_post.html', title='Data Post', getuser=getuser, getpost=getpost)

# edit post
@user.route('/edit/post/<int:id_post>', methods=['GET', 'POST'])
def edit_post(id_post):
    # check, if the user hasn't logged in, then
    if 'user' not in session:
        # user can't access in page this
        flash("You must login.", 'error')
        return redirect('/login')

    # get data user who is logged in
    getuser = datauser.userLogged(session['user'])

    # show post per id
    getpost = brd.showpostperid(id_post)

    if request.method == 'POST':

        judul = request.form['judul']
        kategori = request.form['kategori']
        isi = request.form['isi']

        if judul == '':
            flash('Judul cannot be empty', 'error')
        elif kategori == '':
            flash('Kategori cannot be empty', 'error')
        else:
            brd.editpost(judul, kategori, isi, id_post)
            flash('Post success edited.', 'success')
            redirect(url_for('user.data_post'))

    return render_template('user/edit_post.html', title='Edit Post', getuser=getuser, getpost=getpost)

# upload cover post
@user.route('/cover/post/<int:id_post>', methods=['GET', 'POST'])
def cover_post(id_post):
    # check, if the user hasn't logged in, then
    if 'user' not in session:
        # user can't access in page this
        flash("You must login.", 'error')
        return redirect('/login')

    # get data user who is logged in
    getuser = datauser.userLogged(session['user'])

    # show post per id
    getpost = brd.showpostperid(id_post)

    if request.method == 'POST':
        cover = request.files['cover']

        if cover and allowed_file(cover.filename):
            filename = secure_filename(cover.filename)
            cover.save(os.path.join(UPLOAD_CONFIG, filename))

            # upload cover to database
            brd.upload_cover(filename, id_post)

            flash('Cover post has been upload', 'success')
            return redirect(url_for('user.data_post'))
        else:
            flash('Image should jpg or png', 'error')

    return render_template('user/cover_post.html', title='Upload Cover Post', getuser=getuser, getpost=getpost)

# delete post
@user.route('/delete/post/<int:id_post>')
def delete_post(id_post):

    # check, if the user hasn't logged in, then
    if 'user' not in session:
        # user can't access in page this
        flash("You must login.", 'error')
        return redirect('/login')
    
    brd.deletepost(id_post)

    flash('Post has been deleted', 'success')
    return redirect(url_for('user.data_post'))

@user.route('/edit/password', methods=['GET', 'POST'])
def edit_password():
    # check, if the user hasn't logged in, then
    if 'user' not in session:
        # user can't access in page this
        flash("You must login.", 'error')
        return redirect('/login')

    # get data user who is logged in
    getuser = datauser.userLogged(session['user'])

    if request.method == 'POST':
        old_pass = request.form['old_pass']
        new_pass = request.form['new_pass']
        reply_new_pass = request.form['reply_new_pass']

        check_pass = brd.check_pass(session['user'])

        if check_password_hash(check_pass[0][1], old_pass):
            if new_pass != reply_new_pass:
                flash('New Password is not same with Reply Password', 'error')
                return redirect(url_for('user.edit_password'))
            else:
                brd.change_pass(generate_password_hash(new_pass), session['user'])
                flash('Password success is changes. Please login again', 'success')

                # auto logout
                # delete session
                session.pop('user', None)

                return redirect('/login')
        else:
            flash('Old Password is wrong', 'error')
            return redirect(url_for('user.edit_password'))
    else:
        return render_template('user/edit_password.html', title='Edit Password', getuser=getuser)

@user.route('/logout')
def logout():
	# delete session
	session.pop('user', None)
	flash('You success logout. Thanks has been use this application.', 'success')
	return redirect('/login')
