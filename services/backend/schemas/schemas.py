# from pydantic import BaseModel
# from typing import List, Union
#
# #All words
# # This can also be used if you want words for tests
# class Word(BaseModel):
#     """Create for every word in Book.words """
#     word_id: Union[int, None] = None #this field is optional
#     book_id: Union[int, None] = None #this field is optional
#     word_level: str
#     uk_word: str
#     en_word: str
#
#     class Config:
#         orm_mode = True
#
#
# #All books that user have read
# class Book(BaseModel):
#     book_id: Union[int, None] = None #this field is optional
#     user_id: Union[int, None] = None #this field is optional
#     book_name: str
#     book_author: str
#     words: List[Word] = []
#
#     class Config:
#         orm_mode = True
#
# #User settings
# class User_settings(BaseModel):
#     """User settings must be validated with this"""
#     user_name: str
#     email: str
#     native_lang: str
#     books: list[Book] = []
#
#     class Config:
#         orm_mode = True
