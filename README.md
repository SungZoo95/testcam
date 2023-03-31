# :musical_note: Project 우리 알리미 'SORI' 

<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/228908423-65d2812a-8034-43fd-979c-3553052841f8.PNG" width="200"></p>

<div align="center">
저시력자들을 위한 음성고지서 서비스 SORI입니다. 
데모 버전입니다.
</div>

------------------------------

<br>

</br>

## 💁 팀 구성  
|  팀  | 멤버     |      
|:-----:|:----------:|
|조장 김의석|<img src="https://user-images.githubusercontent.com/119566469/228912270-95157db4-8d2e-4a63-8f1c-a3bce062ec18.JPG" width = 150>| 
|객체팀(Text Detection(Yolov5)) <br>이한재  최성주|<img src="https://user-images.githubusercontent.com/119566469/228913186-aa0d59e6-6462-46b3-8282-2e1dd2f580f6.JPG" width = 150>  <img src="https://user-images.githubusercontent.com/119566469/228913198-ad1cc97e-0937-4b73-ac8d-be3912bec12c.JPG" width = 150>|
|텍스트팀(Text Recognition(Pytesseract)) <br> 김의석 박진호|<img src="https://user-images.githubusercontent.com/119566469/228912270-95157db4-8d2e-4a63-8f1c-a3bce062ec18.JPG" width = 150>  <img src="https://user-images.githubusercontent.com/119566469/228914447-d2da8896-61c8-4e38-83b2-d8bce609a2cf.JPG" width = 150>|
|보이스팀(Voice(TensorflowTTS)) <br> 고준성 김수윤|<img src="https://user-images.githubusercontent.com/119566469/228914919-0eefb368-1855-4d2b-8a5b-0925407c42c1.JPG" width = 150>  <img src="https://user-images.githubusercontent.com/119566469/228914945-2e90b14a-2cf5-4e6e-a9a9-b68444df74f4.JPG" width = 150>|

------------------------------------

## 아이디어 구상 
저시력자들을 대상으로 QR코드를 이용하여 고지서의 내용을 음성으로 전환해주는 서비스가 존재하나 몇가지 문제로 서비스의 제한이 많아 무용지물 상태라는 뉴스를 보았습니다.<br>
저희는 QR코드가 아닌 고지서 전체를 찍으면 음성으로 안내해주는 서비스를 도전했습니다.


<br>

</br>

## 📜 사용환경
### Languege 
- Python
### Text Detection
- CUDA 11.2 - torch 1.7.1 - torchvision 0.8.2
- Fine tuning form YoloV5 pretrained weights
- opencv - Python 4.7.0.72

### Text Recognition
- tesseract 5.3.0

### Voice 
- Window 11
- WSL2: Ubuntu 22.04 LTS
- Python>=3.8 
- GPU: GeforceRTX 3080ti
- CPU: AMD Ryzen 7 5800X 8-Core Processor
- RAM == 64.0GB 

<br>

</br>


<br>

</br>

## 프로세스 
<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/228916839-1d6f27be-d9d0-4688-85bf-0997adb0bf93.PNG" width="700"></p>

-------------------------------------

- Text Detection : Yolov5 모델을 사용해 Image의 원하는 부분을 추출 
<br>

- Text Recognition : Pytesseract를 사용해 Text Detection을 통해 나온 이미지의 글자를 추출
<br>

- Voice : TensorflowTTS를 사용해 Text Recognition의 글자들을 음성으로 생성합니다. 

---------------------------------------

## 🛠️ 모델 기능별 구현

### Text Detection
- YoloV5는 실시간 객체인식 분야에서 yolo는 one-stage detector로써 two-stage detector모델들에 비해 추론속도와 모델크기에 있어서 강점.
<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/229000082-dea4e659-79df-4f6a-b794-616eeb740a13.png" width="700"></p>


- 고지서 내의 핵심 내용이 담긴 영역을 YoloV5를 통해 가져온다.

<div>
  <img src="https://user-images.githubusercontent.com/119566469/228919068-51ccc13f-e757-4ea7-b8fc-1337cbcd6475.PNG" width="300">
  <img src="https://user-images.githubusercontent.com/119566469/228919992-b880bd03-b3d2-478e-b6e5-329a1a85edda.png" width="308">
</div>


<bt>

</br>

- Text Detection 
<div>
  <img src="https://user-images.githubusercontent.com/119566469/228921514-4743c267-1819-4b32-8585-d9bde7988923.jpg" width="300">
</div>


<br>
</br>

### Text Recognition
- 두 가지 Model fine tuning(TrOCR, CRNN)과 Library(EasyOCR, Tesseract)의 성능 비교를 통해 최종적으로 Tesseract를 사용하여 프로젝트 진행
<div>
  <img src="https://user-images.githubusercontent.com/119566469/229001108-1b5b6a1a-a3aa-4f88-a210-9846bfa557dd.jpeg" width="300">
  <img src="https://user-images.githubusercontent.com/119566469/229001112-6e5bebda-0f0e-481d-88ed-725add778a0a.png" width="300">
  <img src="https://user-images.githubusercontent.com/119566469/229001115-695b8651-479e-4b31-9eb1-1825415986c5.png" width="300">
</div>
- 라이브러리 선정 후 추가적인 학습과 이미지 전처리를 통해 인식률을 높임



<br>
</br>

### Voice 
- Tortoise 등 여러 TTS 모델이 있으나 한국어를 지원 하지 않거나 라이브러리 호환 문제로 TACOTRON2, FastSpeech2를 기반으로 모델 사용.
<div>
  <img src="https://user-images.githubusercontent.com/119566469/229001350-f2a81d9e-4d30-4fa2-b863-f7b82986536f.png" width="600">
</div>
- 프로토타입 모델 구현 전 TACOTRON2 기반으로 Language : KOR 선택이 가능하도록 설계된 TeonsorFlowTTS의 업데이트로 인한 의존성 문제로 TeonsorFlowTTS의 FastSpeech2 모델 사용을 최종적으로 결정.