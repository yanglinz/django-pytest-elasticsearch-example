from example.elasticsearch import search_media


def index_test_fixtures(es, index_name, data):
    created = es.index(index=index_name, body=data)
    assert created["result"] == "created"
    es.indices.refresh(index_name)


class TestElasticsearch:
    def test_elasticsearch(self, elasticsearch):
        # Setup test fixtures
        index_test_fixtures(
            elasticsearch,
            "movie",
            {
                "title": "American Psycho",
                "description": "A wealthy New York City investment banking executive, Patrick Bateman, hides his alternate psychopathic ego from his co-workers and friends as he delves deeper into his violent, hedonistic fantasies.",
            },
        )
        index_test_fixtures(
            elasticsearch,
            "show",
            {
                "title": "The Wire",
                "description": "The Wire is an American crime drama television series created and primarily written by author and former police reporter David Simon.",
            },
        )
        index_test_fixtures(
            elasticsearch,
            "show",
            {
                "title": "Breaking Bad",
                "description": "Breaking Bad is an American neo-Western crime drama television series created and produced by Vince Gilligan.",
            },
        )

        # Make assertions
        results = search_media("American")
        assert results == [1]
