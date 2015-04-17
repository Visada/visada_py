import visada.client
import time

API_KEY = <Your API Key Here>

review_file = 'example_data/lens_reviews.txt'

# Instantiate the API object with your API key
api_client = visada.client.VisadaAPI(API_KEY)

# Create a new review set - you'll refer to it via its review_set_id
review_set_id = api_client.create_review_set()
print 'Using Review Set: %s'%review_set_id

# Read in reviews from example text file:
with open(review_file, 'r') as f:
    doc = f.readlines()
    review_rating = map(float, doc[::2])
    review_text = doc[1::2]
    reviews = zip(review_text, review_rating)


# Add reviews to the review set
print 'Adding Reviews'
for text,rating in reviews:
    api_client.add_review_to_review_set(review_set_id, text.replace('\n',''), rating)


info = api_client.get_review_set_info(review_set_id)
print 'Added %d Reviews, Beginning Processing'%(info['n_reviews'])

# Begin Summarization process
# this may take a few minutes depending on the number and length of the reviews
api_client.start_review_set_summarization(review_set_id)

#Poll the API until the summarization process is finished
while True:
    result = api_client.get_review_set_info(review_set_id)
    if result['status'] != 'processing':
        break
    else:
        time.sleep(5)

if result['status'] == 'done':
    print 'Summary Complete'
    print 'View at %s'%api_client.get_visualizer_url(review_set_id)
    print "Or inspect the result['result'] dictionary variable directly"
elif result['status'] == 'error':
    print 'An Error Occurred: %s'%result['error']

