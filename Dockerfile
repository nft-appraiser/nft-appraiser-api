FROM python:3.8.10

RUN apt update
RUN apt upgrade -y
RUN apt install -y libgl1-mesa-dev emacs vim git

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install \
  django numpy pandas scikit-learn requests cairosvg opencv-python pillow tqdm ipywidgets tensorflow==2.6.0 cloudpickle \
  matplotlib==3.4.3
RUN pip install keras==2.6

ADD . /root
RUN git clone https://github.com/rishigami/Swin-Transformer-TF.git
RUN cp -rp /Swin-Transformer-TF /root/Swin-Transformer-TF
RUN rm -r /Swin-Transformer-TF
