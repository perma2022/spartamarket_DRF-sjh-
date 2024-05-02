✅프로젝트 소개
스파르타 마켓 DRF
CRUD RESTful API 

✅설치 및 사용 방법

Flask                         3.0.2
Flask-Migrate                 4.0.7
Flask-SQLAlchemy              3.1.1
Django                        4.2
django-extensions             3.2.3
django-seed                   0.3.1
djangorestframework           3.15.1
djangorestframework-simplejwt 5.3.1

✅기능

계정 관련 기능 (accounte)

1. 회원가입
Endpoint: /api/accounts
Method: POST
조건: id(유저네임), 비밀번호(password), 이메일(email),
+ 이름(name), 닉네임(nickname) 생일(birthday) 필수 입력하며 성별, 자기소개 생략 가능
검증: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
구현: 데이터 검증 후 저장.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/3e0a64e2-a03c-4f2d-bd56-ef2f58104a53)


2. 로그인
Endpoint: /api/accounts/login
Method: POST
조건: email과 비밀번호 입력 필요.
검증: email과 비밀번호가 데이터베이스의 기록과 일치해야 함.
구현: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/8cdcd54e-b9bb-4d89-bed4-9f8c6e8bc67a)


3. 프로필 조회
Endpoint: /api/accounts/<str:username>
Method: GET
조건: 로그인 상태 필요.
검증: 로그인 한 사용자만 프로필 조회 가능
구현: 로그인한 사용자의 정보를 JSON 형태로 반환.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/e726ca7d-a50f-44cd-b038-e6413f1c8300)


4. 본인 정보 수정
Endpoint: /api/accounts/<str:username>
Method: PUT
조건: 이메일, 이름, 닉네임, 생일 입력 필요하며, 성별, 자기소개 생략 가능
검증: 로그인 한 사용자만 본인 프로필 수정 가능. 수정된 이메일은 기존 다른 사용자의 이메일과 username은 중복되면 안 됨.
구현: 입력된 정보를 검증 후 데이터베이스를 업데이트.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/ded95cf3-a877-4949-b748-7ff78d9b73d8)


상품 관련 기능  (products)

5. 상품 등록
Endpoint: /api/products
Method: POST
조건: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.
구현: 새 게시글 생성 및 데이터베이스 저장.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/84096a9f-58c8-45d7-a6f9-642a48c13a65)


6. 상품 목록 조회
Endpoint: /api/products
Method: GET
조건: 로그인 상태 불필요.
구현: 모든 상품 목록 페이지네이션으로 반환.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/de64de20-39fc-4d29-82a5-b0c2c373a9bc)


7. 상품 수정
Endpoint: /api/products/<int:productId>
Method: PUT
조건: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.
검증: 요청자가 게시글의 작성자와 일치하는지 확인.
구현: 입력된 정보로 기존 상품 정보를 업데이트.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/89bddb3c-2bf2-4167-bab0-0c6ff1d7f5c2)


8. 상품 삭제
Endpoint: /api/products/<int:productId>
Method: DELETE
조건: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.
검증: 요청자가 게시글의 작성자와 일치하는지 확인.
구현: 해당 상품을 데이터베이스에서 삭제.
![image](https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/7c7f28b5-c5b4-4c2c-b00d-e9bc0e209a28)


✅ERD
(ERD 작성 잘못해서 죄송합니다ㅠ..ㅠ)
<img width="2624" alt="erd" src="https://github.com/perma2022/spartamarket_DRF-sjh-/assets/121236442/25213579-c562-41c8-a820-93643f374f3c">

