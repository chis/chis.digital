from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from datetime import datetime
# custom function
from app.generate_unique_list import generate_unique_list

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            post = Post(body=form.post.data, title=form.title.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your post is now live!')
            return redirect(url_for('index'))
        else:
            flash("Illegal action!")
            return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Home', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)

@app.route('/a', methods=['GET', 'POST'])
def a():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('a'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('a.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


    
@app.route('/edit_post/<id>/', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.post.data
        post.title = form.title.data
        db.session.commit()
        flash("Changes made")
        return redirect(url_for('index'))
    elif request.method == "GET":
        form.post.data = post.body
        form.title.data = post.title
    return render_template('edit_post.html', title='Edit Post: {}'.format(post.title), form=form)


@app.route('/delete_post/<id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/post/<id>')
def view_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    if post == None:
        redirect(url_for('index'))
    return render_template('view_post.html', title=post.title, post=post)

        
@app.route('/archive', methods=['GET', 'POST'])
def archive():
    posts = Post.query.order_by(Post.id.desc()).all()
    each_post_as_year = []
    for post in posts:
        each_post_as_year.append(post.timestamp.strftime('%Y'))
    each_year = generate_unique_list(each_post_as_year)
    return render_template('archive.html', title='Archives', years=each_year)