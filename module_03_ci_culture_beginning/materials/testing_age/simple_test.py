from module_03_ci_culture_beginning.materials.testing_age.social_age import get_social_status


def check_if_can_get_child_status():
    age = 12
    expected_res = 'ребенок'
    function_res = get_social_status(age)
    assert expected_res == function_res, 'Not matched'


def check_if_can_get_adult_status():
    age = 49
    expected_res = 'взрослый'
    function_res = get_social_status(age)
    assert expected_res == function_res, 'Not matched'

def check_if_can_get_teenager_status():
    age = 17
    expected_res = 'подросток'
    function_res = get_social_status(age)
    assert expected_res == function_res, 'Not matched'

def check_if_can_get_aged_status():
    age = 60
    expected_res = 'пожилой'
    function_res = get_social_status(age)
    assert expected_res == function_res, 'Not matched'

def check_if_can_get_pensioner_status():
    age = 66
    expected_res = 'пенсионер'
    function_res = get_social_status(age)
    assert expected_res == function_res, 'Not matched'


if __name__ == '__main__':
    check_if_can_get_child_status()
    check_if_can_get_adult_status()
    check_if_can_get_teenager_status()
    check_if_can_get_aged_status()
    check_if_can_get_pensioner_status()
