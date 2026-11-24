class Issue:
    
    def __init__(self,issue_id,book_id,member_id,issue_date,due_date,return_date,fine):
        
        self.issue_id=issue_id
        self.book_id=book_id
        self.member_id=member_id
        self.issue_date=issue_date
        self.due_date=due_date
        self.return_date=return_date
        self.fine=fine