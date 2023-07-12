"""
Title: Creating Database for Library Management using SQL database in Python
Developed by - @author: Shubham Lingayat  (https://github.com/shubhzz5/)

"""
import sqlite3
Mybooks = sqlite3.connect("books.db")
cursor_books = Mybooks.cursor()
cursor_books.execute("CREATE TABLE book_data (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT(20) NOT NULL, price REAL, number_books INTEGER)")
Mybooks.close()