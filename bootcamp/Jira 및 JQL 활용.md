# Jira 및 JQL 활용

## Issue Tracking

![image-20230105103618370](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105103618370.png)

할일을 Issue라고 함

이슈 상태를 추적해서 이슈 상태가 어떻고 어떤 값을 가지고 있는지 확인

## Project Management

![image-20230105103736599](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105103736599.png)

## Agile

![image-20230105103901842](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105103901842.png)

https://agilemanifesto.org/iso/kr/manifesto.html

## Scrum vs Kanban

![image-20230105104215416](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105104215416.png)

지라 보드에서 두가지 개념 사용 가능

### Scrum meeting



Scrum 방법론을 사용할때 

![image-20230105104504579](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105104504579.png)

한일 하고 있는 일 공유

![image-20230105104429445](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105104429445.png)

번다운 차트

이슈들이 얼마나 빨리 해결이 됐는지

스크럼미팅 빨리 끝내려고 일어서서 함

## DevOps

![image-20230105104850780](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105104850780.png)

development 개발

oprations 운영

개발팀 기능 추가하려고 하는데 운영은 싫어함

`사일로 현상` : 각자 자신의 곳간에 쌓아두고 곳간 지키겠다. 조직간의 이기주의

![image-20230105105107748](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105105107748.png)

이런 문제를 해결하기 위해 합쳐버림

![image-20230105105231627](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105105231627.png)

![image-20230105105426311](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105105426311.png)

![image-20230105105807819](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105105807819.png)

## Jira 이용

![image-20230105110027743](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105110027743.png)

지라 클라우드 쓰는데 이건 지라 서버 버전

![image-20230105110110455](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105110110455.png)

![image-20230105110200155](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105110200155.png)

Create 누르면 생성

![image-20230105110238122](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105110238122.png)

### Issue type

`Task`: 유저 스토리가 아닌데 해야할 일

`Story`: 유저 스토리 제일 자주 사용, 사용자가 어떤 행위를 했을 때 어떤 동작을 한다

`Bug`: 이미 개발이 됐는데 버그가 일어남

`Epic` : 큰 틀, 이 epic과 관련된 이슈를 연관

### Status

할일

완료

진행중 

이 상태를 바꾸면서 그 상태를 표현해주면 된다

### Epic Name

epic에만 존재

다른 이슈에서 epic을 지정해줄 때 이름

### Component

이슈들을 하나의 카테고리로 묶엊무

![image-20230105110800549](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105110800549.png)

### Label

이것도 카테고리화인데 Component처럼 정해놓는게 아니라 자유롭게

대소문자 구분 조심

### Sprint

어느 스프린트 할당할지 지정
### Version

어펙티드는 어떤 버전인지 픽스는 고친 버전

## JQL

Jira Query Language

Jira Issue를 구조적으로 검색하기 위해 제공하는 언어

SQL과 비슷한 문법

Jira의 각 필드들에 맞는 특수한 예약어들을 제공

쌓인 Issue들을 재가공해 유의미한 데이터를 도출해내는데 활용 (Gadget, Agile Board 등)

### JQL Operators

=, !=. >, >=

in, not in

~ (contains), !~(not contains)

is empty, is not empty, is null, is not null

### JQL keywords

AND

OR

NOT

EMPTY

NULL

ORDER BY



![image-20230105113132548](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113132548.png)

![image-20230105113222729](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113222729.png)

![image-20230105113229567](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113229567.png)

![image-20230105113239495](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113239495.png)

![image-20230105113248453](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113248453.png)

![image-20230105113254629](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113254629.png)

![image-20230105113310759](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113310759.png)

![image-20230105113333053](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113333053.png)

상대적 날짜를 사용한다

created, updated

![image-20230105113424249](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113424249.png)

![image-20230105113431003](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113431003.png)

![image-20230105113438299](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113438299.png)

## JQL Functions

endOfDay(), startOfDay()

endOfWeek() (Saturday), startOfWeek() (Sunday)

endOfMonth(), startOfMonth(), endOfYear(), startOfYear()

currentUser()

![image-20230105113614201](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113614201.png)

일요일 이후 업데이트된 것

![image-20230105113716746](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113716746.png)

월요일을 이용하고 싶으면 괄호 안에 1d 화요일은 2d

![image-20230105113758654](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113758654.png)

![image-20230105113814580](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113814580.png)

resolution 입혀져 있어야 끝났다 판단

![image-20230105113917932](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113917932.png)

필터 저장

![image-20230105113942877](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105113942877.png)

![image-20230105114010446](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105114010446.png)

![image-20230105114046372](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105114046372.png)

### Jira Dashborad, Chart

![image-20230105124454358](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105124454358.png)

![image-20230105124518921](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105124518921.png)

![image-20230105124553996](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105124553996.png)

![image-20230105124730414](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105124730414.png)

Kanban Board

![image-20230105124932374](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105124932374.png)

![image-20230105125001780](./Jira%20%EB%B0%8F%20JQL%20%ED%99%9C%EC%9A%A9.assets/image-20230105125001780.png)

현업에서 사용하는 방식