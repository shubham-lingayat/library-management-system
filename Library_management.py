"""
Title: Library Management System using SQL database in Python
Developed by - @author: Shubham Lingayat  (https://github.com/shubhzz5/)

"""
import sqlite3
Mybooks = sqlite3.connect("books.db")

num = int(input("Choose action from the list:\n\t1.Insert new books to the Record.\n\t2.Print all the Record."+
                "\n\t3.Add books to Purchase.\n\t4.Modify the Record.\n\t5.Delete the Books from the record.\n\t-->"))

# --- 1.Insert new books to the Record.
if num==1:
    more_books = "Y"
    while (more_books == "Y"):
        cursor_books = Mybooks.cursor()
        
        book_title = input("Enter the Book Title: ")
        book_author = input("Enter the Name of Book Author: ")
        book_price = float(input("Enter the Price of Book: "))
        book_number = int(input("Enter the number of books available: "))
        
        try:
            cursor_books.execute("INSERT INTO book_data (title, author, price, number_books) VALUES(?, ?, ?, ?);",(book_title, book_author, book_price, book_number)) 
            Mybooks.commit()
            print("One Record added Successfully.")
            
        except:
            print("Error in Operation.")
            Mybooks.rollback()
        more_books = input("\nDo you want to add more books to database?(Y/N): ")        
    Mybooks.close()

# --- 2.Print all the Record.
elif num==2:
    sql = "SELECT * FROM book_data;"
    
    cursor_books = Mybooks.cursor()
    cursor_books.execute (sql)
    while True:
        record = cursor_books.fetchone()
        if record == None:
            break
        print(record)
    
# --- 3.Add books to Purchase.
elif num==3: 
    more_books = "Y"
    m = 0
    while (more_books == "Y"):
        name = input("Book Title: ")
        sql = "SELECT * FROM book_data WHERE title = '"+ name +"';"
        
        cursor_books = Mybooks.cursor()
        cursor_books.execute(sql)
        
        record = cursor_books.fetchone()
        print(record)
        
        y = int(input("\nEnter number of copies: "))
        
        m = m + (record[3]*y)
        print("Total Cost: ",m)
        
        sql ="UPDATE book_data SET number_books = '"+ str(record[4]-y) +"'WHERE title = '"+ name +"';"
        
        try:
            cursor_books.execute(sql)
            Mybooks.commit()
            print("Successfully update value of available books number")
            
        except:
            print("Error in update value of available books number")
            Mybooks.rollback()
            
        more_books = input("\nDo you want to add more books to purchase?(Y/N): ")
 
# --- 4.Modify the Record.
elif num==4:
    more_books = "Y"
    m = 0
    while (more_books == "Y"):
        name = input("Book Title: ")
        sql = "SELECT * FROM book_data WHERE title = '"+ name +"';"
        
        cursor_books = Mybooks.cursor()
        cursor_books.execute(sql)
        
        record = cursor_books.fetchone()
        print(record)
        
        y = int(input("\nEnter the number of available copies: "))
                
        sql ="UPDATE book_data SET number_books = '"+ str(y) +"'WHERE title = '"+ name +"';"
        
        try:
            cursor_books.execute(sql)
            Mybooks.commit()
            print("Successfully update value of available books number")
            
        except:
            print("Error in update value of available books number")
            Mybooks.rollback()
            
        more_books = input("\nDo you want to modify more books?(Y/N): ")
        
# --- 5.Delete the Books from the record.
elif num==5:
    more_books = "Y"
    m = 0
    while (more_books == "Y"):
        name = input("Book Title: ")
        sql = "SELECT * FROM book_data WHERE title = '"+ name +"';"
        
        cursor_books = Mybooks.cursor()
        cursor_books.execute(sql)
        
        record = cursor_books.fetchone()
        print(record)
                        
        sql ="DELETE FROM book_data WHERE title = '"+ name +"';"
        
        try:
            cursor_books.execute(sql)
            Mybooks.commit()
            print("Successfully deleted the book from the record.")
            
        except:
            print("Error to delete book from the record.")
            Mybooks.rollback()
            
        more_books = input("\nDo you want to delete more books?(Y/N): ")
    
else:
    print("Please enter the right choice number.")