# Создайте класс Статья. Необходимо хранить следующую
# информацию:
# название статьи,
# автор статьи,
# количество знаков,
# название издания или сайта, где статья была
# впервые опубликована,
# краткое описание.
# Создайте необходимые методы для этого класса.
# Реализуйте паттерн MVC для класса Статья и код для
# использования модели, контроллера и представления.

class Article:
    def __init__(self, title, author, character_count, publication, description):
        self.title = title
        self.author = author
        self.character_count = character_count
        self.publication = publication
        self.description = description

    def get_summary(self):
        return f"{self.title} by {self.author} - {self.character_count} characters"

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nCharacter Count: {self.character_count}\nPublication: {self.publication}\nDescription: {self.description}"
    

class ArticleController:
    def __init__(self):
        self.articles = []

    def add_article(self, title, author, character_count, publication, description):
        article = Article(title, author, character_count, publication, description)
        self.articles.append(article)

    def get_articles(self):
        return self.articles

    def get_article_summary(self, index):
        if 0 <= index < len(self.articles):
            return self.articles[index].get_summary()
        return None
    

class ArticleView:
    def display_article(self, article):
        print(article)

    def display_article_summary(self, summary):
        print(summary)

    def display_all_articles(self, articles):
        for article in articles:
            print(article)
            print("-" * 40)
            

def main():
    controller = ArticleController()
    view = ArticleView()

    # Добавление статей
    controller.add_article("Python Basics", "John Doe", 1500, "Tech Magazine", "An introduction to Python programming.")
    controller.add_article("Advanced Python", "Jane Smith", 2000, "Code Journal", "Deep dive into Python's advanced features.")

    # Получение и отображение всех статей
    articles = controller.get_articles()
    view.display_all_articles(articles)

    # Получение и отображение краткого описания первой статьи
    summary = controller.get_article_summary(0)
    view.display_article_summary(summary)

if __name__ == "__main__":
    main()