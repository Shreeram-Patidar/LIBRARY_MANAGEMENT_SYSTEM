from dao.issuedao import IssueDAO
from dao.bookdao import BookDAO
from dao.memberdao import MemberDAO
from datetime import date, timedelta

class IssueService:
    
    def __init__(self):
        self.issue_dao=IssueDAO()
        self.book_dao=BookDAO()
        self.member_dao=MemberDAO()
        
    def issue_book(self,book_id,member_id):
        if book_id<=0:
            print("Invalid book Id")
            return False
        if member_id<=0:
            print("Invalid member Id")
            return False
        
        book=self.book_dao.search_book_by_id(book_id)
        
        if book is None:
            print("Book does not exist")
            return False
        
        member=self.member_dao.search_member_by_id(member_id)
        
        if member is None:
            print("Member does not exist")
            return False
        
        availability=self.issue_dao.check_book_availability(book_id)
        
        if availability is None:
            print("Unable to check book availablity")
            return False
        
        if availability[0]<=0:
            print("Book is currently unavailable")
            return False
        
        count=self.issue_dao.count_active_issues(member_id)
        
        if count==-1:
            print("Unable to check member issue limit")
            return False
        if count>=3:
            print("Member already has 3 active books")
            return False
        
        issue_date=date.today()
        due_date=issue_date+timedelta(days=14)
        
        return self.issue_dao.issue_book(book_id,member_id,issue_date,due_date)
    
    def display_all_issues(self):
        return self.issue_dao.display_all_issues()
    
    def return_book(self, issue_id):
        
        if issue_id<=0:
            print("Invalid issue ID")
            return False
        return self.issue_dao.return_book(issue_id,date.today())