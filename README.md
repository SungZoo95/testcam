# :musical_note: 음성 고지서 서비스 ‘SORI’ :musical_note:

<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/228908423-65d2812a-8034-43fd-979c-3553052841f8.PNG" width="200"></p>

<div align="center">
저시력자들을 위한 음성고지서 서비스 SORI입니다. 
데모 버전입니다.
</div>

------------------------------

<br>

</br>

## 역할 분담 
|  팀  | 멤버     |      
|:-----:|:----------:|
|조장 김의석|<img src="https://user-images.githubusercontent.com/119566469/228912270-95157db4-8d2e-4a63-8f1c-a3bce062ec18.JPG" width = 150>| 
|객체팀(Text Detection(Yolov5)) <br>이한재  최성주|<img src="https://user-images.githubusercontent.com/119566469/228913186-aa0d59e6-6462-46b3-8282-2e1dd2f580f6.JPG" width = 150>  <img src="https://user-images.githubusercontent.com/119566469/228913198-ad1cc97e-0937-4b73-ac8d-be3912bec12c.JPG" width = 150>|
|텍스트팀(Text Recognition(Pytesseract)) <br> 김의석 박진호|<img src="https://user-images.githubusercontent.com/119566469/228912270-95157db4-8d2e-4a63-8f1c-a3bce062ec18.JPG" width = 150>  <img src="https://user-images.githubusercontent.com/119566469/228914447-d2da8896-61c8-4e38-83b2-d8bce609a2cf.JPG" width = 150>|
|보이스팀(Voice(TensorflowTTS)) <br> 고준성 김수윤|<img src="https://user-images.githubusercontent.com/119566469/228914919-0eefb368-1855-4d2b-8a5b-0925407c42c1.JPG" width = 150>  <img src="https://user-images.githubusercontent.com/119566469/228914945-2e90b14a-2cf5-4e6e-a9a9-b68444df74f4.JPG" width = 150>|

------------------------------------

<br>

</br>

## 아이디어 구상 
저시력자들을 대상으로 QR코드를 이용하여 고지서의 내용을 음성으로 전환해주는 서비스가 존재하나 몇가지 문제로 서비스의 제한이 많아 무용지물 상태라는 뉴스를 보았습니다.<br>
저희는 QR코드가 아닌 고지서 전체를 찍으면 음성으로 안내해주는 서비스를 도전했습니다.

---------------------------------------------------

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

## 예시 

- 예시 고지서 이미지입니다

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

- Text Recognition


