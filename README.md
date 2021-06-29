# 궁(금해), 예(측 건수)

* 멀티캠퍼스 1차 전공 프로젝트



## 🛵프로젝트 소개 

* 공공데이터를 활용하여, 머신러닝 알고리즘을 사용해 예측하고 서비스 개발을 목표로 하는 프로젝트입니다.
* 외부환경(날씨, 미세먼지, 코로나 확진자수)를 통해 배달 주문건수를 예측해, 실시간으로 시각화하여 보여주는 서비스입니다.



## 🎞 데모 영상 

* 배포는 하지 않았고, 로컬에서 실행되는 데모 웹사이트 영상입니다.

<img width="600" height="335" alt="screen shot 2021-05-10 at 18 49 pm " src="https://user-images.githubusercontent.com/51108153/117640625-25be5580-b1c0-11eb-9741-8ce59603a58c.gif">



## 📃 데이터 명세 

|                             출처                             |          데이터 이름          | 제공 형태 |                             요약                             |
| :----------------------------------------------------------: | :---------------------------: | :-------: | :----------------------------------------------------------: |
| [KT-빅데이터센터](https://bdp.kt.co.kr/invoke/SOKBP2603/?goodsCode=KGUINDTORDER) | 시간-지역별 <br>배달 주문건수 |    csv    | 지역-시간-업종별 주문배달건수 기록 자료<br>기간 : 2019.07.17 ~ 2020.09.30 |
| [기상자료개방포털](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36) |      종관기상관측(ASOS)       |    csv    |                 시간대별 기상 요소 관측 자료                 |
| [에어코리아](https://www.airkorea.or.kr/web/pastSearch?pMENU_NO=123) |        미세먼지 데이터        |    csv    |                 시간대별 미세먼지 관측 자료                  |
| [경기도 <br>감염병관리지원단](http://www.gidcc.or.kr/%ec%bd%94%eb%a1%9c%eb%82%98covid-19-%ed%98%84%ed%99%a9/) |        코로나 확진자수        |   excel   |            일별, 지역별 코로나 확진자수 기록 자료            |
| [서울 <br>열린데이터 광장](http://data.seoul.go.kr/dataList/OA-20279/S/1/datasetView.do) |  서울시 코로나19 확진자 현황  |    csv    |         서울시 기준의 코로나19 확진자 관련 정보 현황         |



## 🚥 커밋 메시지 규칙

```bash
################## Analysis Commit Convention ##################
Data : 데이터 관련 사항(데이터 수집, 전처리, 수정, cleansing)
EDA : 탐색적 데이터 분석 관련 사항
Model : 모델 생성 관련 사항
Valid : 모델 검증 관련 사항

################## Usual Commit Convention ##################
Feat     : 새로운 기능 추가
Perf     : 성능 개선
Fix      : 버그 수정, 보완
Refactor : 코드 리팩토링
Style    : 코드 포맷팅, 코드 변경이 없는 경우 (스페이스, 세미콜론 누락 등)
Docs     : 문서 추가, 수정, 삭제
Build    : 빌드 시스템 수정, 외부 종속 라이브러리 수정
Test     : 기존 테스트 코드 수정 및 새로운 테스트 코드 추가
Chore    : 소스코드, 테스트 파일을 제외한 수정

Ex. 데이터 전처리 파일 commit 시
$ git commit -m 'Data: Data preprocessing
> 데이터 전처리 파일 commit'
```

