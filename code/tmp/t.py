import torch
import torch.nn as nn

gru = nn.GRU(input_size=50, hidden_size=50, batch_first=True)


embed = nn.Embedding(3, 50)


x = torch.LongTensor([[0, 1, 2]])  # x.size() --> torch.Size([1, 3])


x_embed = embed(x)  # x_embed.size() --> torch.Size([1, 3, 50])

x = torch.LongTensor([[0, 1, 2], [0, 1, 2]])  
x_embed = embed(x)
print(x_embed.size())   

# =======> torch.Size([2, 3, 50])
out, hidden = gru(x_embed)  



out.size() 
#  =======> torch.Size([2, 3, 50])
print(hidden.size()) 
#  =======> torch.Size([1, 2, 50])