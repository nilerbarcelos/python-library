import decimal
import ujson

import http.client
from django.http import HttpResponse
from voluptuous import Schema, MultipleInvalid


class JsonForm(object):
    schema = Schema({})

    def __init__(self, json):
        self._cleaned_value = None
        self._json = json
        self._is_valid = None
        self._errors = []

    def is_valid(self):
        try:
            json = ujson.loads(self._json)
            self._cleaned_value = self.schema(json)
            self._errors = self.custom_validation(self._cleaned_value)
        except ValueError:
            self._errors.append('string is not in a valid JSON format..')
        except MultipleInvalid as e:
            for error in e.errors:
                self._errors.append(str(error).replace('u\'', '\''))
        except decimal.InvalidOperation:
            self._errors.append('invalid decimal number.')
        except Exception as e:
            self._errors.append({'message': str(e)})

        self._is_valid = not self._errors
        if not self._is_valid:
            self._cleaned_value = None

        return self._is_valid

    def custom_validation(self, cleaned_value):
        return []

    def custom_parsing(self, cleaned_value):
        return cleaned_value

    def cleaned_value(self):
        return self.custom_parsing(self._cleaned_value)

    def create_error_response(self):
        if self._is_valid is None:
            raise Exception('is_valid() was not called.')
        if self._is_valid is True:
            raise Exception('Valid form cannot generate an error response.')

        return HttpResponse(
            status=http.client.UNPROCESSABLE_ENTITY,
            content_type='application/json',
            content=ujson.encode({
                'message': 'Invalid JSON structure.',
                'errors': self._errors,
            }))
