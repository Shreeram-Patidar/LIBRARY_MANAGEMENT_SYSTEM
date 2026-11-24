
from dao.memberdao import MemberDAO

class MemberService:

    def __init__(self):
        self.dao = MemberDAO()

    def add_member(self, member):
        
        if member.name.strip()=="":
            print("Member name cannot be empty")
            return False
        if member.email.strip()=="":
            print("Email cannot be empty")
            return False
        if member.phone.strip()=="":
            print("Phone number cannot be empty")
            return False
        if len(member.phone)!=10 or not member.phone.isdigit():
            print("Enter a valid 10-digit phone number")
            return False
        return self.dao.add_member(member)

    def display_all_members(self):
        return self.dao.display_all_members()
    
    def search_member_by_id(self, member_id):
        if member_id<=0:
            print("Invalid member ID")
            return None
        return self.dao.search_member_by_id(member_id)

    def search_member_by_name(self, name):
        if name.strip()=="":
            print("Please enter a member name")
            return []
        return self.dao.search_member_by_name(name)

    def update_member(self, member):

        if member.member_id<=0:
            print("Invalid member ID")
            return False
        if member.name.strip()=="" or member.email.strip()=="":
            print("Name and email cannot be empty")
            return False
        if len(member.phone)!=10 or not member.phone.isdigit():
            print("Enter a valid 10-digit phone number")
            return False
        return self.dao.update_member(member)

    def delete_member(self, member_id):

        if member_id<=0:
            print("Invalid member ID")
            return False
        return self.dao.delete_member(member_id)
