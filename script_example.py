import DRL_Snakey as Snakey

game = Snakey.Game()
agent = Snakey.agent.MC()
UI = Snakey.UI()
UI.show(game, agent)