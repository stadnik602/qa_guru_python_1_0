def even_more_readable_name(func, **kwargs):
    func_name = func.__name__.replace('_', ' ').title()
    args_name = ", ".join(key + "=" + kwargs[key] for key in kwargs.keys())
    return f"{func_name} [{args_name}]"

def find_registration_button_on_login_page_2(page_url, button_text):
    actual_result = even_more_readable_name(find_registration_button_on_login_page_2, page_url=page_url, button_text=button_text)
    # print(actual_result)
    dict = {'button_text': 'Register', 'page_url': 'https://companyname.com/login'}
    ret = dict.get("page_url")
    print(ret)
    print(dict)
    print(dict.items())
    print(dict.keys())
    print(dict.values())
    print('------------')
    args_name = ", ".join(key + "=" + value for key, value in dict.items())
    print(args_name)
    items = list(dict.items())
    print(items)
    nn = items[0]
    print(nn)




find_registration_button_on_login_page_2(page_url="https://companyname.com/login", button_text="Register")
