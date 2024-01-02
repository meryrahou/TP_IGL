from elasticsearch_dsl import Document, Text, Keyword, Date
from elasticsearch_dsl.connections import connections
from .models import Article

# Specify the complete Elasticsearch URL
connections.create_connection(hosts=['http://localhost:9200'])

class ArticleIndex(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    abstract = Text(analyzer='snowball')
    authors = Text(analyzer='snowball')
    institutions = Text(analyzer='snowball')
    keywords = Text(analyzer='snowball')
    text = Text(analyzer='snowball')
    pdf_url = Keyword()

    class Index:
        name = 'article_index'
