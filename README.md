Visada API Python Client
====================

This is the Python client for using the Visada API. You'll need to get an API key by [signing up](http://api.visada.io/signup).

Here's what you can do with the API:

* Review summarization: extract reasons why reviewers liked or didn't like the entity being reviewed. Here's an example of
a [review summary](http://api.visada.io/review_sets/552ef4c6db5f093b870180be/visualize) which summarizes the reviews
of this [suitcase at Amazon](http://www.amazon.com/Rockland-Luggage-Melbourne-Expandable-Turquoise/dp/B00CBT5F44/ref=lp_15743261_1_5?s=apparel&ie=UTF8&qid=1429140644&sr=1-5%27).
* Face blemish removal (coming soon)
* Makeup simulation (coming soon)



Initialization
--------------

```$ pip install requests
$ python setup.py install
$ python

import visada.client

# Instantiate the API object with your API key
api_client = visada.client.VisadaAPI(<YOUR API KEY>)
```



Usage - Review Summarization
----------------------------

```python
# Create a new review set - you'll refer to it via its review_set_id
review_set_id = api_client.create_review_set()

# Add reviews to the review set; here's an example of adding reviews.
# A single review consists of the text of the review, and the score assigned to the review.
# You'll want to add as many reviews as possible to get the best possible summary.

api_client.add_review_to_review_set(review_set_id, 'This suitcase was so-so.', rating=3)
api_client.add_review_to_review_set(review_set_id, 'This suitcase was amazing.', rating=5)
api_client.add_review_to_review_set(review_set_id, 'This suitcase was terrible.', rating=1)

# Once you've added all your reviews, start the summarization process

status = api_client.start_review_set_summarization(review_set_id)

# Poll the API until the summarization process is finished

while True:
    result = api_client.get_review_set_info(review_set_id)
    if result['status'] != 'processing':
        break
    else:
        time.sleep(5)


```

You can visualize the review summary via a special URL:

```python
    url = api_client.get_visualizer_url(review_set_id)
'''

Open the URL in your browser (just like the example above, [http://api.visada.io/review_sets/552ef4c6db5f093b870180be/visualize](http://api.visada.io/review_sets/552ef4c6db5f093b870180be/visualize)) to
see the result.
