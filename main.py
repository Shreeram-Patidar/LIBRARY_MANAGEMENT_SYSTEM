from models.book import Book
from models.member import Member

from service.bookservice import BookService
from service.memberservice import MemberService
from service.issueservice import IssueService

from datetime import date

book_service=BookService()
member_service=MemberService()
issue_service=IssueService()

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Book Management")
    print("2. Member Management")
    print("3. Issue & Return Management")
    print("4. Exit")
    
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        while True:
            
            print("\n========== BOOK MANAGEMENT ==========")
            print("1. Add Book")
            print("2. Display All Books")
            print("3. Search Book By ID")
            print("4. Search Book By Title")
            print("5. Update Book")
            print("6. Delete Book")
            print("7. Back to Main Menu") 
           
            ch=int(input("Enter your choice:"))
            if ch==1:
                title=input("Enter book title:")
                author=input("Enter author name:")
                category=input("Enter category:")
                price=float(input("Enter price:"))
                total=int(input("Enter total copies:"))
               
                book=Book(None,title,author,category,price,total,total)
                result=book_service.add_book(book)
                if result:
                    print("Book added successfully")
                else:
                    print("Book addition failed")
                    
            elif ch==2:
                books=book_service.display_all_books()
                if books:
                    print("\n---------- BOOK LIST ----------")
                    for book in books:
                        print(book)
                else:
                    print("No books found")
            
            elif ch==3:
                book_id=int(input("Enter book ID:"))
                book=book_service.search_book_by_id(book_id)
                if book:
                    print("Book found",book)
                else:
                    print("Book not found")
            
            elif ch==4:
                title=input("Enter book title:")
                books=book_service.search_book_by_title(title)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No matching books found")
                    
            elif ch==5:
                book_id=int(input("Enter book ID to update:"))
                old_book=book_service.search_book_by_id(book_id)
                if old_book:
                    title = input("Enter new title: ")
                    author = input("Enter new author: ")
                    category = input("Enter new category: ")
                    price = float(input("Enter new price: "))
                    
                    book=Book(book_id,title,author,category,price,old_book[5],old_book[6])
                    result=book_service.update_book(book) 
                    if result:
                        print("Book updated successfully")
                    else:
                        print("Book update failed")
                        
                else:
                    print("Book not found")
                    
            elif ch==6:
                book_id=int(input("Enter book ID to delete:"))
                result=book_service.delete_book(book_id)
                if result:
                    print("Book deleted successfully")
                else:
                    print("Book deletion failed")
            
            elif ch==7:
                break
            
            else:
                print("Invaild choice")
                
    elif choice==2:
        while True:
            print("\n========== MEMBER MANAGEMENT ==========")
            print("1. Register Member")
            print("2. Display All Members")
            print("3. Search Member By ID")
            print("4. Search Member By Name")
            print("5. Update Member")
            print("6. Delete Member")
            print("7. Back to Main Menu")
            
            ch=int(input("Enter your choice:"))
            
            if ch==1:
                name=input("Enter member name:")
                email=input("Enter email:")
                phone=input("Enter phone number:")
                
                member=Member(None,name,email,phone,date.today())
                result=member_service.add_member(member)
                
                if result:
                    print("Member registerd successfully")
                else:
                    print("Member registration failed")
            
            elif ch==2:
                members=member_service.display_all_members()
                if members:
                    print("\n---------- MEMBER LIST ----------")
                    for member in members:
                        print(member)
                else:
                    print("No members found")
            
            elif ch==3:
                member_id=int(input("Enter member ID:"))
                member=member_service.search_member_by_id(member_id)
                if member:
                    print("Member found:",member)
                else:
                    print("Member not found")
                
            elif ch==4:
                name=input("Enter member name:")
                members=member_service.search_member_by_name(name)
                if members:
                    for member in members:
                        print(member)
                else:
                    print("No matching members found")
                
            elif ch==5:
                member_id=int(input("Enter member ID to update:"))
                old_member=member_service.search_member_by_id(member_id)
                if old_member:
                    name=input("Enter new name:")
                    email=input("Enter your email:")
                    phone=input("Enter new phone:")
                    member=Member(member_id,name,email,phone,old_member[4])
                    result=member_service.update_member(member)
                    if result:
                        print("Member updated successfully")
                    else:
                        print("Member update failed")
                
                else:
                    print("Member not found")
            
            elif ch==6:
                member_id=int(input("Enter member ID to delete:"))
                result=member_service.delete_member(member_id)
                if result:
                    print("Member deleted successfully")
                else:
                    print("Member deletion failed")
                    
            elif ch==7:
                break
            
            else:
                print("Invalid choice")
                
    elif choice==3:
        while True:
            print("\n========== ISSUE & RETURN MANAGEMENT ==========")
            print("1. Issue Book")
            print("2. Display All Issues")
            print("3. Return Book")
            print("4. Back to Main Menu")
            
            ch=int(input("Enter your choice:"))
            
            if ch==1:
                book_id=int(input("Enter book ID:"))
                member_id=int(input("Enter member ID:"))
                result=issue_service.issue_book(book_id,member_id)
                if result:
                    print("Book issued successfully")
                else:
                    print("Book issue failed")
                    
            elif ch==2:
                issues=issue_service.display_all_issues()
                if issues:
                    print("\n---------- ISSUE LIST ----------")
                    
                    for issue in issues:
                        print(issue)
                else:
                    print("No issue record found")
                    
            elif ch==3:
                issue_id=int(input("Enter issue ID:"))
                result=issue_service.return_book(issue_id)
                if result:
                    print("Book returned successfully")
                else:
                    print("Book return failed")
            
            elif ch==4:
                break
            
            else:
                print("Invalid choice")
    elif choice==4:
        break
    else:
        print("Invalid Choice!")