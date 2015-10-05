def task_unit_test():
    return { 'actions' : [ 'python tests/run_all_tests.py']  } 

def task_unit_test_watch():
    return { 'actions' : [ 'nosetests --with-watch' ] }

def task_run_coffee():
    return { 'actions' : [ 'sudo src/./run' ] } 

def task_check_coverage():
    return { 'actions' : [ 'coverage run --source=src tests/run_all_tests.py','coverage report -m' ],
            'verbosity' : 2
            }
