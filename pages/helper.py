def format_categories(categories):
    formated = []
    for cat in categories:
        res = cat.images(f'{cat.id}')
        formated.append({"name": cat.cat_name,
                         "id": cat.id,
                        "photo_count": res[0], "url": res[1], })
    return formated


def trip_value(value):
    return value.strip()


def is_greater_than(value, num):
    return len(value) > num


def my_validator(value, validate_funcs):
    errors = []
    for func in validate_funcs:
        error = func(value)
        if error:
            errors.append(error)
    return errors

# Validators


def should_be_string(value):
    if not isinstance(value, str):
        return "Should be a string"


def should_be_greater_than_3(value):
    if not is_greater_than(value, 3):
        return "Should have three letters or more"


def should_be_an_email(value):
    if value.find("@") == -1:
        return "Should be a valid email"


def validator_executor(value, validators=[]):
    res = {}
    validation_errors = my_validator(
        value, validators)

    if len(validation_errors):
        res[value] = validation_errors
    return res


def validate_post_data(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    errors = []

    # fname
    # validation_errors = my_validator(
    #     fname, [should_be_string, should_be_greater_than_3])

    # if len(validation_errors):
    #     errors['fname'] = validation_errors
    #     validation_errors = []

    res = validator_executor(
        fname, [should_be_string, should_be_greater_than_3])
    errors.append(res)

    # # lname
    # validation_errors = my_validator(
    #     lname, [should_be_string, should_be_greater_than_3])

    # if len(validation_errors):
    #     errors['lname'] = validation_errors
    #     validation_errors = []

    # # email
    # validation_errors = my_validator(
    #     email, [should_be_string, should_be_an_email])

    # if len(validation_errors):
    #     errors['email'] = validation_errors
    #     validation_errors = []

    cleanValues = {
        "fname": fname,
        "lname": lname,
        "email": email,
        "subject": subject,
        "message": message,
    }

    return errors, cleanValues
