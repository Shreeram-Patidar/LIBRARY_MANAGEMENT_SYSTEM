from database.db import get_connection

class BookDAO:
    
    def add_book(self,book):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            
            if con is None:
                return False
            
            cursor=con.cursor()
            
            query="insert into books(title, author, category, price, total_copies, available_copies) values(%s,%s,%s,%s,%s,%s)"
            
            values=(book.title,book.author,book.category,book.price,book.total_copies,book.available_copies)
            
            cursor.execute(query,values)
            
            con.commit()
            
            return True
        
        except Exception as e:
            print("Error addding book:",e)
            if con:
                con.rollback()
            return False
        
        finally:
            if cursor:
                cursor.close()
                
            if con:
                con.close()
                
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
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return None
            
            cursor=con.cursor()
            
            query="select * from books where book_id = %s"
            
            cursor.execute(query,(book_id,))
            
            result=cursor.fetchone()
            
            return result
        
        except Exception as e:
            print("Error searching book:",e)
            return None
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def search_book_by_title(self,title):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return []
            
            cursor=con.cursor()
            
            query="select * from books where title like %s"
            
            cursor.execute(query,("%"+title+"%",))
            
            result=cursor.fetchall()
            
            return result
        
        except Exception as e:
            print("Error searching book:",e)
            return []
        
    def update_book(self,book):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return False
            
            cursor=con.cursor()
            
            query="update books set title=%s,author=%s,category=%s,price=%s where book_id=%s"
            
            values=(book.title,book.author,book.category,book.price,book.book_id)
            
            cursor.execute(query,values)
            
            if cursor.rowcount==0:
                return False
            
            con.commit()
            return True
        
        except Exception as e:
            print("Error updating book:",e)
            if con:
                con.rollback()
            return False
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def delete_book(self,book_id):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return False
            
            cursor=con.cursor()
            
            query="Delete from books where book_id=%s"
            
            cursor.execute(query,(book_id,))
            
            if cursor.rowcount==0:
                return False
            
            con.commit()
            return True
        
        except Exception as e:
            print("Error deleting book:",e)
            if con:
                con.rollback()
            return False
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()