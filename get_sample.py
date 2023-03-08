import json
from random import choice

sampled_file_path = 'data/sampled_50k.json'
dataset = []
with open(sampled_file_path,encoding='utf-8') as file:
  s = file.readline()
  jdata = json.loads(s)
  for d in jdata:
      if d['rating']==None:
        continue
      dataset.append(d)
