def task_unit_test():
    return {'actions': ['nosetests -w . unit_tests']}


def task_unit_test_watch():
    return {'actions': ['nosetests --with-watch -w . unit_tests']}


def task_integration_test():
    return {'actions': ['nosetests -w . integration_tests']}


def task_run_coffee():
    return {'actions': ['sudo src/run'],
            'verbosity': 2
            }


def task_check_coverage():
    return {'actions':
            ['coverage run --source=src unit_tests/run_all_unit_tests.py',
             'coverage report -m --fail-under=51'],
            'verbosity': 2
            }


def task_check_style():
    return {'actions': ['flake8 . --exclude=env/*']}
