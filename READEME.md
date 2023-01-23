# 项目信息
用于给智能设备做语音服务
# 版本信息
V0.1.2
具体改动：验证了可移植性，可以在Linux和Windows上运行
日期：2022.12.16 23：42

# 作者信息
作者：杨康震
QQ：2737312763
# 部署流程
1. 安装ffmpeg,espeak并放到系统路径
2. 注意，库安装ffmpeg-python而不是python-ffmpeg或者ffmpeg
3. 安装Whisper所需要的库文件,torch需要自行安装，版本推荐1.12.1，cuda16，gpu版本 
4. 安装picovoice的VAD和KWS库
5. 训练自己的KWS模型
6. 使用时注意替换picovoice_kws.py内的模型名称

~~~
sudo apt-get install ffmpeg
sudo apt-get install espeak
pip install ffmpeg-python
#whisper依赖安装
#conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch
#或者
#conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
pip install pvcobra
pip install pvporcupine
pip install pvrecorder
pip install tqdm
pip install transformers==4.25.1

