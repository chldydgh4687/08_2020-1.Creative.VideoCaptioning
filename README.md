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
    - [S2VT 논문 이해](https://github.com/chldydgh4687/2020-1.VideoCaptioning/wiki/%5B-S2VT-%5D-Sequence-to-Sequence-Video-to-Text)
    - [COCO 평가 코드 임포트 및 고화질 Video Captioning 논문 평가점수 복원]()

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
    - [CNN FEATURES](https://github.com/hobincar/pytorch-video-feature-extractor)
    - [COCO Captions](https://github.com/salaniz/pycocoevalcap)
---

## 이용 Caffe 버전 - recurrent ([Github link](https://github.com/vsubhashini/caffe/tree/recurrent/examples/s2vt) )
- 해당 Caffe는 recurrent 라는 브런치. 최신화할 경우 /examples/S2VT 가 존재하지않음에 주의.
