Перед тем как переходить к последующим урокам, нам обязательно нужно научиться 
    деплоить приложения. В дальнейшем от вас часто будет требоваться сдать вашу домашнюю 
    работу в виде работающего сайта.

Поэтому обязательно проделайте deploy того сайта, который находится в материалах к занятию
    в папке new_year_application.


aisaev@aisaev-VirtualBox:~$ ssh-keygen -t rsa -b 2048 -C "Yandex Machine" -f yandex


aisaev@aisaev-VirtualBox:~$ ssh -i yandex aisaev_ramazan@130.193.55.94
aisaev_ramazan@aisaev68:~$ sudo adduser ramazan
aisaev_ramazan@aisaev68:~$ sudo usermod -aG sudo ramazan
aisaev_ramazan@aisaev68:~$ su - ramazan
ramazan@aisaev68:~$ cd ~
ramazan@aisaev68:~$ mkdir -p .ssh
ramazan@aisaev68:~$ chmod 700 .ssh
ramazan@aisaev68:~$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyU9wiw8X5RG4HE8u6mWQ5urUJUYhE66eeKCYLnaxjAYLaBlMyRaDs3SSXBTWU5yYyiY82jh62mRX8reJlHYoC/T5x7niIvfv6KIBwrFnStO2oVCAMsfQFeeRMQeRbYlS5cnptadAeCtRdurN/vbqq+YZtbrLf4LnHZuy0d3H0A1Ldsy5TWSZcL+meMr8p/VWOmffLhjdbBk/YmRShOVXfA6mzscIOOfI2d1Ub+xXJ6RAhMZzLKOu9+QToBPi2z5Iccj0v0YjvT/xd92qQIs5b/X19ypcTqqSxn8To8oM0TnlIG3rWyb3gqcA2opZst1L+cK3q/OlAHU027UxunDaT Yandex Machine" > ~/.ssh/authorized.keys 
ramazan@aisaev68:~$ mkdir deploy_skillbox
ramazan@aisaev68:~$ cd deploy_skillbox
ramazan@aisaev68:~/deploy_skillbox$ sudo apt install python3-virtualenv
ramazan@aisaev68:~/deploy_skillbox$ python3 -m virtualenv -p python3 venv
ramazan@aisaev68:~/deploy_skillbox$ source venv/bin/activate
(venv) ramazan@aisaev68:~/deploy_skillbox$ pip install flask
(venv) ramazan@aisaev68:~/deploy_skillbox$ touch hello_world_again.py
(venv) ramazan@aisaev68:~/deploy_skillbox$ nano hello_world_again.py
(venv) ramazan@aisaev68:~/deploy_skillbox$ export FLASK_APP=hello_world_again.py
(venv) ramazan@aisaev68:~/deploy_skillbox$ flask run -h 10.129.0.6

http://130.193.55.94:5000/hello/Tom 