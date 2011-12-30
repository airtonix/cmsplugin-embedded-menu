import os

from django.template.loader import get_template
from django.template.loaders.app_directories import app_template_dirs
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

from cms.models import Placeholder, Page

from .formatting import deslugify

class DynamicChoice(object):
    """
    Trivial example of creating a dynamic choice
    """

    def __iter__(self, *args, **kwargs):
        for choice in self.generate():
            if hasattr(choice,'__iter__'):
                yield (choice[0], choice[1])
            else:
                yield choice, choice

    def __init__(self, *args, **kwargs):
        """
        If you do it here it is only initialized once. Then just return generated.
        """
        self.generated = range(10)

    def generate(self, *args, **kwargs):
        """
        If you do it here it is  initialized every time the iterator is used.
        """
        return range(10)


class PageAttributeDynamicChoices(DynamicChoice):

    def __init__(self, *args, **kwargs):
        super(PageAttributeDynamicChoices, self).__init__(self, *args, **kwargs)

    def generate(self,*args, **kwargs):
        choices = list()
        return choices


class PlaceholdersDynamicChoices(DynamicChoice):

    def __init__(self, *args, **kwargs):
        super(PlaceholdersDynamicChoices, self).__init__(self, *args, **kwargs)

    def generate(self,*args, **kwargs):
        choices = list()
        for item in Placeholder.objects.all().values("slot").distinct():
            choices += ((
              item['slot'],
              deslugify(item['slot'])
              ), )

        return choices

class PageIDsDynamicChoices(DynamicChoice):

    def __init__(self, *args, **kwargs):
        super(PageIDsDynamicChoices, self).__init__(self, *args, **kwargs)

    def generate(self,*args, **kwargs):
        choices = list()
        for item in Page.objects.all():
            if not item.reverse_id :
                continue

            choices += ((
              item.reverse_id,
              "{0} [{1}]".format(item.get_title(), item.reverse_id)
              ), )

        return choices


class DynamicTemplateChoices(DynamicChoice):
    path = None
    exclude = None
    inlude = None

    def __init__(self, path=None, include=None,
                       exclude=None, *args, **kwargs):
        super(DynamicTemplateChoices, self).__init__(self, *args, **kwargs)
        self.path = path
        self.include = include
        self.exlude = exclude

    def generate(self,*args, **kwargs):
        choices = list()

        for template_dir in app_template_dirs:
          results = self.walkdir(os.path.join(template_dir, self.path))
          if results:
              choices += results

        return choices

    def walkdir(self, path=None):
        output = list()

        if not os.path.exists(path):
            return None

        for root, dirs, files in os.walk(path):

            if self.include:
                files = filter(lambda x: self.include in x, files)

            if self.exlude:
                files = filter(lambda x: not self.exlude in x, files)

            for item in files :
                output += ( (
                    os.path.join(self.path, item),
                    deslugify(os.path.splitext(item)[0]),
                ),)

            for item in dirs :
                output += self.walkdir(os.path.join(root, item))

        return output
