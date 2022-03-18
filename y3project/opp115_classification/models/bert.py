# coding: UTF-8
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer


class Config(object):

    """配置参数"""
    def __init__(self, dataset):
        self.model_name = 'bert'
        self.train_path = dataset + '/data/train.csv'                                # 训练集
        self.dev_path = dataset + '/data/dev.csv'                                    # 验证集
        self.test_path = dataset + '/data/test.csv'                                  # 测试集
        
        self.class_list = [x.strip() for x in open(
            dataset + '/data/class.txt', encoding='utf-8').readlines()]              # 类别名单
        self.save_path = dataset + '/saved_dict/' + self.model_name + '.ckpt'        # 模型训练结果
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   # 设备调整

        self.require_improvement = 1000                                 # early stopping 若超过1000batch效果还没提升，则提前结束训练

        self.num_classes = len(self.class_list)                         # 类别数
        self.num_epochs = 10                                             # epoch数
        self.batch_size = 64                                           # mini-batch size

        self.pad_size = 100                                              # length of the sentence(短填长切)
        # 长于截断，短填充
        self.learning_rate = 3e-5                                       # 学习率
        self.bert_path = 'bert-base-uncased' 
        # version
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_path)
        # tokennizer of bert
        self.hidden_size = 768


class Model(nn.Module):

    def __init__(self, config):
        super(Model, self).__init__()
        self.bert = BertModel.from_pretrained(config.bert_path)
        for param in self.bert.parameters():
            param.requires_grad = True
        self.fc = nn.Linear(config.hidden_size, config.num_classes)

    def forward(self, x):
        # input secntence
        # 对padding部分进行mask，和句子一个size，padding部分用0表示？？？？
        outputs = self.bert(input_ids=x[0], attention_mask=x[2])
        pooled = outputs[1]
        out = self.fc(pooled)
        return out
