# Deep Reinforcement Learning 深層強化学習による Gluttonous Snake ゲーム　DRL_Snakey

深層強化学習によるGluttonous Snake(食いしん坊蛇)ゲームAIとゲーム環境

[![Build Status](https://travis-ci.org/cstrikest/DRL_Snakey.svg?branch=master)](https://travis-ci.org/cstrikest/DRL_Snakey)
![GitHub](https://img.shields.io/github/license/cstrikest/DRL_Snakey.svg)

![PyPI - Downloads](https://img.shields.io/pypi/dm/DRL_Snakey.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/cstrikest/DRL_Snakey.svg)

![PyPI](https://img.shields.io/pypi/v/DRL_Snakey.svg)
![GitHub release](https://img.shields.io/github/release/cstrikest/DRL_Snakey.svg)

[![Readme](https://img.shields.io/badge/Readme-Chinese-red.svg)](http://github.com/cstrikest/DRL_Snakey)
[![Readme](https://img.shields.io/badge/Readme-Japanese-orange.svg)](http://github.com/cstrikest/DRL_Snakey/blob/master/README-JP.md)


![ゲームスタート画面](https://github.com/cstrikest/ML_Snakey/blob/master/images/gamestart_image.png?raw=true)

## 開発環境

Pythonバージョン: Python3.6または以上のバージョン

### 外部ライブラリー

* pygame
* tensorflow / tensorflow-gpu
* h5py
* numpy
* matplotlib

## ゲームの説明

**デモスクリプト: Snakey_play.py**

このスクリプトはDRL_Snakeyパッケージと関係なく、AI部分は含まれていない人間が遊べるゲー
ムのデモスクリプトである。

パッケージを使用する前にこのスクリプトを実行してみよう。

![ゲーム開始画面](https://github.com/cstrikest/ML_Snakey/blob/master/images/game_image.png?raw=true)

### ゲームのルール

基本的には蛇をコントロールして食べ物を食べながら自分を咬まないようにゲームを進む。食物を
食べると蛇自分の長さも伸びるので難易度がどんどん増えでいく。一応ボムのルールが入っている
が、普通はボムなしにする。

人間プレーヤーがゲームを遊ぶとき、スピードレベルがあり、食物を5個食べると蛇のスピードが
上がる。

ゲームは大きさ200×200ピクセル平面に行い、10×10ピクセルごとにブロックとして表す。ゲーム
画面の右側はディテールエリアである。

方向キーで蛇をコントロールすることができ、いつでも`Q`を押してゲームを閉じられる。ゲーム
中にで`P`は一時停止、そして`N`はステッピングモードに変え、`F`はビジュアルモードに変える。

ゲームオーバーするとゲームオーバー画面に入り、`R`を押すとゲームをやり直す。`S`はスコア
ボード。

### AI部分の説明

AIにはゲームのスピードやレベルが意味なし、そしてゲームUIのFPS値より一番速いスピードで実
行する。（だが計算が思い場合FPSに達せないという状況もよくでる。）

デモスクリプトを除き、ゲームは主に**ゲームルール**、**UIエンジン**、**エージェント**
3部分で構成され、UIがなくてもゲームを実行することができる。

本プロジェクトの中にいくつのAIスクリプトがあり、また以下に説明する。

**ゲーム中に`F`キーを押すとビジュアルモードに変えることができる、どうぞ活用してください。**

### パッケージの使用方法

まずパッケージを導入する

    import DRL_Snakey as Snakey
    
ゲームオブジェクトを宣言する。このクラスはゲームルールだけが入っている。(DRL_Snakey.Game)。

    game = Snakey.Game()
    
ゲームをコントロールするagentオブジェクト。ここで簡単なロジックaengtお使って例を挙げる。

    agent = Snakey.agent.Logic()
    
pygameを使うゲームUIオブジェクト。
    
    ui = Snakey.UI()
    
UIクラスのshow(game, agent)関数でゲーム画面を起動する。

    ui.show(game, agent)

agentのトレーニングが必要とかUIがいらないときは、以下のスクリプトを使う。

    import DRL_Snakey as Snakey
    
    
    game = Snakey.Game()
    agent = Snakey.agent.Logic()
    
    while True:
        game.next_step(agent.get_next_direction(game))
        if game.deathflag:
            print("Gameover. score:", game.ate)
            game.reset()
            
## DRL_Snakeyの説明

DRL_Snakeyは主に、ゲームの基盤`DRL_Snakey.core`，agent`DRL_Snakey.agent`とツール
`DRL_Snakey.utlis`3部分に分けている。

その中の`DRL_Snakey.core.Game`はゲームの基盤ルールで，デス判定や地図の処理機能があ
り、ゲームの本体として扱う。
`DRL_Snakey.core.UI`はUI関連であり、pygameを使って画面を作る。。

`DRL_Snakey.agent`は知能体agnet部分である、中には幾つのAIクラスがある。Agentが
ゲームの状態を読み込み、そしてそれに対応する蛇の向きを決定する。

Agentクラスのストラクチャー:

    class Agent(object):
	def get_next_direction(self, Game):
		"""
		知能体がゲームの状態に基づく判断により、蛇の向きを決定する。
		:return: 方向["W", "S", "A", "D"]
		"""
		pass
	
	def custom_function(self, Game):
		"""
		カスタム関数。
		"""
		pass

`DRL_Snakey.core.snake`の中には、`Snake`というクラスでゲームの蛇を表す。

ps. 興味があればどうぞ自分のAgentを書き、そしてpull requestしてお願いしますね。

### DRL_Snakey.agent.Logic_AI.Logic

簡単なデモンストレーション用Agentで、ボムを完全に無視して食物だけ狙っていくアルゴリズムである。

蛇の頭の座標と食物の座標を比べ、その水平と垂直の差を使って向きを判断する。

このAIはゲーム20回のうちに最高得点が68，平均値は49.6である。

![简易AI演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/Logic_play.gif?raw=true)

### DRL_Snakey.agent.DP_AI.DP

DP(Dynamic Programming)マルコフ決定過程-動的計画法。

ベルマン最適方程式を使って方策往復を行い、地図の中の各ボロックの価値を計算する。そして
周りの一番価値高いボロックにいく。

コンストラクタパラメータの説明:

* `discount`: 減衰率
* `iteration`: 往復回数
* `walk_reward`: 歩きの報酬
* `eat_self_reward`: 自分を咬んだ報酬
* `food_reward`: 食物を食べた報酬

`F`を押してビジュアルモードに変え、詳しく各ボロックの価値を見ることができる。

実際に実行してみると、AIが価値の判断により、場所が危険な食物をしばらく放置し、安全になる
まで遠回りをして待つ。

このAIはゲーム20回のうちに最高得点が119，平均値は69.2である。（最適パラメータ）

![DP演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/DP_play.gif?raw=true)

### DRL_Snakey.agent.MC_AI.MC

MC(Monte-Calo)モンテカルロ法。

毎回歩くときある方策により三つの可能か方向の平均動作価値を計算し、そのうちの
一番価値高い方向を選択して歩く。本AIが使用されている基本方策は`DRL_Snakey.agent.Logic_AI.Logic`
である。

コンストラクタパラメータの説明:

* `discount`: 減衰率
* `iteration`: 往復回数
* `max_step`: 予測最大歩き回数
* `epsilon`: 探索率
* `walk_reward`: 歩きの報酬
* `eat_self_reward`: 自分を咬んだ報酬
* `food_reward`: 食物を食べた報酬

このAIはゲーム20回のうちに最高得点が89，平均値は50.5である。

![MC演示](https://github.com/cstrikest/ML_Snakey/blob/master/images/MC_play.gif?raw=true)
