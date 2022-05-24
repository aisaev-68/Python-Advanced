# import logging
# import os
# import string
#
# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='environ.log', filemode='w', level=logging.DEBUG,
#                     format='%(asctime)s -- %(filename)s:%(lineno)d -- %(levelname)s -- %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8')
#
#
# def func1():
#     logger.info("Шаг 1")
#     logger.debug("Это просто разминка")
#
#     while True:
#         data = input("Ваш ответ? ")
#
#         try:
#             number = int(data)
#
#             if number != 9973:
#                 logger.debug("Нам нужно максимальное простое число меньшее чем 10000")
#                 print("Не правильно!")
#             break
#         except Exception as error:
#             logging.exception('Ошибка {}'.format(error))
#
#     print("Шаг 1 пройден")
#
#
# def func2():
#     logger.info("Шаг 2")
#     logger.debug("Задайте переменной окружения SKILLBOX значение awesome")
#     logger.debug("Вы можете задать значение переменной окружения вот так:")
#     logger.debug("$ export VARNAME=value")
#     os.environ["SKILLBOX"] = 'awesome'
#     logger.debug("Переменная окружения SKILLBOX = awesome задана")
#     while True:
#         input("Для продолжения нажмите ENTER...")
#
#         try:
#             if os.environ["SKILLBOX"].lower() == "awesome":
#                 break
#         except Exception as err:
#             logging.exception('Ошибка {}'.format(err))
#
#         print("Вы не готовы...")
#
#     print("Шаг 2 пройден")
#
#
# def func3():
#     logger.info("Шаг 3")
#
#     logger.debug("Создайте файл hw7.txt с английским палиндромом внутри")
#     with open("hw7.txt", "w", encoding='utf-8') as file:
#         file.write('rotator')
#     logger.debug("Создан файл hw7.txt с английским палиндромом внутри")
#     while True:
#         try:
#             input("Для продолжения нажмите ENTER...")
#
#             with open("hw7.txt", "r") as fi:
#                 data = fi.read().lower()
#
#                 data_str = [it for it in data if it in string.ascii_lowercase]
#
#                 if data_str == data_str[::-1]:
#                     print(data_str)
#                     break
#
#                 logger.debug(f"{data_str} != {data_str[::-1]}")
#         except Exception as er:
#             logging.exception('Ошибка {}'.format(er))
#
#         print("Не работает...")
#
#     print("Шаг 3 пройден")
#
#
# def what_went_wrong():
#     func1()
#     func2()
#     func3()
#
#
# if __name__ == "__main__":
#     what_went_wrong()


# Исправленная программа, а код исправленный выше откомментирован
import base64

