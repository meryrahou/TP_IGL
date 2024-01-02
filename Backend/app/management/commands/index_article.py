# yourappname/management/commands/index_articles.py
from django.core.management.base import BaseCommand
from elasticsearch.helpers import bulk
from ...models import Article
from ...index import ArticleIndex

class Command(BaseCommand):
    help = 'Index articles in Elasticsearch'

    def handle(self, *args, **options):
        ArticleIndex.init()  # Initialize the Elasticsearch index

        # Index all articles
        articles = Article.objects.all()
        actions = [
            {
                "_op_type": "index",
                "_index": "article_index",
                "_id": article.id,
                "_source": {
                    # Map model fields to Elasticsearch fields
                    "title": article.title,
                    "abstract": article.abstract,
                    "authors": ", ".join(str(author) for author in article.authors.all()),
                    "institutions": ", ".join(str(institution) for institution in article.institutions.all()),
                    "keywords": ", ".join(str(keyword) for keyword in article.keywords.all()),
                    "text": article.text,
                    "pdf_url": article.pdf_url,
                }
            }
            for article in articles
        ]

        # Get the Elasticsearch connection
        es = ArticleIndex._get_connection()

        # Bulk indexing
        success, failed = bulk(client=es, actions=actions,
                       stats_only=True)

        self.stdout.write(self.style.SUCCESS(f'Successfully indexed {success} articles'))
        self.stdout.write(self.style.ERROR(f'Failed to index {failed} articles'))
