automatic prompt generation for stable diffusion
=======
# Introduction

This project is to help users better use text-to-image models such as Stable Diffusion. When users would like to generate some objects or certain landscapes, but the input prompts are too simple, resulting in relatively low quality output images and relatively monotonous content, this project is finetune GPT-2 on DiffusionDB for to realize the mapping of users' simple prompts to complex prompts.

Twitcher 

**Advisors** 

| Name | RUC Email | GitHub Username |
| ---- | --------- | --------------- |
|  Hanzhong Guo    |  2022100402@ruc.edu.cn   |   Guohanzhong         |


## Installing / Getting started

A quick introduction of the minimal setup you need to get the app up & running.

```shell
git clone https://github.com/Guohanzhong/automatic-prompt-generation-for-diffusion-model.git
cd automatic-prompt-generation-for-diffusion-model

# Install all the dependencies for the frontend
pip install -r requirements.txt
```

## Demo for the Results


## Finetune GPT-2

Once the datasets are set up, you can train your own StyleGAN networks as follows:

1. Edit [train.py](./train.py) to specify the dataset and training configuration by uncommenting or editing specific lines.
2. Run the training script with `python train.py`.
3. The results are written to a newly created directory `results/<ID>-<DESCRIPTION>`.
4. The training may take several days (or weeks) to complete, depending on the configuration.

By default, `train.py` is configured to train the highest-quality StyleGAN (configuration F in Table 1) for the FFHQ dataset at 1024&times;1024 resolution using 8 GPUs. Please note that we have used 8 GPUs in all of our experiments. Training with fewer GPUs may not produce identical results &ndash; if you wish to compare against our technique, we strongly recommend using the same number of GPUs.

Expected training times for the default configuration using Tesla V100 GPUs:

| GPUs | 1024&times;1024  | 512&times;512    | 256&times;256    |
| :--- | :--------------  | :------------    | :------------    |
| 1    | 41 days 4 hours  | 24 days 21 hours | 14 days 22 hours |
| 2    | 21 days 22 hours | 13 days 7 hours  | 9 days 5 hours   |
| 4    | 11 days 8 hours  | 7 days 0 hours   | 4 days 21 hours  |
| 8    | 6 days 14 hours  | 4 days 10 hours  | 3 days 8 hours   |

```shell
python run_clm.py     --model_name_or_path gpt2   --train_file /mnt/guohanzhong/bingdialogue/promptreinforce/diffusiondb.txt  --per_device_train_batch_size 5     --per_device_eval_batch_size 4     --do_train     --do_eval     --output_dir /mnt/guohanzhong/bingdialogue/promptreinforce/temp/  --overwrite_output_dir True
```
## Database

Our dataset is DIFFUSIONDB. DIFFUSIONDB is the first large-scale dataset containing 14 million Stable Diffusion images and their text prompts and hyperparameters. This dataset provides exciting research opportunities in prompt en- gineering, deepfake detection, as well as understanding and debugging large text-to-image generative models and its github is [DiffusionDB](https://poloclub.github.io/diffusiondb)

Before the finetune model, we need to prepare the dataset of DiffusionDB, and we only need its text data at this stage, with a total of two million text data. The data format of the text data is shown below, each piece of data is a detailed user-written prompt, and this prompt can produce high-quality images.
```shell
<BOS> doom eternal, game concept art, veins and worms, muscular, crustacean exoskeleton, chiroptera head, chiroptera ears, mecha, ferocious, fierce, hyperrealism, fine details, artstation, cgsociety, zbrush, no background <EOS> 
```
The data can be obtained as follows.
