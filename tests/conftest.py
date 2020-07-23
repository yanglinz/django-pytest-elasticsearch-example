import pytest
from django.conf import settings
from elasticsearch import Elasticsearch

from example.elasticsearch import MOVIE_MAPPING, SHOW_MAPPING

doc_types = {
    "movie": MOVIE_MAPPING,
    "show": SHOW_MAPPING,
}

ELASTICSEARCH_TEST_HOST = "http://elasticsearch_test:9200"


def setup_elasticsearch():
    es = Elasticsearch(ELASTICSEARCH_TEST_HOST)

    for doc_type, schema in doc_types.items():
        # Define index settings
        body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1,
                "index.store.type": "mmapfs",
            }
        }
        body["mappings"] = schema
        es.indices.create(index=doc_type, ignore=[], body=body)


def teardown_elasticsearch():
    es = Elasticsearch(ELASTICSEARCH_TEST_HOST)
    for doc_type in doc_types.keys():
        index_name = doc_type
        es.indices.delete(index=index_name)


@pytest.fixture
def elasticsearch(settings):
    settings.ELASTICSEARCH_HOST = ELASTICSEARCH_TEST_HOST

    setup_elasticsearch()
    yield Elasticsearch(ELASTICSEARCH_TEST_HOST)
    teardown_elasticsearch()
