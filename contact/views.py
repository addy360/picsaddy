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

    return render(request, "contact.html")
