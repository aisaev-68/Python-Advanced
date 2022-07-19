**Урок 3**

1. Познакомиться с плагинами Logstash:
[плагины для input](https://www.elastic.co/guide/en/logstash/6.8/input-plugins.html) (file, tcp,udp, beats)
[плагины для filter](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html) (mutate, grok)
[плагины для output](https://www.elastic.co/guide/en/logstash/current/output-plugins.html) (stdout, file, elasticsearch)

2. Написать шаблон, используя [grok-тренажер](http://grokdebug.herokuapp.com/) для строки вида: 1**27.0.0.1 - - [20/Oct/2021:19:09:19 -0400] "GET / HTTP/1.1" 401 194 "" "Mozilla/5.0 Gecko" "-"**
