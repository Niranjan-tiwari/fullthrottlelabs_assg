from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer

from .messages import Message


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def incorrect_fields_response(errors):
    """
    generate the response for incorrect_fields
    :param errors: dictionary of errors
    :return: JSONResponse for incorrect_fields
    """
    errors_keys = errors.keys()
    print(errors_keys)
    if len(errors_keys) == 1:
        error_key = errors_keys[0]
        error_message = errors.get(error_key)[0]
        return JSONResponse({'code': 0, 'response': errors, 'message': "{}".format(error_message)})
    else:
        incorrect_fields = ", ".join(errors_keys)
        return JSONResponse({'code': 0, 'response': errors, 'message': "{} fields are {}".format(
            incorrect_fields, Message.code(3))})
