Visada API Python Client
====================

This is the Python client for using the Visada API. You'll need to get an API key by [signing up](http://api.visada.io/signup).

Here's what you can do with the API:

* Review summarization: extract reasons why reviewers liked or didn't like the entity being reviewed. Here's an example of
a [review summary](http://api.visada.io/review_sets/552ef4c6db5f093b870180be/visualize) which summaries the reviews
of this [suitcase at Amazon](http://www.amazon.com/Rockland-Luggage-Melbourne-Expandable-Turquoise/dp/B00CBT5F44/ref=lp_15743261_1_5?s=apparel&ie=UTF8&qid=1429140644&sr=1-5%27).
* Face blemish removal (coming soon)
* Makeup simulation (coming soon)



Initialization
--------------

```python
import visada.client

# Instantiate the API object with your API key
api_client = visada.client.VisadaAPI(<YOUR API KEY>)
```



Usage - Review Summarization
----------------------------

```python
# Create a new review set - you'll refer to it via its review_set_id
review_set_id = api_client.create_review_set()

# Add reviews to the review set; here's are examples of adding reviews.
# A single review consists of the text of the review, and the score assigned to the review.
# You'll want to add as many reviews as possible to get the best possible summary.

api_client.add_review(review_set_id, 'This suitcase was so-so.', 3)
api_client.add_review(review_set_id, 'This suitcase was amazing.', 5)
api_client.add_review(review_set_id, 'This suitcase was terrible.', 1)

# Once you've added all your reviews, start the summarization process

status = api_client.start_review_set_summarization_process(review_set_id)

# Poll the API until the summarization process is finished

while True:
    result = api_client.get_review_set_info(review_set_id)
    if result['status'] != 'processing':
        break
    else:
        time.sleep(5)


```


