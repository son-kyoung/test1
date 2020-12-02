# 파이썬으로 6개월치 업무를 하루만에 끝내기


## 1. 소개
<6개월 치 업무를 하루 만에 끝내는 업무 자동화 (2020, 생능출판사)> 도서에 수록될 업무 자동화 예제 코드들입니다.


## 2. 학습 안내
#### (1) 난이도
이 책은 얕고 넓은 지식 습득을 지향합니다. 간단히 배워 현란하고 다양한 자동화를 수행하도록 하는 것을 목표로 하고 있으므로 책과 코드에서는 파이썬 문법에 대한 깊이 있는 설명을 지양하고 있습니다.

#### (2) 비전공자 및 초보자를 위한 학습 가이드라인 
원리를 깊게 이해하려 하지 않고, 무작정 예제를 따라해 보고 넘어가는 식으로 차근차근 진도를 나가시기를 바랍니다. 원리는 잘 몰라도 됩니다.

"어? 이게 되네?"

를 느끼시는 데 중점을 두세요. 원리가 왜 중요하지 않냐면, 이 책에서 함께 제공하는 매크로가 굉장히 사용이 용이하기 때문입니다. 이 매크로만 잘 사용하시면 사실상 일반적인 사무직이 할 수 있는 업무는 모두 자동화가 가능합니다.

이후에는 본인이 자동화 하고 싶은 업무를 한 두개씩 직접 만들어 보는 것을 추천합니다. 아주 간단한 것 부터 조금씩 다양하고 많은 것으로 뻗어나가 보시기 바랍니다.

매크로 활용을 집중적으로 연습하신다면 한 두달 안에 눈에 띄는 성과를 보실 수 있을 것입니다.

#### (3) 컴퓨터공학 및 관련 분야 전공자를 위한 학습 가이드라인
이 책에서는 파이썬을 활용한 객체지향 프로그래밍에 중점을 두고 있습니다. 자동화하려는 업무가 복잡해질수록 main.py 함수를 간소하게 코딩하는 점에 주목해 주세요.

아래 순서로 중요도가 높습니다. 작가가 아래 토픽들을 어떻게 해결하고 넘어갔는지를 잘 지켜보시기 바랍니다.

(1) 다양한 라이브러리의 활용방법<br>
(2) main 함수의 간소화<br>
(3) 자동화 시나리오를 설계하는 방법<br>
(4) 파이썬을 활용해 HTML과 상호작용하는 과정

#### (4) 강사를 위한 교습 가이드라인
실용성을 추구하기 위하여 이 책에서는 프로그래밍의 기본적인 철학이나 파이썬 문법, 자료구조론과 알고리즘 등의 기초지식은 거의 설명하지 않고 넘어갑니다.

강의 중 반복문, 조건문, 함수 등 기초적인 파이썬 개념을 함께 소개해 주신다면 훨씬 깊은 이해를 제공할 수 있을 것으로 생각됩니다.

#### (5) 독학으로 깊이 있는 공부를 원하시는 분들께
파이썬을 어느정도 할 줄 아는 분께서 이 책의 코드를 보실 때 가장 얻어가는 것이 많을 것으로 생각됩니다. 이 책이 마음에 드셔서 더 깊은 공부를 원하신다면, 생능출판사의 파이썬 책을 한 권 구입하셔서 함께 공부하시는 것을 추천드립니다.


## 3. 저작권
#### (1) 비영리적 사용
  본 코드를 비영리적인 목적으로 활용하는 것은 자유입니다. 단, 본 코드에 기재된 저작자 정보를 지우지 말아주세요.
#### (2) 교육적 목적
  본 코드를 교육적 목적으로 활용하는 것은 무료입니다. 단, 본 코드에 기재된 저작자 정보를 지우지 말아주세요. 또한 코드가 교육 목적으로 어떻게 활용되는지에 대하여 저자가 매우 뜨거운 관심을 가지고 있사오니, 교육자료로 사용시 이메일로 연락을 부탁드립니다.
#### (3) 상업적 목적
  본 코드를 상업적 목적으로 사용하는 것은 금지되어 있습니다. 본 코드를 출판물에 수록하거나, 본 코드를 활용하여 상업적 프로그램을 제작하는 것은 금지되어 있습니다.
#### (4) 독자의 코드 활용
  <6개월 치 업무를 하루 만에 끝내는 업무 자동화 (2020, 생능출판사)> 책을 구매히신 독자님께서는 본 코드를 자유롭게 사용하실 수 있습니다. 상업적 프로그램을 제작하는 것도 가능합니다. 단, 본 코드를 출판물에 수록하는 등의 행위는 금지되어 있습니다. 출판사로 문의 부탁드립니다.
  
## 4. Dependencies
#### (1) 자동화를 위한 기본 도구
Python 3
>https://python.org

PyCharm
>https://www.jetbrains.com/ko-kr/pycharm/

Git Bash
>https://gitforwindows.org/

