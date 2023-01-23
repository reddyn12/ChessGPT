


import os
from tqdm import tqdm
import numpy as np
from datasets import load_dataset # huggingface datasets
import customToken
import sys

# #%%
# print(len(customToken.tokens))

# #%%
# import tiktoken
# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2

#iLab1 num_pro=8 works no errors
num_proc = 3

dpath = "dataPre/KingBase2019/kingCleanV2.pgn"
dataset = load_dataset("text", data_files=dpath)


# owt by default only contains the 'train' split, so create a test split
split_dataset = dataset["train"].train_test_split(test_size=0.0005, seed=2357, shuffle=True)
split_dataset['val'] = split_dataset.pop('test') # rename the test split to val


# snc = tiktoken.get_encoding("gpt2")
# snc.encode_ordinary()




def process(example):
    # print(example["text"], "this is a prob")
    # if("*" in example["text"]):
    #     print(example["text"])
    #     sys.exit()
    ids = customToken.tokenize(example["text"])
    ids.append(customToken.eos_token_id)
    out = {"ids": ids, "len":len(ids)}
    return out

tokenized = split_dataset.map(
    process,
    remove_columns=['text'],
    desc="tokenizing the splits",
    #num_proc=num_proc,
)


#sys.exit()
for split, dset in tokenized.items():
    arr_len = np.sum(dset['len'])
    filename = os.path.join(os.path.dirname(__file__),"data", "KingBase" ,f'{split}.bin')
    dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
    arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

    print(f"writing {filename}...")
    idx = 0
    for example in tqdm(dset):
        arr[idx : idx + example['len']] = example['ids']
        idx += example['len']
    arr.flush()



# to read the bin files later, e.g. with numpy:
# m = np.memmap('train.bin', dtype=np.uint16, mode='r')