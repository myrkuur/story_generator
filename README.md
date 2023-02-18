# Story Generator
Using T5 and keytotext generate short sentences in style of LOTR

## Introduction 
### Training
For training `t5-base` is used and after lots of cleaning the model was finetunned for 3 epochs on google colab gpus; training not book is available at `notebooks`.

<hr>

### Web App
Using `FastApi` a web app was designed for more user friendly interactions. After running the app you can choose the file with image of a car and see the results, **Note:** that if you are running the app for the first time it will take a bit because it needs to download trained models from google drive.
<hr><hr>

## How to install
1. Clone the repo into your local device.
2. Move to clone project directory (you should be in `story_gen`)
3. Create conda virtual environment using command below: (you can change environment name to what you like, here we choose `story_gen`)
    ```
    conda create -n story_gen python=3.7 anaconda
    ```
4. Activate your environment using command below:
    ```
    conda activate story_gen
    ```
5. Install requirements using command below:
    ```
    pip install -r requirements.txt
    ```
6. Move to `/src` using command below:
    ```
    cd src
    ```
7. Run the following command to start the app:
    ```
    uvicorn main:app --reload
    ```
8. After app starts, open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
<hr><hr>

## Challenges And Improvement Ideas:
1. Right now the model only has seen LOTR style, in the future might be nice to add other styles.
2. Training data is really few and some other generative models like `gpt2` will not preform well, so it would be great to work on gathering more data.
3. Although lots of preprocessing was done one the text it still needs more cleaning.