command = b'IyBpbXBvcnQgYmFzZTY0CiMKIyBjb21tYW5kID0gYiJhVzF3YjNKMElHeHZaMmRwYm1jS2FXMXdiM0owSUc5ekNtbHRjRzl5ZENCemRISnBibWNLQ214dloyZGxjaUE5SUd4dloyZHBibWN1XG5aMlYwVEc5bloyVnlLRjlmYm1GdFpWOWZLUW9LQ21SbFppQm1kVzVqTVNncE9nb2dJQ0FnYkc5bloyVnlMbWx1Wm04b0l0Q28wTERRXG5zeUF4SWlrS0lDQWdJR3h2WjJkbGNpNWtaV0oxWnlnaTBLM1JndEMrSU5DLzBZRFF2dEdCMFlMUXZpRFJnTkN3MExmUXZOQzQwTDNRXG51dEN3SWlrS0NpQWdJQ0IzYUdsc1pTQlVjblZsT2dvZ0lDQWdJQ0FnSUdSaGRHRWdQU0JwYm5CMWRDZ2kwSkxRc05HSUlOQyswWUxRXG5zdEMxMFlJL0lDSXBDZ29nSUNBZ0lDQWdJSFJ5ZVRvS0lDQWdJQ0FnSUNBZ0lDQWdiblZ0WW1WeUlEMGdhVzUwS0dSaGRHRXBDZ29nXG5JQ0FnSUNBZ0lDQWdJQ0JwWmlCdWRXMWlaWElnSVQwZ09UazNNem9LSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJR3h2WjJkbGNpNWtaV0oxXG5aeWdpMEozUXNOQzhJTkM5MFlQUXR0QzkwTDRnMEx6UXNOQzYwWUhRdU5DODBMRFF1OUdNMEwzUXZ0QzFJTkMvMFlEUXZ0R0IwWUxRXG52dEMxSU5HSDBMalJnZEM3MEw0ZzBMelF0ZEM5MFl6UmlOQzEwTFVnMFlmUXRkQzhJREV3TURBd0lpa0tJQ0FnSUNBZ0lDQWdJQ0FnXG5JQ0FnSUhCeWFXNTBLQ0xRbmRDMUlOQy8wWURRc05DeTBMalF1OUdNMEwzUXZpRWlLUW9nSUNBZ0lDQWdJQ0FnSUNCaWNtVmhhd29nXG5JQ0FnSUNBZ0lHVjRZMlZ3ZENCRmVHTmxjSFJwYjI0NkNpQWdJQ0FnSUNBZ0lDQWdJSEJoYzNNS0NpQWdJQ0J3Y21sdWRDZ2kwS2pRXG5zTkN6SURFZzBML1JnTkMrMExuUXROQzEwTDBpS1FvS0NtUmxaaUJtZFc1ak1pZ3BPZ29nSUNBZ2JHOW5aMlZ5TG1sdVptOG9JdENvXG4wTERRc3lBeUlpa0tDaUFnSUNCc2IyZG5aWEl1WkdWaWRXY29JdENYMExEUXROQ3cwTG5SZ3RDMUlOQy8wTFhSZ05DMTBMelF0ZEM5XG4wTDNRdnRDNUlOQyswTHJSZ05HRDBMYlF0ZEM5MExqUmp5QlRTMGxNVEVKUFdDRFF0OUM5MExEUmg5QzEwTDNRdU5DMUlHRjNaWE52XG5iV1VpS1FvZ0lDQWdiRzluWjJWeUxtUmxZblZuS0NMUWt0R0xJTkM4MEw3UXR0QzEwWUxRdFNEUXQ5Q3cwTFRRc05HQzBZd2cwTGZRXG52ZEN3MFlmUXRkQzkwTGpRdFNEUXY5QzEwWURRdGRDODBMWFF2ZEM5MEw3UXVTRFF2dEM2MFlEUmc5QzIwTFhRdmRDNDBZOGcwTExRXG52dEdDSU5HQzBMRFF1am9pS1FvZ0lDQWdiRzluWjJWeUxtUmxZblZuS0NJa0lHVjRjRzl5ZENCV1FWSk9RVTFGUFhaaGJIVmxJaWtLXG5DaUFnSUNCM2FHbHNaU0JVY25WbE9nb2dJQ0FnSUNBZ0lHbHVjSFYwS0NMUWxOQzcwWThnMEwvUmdOQyswTFRRdnRDNzBMYlF0ZEM5XG4wTGpSanlEUXZkQ3cwTGJRdk5DNDBZTFF0U0JGVGxSRlVpNHVMaUlwQ2dvZ0lDQWdJQ0FnSUhSeWVUb0tJQ0FnSUNBZ0lDQWdJQ0FnXG5hV1lnYjNNdVpXNTJhWEp2YmxzaVUwdEpURXhDVDFnaVhTNXNiM2RsY2lncElEMDlJQ0poZDJWemIyMWxJam9LSUNBZ0lDQWdJQ0FnXG5JQ0FnSUNBZ0lHSnlaV0ZyQ2lBZ0lDQWdJQ0FnWlhoalpYQjBJRVY0WTJWd2RHbHZiam9LSUNBZ0lDQWdJQ0FnSUNBZ2NHRnpjd29LXG5JQ0FnSUNBZ0lDQndjbWx1ZENnaTBKTFJpeURRdmRDMUlOQ3owTDdSZ3RDKzBMTFJpeTR1TGlJcENnb2dJQ0FnY0hKcGJuUW9JdENvXG4wTERRc3lBeUlOQy8wWURRdnRDNTBMVFF0ZEM5SWlrS0NncGtaV1lnWm5WdVl6TW9LVG9LSUNBZ0lHeHZaMmRsY2k1cGJtWnZLQ0xRXG5xTkN3MExNZ015SXBDZ29nSUNBZ2JHOW5aMlZ5TG1SbFluVm5LQ0xRb2RDKzBMZlF0TkN3MExuUmd0QzFJTkdFMExEUXVkQzdJR2gzXG5OeTUwZUhRZzBZRWcwTERRdmRDejBMdlF1TkM1MFlIUXV0QzQwTHdnMEwvUXNOQzcwTGpRdmRDMDBZRFF2dEM4MEw3UXZDRFFzdEM5XG4wWVBSZ3RHQTBMZ2lLUW9nSUNBZ2QyaHBiR1VnVkhKMVpUb0tJQ0FnSUNBZ0lDQjBjbms2Q2lBZ0lDQWdJQ0FnSUNBZ0lHbHVjSFYwXG5LQ0xRbE5DNzBZOGcwTC9SZ05DKzBMVFF2dEM3MExiUXRkQzkwTGpSanlEUXZkQ3cwTGJRdk5DNDBZTFF0U0JGVGxSRlVpNHVMaUlwXG5DZ29nSUNBZ0lDQWdJQ0FnSUNCM2FYUm9JRzl3Wlc0b0ltaDNOeTUwZUhRaUxDQWljaUlwSUdGeklHWnBPZ29nSUNBZ0lDQWdJQ0FnXG5JQ0FnSUNBZ1pHRjBZU0E5SUdacExuSmxZV1FvS1M1c2IzZGxjaWdwQ2dvZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnWkdGMFlWOXpkSElnXG5QU0JiYVhRZ1ptOXlJR2wwSUdsdUlHUmhkR0VnYVdZZ2FYUWdhVzRnYzNSeWFXNW5MbUZ6WTJscFgyeHZkMlZ5WTJGelpWMEtDaUFnXG5JQ0FnSUNBZ0lDQWdJQ0FnSUNCcFppQmtZWFJoWDNOMGNpQTlQU0JrWVhSaFgzTjBjbHM2T2kweFhUb0tJQ0FnSUNBZ0lDQWdJQ0FnXG5JQ0FnSUNBZ0lDQmljbVZoYXdvS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUd4dloyZGxjaTVrWldKMVp5aG1JbnRrWVhSaFgzTjBjbjBnXG5JVDBnZTJSaGRHRmZjM1J5V3pvNkxURmRmU0lwQ2lBZ0lDQWdJQ0FnWlhoalpYQjBJRVY0WTJWd2RHbHZiam9LSUNBZ0lDQWdJQ0FnXG5JQ0FnY0dGemN3b0tJQ0FnSUNBZ0lDQndjbWx1ZENnaTBKM1F0U0RSZ05DdzBMSFF2dEdDMExEUXRkR0NMaTR1SWlrS0NpQWdJQ0J3XG5jbWx1ZENnaTBLalFzTkN6SURNZzBML1JnTkMrMExuUXROQzEwTDBpS1FvS0NtUmxaaUIzYUdGMFgzZGxiblJmZDNKdmJtY29LVG9LXG5JQ0FnSUdaMWJtTXhLQ2tLSUNBZ0lHWjFibU15S0NrS0lDQWdJR1oxYm1NektDa0tDZ3AzYUdGMFgzZGxiblJmZDNKdmJtY29LUW89IgojCiMgaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKIyAgICAgZXhlYyhiYXNlNjQuZGVjb2RlYnl0ZXMoY29tbWFuZCkuZGVjb2RlKCJ1dGY4IikpCgoKaW1wb3J0IGxvZ2dpbmcKaW1wb3J0IG9zCmltcG9ydCBzdHJpbmcKCmxvZ2dlciA9IGxvZ2dpbmcuZ2V0TG9nZ2VyKF9fbmFtZV9fKQpsb2dnaW5nLmJhc2ljQ29uZmlnKGZpbGVuYW1lPSdlbnZpcm9uLmxvZycsIGZpbGVtb2RlPSd3JywgbGV2ZWw9bG9nZ2luZy5ERUJVRywKICAgICAgICAgICAgICAgICAgICBmb3JtYXQ9JyUoYXNjdGltZSlzIC0tICUoZmlsZW5hbWUpczolKGxpbmVubylkIC0tICUobGV2ZWxuYW1lKXMgLS0gJShtZXNzYWdlKXMnLAogICAgICAgICAgICAgICAgICAgIGRhdGVmbXQ9JyVZLSVtLSVkICVIOiVNOiVTJywgZW5jb2Rpbmc9J3V0Zi04JykKCgpkZWYgZnVuYzEoKToKICAgIGxvZ2dlci5pbmZvKCLQqNCw0LMgMSIpCiAgICBsb2dnZXIuZGVidWcoItCt0YLQviDQv9GA0L7RgdGC0L4g0YDQsNC30LzQuNC90LrQsCIpCgogICAgd2hpbGUgVHJ1ZToKICAgICAgICBkYXRhID0gaW5wdXQoItCS0LDRiCDQvtGC0LLQtdGCPyAiKQoKICAgICAgICB0cnk6CiAgICAgICAgICAgIG51bWJlciA9IGludChkYXRhKQoKICAgICAgICAgICAgaWYgbnVtYmVyICE9IDk5NzM6CiAgICAgICAgICAgICAgICBsb2dnZXIuZGVidWcoItCd0LDQvCDQvdGD0LbQvdC+INC80LDQutGB0LjQvNCw0LvRjNC90L7QtSDQv9GA0L7RgdGC0L7QtSDRh9C40YHQu9C+INC80LXQvdGM0YjQtdC1INGH0LXQvCAxMDAwMCIpCiAgICAgICAgICAgICAgICBwcmludCgi0J3QtSDQv9GA0LDQstC40LvRjNC90L4hIikKICAgICAgICAgICAgYnJlYWsKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGVycm9yOgogICAgICAgICAgICBsb2dnaW5nLmV4Y2VwdGlvbign0J7RiNC40LHQutCwIHt9Jy5mb3JtYXQoZXJyb3IpKQoKICAgIHByaW50KCLQqNCw0LMgMSDQv9GA0L7QudC00LXQvSIpCgoKZGVmIGZ1bmMyKCk6CiAgICBsb2dnZXIuaW5mbygi0KjQsNCzIDIiKQogICAgbG9nZ2VyLmRlYnVnKCLQl9Cw0LTQsNC50YLQtSDQv9C10YDQtdC80LXQvdC90L7QuSDQvtC60YDRg9C20LXQvdC40Y8gU0tJTExCT1gg0LfQvdCw0YfQtdC90LjQtSBhd2Vzb21lIikKICAgIGxvZ2dlci5kZWJ1Zygi0JLRiyDQvNC+0LbQtdGC0LUg0LfQsNC00LDRgtGMINC30L3QsNGH0LXQvdC40LUg0L/QtdGA0LXQvNC10L3QvdC+0Lkg0L7QutGA0YPQttC10L3QuNGPINCy0L7RgiDRgtCw0Lo6IikKICAgIGxvZ2dlci5kZWJ1ZygiJCBleHBvcnQgVkFSTkFNRT12YWx1ZSIpCiAgICBvcy5lbnZpcm9uWyJTS0lMTEJPWCJdID0gJ2F3ZXNvbWUnCiAgICBsb2dnZXIuZGVidWcoItCf0LXRgNC10LzQtdC90L3QsNGPINC+0LrRgNGD0LbQtdC90LjRjyBTS0lMTEJPWCA9IGF3ZXNvbWUg0LfQsNC00LDQvdCwIikKICAgIHdoaWxlIFRydWU6CiAgICAgICAgaW5wdXQoItCU0LvRjyDQv9GA0L7QtNC+0LvQttC10L3QuNGPINC90LDQttC80LjRgtC1IEVOVEVSLi4uIikKCiAgICAgICAgdHJ5OgogICAgICAgICAgICBpZiBvcy5lbnZpcm9uWyJTS0lMTEJPWCJdLmxvd2VyKCkgPT0gImF3ZXNvbWUiOgogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGVycjoKICAgICAgICAgICAgbG9nZ2luZy5leGNlcHRpb24oJ9Ce0YjQuNCx0LrQsCB7fScuZm9ybWF0KGVycikpCgogICAgICAgIHByaW50KCLQktGLINC90LUg0LPQvtGC0L7QstGLLi4uIikKCiAgICBwcmludCgi0KjQsNCzIDIg0L/RgNC+0LnQtNC10L0iKQoKCmRlZiBmdW5jMygpOgogICAgbG9nZ2VyLmluZm8oItCo0LDQsyAzIikKCiAgICBsb2dnZXIuZGVidWcoItCh0L7Qt9C00LDQudGC0LUg0YTQsNC50LsgaHc3LnR4dCDRgSDQsNC90LPQu9C40LnRgdC60LjQvCDQv9Cw0LvQuNC90LTRgNC+0LzQvtC8INCy0L3Rg9GC0YDQuCIpCiAgICB3aXRoIG9wZW4oImh3Ny50eHQiLCAidyIsIGVuY29kaW5nPSd1dGYtOCcpIGFzIGZpbGU6CiAgICAgICAgZmlsZS53cml0ZSgncm90YXRvcicpCiAgICBsb2dnZXIuZGVidWcoItCh0L7Qt9C00LDQvSDRhNCw0LnQuyBodzcudHh0INGBINCw0L3Qs9C70LjQudGB0LrQuNC8INC/0LDQu9C40L3QtNGA0L7QvNC+0Lwg0LLQvdGD0YLRgNC4IikKICAgIHdoaWxlIFRydWU6CiAgICAgICAgdHJ5OgogICAgICAgICAgICBpbnB1dCgi0JTQu9GPINC/0YDQvtC00L7Qu9C20LXQvdC40Y8g0L3QsNC20LzQuNGC0LUgRU5URVIuLi4iKQoKICAgICAgICAgICAgd2l0aCBvcGVuKCJodzcudHh0IiwgInIiKSBhcyBmaToKICAgICAgICAgICAgICAgIGRhdGEgPSBmaS5yZWFkKCkubG93ZXIoKQoKICAgICAgICAgICAgICAgIGRhdGFfc3RyID0gW2l0IGZvciBpdCBpbiBkYXRhIGlmIGl0IGluIHN0cmluZy5hc2NpaV9sb3dlcmNhc2VdCgogICAgICAgICAgICAgICAgaWYgZGF0YV9zdHIgPT0gZGF0YV9zdHJbOjotMV06CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZGF0YV9zdHIpCiAgICAgICAgICAgICAgICAgICAgYnJlYWsKCiAgICAgICAgICAgICAgICBsb2dnZXIuZGVidWcoZiJ7ZGF0YV9zdHJ9ICE9IHtkYXRhX3N0cls6Oi0xXX0iKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXI6CiAgICAgICAgICAgIGxvZ2dpbmcuZXhjZXB0aW9uKCfQntGI0LjQsdC60LAge30nLmZvcm1hdChlcikpCgogICAgICAgIHByaW50KCLQndC1INGA0LDQsdC+0YLQsNC10YIuLi4iKQoKICAgIHByaW50KCLQqNCw0LMgMyDQv9GA0L7QudC00LXQvSIpCgoKZGVmIHdoYXRfd2VudF93cm9uZygpOgogICAgZnVuYzEoKQogICAgZnVuYzIoKQogICAgZnVuYzMoKQoKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICB3aGF0X3dlbnRfd3JvbmcoKQ=='
if __name__ == "__main__":
    exec(base64.decodebytes(command).decode("utf8"))
