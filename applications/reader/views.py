from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import BookLoanForm
from .models import BookLoan


class RegisterLoan(FormView):
    template_name = 'reader/book_loan_form.html'
    form_class = BookLoanForm
    success_url = '.'

    def form_valid(self, form):
        bookloans = []
        for book in form.cleaned_data['books']:
            bookloan = BookLoan(
                reader=form.cleaned_data['reader'],
                book=book,
            )
            bookloans.append(bookloan)

        BookLoan.objects.bulk_create(bookloans)

        return super(RegisterLoan, self).form_valid(form)


class InvalidLoan(TemplateView):
    template_name = 'reader/invalid.html'
