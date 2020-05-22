from django.db.utils import IntegrityError
from django.db.models import Model


class ImportData:
    def __init__(self, model, data):
        if not isinstance(model(), Model):
            raise TypeError()

        self.data = data
        self.model = model
        self.messages = []

    def execute(self):
        for data in self.data:
            self._create_or_continue(data)

    def get_messages(self):
        return self.messages

    def _create_or_continue(self, data):
        key_dict = data[next(iter(data))]
        try:
            self.model.objects.create(**data)
            self.messages.append("%s created" % (key_dict))
        except IntegrityError:
            self.messages.append("%s already created" % (key_dict))
