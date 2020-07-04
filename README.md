# 2020-1.VideoCaptioning
2020-1. SEJONG.UNIV_창의학기제 : 저화질 영상에 대한 Video Captioning 네트워크 성능 향상 연구

---

# Environment

- linux 18.04 + docker
- cuda 8.0
- caffe
- python 2.7

---

# 연구의 과정

- 1주차 : Video Captioning 논문 조사 및 CNN 학습 및 점수 비교
    - [S2VT 논문 이해]()
    - [COCO 지표 결합 및 고화질 Video Captioning 논문 평가점수 복원_]()

- 2주차 : 저화질 영상 생성 알고리즘 개발과 저화질 영상에 기존의 Video Captioning 네트워크 적용

- 3주차 : 저화질 Video Captioning 성능 향상 연구

- 마무리 보고서

---

# Datasets 

### MSVD

Microsoft Video Description (MSVD) dataset comprises of 1,970 YouTube clips with human annotated sentences written by AMT workers. The audio is muted all clips to avoid bias.
The play-time of each video in the dataset is usually between 10 to 25 seconds mainly showing one activity. The orignal datasets description comprises multilingual description. This project'll use English description. and Almost all research groups have split this dataset into training, validation and testing partitions of 1200, 100 and 670 videos respectively. thus, I use splited dataset form( training, validation and testing partitions of 1200, 100 and 670 videos ).

---

# Reference

- Paper  
    - Captioning
        - [S2VT ( Sequence to Sequence Video to Text )](https://vsubhashini.github.io/s2vt.html)  
        - [Reconstruction Network for Video Captioning](https://arxiv.org/pdf/1504.00325.pdf)  
        - [Microsoft COCO Captions : Data Collection and Evaluation Server](https://arxiv.org/pdf/1803.11438.pdf)  
    - CNN Feature
        - [Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/pdf/1602.07261.pdf)
        - [VGG16 : Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556.pdf%20http://arxiv.org/abs/1409.1556.pdf)
  
- Github  
    - [S2VT](https://github.com/vsubhashini/caffe/tree/recurrent/examples/s2vt)
    - [CNN FEATURES]()

---

## 이용 Caffe 버전 - recurrent ([Github link](https://github.com/vsubhashini/caffe/tree/recurrent/examples/s2vt) )
### 해당 Caffe는 recurrent 라는 브런치. 최신화할 경우 /examples/S2VT 가 존재하지않음에 주의.
Caffe is a deep learning framework made with expression, speed, and modularity in mind.
It is developed by the Berkeley Vision and Learning Center ([BVLC](http://bvlc.eecs.berkeley.edu)) and community contributors.

Check out the [project site](http://caffe.berkeleyvision.org) for all the details like

- [DIY Deep Learning for Vision with Caffe](https://docs.google.com/presentation/d/1UeKXVgRvvxg9OUdh_UiC5G71UMscNPlvArsWER41PsU/edit#slide=id.p)
- [Tutorial Documentation](http://caffe.berkeleyvision.org/tutorial/)
- [BVLC reference models](http://caffe.berkeleyvision.org/model_zoo.html) and the [community model zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo)
- [Installation instructions](http://caffe.berkeleyvision.org/installation.html)

and step-by-step examples.

[![Join the chat at https://gitter.im/BVLC/caffe](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/BVLC/caffe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Please join the [caffe-users group](https://groups.google.com/forum/#!forum/caffe-users) or [gitter chat](https://gitter.im/BVLC/caffe) to ask questions and talk about methods and models.
Framework development discussions and thorough bug reports are collected on [Issues](https://github.com/BVLC/caffe/issues).

Happy brewing!

## License and Citation

Caffe is released under the [BSD 2-Clause license](https://github.com/BVLC/caffe/blob/master/LICENSE).
The BVLC reference models are released for unrestricted use.

Please cite Caffe in your publications if it helps your research:

    @article{jia2014caffe,
      Author = {Jia, Yangqing and Shelhamer, Evan and Donahue, Jeff and Karayev, Sergey and Long, Jonathan and Girshick, Ross and Guadarrama, Sergio and Darrell, Trevor},
      Journal = {arXiv preprint arXiv:1408.5093},
      Title = {Caffe: Convolutional Architecture for Fast Feature Embedding},
      Year = {2014}
    }
