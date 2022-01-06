from modules.Authentication import Authenticate 
class Fetcher:
    
    def get_books(num=50):
        cursor = Authenticate.session.cursor()
        cursor.execute(f"SELECT title,GROUP_CONCAT(author_book.name),image FROM book\
                    INNER JOIN author_book\
                    ON book.Id=author_book.Book\
                    GROUP BY book.Id\
                    LIMIT {num}")
        return cursor.fetchall()

