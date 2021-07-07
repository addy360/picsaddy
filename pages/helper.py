def format_categories(categories):
    formated = []
    for cat in categories:
        res = cat.images(f'{cat.id}')
        formated.append({"name": cat.cat_name,
                         "id": cat.id,
                        "photo_count": res[0], "url": res[1], })
    return formated
