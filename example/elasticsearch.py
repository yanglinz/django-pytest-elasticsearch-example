from elasticsearch import Elasticsearch

from django.conf import settings


MOVIE_MAPPING = {
    "properties": {
        "id": {"type": "keyword"},
        "title": {"type": "text"},
        "description": {"type": "text"},
    }
}

SHOW_MAPPING = {
    "properties": {
        "id": {"type": "keyword"},
        "title": {"type": "text"},
        "description": {"type": "text"},
    }
}


def search_media(query):
    """Helper method to get movies and shows based on a search query
    """
    client = Elasticsearch(settings.ELASTICSEARCH_HOST)
    body = {"query": {"match_all": {}}}
    body = {
        "query": {
            "multi_match": {"query": query, "fields": ["title", "description"]}
        }
    }
    response = client.search(index=["movie", "show"], body=body)
    return [h["_source"] for h in response["hits"]["hits"]]
