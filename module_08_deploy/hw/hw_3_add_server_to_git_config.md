Скажите, вам не надоело постоянно добавлять "-i timeweb" при каждом вызове ssh?
Да и "-e 'ssh -i timeweb'" при вызове rsync выглядит немного не приятно.

К счастью есть способ от этого отказаться, внеся файлик с ключём в специальную конфигурацию.
В качестве первого домашнего задания выполните следующую инструкцию.

1. на локальной машине создайте папку ~/.ssh и задайте на неё права как мы проходили на занятии
```shell script
$ mkdir -p ~/.ssh
$ chmod 700 ~/.ssh
```

2. создайте в папке `~/.ssh` файл с именем config
```shell script
    $ touch ~/.ssh/config && chmod 600 ~/.ssh/config
```

3. скопируйте ключ `timeweb` и `timeweb.pub` в папку `~/.ssh/`
```shell script
    $ cp -fv timeweb timeweb.pub ~/.ssh/
    $ chmod 600 ~/.ssh/timeweb*
```

4. *(опционально)* если вы этого ещё не сделали, прочитайте, что же это за `700` и `600` такие вот тут
    https://www.opennet.ru/man.shtml?category=1&topic=chmod

5. откройте файл ~/.ssh/config на редактирование в вашем любимом текстовом редакторе и
    напишите примерно следующие строки
```
Host <ip_address_of_your_machine>
  User <your_remote_system_user_name>
  IdentityFile ~/.ssh/timeweb
```

6. попробуйте залогиниться
```shell script
    $ ssh <your_remote_system_user_name>@<ip_address_of_your_machine>
```
