# Flutter

## How Flutter Work

네이티브 프레임워크 동작방식

- 직접적으로 소통

플러터

- 실제 iOS, 안드로이드 버튼 만드는 것이 아님
- 비디오 게임 엔진처럼 작동

프레임워크에서 여러 종류로 분류

그리고 직접 운영체제랑 소통하는게 아니라 엔진이 화면 상에 우리가 말한 것을 그려줌

Unity, c#

코드 짜면 코드를 패키징해서 앱스토어로 보냄

그 앱을 다운 받으면 Unity 코드 작동

엔진 - 무언가를 그려주는 역할

플랫폼의 Native Widget을 사용하지 않음 

엔진이 모든것을 그려줌

엔진이 프레임 워크를 동작시키고 엔진이 input, button을 그려줌

### iOS에서 플러터 작동

- 엔진의 C 및 C++ 코드가 컴파일
- 다트 코드는 네이티브 ARM 라이브러리로 컴파일
- 라이브러리 'runner' iOS 프로젝트
- 이 모든건 .ipa라고 하는 iOS 어플리케이션의 포맷으로 빌드

- 유저 앱 실행 
- 앱은 Flutter 라이브러리를 불러옴
- 우리가 만든 UI를 빌드

엔진이 코드를 동작시키는 주체

플랫폼은 엔진을 동작시키고 엔진이 Dart Flutter 코드 동작시키면 화면에 UI를 그려줌

엔진이 여는건 runner iOS 프로젝트

### 안드로이드

C와 C++로 짜여진 엔진이 안드로이드의 NDK와 함께 컴파일

Dart코드는 네이티브와 ARM, 그리고 x86 라이브러리로 컴파일

이 라이브러리는 runner 안드로이드 프로젝트에 포함되고 이 모든건 .apk로 빌드

유저 어플리케이션 실행

Flutter 엔진을 동작시키는 runner 프로젝트를 실행

엔진이 Dart 코드를 실행



문제점도 네이티브 위젯을 사용하지 않음

실제 네이비트가 아님

운영체제가 아니라 렌더링

위젯들이 가짜임, 운영체제에 의한 것이 아니라 렌더링 엔진에 의한

그런데 오히려 이게 플러터로 통제할 수 있는 것이 많아진다는 뜻

어플리케이션의 호스트에 의존할 필요가 없음

## React Native vs Flutter

React Native는 운영체제와 직접 소통하기 때문에 그런거 쓰려면 쓰고 플러터는 모든 픽셀 통제하려면 씀

# Hello World

```dart
void main() {
  runApp(MyApp());
}
```

MyApp이라는 클래스 만들어주는데

3가지의 코어 위젯 중 하나로 extend해줌

```dart
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {

}
```

그러면 애플리케이션이 빌드하지 않았다고 뜸

모든 위젯은 .build가 필요함

### Build

플러터가 실행 build 메소드가 뭘 리턴하든지 화면에 보여줌

- UI를 만드는것

가장 기초적이고 쉬운 StateLessWidget 사용

상속받으려면 StateLessWidget이 정해놓은 계약

- 이게 build를 넣으라는 것
- 이 메소드가 뭘 return하든지 화면에 띄워줌

```dart
import 'package:flutter/cupertino.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    throw UnimplementedError();
  }
}
```

override는 부모 클래스에 이미 있는 메소드를 override한다는 것

build 메소드는 BuildContext 타입의 context라는 parameter를 받아옴

- 일단 무시

이 위젯은 근본 위젯임

- MaterialApp(구글) 이랑 CupertinoApp(ios) return
- 어떤 스타일로 할지
- 둘 중 어느것처럼도 보이고 싶지 않아도 설정하긴 해야함
  - 구글 스타일 뺄 수 있음

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Text('Hello world!'),
    );
  }
}
```

![image-20230309130029887](./230309%20Flutter.assets/image-20230309130029887.png)

## scaffold

모든 화면은 scaffold가 필요하다

중앙 정렬 등등 해줌

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Text('Hello world'),
      ),
    );
  }
}
```

![image-20230309125953768](./230309%20Flutter.assets/image-20230309125953768.png)



Appbar를 만들고 그 안에 title이 있음 거기에 텍스트 넣어줌

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Hello flutter'),
        ),
        body: Text('Hello world'),
      ),
    );
  }
}
```

![image-20230309130426433](./230309%20Flutter.assets/image-20230309130426433.png)

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Hello flutter'),
        ),
        body: Center(
          child: Text('Hello world'),
        )
      ),
    );
  }
}
```

![image-20230309131050408](./230309%20Flutter.assets/image-20230309131050408.png)



센터라는 위젯 사용 - 안에 있는 것들을 가운데에 배치



## column, row

#### children

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
        body: Column(
          children: [
            Row(
              children: [
                Column(children: [
                  Text('Hey, Selena'),
                  Text('Welcome back'),
                ],)
              ],
            )
          ],
        )
      ),
    );
  }
}
```



sizedbox : 그 크기의 공간을 만듦

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
        body: Column(
          children: [
            SizedBox(
              height: 80,
            ),
            Row(
              children: [
                Column(children: [
                  Text(
                    'Hey, Selena',
                    style: TextStyle(
                      color: Colors.white,
                    ),
                  ),
                  Text(
                    'Welcome back',
                    style: TextStyle(
                      color:Colors.white
                    ),
                  ),
                ],)
              ],
            )
          ],
        )
      ),
    );
  }
}
```

#### MainAxisAlignment

column의 MainAxisAlignment는 수직방향

#### CrossAxisAlignment

crossAxisalignment는 수평

### Text

#### ''

#### style

##### TextStyle

###### color

###### fontSize

###### fontWeight

## Sizedbox

사이즈 필수

## Padding

### Padding

#### EdgeInsets

##### EdgeInsets.symmetric

###### horizontal, ?

### child

## Dev tools

![image-20230309151526833](./230309%20Flutter.assets/image-20230309151526833.png)

이거 누르면 뜸

![image-20230309151539449](./230309%20Flutter.assets/image-20230309151539449.png)

이런식으로 다양하게 볼 수 있음

![image-20230309151613666](./230309%20Flutter.assets/image-20230309151613666.png)

Select Widget Mode하면 에뮬레이터 눌러서 선택 가능

![image-20230309151635559](./230309%20Flutter.assets/image-20230309151635559.png)

이거 누르면 패딩같은거 한번에 보임

## Button



$ 넣을때 변수표시 아니라 그냥 달러 넣는다는거 알려주려면

`\$` 넣어줌

### Container

div같은거

#### BoxDecoration

![image-20230309153655078](./230309%20Flutter.assets/image-20230309153655078.png)



## 파란줄

const는 컴파일하기 전에 알수 있는 값

수정 못함

이 변수를 위한 메모리공간을 만드는 대신 value 검토하고 대체함

## 전구

![image-20230309161555656](./230309%20Flutter.assets/image-20230309161555656.png)

짱임

Ctrl alt M - 메소드 추출