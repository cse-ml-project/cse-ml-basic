### linux VM 설치
password 방식으로 설정

### xrdp 설치
https://docs.microsoft.com/ko-kr/azure/virtual-machines/linux/use-remote-desktop

### xfce4 설치
```
sudo apt-get update

sudo apt-get install xfce4

sudo apt-get install xrdp

echo xfce4-session >~/.xsession

sudo service xrdp restart
```

Tab Key not working when using Xfce desktop
https://www.starnet.com/xwin32kb/tab-key-not-working-when-using-xfce-desktop/

### Visual Studio code 설치
https://code.visualstudio.com/Download

ubuntu visual studio code not work - xrdp
https://stackoverflow.com/questions/36694941/visual-studio-code-1-fails-to-launch-on-ubuntu-using-xrdp

sudo sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/lib/x86_64-linux-gnu/libxcb.so.1

### tf 설치
설치 링크 
https://www.tensorflow.org/install/  

1. docker - 격리된 환경에서 수행
```
sudo apt-get install docker
docker run -it gcr.io/tensorflow/tensorflow bash
```

2. native pip
```
sudo apt-get install python3-pip python3-dev
pip3 install tensorflow
```

3. validation 수행
```
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

4. MNIST 처리
tf-mnist-softmax.py  
tf-mnist-cnn.py  
참조