FROM python:3.8.10

WORKDIR /code
RUN apt update
RUN apt upgrade -y
RUN apt install -y libgl1-mesa-dev emacs vim git npm curl
RUN curl -sL curl -fsSL https://deb.nodesource.com/setup_16.x | bash - 
RUN apt install -y nodejs
RUN npm install -g create-react-app
RUN npm install react-dropzone
RUN npm install -D webpack webpack-cli 
RUN npm install @babel/preset-react babel-loader --dev

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install \
  django djangorestframework numpy pandas scikit-learn requests cairosvg opencv-python pillow tqdm ipywidgets tensorflow==2.6.0 cloudpickle \
  matplotlib==3.4.3
RUN pip install keras==2.6

ADD . /root
WORKDIR /
RUN git clone https://github.com/rishigami/Swin-Transformer-TF.git
RUN cp -rp /Swin-Transformer-TF /root/code/Swin-Transformer-TF
RUN rm -r /Swin-Transformer-TF
