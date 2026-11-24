from database.db import get_connection

class IssueDAO:
    
    def issue_book(self,book_id,member_id,issue_date,due_date):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return False
            cursor=con.cursor()
            query1="update books set available_copies=available_copies-1 where book_id=%s and available_copies>0"
            cursor.execute(query1,(book_id,))
            if cursor.rowcount==0:
                con.rollback()
                return False
            query2="insert into book_issues(book_id,member_id,issue_date,due_date) values(%s,%s,%s,%s)"
            values=(book_id,member_id,issue_date,due_date)
            cursor.execute(query2,values)
            con.commit()
            return True
        
        except Exception as e:
            print("Error issuing book:",e)
            if con:
                con.rollback()
            return False
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def display_all_issues(self):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return []
            cursor=con.cursor()
            query="select bi.issue_id,b.title,m.name,bi.issue_date,bi.due_date,bi.return_date,bi.fine from book_issues as bi inner join books as b on bi.book_id=b.book_id inner join members as m on bi.member_id=m.member_id"
            cursor.execute(query)
            result=cursor.fetchall()
            return result
        
        except Exception as e:
            print("Error displaying issued books:",e)
            return []
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def return_book(self,issue_id,return_date):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return False
            cursor=con.cursor()
            query1="select book_id,due_date from book_issues where issue_id=%s and return_date is NULL"
            cursor.execute(query1,(issue_id,))
            issue=cursor.fetchone()
            if issue is None:
                print("Active issue not found")
                return False
            
            book_id=issue[0]
            due_date=issue[1]
            
            late_days=(return_date-due_date).days
            fine=0
            if late_days>0:
                       fine=late_days*5
                       
            query2="update book_issues set return_date=%s,fine=%s where issue_id=%s"
            cursor.execute(query2,(return_date,fine,issue_id))
            
            query3="update books set available_copies=available_copies+1 where book_id=%s"
            cursor.execute(query3,(book_id,)) 
            con.commit() 
            
            print("Book returned successfully")
            print("Late days:",max(late_days,0))
            print("Fine: ₹",fine)
            
            return True
        
        except Exception as e:
            print("Error returning book:",e)
            if con:
                con.rollback()
            return False  
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()     
     
    def count_active_issues(self,member_id):
         
        con=None
        cursor=None
         
        try:
            con=get_connection()
            if con is None:
                return -1
            cursor=con.cursor()
            query="select count(*) from book_issues where member_id=%s and return_date is null"
            cursor.execute(query,(member_id,))
            result=cursor.fetchone()
            return result[0]
         
        except Exception as e:
            print("Error counting issues:",e)
            return -1
         
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
    
    def check_book_availability(self,book_id):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return None
            cursor=con.cursor()
            query="select available_copies from books where book_id=%s"
            cursor.execute(query,(book_id,))
            result=cursor.fetchone()
            return result
        
        except Exception as e:
            print("Error checking availability",e)
            return None
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()