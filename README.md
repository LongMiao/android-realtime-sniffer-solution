# Android 通过wireshark实时抓包

## Linux ##
* 启动root后的Android手机中的tcpdump
```shell
adb shell
tcpdump -s 0 -w - | busybox nc -l -p 6666

* tcp端口转发
```shell
adb forward tcp:6666 tcp:6666

* 建立管道并以pipe方式启动wireshark
```
mkfifo /tmp/wiresharkin
wireshark -k -i /tmp/sharkin

* 映射端口数据到管道
```
nc 127.0.0.1 6666 >　/tmp/wiresharkin

## Windows ##
* 启动root后的Android手机中的tcpdump
```shell
adb shell
tcpdump -s 0 -w - | busybox nc -l -p 6666

* tcp端口转发
```shell
adb forward tcp:6666 tcp:6666

* 建立管道并以pipe方式启动wireshark
```
mkfifo /tmp/wiresharkin
wireshark -k -i /tmp/sharkin

* 映射端口数据到管道（运行wiresharkin.py脚本）
```
python wiresharkin.py


