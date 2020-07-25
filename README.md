# Django Pytest Elasticsearch Example

When writing tests that interface with databases or distributed caches, I've
found that mocking the database/caches out tends to produce tests that are
brittle and offer very little value, because these mock-based tests usually fail
to capture the subtle nuances in behavior of the system under tests.

I've found that there's no substitute for testing against the real thing. While
Django offers a good story for
[testing against databases](https://docs.djangoproject.com/en/3.0/topics/testing/overview/#the-test-database),
I couldn't find any good examples of similar strategies for Elasticsearch.

So here is an example repo that demonstrates how to properly test code Python
that interface with Elasticsearch. We use Django and Pytest specifically in this
instance, but the general idea should readily extend to other languages and
frameworks.

Read more about the details here.
