---
layout: post
title: ServerCommand
date: 2026-06-08 16:57 +0800
description: 常用的服务器命令。
tags: [Server，Command]
categories: [Technology, Tools]
pin: true
---

## 修改终端文字大小

**sudo dpkg-reconfigure console-setup**

## netstat

### 常用命令


|- ano | Linux<br>所有/监听: a/l <br>TCP/UDP: t/u <br>-anp:带pid的所有连接|通过pid查进程连接的目标IP. |
|-------|-------|---|
|-r|查路由表。=linux in -rn|用于排查:<br>默认网关是否正确<br>路由是否被错误配置<br>某个网段是否可达|
|-s|输出<br>TCP 重传次数、<br>UDP 错误计数<br>ICMP 错误计数<br>丢包统计等|适合排查<br>网络不稳定<br>TCP 重传异常<br>系统网络栈是否出现异常|




### 参数 | Parameters
#### 特有参数 | Specific Parameters


| Windows | Linux |
| ------- | -------- |
| -b 显示创建连接的可执行文件路径(需管理员权限) |-t  仅显示 TCP 连接|
| -e 显示以太网统计信息（收发字节数、数据包数） |-u 仅显示 UDP 连接|
| -f 显示外部地址的完全限定域名（FQDN）|-l 仅显示监听（LISTEN）状态的端口|
| -y 显示所有 TCP 连接 |-i 显示网络接口统计信息|
| Interval 用数字直接指定刷新间隔（如 netstat 5 每 5 秒刷新）|-c 持续刷新（按 Ctrl+C 停止）|

#### 基本参数 | Basic Parameters

| Parameter      | Description         |
| -------    | -------      |
| -a | 	显示所有活动的TCP连接及正在监听的TCP和UDP端口。|
|-b|显示创建每个连接或监听端口所涉及的可执行文件。在某些情况下，知名可执行文件会托管多个独立组件，此时将显示参与创建连接或监听端口的组件序列。这种情况下，可执行文件名位于底部的[]中，顶部是其调用的组件，依此类推，直到TCP/IP协议层。请注意，此操作可能耗时较长，并且除非您拥有足够权限，否则会执行失败。|
|-e|显示以太网统计信息，如发送和接收的字节数及数据包数量。可与 -s 结合使用。|
|-n|显示活动的 TCP 连接，但地址和端口号以数字形式表示，且不会尝试解析名称。|
|-o|显示活动的 TCP 连接，并包含每个连接的进程 ID (PID)。可与 -a、-n 和 -p 组合使用。|
|-p|显示指定协议的连接情况。其中，协议(Protocol)可以是 tcp、udp、tcpv6 或 udpv6。若将此参数与 -s 一起使用以按协议显示统计信息，则协议可以是 tcp、udp、icmp、ip、tcpv6、udpv6、icmpv6 或 ipv6。|
|-q|显示所有连接、监听端口以及已绑定但未监听的TCP端口。已绑定但未监听的端口可能与活动连接有关，也可能无关。|
|-s	|按协议显示统计信息。默认情况下，会显示TCP、UDP、ICMP和IP协议的统计信息。如果安装了IPv6协议，则会显示基于IPv6的TCP、基于IPv6的UDP、ICMPv6和IPv6协议的统计信息。可使用-p参数指定一组协议。|
|-r|显示IP路由表。等同于Linux下的-rn|
|interval|持续监控。等同于Linux下的-c。每隔 interval 秒重新显示所选信息。按 CTRL+C 停止重新显示。如果省略此参数，此命令将仅输出所选信息一次。|


![Parameter](assets/fodder/netstat.webp)


### 备表 | Remarks

| Parameter      | Description         |
| -------    | -------      |
| State           | Indicates the state of a TCP connection, including:<br>CLOSE_WAIT: 对端关了，但本地程序没有 close ( 常见于程序 bug ) .<br>CLOSED:	初始状态，无连接存在.<br>ESTABLISHED: 三次握手完成，连接已建立，双方可正常双向传输数据(全双工).<br>FIN_WAIT_1: 发出 FIN 后等待 ACK，极短暂；若堆积说明对端无响应（网络问题或对端宕机）.<br>FIN_WAIT_2: 收到 ACK 后等待对端 FIN；若大量堆积，说明对端应用有 Bug，未正常关闭连接.<br>LAST_ACK: 发出自己的 FIN 后等待最终 ACK，极短暂.<br>LISTEN: 在监听的端口，等待连接.<br>SYN_RECEIVED: 服务端收到 SYN 并回复 SYN+ACK 后，等待客户端的最终 ACK.<br>SYN_SEND: 客户端发送 SYN 包后，等待服务端回复 SYN+ACK.<br>TIMED_WAIT: 连接关闭后的等待释放 (常见，通常正常) .<br>TIME_WAIT：主动关闭方收到对方 FIN 并发送 ACK 后进入，持续 2MSL（Linux 默认 60 秒），确保对方收到 ACK 且旧报文在网络中消亡。<br>CLOSE_WAIT：被动关闭方收到 FIN 并回复 ACK 后进入，等待应用层调用 close()。如果堆积，说明应用代码有 Bug（忘记关闭连接）。<br>CLOSING：双方几乎同时发送 FIN 时出现的罕见状态。|
| Proto    | The name of the protocol (TCP or UDP).    |
| Local address   | The IP address of the local computer and the port number being used. The name of the local computer that corresponds to the IP address and the name of the port is shown unless the -n parameter is specified. If the port is not yet established, the port number is shown as an asterisk (*).  |
| Foreign address   | The IP address and port number of the remote computer to which the socket is connected. The names that corresponds to the IP address and the port are shown unless the -n parameter is specified. If the port is not yet established, the port number is shown as an asterisk (*).    |


