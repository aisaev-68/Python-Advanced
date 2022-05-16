import subprocess


def run_program():
    with open('test_input.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    for item in data:
        item = '\n'.join(item.split())
        res = subprocess.run(['python', 'test_program.py'], input=item, encoding='utf-8')
        print(res)

if __name__ == '__main__':
    run_program()
