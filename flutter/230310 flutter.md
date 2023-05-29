# Flutter

## State

위젯의 state는 위젯에 들어갈 state

데이터가 변경되면 해당 위젯의 UI도 바뀜

StatefulWidget으로 하면 공간이 두개 생김

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int counter = 0;

  void onClicked() {
    counter = counter + 1;
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: const Color(0xFFF4EDDB),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text('Click Count', style: TextStyle(fontSize: 30)),
                Text('$counter', style: const TextStyle(fontSize: 40)),
                IconButton(
                    iconSize: 40,
                    onPressed: onClicked,
                    icon: const Icon(Icons.add_box_rounded))
              ],
            ),
          )),
    );
  }
}

```

이상태로 안됨

setState가 필요

state에 데이터가 변할 때 알려주는 함수

- build를 다시 실행

변수 바뀌고 setstate()해도됨

안에 있으면 더 가독성 있긴함

## IconButton

### iconsize

### onPressed

### icon



## context

모든 부모 요소의 성질이 담김

### Theme

MaterialAPP

아래에 넣는걸로 기본 Theme 저장 가능

#### ThemeData

`of`는 속한다는 ㄷ뜻



## Widget Lifecycle

### initState()

초기화하는 기능

빌드 위에서 써야 함

그냥 빌드 위에서 코드 써도 초기화 가능해서 거의 필요 없음

부모 요소에 의존하는 데이터를 쓸 때 사용

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    print('initState!');
  }

  @override
  Widget build(BuildContext context) {
    print('build');
    return MaterialApp(
      theme: ThemeData(
        textTheme: const TextTheme(
          titleLarge: TextStyle(color: Colors.red),
        ),
      ),
      home: const Scaffold(
          backgroundColor: Color(0xFFF4EDDB),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                MyLargeTitle(),
              ],
            ),
          )),
    );
  }
}

class MyLargeTitle extends StatelessWidget {
  const MyLargeTitle({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Text('My Large Title',
        style: TextStyle(
            fontSize: 30,
            color: Theme.of(context).textTheme.titleLarge?.color));
  }
}

```



```
Performing hot restart...
Syncing files to device sdk gphone64 x86 64...
Restarted application in 1,169ms.
I/flutter (17633): initState!
I/flutter (17633): build
I/flutter (17633): build
D/EGL_emulation(17633): app_time_stats: avg=5477.61ms min=381.38ms max=10573.84ms count=2
I/flutter (17633): build

```

## dispose는 위젯이 스크린에서 제거될 때 호출되는 메서드

API 업데이트나 form의 리스너로부터 벗어나기

이벤트 리스너로부터 구독 취소하거나