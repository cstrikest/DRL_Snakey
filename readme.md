# 贪吃蛇游戏 机器学习AI
使用神经网络训练一个可以玩贪吃蛇游戏的AI。

Python版本 Python3.6

依赖库

- pygame 1.9.5
- tensorflow / tensorflow-gpu

## 游戏部分说明

#### Snakey_UI.py

![游戏开始界面](https://github.com/cstrikest/ML_Snakey/blob/master/images/gamestart_image.png?raw=true)

提供了一个可以供人类游玩的贪吃蛇游戏UI。游戏素材图片比较简陋。游戏内容设有等级划分，随着获取食物的数量上升，蛇前进的速度会变快。

同时每增加一个难度会多出现一个触碰到便会游戏结束的炸弹。

游戏在一个200×200像素的平面中运行，每10×10个像素作为一个单元。 右侧有计分面板。

游戏右侧是一个100×200像素的信息面板。主要用到的信息会在右侧给出

使用WSAD控制移动方向，任何时候都可以使用Q键退出。

游戏结束画面按R重新开始，按S则会跳出计分板。

![游戏面板](https://github.com/cstrikest/ML_Snakey/blob/master/images/game_image.png?raw=true)

#### Snakey_core.py

为了给模型训练加快速度的游戏核心逻辑类。只保留游戏规则，舍弃所有UI相关，提升训练时的速度。

#### Snakey_UI_AI_interface.py

非人类玩家的游戏UI，目前是通过AI_core_logic.py中get_next_direction()来获取下一步的方向信息。

之后还会使用通过神经网络训练出的模型进行游戏控制。

现阶段可直接运行此脚本观看基于AI_core_logic.py的AI游戏过程。

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