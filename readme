# 快速探测C段（可DIY）

1. 安装Masscan (centos)
```
yum install git gcc make libpcap-devel
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make

#run
#./masscan 203.58.19.1/24 -p80 --banners -oX result.xml
./bin/masscan
```
![](https://i.imgur.com/GGjConO.png)
2. Python2.7.X 
```
pip install requests
```

下载地址：
```
http://118.25.136.144/main
```
使用方法
```
主程序是Python编写，通过Pyinstaller进行编译生成，所以文件较大。

将main放到../masscan/bin目录下（bin目录下可见Masscan脚本），当然将Masscan设置环境变量也行，就省去这一步。
./main
Input IPs(10.10.10.1/24) 
暂时只扫描C类段
```

```
通过Masscan扫描80-90、7000-10000端口，端口可以自定义。
通过获取端口并拼接获取WEB服务的指纹，包括Title、headers。
通过获取的Banner值进行正则判断，现版本可以识别Weblogic、Struts，后期开发可以实现识别中间件后进行自动检测CVE及历史漏洞。
```

![](https://i.imgur.com/GiJdkO6.png)

2. 注意事项
```
最好将VPS放在国内，对于护网和红队来说.
如果目标在国外的话，就找个国外的VPS.
对于任何的扫描器或者漏扫而言，服务器的丢包时不得不考虑的一个事项。
```
