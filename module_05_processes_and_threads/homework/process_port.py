# Для проверки работы запустите в терминале python3 flask_server.py & и введите номер порта 5001
# после чего запустите данный файл


import shlex
import subprocess
import os


def proc_run(port: int):
    command = 'lsof -i :{}'.format(shlex.quote(str(port)))
    # capture_output=True перенаправление вывода в stdout
    res_lsof = subprocess.run(shlex.split(command), capture_output=True, encoding='utf-8')
    if res_lsof.returncode == 0:
        res_pid = res_lsof.stdout.split('\n')[1].split()[1]
        res_port = int(res_lsof.stdout.split('\n')[1].split()[8].split(':')[1])
        if res_port == port:
            print(f'Порт занят процессом {res_pid}')
            os.kill(int(res_pid), 9)
            print(f'Процесс {res_pid} удален')
        else:
            print(f'Порт {port} свободен')
    else:
        print(f'Порт {port} свободен')
    subprocess.run(['python3', 'flask_server.py'], input=str(port), text=True)


if __name__ == '__main__':
    res = subprocess.run(['python3', 'flask_server.py'], input='5001', text=True)
    if res.returncode != 0:
        proc_run(5001)
