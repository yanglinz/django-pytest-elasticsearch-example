# Django Pytest Elasticsearch Example

## Intro

When writing tests that interface with databases or distributed caches, I've
found that mocking the database/caches out tends to produce tests that are
brittle and offer very little value, because these mock-based tests usually fail
to capture the subtle nuances in behavior of the system under tests.

I've found that there's no substitute for testing against the real thing. While
Django offers a good story for
[testing against databases](https://docs.djangoproject.com/en/3.0/topics/testing/overview/#the-test-database),
I couldn't find any good examples of similar strategies for Elasticsearch.

So here is an example repo that demonstrates how to properly test Python code
that interface with Elasticsearch. We use Django and Pytest specifically in this
instance, but the general idea should readily extend to other languages and
frameworks.

Read more about the details
[here](https://yanglinzhao.com/posts/test-elasticsearch-in-django).

## Running Locally

If you'd like to run the repo locally,
[`docker-compose`](https://docs.docker.com/compose/install/) is a requirement.
First build the docker image by running the following command:

```sh
docker-compose build
```

Next, run the example test inside a docker container:

```sh
docker-compose run web poetry run pytest tests
```
