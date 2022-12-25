automatic prompt generation for stable diffusion
=======
# Introduction

This project is to help users better use text-to-image models such as Stable Diffusion. When users would like to generate some objects or certain landscapes, but the input prompts are too simple, resulting in relatively low quality output images and relatively monotonous content, this project is finetune GPT-2 on DiffusionDB for to realize the mapping of users' simple prompts to complex prompts.

Twitcher is a web application to bridge the gaps between scientists' need for more accurate and reliable data and amateur birders' demand for an accessible bird report platform. The app will allow birders to submit bird observational reports and to ask for help in the community when having difficulties to identify birds. A birder can use the app to see what are the bird species observed in theirs cities, learn the description and distribution of various bird species, use the app to keep track of their species lists, and share their achievements on social media platforms. By creating a fun, accessible tool for amateur users, we hope our platform can attract more users to submit their bird observation reports, and ultimately providing higher quality data for professional scientists. We also decided to not have a mobile client because according to conversations with birders, most of them have a habit of carrying a notebook and recording specific locations (longitude, lattitude) and other relevant information immediately and can upload to the web client later. Also, many places of bird-sightings may not have signal to enable the submission of reports immediately.

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

## Preparing datasets for training

The training and evaluation scripts operate on datasets stored as multi-resolution TFRecords. Each dataset is represented by a directory containing the same image data in several resolutions to enable efficient streaming. There is a separate *.tfrecords file for each resolution, and if the dataset contains labels, they are stored in a separate file as well. By default, the scripts expect to find the datasets at `datasets/<NAME>/<NAME>-<RESOLUTION>.tfrecords`. The directory can be changed by editing [config.py](./config.py):

```
result_dir = 'results'
data_dir = 'datasets'
cache_dir = 'cache'
```

To obtain the FFHQ dataset (`datasets/ffhq`), please refer to the [Flickr-Faces-HQ repository](https://github.com/NVlabs/ffhq-dataset).

To obtain the CelebA-HQ dataset (`datasets/celebahq`), please refer to the [Progressive GAN repository](https://github.com/tkarras/progressive_growing_of_gans).

To obtain other datasets, including LSUN, please consult their corresponding project pages. The datasets can be converted to multi-resolution TFRecords using the provided [dataset_tool.py](./dataset_tool.py):

```
> python dataset_tool.py create_lsun datasets/lsun-bedroom-full ~/lsun/bedroom_lmdb --resolution 256
> python dataset_tool.py create_lsun_wide datasets/lsun-car-512x384 ~/lsun/car_lmdb --width 512 --height 384
> python dataset_tool.py create_lsun datasets/lsun-cat-full ~/lsun/cat_lmdb --resolution 256
> python dataset_tool.py create_cifar10 datasets/cifar10 ~/cifar10
> python dataset_tool.py create_from_images datasets/custom-dataset ~/custom-images
```

## Training networks

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


## Database

Our dataset is DIFFUSIONDB. DIFFUSIONDB is the first large-scale dataset containing 14 million Stable Diffusion images and their text prompts and hyperparameters. This dataset provides exciting research opportunities in prompt en- gineering, deepfake detection, as well as understanding and debugging large text-to-image generative models and its github is https: //poloclub.github.io/diffusiondb.

