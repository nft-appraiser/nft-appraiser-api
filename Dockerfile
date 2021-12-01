FROM python:3.9

RUN apt update
RUN apt upgrade -y
RUN apt install -y libgl1-mesa-dev emacs vim

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install \
  django numpy pandas scikit-learn requests cairosvg opencv-python pillow tqdm ipywidgets tensorflow==2.6.0 cloudpickle \
  matplotlib==3.4.3

ADD . /root
