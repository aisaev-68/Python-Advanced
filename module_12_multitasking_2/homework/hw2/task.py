import subprocess


def process_count(username: str) -> int:
    # к-во процессов, запущенных из-под текущего пользователя
    ps = subprocess.Popen(f'ps -U {username}', shell=True, stdout=subprocess.PIPE)
    return len(ps.stdout.readlines())


def total_memory_usage(root_pid: int) -> int:
    # суммарное потребление памяти древа процессов
    ps = subprocess.Popen(f'pmap -x {root_pid}', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    lst = ps.stdout.readlines()
    l = len(lst)
    return int(lst[l - 1].split()[3])


print('Количество процессов, запущенных из-под текущего пользователя:', process_count('aisaev'))
print('Суммарное потребление памяти древа процессов:', str(total_memory_usage(21239)), 'kb.')
