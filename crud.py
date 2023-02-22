from sqlalchemy.orm import Session
from . import model, schemas


# create Book
def create_book(db: Session, book: schemas.Book):
    db_book = model.Book(book_id = book.book_id, 
                         user_id = book.user_id, 
                         book_name = book.book_name, 
                         book_author, 
                         words = book.words)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# vocabulary page (may also be used for "guest page: send")
# Right now it should return all words. 
# Because I don't see where it indicates that specific word is "unknown"
def get_words(db: Session, userid: int):
    return db.query(model.Book).filter(model.Book.user_id == userid).one().words


# create User
# In "model.py" in "user_table" there must be password column
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed" #TODO: hash password here
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# profile page
# Returns first User with user_id == userid
def get_user(db: Session, userid: int):
    return db.query(model.User).filter(model.User.user_id == userid).one()


# test your knowledge page 


# test your knowledge page "check"
