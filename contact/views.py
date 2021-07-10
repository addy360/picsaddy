from contact.models import Contact
from pages.helper import validate_post_data
from django.shortcuts import render

# Create your views here.


def contact(request):
    if request.method == "POST":
        errors, clean_data = validate_post_data(request)
        if len(errors):
            formated_errors = []
            for err in errors:
                e = list(err.items())[0]
                err_res = [e[0], e[1]]
                formated_errors.append(err_res)
            print(formated_errors)
            context = {"errors": formated_errors}
            return render(request, "contact.html", context)
        print('[+] all data are clean')
        print(clean_data)

        contact = Contact()
        contact.firstName = clean_data['fname']
        contact.lastName = clean_data['lname']
        contact.email = clean_data['email']
        contact.subject = clean_data['subject']
        contact.message = clean_data['message']

        contact.save()

    return render(request, "contact.html")
