# Deep Reinforcement Learning 深度强化学习贪吃蛇游戏 DRL_Snakey

深度强化学习贪吃蛇AI与游戏环境。

[![Build Status](https://travis-ci.org/cstrikest/DRL_Snakey.svg?branch=master)](https://travis-ci.org/cstrikest/DRL_Snakey)
![GitHub](https://img.shields.io/github/license/cstrikest/DRL_Snakey.svg)

![PyPI - Downloads](https://img.shields.io/pypi/dm/DRL_Snakey.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/cstrikest/DRL_Snakey.svg)

![PyPI](https://img.shields.io/pypi/v/DRL_Snakey.svg)
![GitHub release](https://img.shields.io/github/release/cstrikest/DRL_Snakey.svg)

[![Readme](https://img.shields.io/badge/Readme-Chinese-red.svg)](http://github.com/cstrikest/DRL_Snakey)
[![Readme](https://img.shields.io/badge/Readme-Japanese-orange.svg)](http://github.com/cstrikest/DRL_Snakey/blob/master/README-JP.md)


![游戏开始界面](https://github.com/cstrikest/ML_Snakey/blob/master/images/gamestart_image.png?raw=true)

## 环境

Python版本: Python3.6或以上

### 外部依赖

* pygame
* tensorflow / tensorflow-gpu
* h5py
* numpy
* matplotlib

## 游戏说明

**演示文件: Snakey_play.py**

此文件与DRL_Snakey包无关联，不含有任何AI部分，作为一个人类可以游玩的游戏进行演示。

在使用包之前可以先运行该脚本查看游戏效果。

### 规则

人类玩家游玩时，游戏内容设有等级划分，随着获取食物的数量上升，蛇前进的速度会变快。

同时每增加一个难度会多出现一个触碰到便会游戏结束的炸弹。（默认为无炸弹）

游戏在一个200×200像素的平面中运行，每10×10个像素作为一个单元。

游戏右侧是一个100×200像素的信息面板。主要用到的信息会在右侧给出。

使用方向键控制移动方向，任何时候都可以使用Q键退出。游戏结束画面按R重新开始，`S`则会跳出计分板。游戏中按`P`键可以暂停游戏，暂停中N键可以让游戏单步进行,`F`键切换可视化模式。

除单独存在的演示脚本外，游戏主体主要由**游戏逻辑**，**图形引擎**，**智能体**三部分组成，运行时可以根据需要选择是否加载图形引擎显示游戏界面。

### AI部分说明

AI没有游戏的速度区别与等级区分，暂时无视炸弹，并且在使用界面时默认使用最快的刷新速度。

本项目内拥有数个AI脚本，详细见下文的各脚本说明。

**游戏中按F键可切换可视化部分，P键暂停，N键在暂停时单步进行游戏。**

### 使用方法

首先import

    import DRL_Snakey as Snakey
    
创建游戏对象，此游戏类仅包含游戏规则(DRL_Snakey.Game)。

    game = Snakey.Game()
    
游戏控制agent对象。这里以简单逻辑算法AI举例。

    agent = Snakey.agent.Logic()
    
游戏界面对象，通过pygame模块创建可视的游戏界面。
    
    ui = Snakey.UI()
    
通过UI类的show(game, agent)函数创建游戏窗口。

    ui.show(game, agent)

需要训练agent模型或其他等不需要游戏UI界面时，使用以下脚本控制游戏流程。

    import DRL_Snakey as Snakey
    
    
    game = Snakey.Game()
    agent = Snakey.agent.Logic()
    
    while True:
        game.next_step(agent.get_next_direction(game))
        if game.deathflag:
            print("Gameover. score:", game.ate)
            game.reset()
            
## DRL_Snakey说明

DRL_Snakey主要分为游戏环境`DRL_Snakey.core`，智能体`DRL_Snakey.agent`与`DRL_Snakey.utlis`组件三部分组成。

其中`DRL_Snakey.core.Game`为贪吃蛇游戏的基本行动规则，死亡判定以及地图查看等功能。可以视为游戏的本体。
`DRL_Snakey.core.UI`为游戏界面显示相关。通过pygame包来创建可视化的游戏界面。

`DRL_Snakey.agent`为智能体部分，其中拥有众多AI类。智能体会读取游戏中每步的状态，应用相对的决策方法
进行决策，并给出反应。

Agent类的结构:

    class Agent(object):
	def get_next_direction(self, Game):
		"""
		根据智能体对当前环境的判断选择下一步前进的方向。
		:return: 方向["W", "S", "A", "D"]
		"""
		pass
	
    def button_K_e_pressed(self, Game):
        """
        给不同的agnet预留的自定义函数，用来调试或数据可视化。
        """
        pass
        	
	def custom_function(self, Game):
		"""
		给不同的agnet预留的自定义函数，用来调试或数据可视化。
		"""
		pass

`DRL_Snakey.core.snake`中还有一个`Snake`类来表示游戏中的每条蛇。

ps. 请多多编写自己的agent然后pull request

### DRL_Snakey.agent.Logic_AI.Logic

一个简单的演示用逻辑AI，完全无视炸弹，只吃食物。具有十分简单的自身躲避算法。

通过计算蛇头位置与食物的水平竖直差，以之字形接近食物。并且在决策方向前，会通过`Logic.next()`预测
下一步的位置，并调用`Logic.elude()`依次尝试各个方向来避免与自己相撞。但是因为只能预测下一步的危险情况，
所以此AI并不具有很高智能，只是作为演示使用。

此AI在20次尝试中最好成绩为68，平均值为49.6。

![简易AI演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/Logic_play.gif?raw=true)

### DRL_Snakey.agent.DP_AI.DP

DP(Dynamic Programming)动态规划-马尔科夫决策法。

每一步都通过迭代贝尔曼方程计算当前各点的价值，创建价值矩阵。并且朝周围价值最高的点前进。

构造函数参数说明:

* `discount`: 衰减率，贝尔曼方程中对于非即时回报的衰减率。
* `iteration`: 推算价值矩阵的迭代次数。
* `walk_reward`: 每走一步的回报
* `eat_self_reward`: 吃到自己的回报
* `food_reward`: 吃到食物的回报

按F打开可视化模式后，可观察每一步动作所基于的各点价值图像。

实际操作中会发现，AI可以根据价值的判断避开自身，并且在食物环境恶劣的情况下选择在安全地带迂回等待。

此AI在20次尝试中最好成绩为119，平均值为69.2。

![DP演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/DP_play.gif?raw=true)

### DRL_Snakey.agent.MC_AI.MC

MC(Monte-Calo)蒙特卡洛法。

每步分别基于某个策略循环计算三个可行方向的平均动作价值，选择平均动作价值最高的一个动
作。本AI采取的基础策略是`DRL_Snakey.agent.Logic_AI.Logic`。

构造函数参数说明:

* `discount`: 衰减率
* `iteration`: 迭代次数
* `max_step`: 预测最大步数
* `epsilon`: 探索率
* `walk_reward`: 每步的回报
* `eat_self_reward`: 吃到自己的回报
* `food_reward`: 吃到食物的回报

此AI在20次尝试中最好成绩为89，平均值为50.5。

![MC演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/MC_play.gif?raw=true)

## 深度强化学习 DRL AI

作为深度强化学习很好的一个例子，贪吃蛇游戏有着很明显的数据结构。Environment就是地图整体，Action是上下左右
四种可以采取的行动，无需再通过卷积神经网络读取游戏画面。

本项目提供了一个游戏环境，供他人自行编写新的agent或拓展游戏功能。