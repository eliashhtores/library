from django import forms
from applications.book.models import Book
from .models import BookLoan


class BookLoanForm(forms.ModelForm):

    books = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = BookLoan
        fields = ('reader',)

    def __init__(self, *args, **kwargs):
        super(BookLoanForm, self).__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()
