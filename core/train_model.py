import numpy as np
from bert4keras.backend import keras, set_gelu
from bert4keras.tokenizers import Tokenizer
from bert4keras.models import build_transformer_model
from bert4keras.optimizers import Adam, extend_with_piecewise_linear_lr
from bert4keras.snippets import sequence_padding, DataGenerator
from bert4keras.snippets import open
from bert4keras.layers import Lambda,Dense
import os

set_gelu('tanh')  # 切换gelu版本

num_classes = 2
maxlen = 128
batch_size = 32
BASE_DIR = os.path.dirname(__file__)
config_path = os.path.join(BASE_DIR, 'root/model/albert_small_zh_google/albert_config.json')
checkpoint_path = os.path.join(BASE_DIR,'root/model/albert_small_zh_google/albert_model.ckpt')
dict_path = os.path.join(BASE_DIR, 'root/model/albert_small_zh_google/vocab.txt')


def load_data(filename):
    """
    加载数据
    大条格式：（文本，标签id）
    """
    D = []
    with open(filename, encoding='utf-8') as f:
        for l in f:
            text, label = l.strip().split('\t')
            D.append((text, int(label)))
    return D


# 加载数据集
data_path = os.path.join(BASE_DIR, 'root/datasets')
train_data = load_data(os.path.join(data_path, 'train.txt'))
valid_data = load_data(os.path.join(data_path, 'valid.txt'))
test_data = load_data(os.path.join(data_path, 'test.txt'))

# 建立分词器
tokenizer = Tokenizer(dict_path, do_lower_case=True)


class data_generater(DataGenerator):
    def __iter__(self, random=False):
        pass



