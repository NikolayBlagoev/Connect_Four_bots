from smart_agent import Smart_Agent
from game import Game
from time import sleep
import copy
import torch
import torch.nn as nn
class Net(nn.Module):
    
    def __init__(self):

        super(Net, self).__init__()
        self.trainingNow = False
        self.conv1 = nn.Conv2d(1, 12, kernel_size=3, padding=2)
        self.conv2 = nn.Conv2d(12, 24,kernel_size=3)
        self.conv3 = nn.Conv2d(24, 24,kernel_size=1,stride = 1)

        self.relu = nn.ReLU()
        self.max2d = nn.MaxPool2d((2,2))
        self.layer1 = nn.Linear(96, 96)
        self.layer2 = nn.Linear(96, 3)
        self.tan = nn.Tanh()
        self.flat = nn.Flatten()
 
    def forward(self, x):
        x = x.view(-1, 1, 7, 6)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.max2d(x)
        x = self.conv2(x)
        x = self.relu(x)
        intrm = self.conv3(x)
        intrm = self.relu(intrm)
        x = x + intrm
      
        
        x = torch.flatten(x,start_dim = 1)
       
        intrm = x
        x = self.layer1(x)
        x = self.layer2(self.tan(x + intrm) )
        return x
class Deep_Learning_Agent(Smart_Agent):
    def __init__(self, player, depth = 6) -> None:
        self.player = player
        self.depth = depth
        self.verbose = False
        self.net = Net()
        self.net.load_state_dict(torch.load("C4mod.pth"))
        print("READY!")
    def evaluate(self, board: Game):
        
        tens = torch.tensor(board.board).type(torch.FloatTensor).to("cpu")
        res = self.net(tens)[0]
        win_1 = res[2].item()
        win_2 = res[0].item()
        draw = res[1].item()
        if win_1 > win_2 and win_1 > draw:
            return win_1
        
        elif win_2 > win_1 and win_2 > draw:
            return win_2*-1
        elif draw > win_1 and draw > win_2:
            return (draw*-1)/2
        return 0
                
       


    