from django.forms import ModelForm
from django.utils.safestring import SafeString

from .models import (
  MenuPluginSettings,
)


class EmbedPagesAdminForm(ModelForm):

    class Meta:
        model = MenuPluginSettings

    def __init__(self, *args, **kwargs):
        super(EmbedPagesAdminForm, self).__init__(*args, **kwargs)
        choices = [self.fields['root'].choices.__iter__().next()]
        for page in self.fields['root'].queryset:
            choices.append(
                (page.id,
                 SafeString(''.join([u"&nbsp;&nbsp;&nbsp;"*page.level,
                   page.__unicode__()]))))

        self.fields['root'].choices = choices
