
def clashroyale_section_name():
    return 'ClashRoyale'


def clashroyale_option_list():
    return ['api_key', 'clashroyale_api_key']


def developer_section_name():
    return 'DeveloperOptions'


def developer_option_list():
    return developer_default_option_dict().keys()


def developer_default_option_dict():
    return {'debug': False,
            'mock_notification_services': False,
            'mock_clashroyale': False,
            'disable_cache': False}
