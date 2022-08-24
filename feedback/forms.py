from django import forms
from .models import Feedback


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'rating']
        # exclude=['rating']
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name':
                {'max_length': 'name is too long',
                 'min_length': 'name is too short'}
        }

# class FeedBackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2,
#                            error_messages={'max_length': 'слишком много символов',
#                                            'min_length': 'слишком мало символов'})
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
