import re


def email_parse(email_adress):
    re_data = re.match(r"(?P<username>\S+)@(?P<domain>\S+)", email_adress)
    if re_data is not None:
        return re_data.groupdict()
    else:
        raise ValueError(f'wrong email: {email_adress}')


result = email_parse('someone@geekbrains.ru')
print(result)