#### (2) 엑셀 관련 예제를 위해 필요한 도구
PyExcel
> pip install pyexcel pyexcel-xlsx


#### (3) 이미지 관련 예제를 위해 필요한 도구
NumPy
> pip install numpy

Pillow
> pip install pillow


>#### (4) 매크로 관련 예쩨를 위해 필요한 도구
pyWin32
>pip install pywin32

PyperClip
>pip install pyperclip

PyAutoGui
>pip install pyautogui

#### (5) 웹(인터넷) 관련 예제를 위해 필요한 도구
Selenium
>pip install selenium

Chrome(크롬)
>https://www.google.com/intl/ko/chrome/

ChromeDriver (크롬드라이버)
>https://chromedriver.chromium.org/downloads

## 5. 작가 프로필
#### 반병현 (Byunghyun Ban)

#### Career
 - 대구지방노동청 안동지청 사회복무요원 (2018.06. ~ 2020.04.)
 - 농업회사법인 상상텃밭(주) CTO / CBO (2017.03. ~ )
 
#### Academic Background
 - KAIST 바이오및뇌공학과 석사학위 (조기졸업)
 - KAIST 바이오및뇌공학과 학사학위
 - 안동 경안고등학교 (조기졸업)
 
#### Lecture
 - "6개월치 업무를 하루 만에 끝내는 업무 자동화" (2020, Fast Campus 온라인 강의)

- "스마트팜 교육 프로그램" (2020, 대구 서구 인동촌 백년마을 도시재생뉴딜사업, 마을관리사회적협동조합 교육과정)

- "농업경영체, 경작이 아닌 경영을 기획하라" (2020, 한국생명과학고등학교 영농정착후계인력양성 과정)

- "선도농가 멘토링 - 스마트팜" (2020, 한국생명과학고등학교 선도농가 멘토링 현장교수)

- "리더십 3 :리스크 없는 학생창업" (2017 가을학기, KAIST 학부 교양필수 강사)
 
#### Speeches
 - "스마트팜과 파생 직업, 잡을 수 있는 기회들" (2020, KB 희망진로콘서트 "꿈꾸는 대로")

- "스마트팜과 수경재배" (2020, 안동대학교 농업마이스터과정)

- "AI개발을 위한 프레임워크" (2020, 동서울대학교 기업인특강)

- "가장 오래된 산업에 첨단기술 끼얹기" (2020, NYPC 토크콘서트 강연)

- "농촌체험상품 개발 브랜딩, 상표출원 교육 특강" (2020, 한국생명과학고등학교 고교학점제 초청강연)

- "호프스테더 권력거리 이론 관점에서 본 고용노동부 행정혁신 성공사례" (2020, 농촌진흥청 혁신역량향상 교육)

- "잔머리로 시스템을 가지고 노는 방법" (2019, 경안고등학교 초청강연)

- "혁신의 장벽을 개발자스럽게 부수기" (2019, 마소콘 2019 기조연설)

- "수필 두 편으로 50일만에 대한민국 움직이기" (2019, 계명대학교 초청강연)

- "실패하는 스타트업" (2019, POSTECH 기업인 영재교육원 초청강연)

- "파이썬과 함께라는 마음가짐만 있으면 못 할 것은 없다는 마음가짐만 있으면 정말로 못 할 것은 없다" (2019, PyconKR 기조연설)

- "그로스해킹을 통한 행정혁신 사례" (2019, 제 16회 워크 스마트 포럼 - 로보틱 프로세스 자동화(RPA), 행정안전부 초청)

- "행정혁신 성공사례 강연" (2019, 정부혁신 담당관 워크숍, 행정안전부 초청)

- "코딩하는 공익 - 아직 세상을 바꾸고 싶은 개발자에게" (2019, KCD2019 코딩이랑무관합니다만 세션)

- "학생창업과 KAIST" (2018 상반기, E5-KAIST 시니어 멘토 초청강연)

- "학생신분으로 스타트업 세우기" (2016, KLC 벤처포럼 at KAIST)

- "아이디어에서 사업화까지" (2012, 제2회 KAIST 전국 발명대회 시상식)

- "뇌과학에 발을 들이면서" (2012, 안동 경안고등학교 과학동아리 초청) 
 #### Publications
- 공학자의 오경묵상, 부크크, 2020

- 나는 아직 잊힐 준비가 되지 않았어요, 부크크, 2020

- 실전 민사소송법, 부크크, 2020

- 공학자의 지혜묵상, 부크크, 2020

- 코딩하는 공익, 세창미디어, 2020

- 법대로 합시다, 지식과감성#, 2016

- 카이스트 공부벌레들, 살림FRIENDS, 2012
 
 #### Research
 > https://www.researchgate.net/profile/Byunghyun_Ban
 
 #### You Tube
 > https://www.youtube.com/channel/UCpV0ZdloVwvSjxHfnYYQPQg?sub_confirmation=1
