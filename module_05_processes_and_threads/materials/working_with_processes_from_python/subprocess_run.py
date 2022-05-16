import subprocess


def run_program():
    res = subprocess.run(['python', 'test_program.py'], input='some input\notherinput', encoding='utf-8')
    # res1 = subprocess.run(['python', 'test_program.py'], text=True, input='some input\nnotherinput')
    print(res)

if __name__ == '__main__':
    run_program()
