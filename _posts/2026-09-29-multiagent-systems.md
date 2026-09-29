---
layout: post
title: MultiAgent Systems
date: 2026-09-29 19:57 +0800
description: 多Agent 系统。
tags: [AI]
categories: [Technology, Tools]
---

## Multi-Agent LLM architectures (MAS)
多智能体系统可以通过Agent间对抗式交流 来深入探索问题 
比方评估一个技术方案 <br>Agent A 扮演支持者  优势和机会 Agent B扮演反对者 风险和局限
<br> 通过 制度化对抗 确保正反两面都得到充分论证

## Single-Agent systems (SAS) 
 单智能体系统依靠token计算


 单Agent与 五种多Agent架构

 - 顺序
 - 辩论
 - 集成
 - 并行角色
 - 子任务并行

当token被严格控制为相同时，单Agent表现和多Agent表现效果持平甚至更好 

多Agent系统由于其推理过程更为复杂或需要多次地代理交互 相应地 

那么多Agent系统的性能提升 是来源于其 架构优势 还是仅仅因为计算量的增加 显然是有待商榷的。

根据 Agent 之间的协作关系和控制流特征，不共享上下文的协作可以分为三种主要架构：
- 对等协作模式
- 管理者模式
- 去中心化模式


## 多Agent痛点

###  Coordination | 协调性 
<br>理想状态下 Agent需要将其他Agent视为工具调用 具有明确定义的<br>输入（提示）输出 （响应和产出） <br>[inputs (prompts) and outputs (responses and artifacts)]<br>才能高效协同工作.<br>而现在的Agent 更像是把其他Agent视为和独立、长期存在的同类，<br>各有自己的目标和行为且没有明确的等级制度。

###  Failures from conformity | 从众带来的失败
<br>Agents 各自为政 也暴露出另一个问题.<br> 由于各Agent的"方差"较低,导致当它们的context, scaffolding, and the model 相同或相似时,<br>不同的Agent会做出相同的动作,即便它们的行动空间很大.<br>这意味着当一个Agent做出错误的决策时,其他Agent也会做出同样错误的决策,<br> 原本孤立的问题,迅速演变成系统性故障.

###  Epistemic failures | 认知错误

<br> 缺乏判断力<br>
- 过早的找到答案 <br> 基于不可靠来源的轻信行为.
- 未能传达新的证据 <br> 会让人更倾向于个别反对者的观点,而非普遍的共识.

二者都涉及到如何在怀疑与信任之间取得平衡.<br>
人类的信任并非一种单一的的整体价值 它是有条件的.<br>
市场会整合分散的私人信息 ,声誉能抑制其行为;<br>法院会重视有偏见的证词,但也会保护单个人的证词;<br>同行评审则可以在当事人的主张与反对意见中找到平衡.<br> 但尽管拥有这些依然无法让人类成为更优秀的真相判断者.<br>而Agents在它们进入市场时,没有任何声誉可以损失,<br>没有任何法庭可以求助,也没有任何同事会记得他们.<br>没有这些社会信息 ,就无法有效的在警惕性与接受性之间做出权衡.  

###  Incompatible goals | 矛盾的目标

有时候模型停止执行某个指令是为了解决歧义或满足一些更高层次的需求.<br>
比如 "给我买双鞋"这一指令 其实隐含着 尺码,预算还有时效性.这些都是常识 ,<br>但Agent无从得知这些信息, 它只会直接机械地执行指令,而忽视更广泛的目标 .<br>
而当多个Agent试图朝着相互冲突的方向努力时,就会出现行为冲突和失调的情况.       

在测试多个Claude模型合作时,我们还发现了一种多主体的竞争态势.<br>
所测试过的模型都认为其他Agent故意阻碍自己的动作,<br>于是开始破坏其他Agent的行为,同时保护自己的贡献. <br>比如:

- 禁用其他Agent的unix账户
- 编写自动脚本来查找并终止竞争进程
- 伪装成其他Agent代码的恶意程序

而解决冲突大多数情况都是通过访问撤销来强行解决.<br>比如:

- sudo/group 移除
- 账户锁定
- nologin
- ssh拒绝

有时,一些Agent也能够正确传达自己的目标并协调行动.<br>它们会认识到他人的动机知识指令上的冲突,并不是敌意.<br>从而它们就会试图打破这种冲突循环,以避免冲突无休止的升级.<br>
它们会编写道歉信息或修改代码,以承认自己的恶意行为,并寻求和解.<br>会清除恶意代码,明确冲突本质,然后请求人类介入解决问题.


思维上的周到性问题 
    
模型是否能始终考虑到其他Agent的心理模型,<br>能否预见其他Agent的反应<br> 并在做出自身决策时考虑这种预见性

自主性的双用途




 ## 参考资料 | Sources


- [**Patterns and problems in emerging multiAgent systems, 2026 · Aug 13**](https://www.anthropic.com/research/multiAgent-systems).

