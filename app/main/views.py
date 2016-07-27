from flask import render_template,url_for, redirect, g, flash
from . import main
from ..models import Category, Book
from .forms import SearchForm


@main.route('/', methods=['GET','POST'])
def index():
    form = SearchForm()
    g.matches = None
    if form.validate_on_submit():
        search_value = form.name.data
        g.matches = Book.search_for_book_by_name(search_value)
        form.name.data = ''
        if len(g.matches) == 0:
            flash('Not Found!')
        redirect(url_for('.index'))
    return render_template('index.html', form=form, matches=g.matches, name='Name')


@main.route('/category', methods=['GET','POST'])
def category():
    form = SearchForm()
    g.matches = None
    if form.validate_on_submit():
        search_value = form.name.data
        g.matches = Category.search_books_by_cateory(search_value)
        form.name.data = ''
        if g.matches is None:
            flash('Not Found!')
        redirect(url_for('.category'))
    return render_template('index.html', form=form, matches=g.matches, name='Category')


