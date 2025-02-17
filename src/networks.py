import torch
import torch.nn as nn
import torch.nn.functional as F


# inspired from https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
class LeNet(nn.Module):

    def __init__(self):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5, padding='same')
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)  # images are 5x5 with 16 channels
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x, use_dropout=False):                # (N, 28, 28), where N is batch size

        x = F.relu(self.conv1(x))                           # (N, 6, 28, 28)
        x = F.max_pool2d(x, kernel_size=2)                  # (N, 6, 14, 14)

        x = F.relu(self.conv2(x))                           # (N, 16, 10, 10)
        x = F.max_pool2d(x, kernel_size=2)                  # (N, 16, 5, 5)

        x = torch.flatten(x, 1)                             # (N, 16*5*5) = (N, 400)

        x = F.dropout(x, p=0.25, training=use_dropout)      # (N, 400)
        x = F.relu(self.fc1(x))                             # (N, 120)

        x = F.dropout(x, p=0.5, training=use_dropout)       # (N, 120)
        x = F.relu(self.fc2(x))                             # (N, 84)

        x = self.fc3(x)                                     # (N, 10)
        return x
