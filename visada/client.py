import requests, json

API_HOST='http://api.visada.io/'

class VisadaAPI(object):

    def __init__(self, api_key):
        """
        Initialize the Visada API object with your API key.

        :param api_key: Obtain an API key at http://api.visada.io/signup .
        :return:
        """

        self.api_key = api_key
        self.request_headers = {'X-Visada-Api-Key':self.api_key}

    def create_review_set(self):
        """
        Creates a new review set.

        :return: review set ID (a string)
        """

        api_endpoint = API_HOST + 'review_sets'

        response = requests.post(api_endpoint, headers=self.request_headers)

        review_set_id = response.json()['review_set_id']

        return review_set_id


    def __add_review_chunk(self, review_set_id, review_chunk):
        add_reviews_url = API_HOST + 'review_sets/' + review_set_id
        payload = {'reviews':json.dumps(review_chunk)}

        response = requests.post(add_reviews_url, data=payload, headers=self.request_headers)
        return response.json()


    def add_review_to_review_set(self, review_set_id, review_text, review_rating):
        """
        Adds a review to a review set
        :param review_set_id: (string) review set ID obtained from create_review_set
        :param review_text: (string) text of the review
        :param review_rating: (float) rating associated with the review, e.g. 3
        :return:
        """
        return self.__add_review_chunk(review_set_id, [{'text':review_text, 'rating': review_rating}])


    def start_review_set_summarization(self, review_set_id):
        """
        Initiates review set summarization. Use this method after you have added reviews to your review set. Poll
        get_review_set_info to find out when the process has finished.
        :param review_set_id: (string) review set ID
        :return: status of the summarization process
        """
        response = requests.post(API_HOST + 'review_sets/%s/summarize' % review_set_id,
                                headers=self.request_headers)

        return response.json()


    def get_review_set_info(self, review_set_id):
        """
        Retrieves information about the review set, including the summary.
        :param review_set_id:
        :return:
        """
        response = requests.get(API_HOST + 'review_sets/' + review_set_id, headers=self.request_headers)
        return response.json()
