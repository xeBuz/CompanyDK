import sys
from flask import jsonify, request

if sys.version_info >= (3, 0):
    from http.client import responses as http_code
else:
    from httplib import responses as http_code


class BaseController(object):

    def __init__(self):
        self.json = {}
        self.success = False

    def _set_success(self, code):
        """
        Set self.success depending of the status code.
        False should be a Client Error or a Server Error response

        :param code: HTTP status code
        """
        self.success = True if code < 400 else False
        self.json['success'] = self.success

    def _set_status(self, code):
        """
        Set the status property, with code and message

        :param code: HTTP status code
        """
        self.json['status'] = {
            'code': code,
            'message': http_code.get(code, None)
        }

    def _set_data(self, data):
        """
        Set the data property. It could be 'data' for valid responses or 'error' for errors

        :param data:
        """
        if data:
            if self.success:
                if isinstance(data, list):
                    data = [i.serialize for i in data]
                else:
                    if hasattr(data, 'serialize'):
                        data = data.serialize

                self.json['data'] = data
            else:
                self.json['error'] = {
                    'message': data
                }

    def _set_pagination(self, pagination):
        """
        Set the pagination property, with links for: first, prev, next and last page

        :param pagination:
        """
        if pagination:
            pagination_links = {}
            count = len(pagination.items)
            link = "{}?count={}&page={}"

            pagination_links['first'] = link.format(request.base_url, count, 1)
            pagination_links['last'] = link.format(request.base_url, count, pagination.pages)

            if pagination.has_next:
                pagination_links['next'] = link.format(request.base_url, count, pagination.next_num)
            if pagination.has_prev:
                pagination_links['prev'] = link.format(request.base_url, count, pagination.prev_num)

            self.json['links'] = pagination_links

    @staticmethod
    def _set_cors():

        """
        Set CORS Headers

        :return: array
        """
        return {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Request-Headers': 'X-Requested-With, accept, content-type',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS'
        }

    def response(self, code=200, data=None, pagination=None):

        """
        Build the JSON response

        :param code: HTTP code
        :param data: Body response
        :param pagination: Pagination object
        :return: JSON response
        """
        self._set_success(code)
        self._set_status(code)
        self._set_data(data)
        self._set_pagination(pagination)

        return jsonify(self.json), code, self._set_cors()
