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
                "slug": "episode-5",
                "title": "Star Wars: Episode V - The Empire Strikes Back",
                "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy.",
            },
        )
        index_test_fixtures(
            elasticsearch,
            "movie",
            {
                "slug": "episode-3",
                "title": "Star Wars: Episode III - Revenge of the Sith",
                "description": "Three years into the Clone Wars, the Jedi rescue Palpatine from Count Dooku. As Obi-Wan pursues a new threat, Anakin acts as a double agent between the Jedi Council and Palpatine and is lured into a sinister plan to rule the galaxy.",
            },
        )
        index_test_fixtures(
            elasticsearch,
            "movie",
            {
                "slug": "rouge-one",
                "title": "Rogue One: A Star Wars Story",
                "description": "The daughter of an Imperial scientist joins the Rebel Alliance in a risky move to steal the Death Star plans.",
            },
        )

        index_test_fixtures(
            elasticsearch,
            "show",
            {
                "slug": "clone-wars",
                "title": "Star Wars: The Clone Wars",
                "description": "Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.",
            },
        )
        index_test_fixtures(
            elasticsearch,
            "show",
            {
                "slug": "the-mandalorian",
                "title": "The Mandalorian",
                "description": "The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.",
            },
        )

        # Test search helper
        results = search_media("Star Wars")
        results = {r["slug"] for r in results}
        assert results == {"episode-5", "episode-3", "rouge-one", "clone-wars"}

        results = search_media("Jedi")
        results = {r["slug"] for r in results}
        assert results == {"episode-5", "episode-3", "clone-wars"}

        results = search_media("Galaxy")
        results = {r["slug"] for r in results}
        assert results == {"episode-5", "episode-3", "the-mandalorian"}
