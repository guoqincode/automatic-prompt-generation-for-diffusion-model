import logging
import math
import os
import sys
from dataclasses import dataclass, field
from itertools import chain
from typing import Optional

import datasets
from datasets import load_dataset
from absl import app, flags
import evaluate
import transformers
from transformers import (
    CONFIG_MAPPING,
    MODEL_FOR_CAUSAL_LM_MAPPING,
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    default_data_collator,
    is_torch_tpu_available,
    set_seed,
)
from transformers.testing_utils import CaptureLogger
from transformers.trainer_utils import get_last_checkpoint
from transformers.utils import check_min_version
from transformers.utils.versions import require_version
import torch
import logging

FLAGS = flags.FLAGS
flags.DEFINE_string('pre_path', './temp/checkpoint-40000/', help='pretrained_checkpoint')
flags.DEFINE_string('ini_query', "a iron man", help='initial query for user to input')

flags.DEFINE_integer('max_length', 100, help='maximum length for input text')
flags.DEFINE_float('temperature', 0.8, help="temperature for text-generation model")
flags.DEFINE_float('top_k', 0, help="selected top k or not")
flags.DEFINE_float('top_p', 0.9, help="select top p sample to return")


def main(argv):
    model_path  =  FLAGS.pre_path
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    config = AutoConfig.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

    text =  "<BOS> "
    text += FLAGS.ini_query
    encoded_input = tokenizer.encode(text)
    model = model.cuda()
    output_sequences = model.generate(
        input_ids=torch.tensor([encoded_input]).cuda(),
        max_length=FLAGS.max_length,
        temperature=FLAGS.temperature,
        top_k=FLAGS.top_k,
        top_p=FLAGS.top_p,
        repetition_penalty=1.0,
        do_sample=True,
        num_return_sequences=1,
    )
    output = tokenizer.decode(output_sequences[0]).split('<EOS>')[0].split('<BOS>')[1]
    logging.info(output)


if __name__ == '__main__':
    app.run(main)