# 贪吃蛇游戏 机器学习AI

使用神经网络训练一个可以玩贪吃蛇游戏的AI。

![游戏开始界面](https://github.com/cstrikest/ML_Snakey/blob/master/images/gamestart_image.png?raw=true)

## 游戏说明

### 规则

游戏素材图片比较简陋。人类玩家游玩时，游戏内容设有等级划分，随着获取食物的数量上升，蛇前进的速度会变快。

同时每增加一个难度会多出现一个触碰到便会游戏结束的炸弹。

游戏在一个200×200像素的平面中运行，每10×10个像素作为一个单元。 右侧有计分面板。

游戏右侧是一个100×200像素的信息面板。主要用到的信息会在右侧给出。

使用WSAD控制移动方向，任何时候都可以使用Q键退出。

游戏结束画面按R重新开始，按S则会跳出计分板。

### AI部分说明

AI没有游戏的速度区别与等级区分，在有UI的模式下默认使用最快的刷新速度。

除单独存在的演示脚本外，AI部分主要由**物理引擎**，**图形引擎**，**决策逻辑**三部分组成，运行时可以根据需要选择是否加载图形引擎显示游戏界面。

本项目内拥有数个AI逻辑脚本，详细见下文的各脚本说明。

## 环境

Python版本 Python3.6

###外部依赖

* pygame
* tensorflow / tensorflow-gpu
* h5py
* numpy

## 各脚本说明

#### Snakey_UI.py

与其他脚本无关，作为示例的一个单独脚本，提供了供人类游玩的UI。

![游戏面板](https://github.com/cstrikest/ML_Snakey/blob/master/images/game_image.png?raw=true)

#### Game_demonstration.py

演示用脚本，展示了各部分的使用方法。

现阶段可直接运行此脚本观看基于AI_core_logic.py的AI游戏过程。

#### Snakey_core.py

游戏的物理引擎。简化了所有UI部分关联，整合为一个Snakey类。

#### Snakey_UI_core.py

游戏的图形引擎，将游戏过程可视化。

#### AI_core_logic.py AI_core_logic_test.py

一个简单的演示用AI，完全无视炸弹，只吃食物。具有十分简单的自身躲避算法。

经过测试(AI_core_logic_test.py)，此AI在10000次尝试中最好成绩为101，
平均值为47.8496。平均每局游戏耗时0.00888秒。

![简易AI演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/2.gif?raw=true)

#### AI_core_ML.py AI_core_ML_test.py

基于tensorflow.keras的机械学习AI。目前尚未完成，详细内容将在以后说明。

#### training.py

目前尚未完成，用于AI模型训练。

设想：使用强化学习，目标为给定步数内的最高得分。训练先在无炸弹的条件下进行。

## ML部分

...