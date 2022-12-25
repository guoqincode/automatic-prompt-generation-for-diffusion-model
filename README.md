<<<<<<< HEAD
# automatic-prompt-generation-for-stable-diffusion
automatic prompt generation for stable diffusion
=======
# Twitcher

This project aims to develop an application using citizen science approach to crowd-source bird population dynamics information. The application provides a platform for amateur and professional birdwatchers to upload bird sighting reports that will form a database including time, species, and location data. Scientists may use the information in the database to analyze the distribution and dynamics of bird populations. While various existing citizen science databases also provide some of these functionalities, our platform is unique because it allows birders to help each other with bird identification and implements quality control procedures based on a ranking of user contributions. Our platform will reduce the uncertainties that often hamper the use of citizen science data, provide a user-friendly platform for birdwatchers to keep track of their sightings, and foster a lively community among bird enthusiasts.

Twitcher is a web application to bridge the gaps between scientists' need for more accurate and reliable data and amateur birders' demand for an accessible bird report platform. The app will allow birders to submit bird observational reports and to ask for help in the community when having difficulties to identify birds. A birder can use the app to see what are the bird species observed in theirs cities, learn the description and distribution of various bird species, use the app to keep track of their species lists, and share their achievements on social media platforms. By creating a fun, accessible tool for amateur users, we hope our platform can attract more users to submit their bird observation reports, and ultimately providing higher quality data for professional scientists. We also decided to not have a mobile client because according to conversations with birders, most of them have a habit of carrying a notebook and recording specific locations (longitude, lattitude) and other relevant information immediately and can upload to the web client later. Also, many places of bird-sightings may not have signal to enable the submission of reports immediately.

**Advisors** 

| Name | JHU Email | GitHub Username |
| ---- | --------- | --------------- |
|  Nick Xitco    |  nxitco@jhu.edu   |   NickXitco          |


## Installing / Getting started

A quick introduction of the minimal setup you need to get the app up & running.

```shell
git clone https://github.com/cs421sp21-homework/project-g03.git
cd project-g03
cd code

# Install all the dependencies for the frontend
cd frontend
npm install
npm start (to run)

# Direct to api folder
cd ..
cd api

# Install python modules for backend (install python3, venv first if needed)
python -m venv birdy-env
./birdy-env/bin/activate # In Windows, use '.\birdy-env\Scripts\activate' instead
pip install -r requirements.txt
flask run (to run)

# Note everytime you want to run, you need to activate virtual environment again
```

Here you should say what actually happens when you execute the code above.



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

Explaining what database (and version) has been used. Provide download links.

### Deploying / Publishing

auto generate doc

Once you are in the virtual environment with sphinx installed, go to ./code/api/docs and simply run
```
make html
```
to generate the documentation in `docs/build`. These docs are autogenerated from
the docstring comments in python.


Application deployed (up to date): https://rocky-anchorage-47653.herokuapp.com/

API deployed (up to date): https://cs421sp21-g03-twitcher-api.herokuapp.com/
>>>>>>> b1c03cb (first command)
