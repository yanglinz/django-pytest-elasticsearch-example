import pytest
from django.conf import settings
from elasticsearch import Elasticsearch

from example.elasticsearch import MOVIE_MAPPING, SHOW_MAPPING

doc_types = {
    "movie": MOVIE_MAPPING,
    "show": SHOW_MAPPING,
}

test_elasticsearch_host = "http://elasticsearch_test:9200"


def setup_elasticsearch():
    es = Elasticsearch(TEST_ES_HOST)

    for doc_type, mapping_schema in doc_types.items():
        # Create the index
        index_name = "{}_{}".format(settings.ELASTICSEARCH_INDEX_PREFIX, doc_type)
        body = schema.BASE_SCHEMA
        body["settings"]["number_of_shards"] = 1
        body["settings"]["number_of_replicas"] = 1
        body["settings"]["index.store.type"] = "mmapfs"
        es.indices.create(index=index_name, ignore=400, body=body)

        # Update index with specific mapping
        es.indices.put_mapping(index=index_name, doc_type=doc_type, body=mapping_schema)


def teardown_elasticsearch():
    es = Elasticsearch(TEST_ES_HOST)
    for doc_type in doc_types.keys():
        index_name = "{}_{}".format(settings.ELASTICSEARCH_INDEX_PREFIX, doc_type)
        es.indices.delete(index=index_name)


@pytest.fixture
def elasticsearch(settings):
    settings.ELASTICSEARCH_DATA_STORE_HOST = TEST_ES_HOST

    setup_elasticsearch()
    yield Elasticsearch(TEST_ES_HOST)
    teardown_elasticsearch()
