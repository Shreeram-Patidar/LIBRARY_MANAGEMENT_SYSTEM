
from database.db import get_connection


class MemberDAO:

    def add_member(self, member):

        con = None
        cursor = None

        try:
            con = get_connection()
            if con is None:
                return False

            cursor = con.cursor()
            query="insert into members(name, email, phone, join_date) values(%s,%s,%s,%s)"
            values = (member.name,member.email,member.phone,member.join_date)
            cursor.execute(query, values)
            con.commit()
            return True

        except Exception as e:
            print("Error adding member:", e)
            if con:
                con.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def display_all_members(self):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return []
            
            cursor=con.cursor()
            query="select * from members"
            cursor.execute(query)
            result=cursor.fetchall()
            return result
        
        except Exception as e:
            print("Error displaying members:",e)
            return []
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def search_member_by_id(self, member_id):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return None
            
            cursor=con.cursor()
            query="select * from members where member_id=%s"
            cursor.execute(query,(member_id,))
            result=cursor.fetchone()
            return result
        
        except Exception as e:
            print("Error searching member:",e)
            return None
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def search_member_by_name(self,name):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return []
            
            cursor=con.cursor()
            query="select * from members where name like %s"
            cursor.execute(query,("%"+name+"%",))
            result=cursor.fetchall()
            return result
        
        except Exception as e:
            print("Error searching member:",e)
            return []
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def update_member(self,member):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return False
            
            cursor=con.cursor()
            query="update members set name=%s,email=%s,phone=%s where member_id=%s"
            values=(member.name,member.email,member.phone,member.member_id)
            cursor.execute(query,values)
            if cursor.rowcount==0:
                return False
            con.commit()
            return True
        
        except Exception as e:
            print("Error updating member:",e)
            if con:
                con.rollback()
            return False
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
                
    def delete_member(self,member_id):
        
        con=None
        cursor=None
        
        try:
            con=get_connection()
            if con is None:
                return False
            
            cursor=con.cursor()
            query="delete from members where member_id=%s"
            cursor.execute(query,(member_id,))
            if cursor.rowcount==0:
                return False
            con.commit()
            return True
        
        except Exception as e:
            print("Error deleting member:",e)
            if con:
                con.rollback()
            return False
        
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()