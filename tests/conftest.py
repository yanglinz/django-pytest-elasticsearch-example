import pytest
from django.conf import settings
from elasticsearch import Elasticsearch

from example.elasticsearch import MOVIE_MAPPING, SHOW_MAPPING

schemas = {
    "movie": MOVIE_MAPPING,
    "show": SHOW_MAPPING,
}

ELASTICSEARCH_TEST_HOST = "http://elasticsearch_test:9200"


def setup_elasticsearch():
    es = Elasticsearch(ELASTICSEARCH_TEST_HOST)
    for index_name, schema in schemas.items():
        body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1,
                "index.store.type": "mmapfs",
            },
            "mappings": schema,
        }
        es.indices.create(index=index_name, body=body)


def teardown_elasticsearch():
    es = Elasticsearch(ELASTICSEARCH_TEST_HOST)
    for index_name in schemas.keys():
        es.indices.delete(index=index_name)


@pytest.fixture
def elasticsearch(settings):
    settings.ELASTICSEARCH_HOST = ELASTICSEARCH_TEST_HOST

    setup_elasticsearch()
    yield Elasticsearch(ELASTICSEARCH_TEST_HOST)
    teardown_elasticsearch()
