import torch

model = torch.load("latest.pth", map_location=torch.device('cpu'))
dic = {}
for i, key in enumerate(model['state_dict']):
    model['state_dict'][key]=model['state_dict'][key]
for key in model:
    dic[key]=model[key]
torch.save(dic,'weights.pth', _use_new_zipfile_serialization=False)
