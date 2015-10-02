def task_test_unit():
    return { 'actions' : [ 'python tests/run_all_tests.py']  } 

def task_run_coffee():
    return { 'actions' : [ 'sudo src/./run' ] } 
