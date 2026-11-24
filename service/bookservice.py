from dao.bookdao import BookDAO
from database.db import get_connection

class BookService:
    
    def __init__(self):
        self.dao=BookDAO()
        
    def add_book(self,book):
        
        if book.title=="":
            print("Book title cannot be emplty!")
            return False
        if book.author=="":
            print("Author name cannot be empty!")
            return False
        if book.price<=0:
            print("Price must be grater than zero!")
            return False
        if book.total_copies<=0:
            print("Total copies must be greater than zero!")
            return False
        
        book.available_copies=book.total_copies
        
        return self.dao.add_book(book)
    
    def display_all_books(self):
            
            con=None
            cursor=None
            
            try:
                con=get_connection()
                if con is None:
                    return []
                cursor=con.cursor()
                query="select * from books"
                cursor.execute(query)
                result=cursor.fetchall()
                return result
            
            except Exception as e:
                print("Error displaying books:",e)
                return []
            
            finally:
                if cursor:
                    cursor.close()
                if con:
                    con.close()
        
    def search_book_by_id(self,book_id):
        
        if book_id<=0:
            print("Invalid book ID")
            return False
        
        return self.dao.search_book_by_id(book_id)
                
    def search_book_by_title(self,title):
        
        if title=="":
            print("Please enter a book title")
            return []
        
        return self.dao.search_book_by_title(title)
    
    def update_book(self,book):
        
        if book.book_id<=0:
            print("Invalid book ID")
            return False
        if book.title=="" or book.author=="":
            print("Title and Auther cannot be empty")
            return False
        if book.price<=0:
            print("Price must be greater than zero")
            return False
        
        return self.dao.update_book(book)
    
    def delete_book(self,book_id):
        
        if book_id<=0:
            print("Invalid book Id")
            return False
        
        return self.dao.delete_book(book_id)