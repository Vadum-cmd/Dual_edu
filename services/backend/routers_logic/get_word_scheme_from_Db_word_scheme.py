from sqlalchemy.orm import Session

from crud.crud_functions import get_user_profile
from schemas.schema import WordForVocabulary
from models.model import DB_word


def get_word_from_db_word(word: DB_word, user_id: int, db: Session) -> WordForVocabulary:
    user_language = get_user_profile(user_id=user_id, db=db).native_language
    if user_language == "Ukrainian":
        translation = word.uk_word
    else:
        translation = word.es_word
    new_word = WordForVocabulary(**{"word": word.en_word, "translation": translation, "word_level": word.word_level})
    return new_word