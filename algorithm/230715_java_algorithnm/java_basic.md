## 입력

```java
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
```

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String s = scanner.next(); // 단어 하나를 입력 받음
        int i = scanner.nextInt(); // 정수 하나를 입력 받음

        scanner.close(); // 스캐너를 닫아 리소스를 반환함
    }
}

```

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine(); // 한 줄을 입력 받음
        int i = Integer.parseInt(br.readLine()); // 한 줄을 입력 받아 정수로 변환함

        br.close(); // BufferedReader를 닫아 리소스를 반환함
    }
}

```

## ArrayList

`        ArrayList<Integer> list = new ArrayList<Integer>(); // Integer 타입의 ArrayList를 생성합니다.`

- `add(E e)`: 리스트의 끝에 지정된 요소를 추가합니다.
- `add(int index, E element)`: 리스트의 지정된 위치에 특정 요소를 삽입합니다.
- `clear()`: 리스트에서 모든 요소를 제거합니다.
- `contains(Object o)`: 리스트가 특정 요소를 포함하고 있는지 확인합니다.
- `get(int index)`: 리스트의 지정된 위치에 있는 요소를 반환합니다.
- `indexOf(Object o)`: 지정된 요소가 리스트에서 처음으로 나타나는 위치의 인덱스를 반환합니다.
- `isEmpty()`: 리스트가 비어 있는지 확인합니다.
- `remove(Object o)`: 리스트에서 첫 번째로 나타나는 특정 요소를 제거합니다.
- `remove(int index)`: 리스트에서 지정된 위치의 요소를 제거합니다.
- `size()`: 리스트의 요소 수를 반환합니다.
- `set(int index, E element)`: 리스트의 지정된 위치에 있는 요소를 지정된 요소로 대체합니다.
- `toArray()`: 리스트의 모든 요소를 포함하는 배열을 반환합니다.

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        list.add(1);  // list에 1 추가
        list.add(2);  // list에 2 추가
        list.add(3);  // list에 3 추가

        System.out.println(list.get(0)); // 0번 인덱스의 값을 출력, 출력: 1

        list.remove(1);  // 1번 인덱스의 값을 제거

        System.out.println(list.size()); // 리스트의 크기 출력, 출력: 2
    }
}
	
```


네, 맞습니다. Java에서 Array와 List는 서로 다른 자료구조를 가지고 있습니다. 각각의 특징은 다음과 같습니다:

1. Array(배열):
   - 배열의 크기는 생성 시점에 정해지며, 그 후로 변경할 수 없습니다.
   - 배열은 원시 타입(primitive type, int, double, char 등)을 저장할 수 있습니다.
   - 배열은 연속적인 메모리 공간에 데이터를 저장하므로, 인덱스를 이용한 데이터 접근이 빠릅니다.
   - 하지만 배열의 크기는 고정되어 있기 때문에, 데이터의 추가나 삭제가 불편하고, 크기를 변경하려면 새로운 배열을 생성해야 합니다.
2. List:
   - List는 인터페이스로, ArrayList나 LinkedList 등이 List 인터페이스를 구현하고 있습니다.
   - List의 크기는 동적입니다. 즉, 요소를 추가하거나 제거하면서 크기가 자동으로 조절됩니다.
   - List는 오직 객체만을 저장할 수 있습니다. 원시 타입을 저장하려면 해당 원시 타입의 Wrapper 클래스(Integer, Double, Character 등)를 사용해야 합니다.
   - List 인터페이스를 구현한 클래스들은 내부적으로 데이터를 어떻게 관리하느냐에 따라 성능 차이가 나타날 수 있습니다. 예를 들어, ArrayList는 내부적으로 배열을 사용하기 때문에 인덱스를 이용한 데이터 접근이 빠르지만, LinkedList는 데이터 추가/삭제에 유리합니다.

따라서 어떤 자료구조를 사용할지는 상황에 따라 결정해야 합니다. 배열이 필요한 경우도 있고, List가 필요한 경우도 있습니다.

### Arrays.

Java의 `java.util.Arrays` 클래스는 배열에 대한 유용한 유틸리티 메소드를 제공합니다. 여기에는 다음과 같은 메소드들이 포함됩니다:

1. **toString(array)** - 배열을 문자열로 변환합니다. 각 요소는 쉼표와 공백으로 구분됩니다. 이 메소드는 배열의 내용을 인쇄하거나 디버깅에 유용합니다.

   ```java
   int[] array = {1, 2, 3};
   System.out.println(Arrays.toString(array));  // Outputs: [1, 2, 3]
   ```

2. **sort(array)** - 배열의 요소를 오름차순으로 정렬합니다.

   ```java
   int[] array = {3, 1, 2};
   Arrays.sort(array);
   System.out.println(Arrays.toString(array));  // Outputs: [1, 2, 3]
   ```

3. **equals(array1, array2)** - 두 배열이 동일한지 확인합니다. 이 메소드는 두 배열의 길이와 각 요소가 동일한지 비교합니다.

   ```java
   int[] array1 = {1, 2, 3};
   int[] array2 = {1, 2, 3};
   System.out.println(Arrays.equals(array1, array2));  // Outputs: true
   ```

4. **fill(array, value)** - 주어진 값으로 배열의 모든 요소를 채웁니다.

   ```java
   int[] array = new int[5];
   Arrays.fill(array, 1);
   System.out.println(Arrays.toString(array));  // Outputs: [1, 1, 1, 1, 1]
   ```

5. **copyOf(array, length)** - 배열의 복사본을 생성하고 반환합니다. 새 배열의 길이는 주어진 길이입니다.

   ```java
   int[] array1 = {1, 2, 3};
   int[] array2 = Arrays.copyOf(array1, array1.length);
   System.out.println(Arrays.toString(array2));  // Outputs: [1, 2, 3]
   ```

6. **binarySearch(array, key)** - 배열에서 특정 값의 인덱스를 찾습니다. 배열은 정렬되어 있어야 합니다.

   ```java
   javaCopy codeint[] array = {1, 2, 3};
   int index = Arrays.binarySearch(array, 2);
   System.out.println(index);  // Outputs: 1
   ```

이와 같은 메소드들 외에도 `java.util.Arrays` 클래스는 `deepToString()`, `deepEquals()`, `hashCode()`, `deepHashCode()`, `asList()` 등의 메소드를 포함하고 있습니다. 이 메소드들은 다차원 배열이나 배열과 리스트 간의 변환 등, 더 복잡한 연산을 지원합니다.

#### asList

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
```

#### Arrays.stream()

`Arrays.stream()`와 `.stream()`는 모두 Java 8에서 도입된 Stream API를 이용해서 배열이나 컬렉션을 스트림으로 변환하는 메소드입니다. 그러나 이 두 메소드는 사용되는 대상에 따라 다르게 적용됩니다.

1. **Arrays.stream()**: 이 메소드는 java.util.Arrays 클래스의 정적 메소드로서, 배열을 스트림으로 변환하는데 사용됩니다.

   예를 들어:

   ```java
   int[] array = {1, 2, 3, 4, 5};
   IntStream stream = Arrays.stream(array);
   ```

   위 코드에서, `Arrays.stream()` 메소드는 int 배열을 IntStream으로 변환합니다. IntStream은 기본형 int의 스트림을 나타내는 특수한 스트림입니다.

2. **.stream()**: 이 메소드는 Collection 인터페이스(예: List, Set)의 메소드로서, 컬렉션을 스트림으로 변환하는데 사용됩니다.

   예를 들어:

   ```java
   List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
   Stream<Integer> stream = list.stream();
   ```

   위 코드에서, `.stream()` 메소드는 List 컬렉션을 Stream으로 변환합니다. 이 Stream은 객체를 다루는 일반적인 스트림입니다.

따라서, `Arrays.stream()`와 `.stream()` 메소드는 모두 스트림을 생성하는 데 사용되지만, 사용하는 대상(배열 또는 컬렉션)에 따라 적절한 메소드를 선택해야 합니다.

Java 8의 Stream API를 사용하여 int 배열을 String 배열로 변환하는 방법은 다음과 같습니다:

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] intArray = {1, 2, 3, 4, 5};
        String[] strArray = Arrays.stream(intArray)
                                  .mapToObj(Integer::toString)
                                  .toArray(String[]::new);

        System.out.println(Arrays.toString(strArray));  // 출력: [1, 2, 3, 4, 5]
    }
}
```

위의 코드는 `Arrays.stream(intArray)`를 호출하여 int 배열을 IntStream으로 변환하고, `mapToObj(Integer::toString)` 메소드를 사용하여 IntStream의 각 요소를 String으로 변환하며, `toArray(String[]::new)` 메소드를 사용하여 String 스트림을 String 배열로 변환합니다.

`Integer::toString` 메소드 참조는 각 int 값을 String으로 변환하는 데 사용되며, `String[]::new` 메소드 참조는 최종 String 배열을 생성하는 데 사용됩니다.

이렇게 하면 int 배열의 각 요소가 그대로 유지되지만, 이 요소들이 이제는 String 형태로 저장된 String 배열을 얻게 됩니다.

### ArrayList랑 배열 차이

ArrayList와 배열(Type[])은 Java에서 데이터를 저장하고 처리하는 두 가지 주요 방법입니다. 이 둘의 주요 차이점은 다음과 같습니다:

1. 크기: 배열은 고정 길이를 가지므로 한 번 생성하면 크기를 변경할 수 없습니다. 반면에 ArrayList는 동적이며 요소가 추가되거나 제거될 때 자동으로 크기가 조정됩니다.
2. 유형: 배열은 기본 데이터 유형(int, char 등)과 객체를 모두 저장할 수 있습니다. 반면에 ArrayList는 객체만 저장할 수 있으며 기본 데이터 유형을 저장하려면 해당 wrapper 클래스(Integer, Character 등)를 사용해야 합니다.
3. 성능: 배열은 ArrayList보다 접근 속도가 빠르며 메모리 효율성이 더 높습니다. 이는 배열이 런타임에 크기가 변하지 않기 때문입니다. 반면에 ArrayList는 더 많은 메모리를 사용하며 요소를 추가하거나 제거할 때마다 크기를 조정해야 하므로 배열보다 덜 효율적입니다.
4. 편의성: ArrayList는 자체적으로 add, remove, contains 등의 메서드를 가지고 있어 배열보다 훨씬 더 편리하게 사용할 수 있습니다.
5. 다차원: 배열은 다차원 배열을 쉽게 만들 수 있지만, ArrayList에서는 다차원 배열을 직접적으로 만드는 것이 불가능합니다. 다차원 구조를 만들기 위해서는 ArrayList의 ArrayList를 만들어야 합니다.

즉, 배열과 ArrayList는 서로 다른 용도로 사용됩니다. 어떤 것을 사용할지는 사용 사례에 따라 결정됩니다. 크기가 변하지 않고 성능이 중요한 경우 배열을 사용하고, 데이터의 크기가 동적으로 변하거나 데이터 조작 기능이 필요한 경우 ArrayList를 사용하게 됩니다.

배열: 배열은 기본 데이터 유형 및 객체 모두를 저장할 수 있습니다. 예를 들어, 정수, 문자, 불린, 실수와 같은 기본 유형뿐만 아니라 사용자 정의 클래스의 인스턴스 등도 배열에 저장할 수 있습니다.

```java
int[] intArray = new int[10]; // 기본 데이터 유형
String[] strArray = new String[10]; // 객체
```

ArrayList: ArrayList는 객체만 저장할 수 있습니다. 따라서 기본 유형을 저장하려면 해당 기본 유형의 래퍼 클래스를 사용해야 합니다. 예를 들어, Integer는 int의 래퍼 클래스이고, Double은 double의 래퍼 클래스입니다.

```java
ArrayList<Integer> arrayList = new ArrayList<>(); // 기본 데이터 유형의 래퍼 클래스
ArrayList<String> strArrayList = new ArrayList<>(); // 객체
```

이런 특성 때문에 기본 유형을 저장하는 데는 배열이 메모리 사용 면에서 효율적일 수 있지만, 배열의 크기는 변경할 수 없으므로 데이터 집합의 크기가 동적으로 변하는 경우에는 ArrayList를 사용하는 것이 더 편리할 수 있습니다.

또한, Java 5부터는 '오토박싱'과 '언박싱' 기능을 지원하여 기본 데이터 유형과 해당 래퍼 클래스 간의 변환을 자동으로 처리해줍니다. 이로 인해 ArrayList에 기본 데이터 유형을 저장하거나 불러올 때, 개발자는 이 변환 과정을 명시적으로 코드에 쓸 필요가 없어져서 편리해졌습니다.

예를 들어, 다음 코드는 int 값을 ArrayList에 저장하는 과정을 보여줍니다. 이 때, 컴파일러가 int 값을 자동으로 Integer로 변환해주는 오토박싱 과정이 일어납니다.

```java
ArrayList<Integer> list = new ArrayList<>();
int num = 5;
list.add(num); // 오토박싱: 컴파일러가 num을 Integer로 자동 변환
```

이와 유사하게, Integer 객체를 int로 변환하는 언박싱 과정도 자동으로 일어납니다.

```java
int retrievedNum = list.get(0); // 언박싱: 컴파일러가 Integer 객체를 int로 자동 변환
```

### ArrayList랑 배열 각각 정렬하기


Java에서 ArrayList와 int[] 배열을 정렬하는 방법은 다음과 같습니다.

1. ArrayList 정렬하기

Collections.sort() 메소드를 사용하여 ArrayList를 정렬할 수 있습니다.

```java
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(5);
        arrayList.add(9);
        arrayList.add(1);
        arrayList.add(6);

        Collections.sort(arrayList);

        for (int num : arrayList) {
            System.out.println(num);
        }
    }
}
```

이 코드는 arrayList의 요소들을 오름차순으로 정렬합니다.

1. int[] 배열 정렬하기

Arrays.sort() 메소드를 사용하여 int[] 배열을 정렬할 수 있습니다.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] array = {5, 9, 1, 6};

        Arrays.sort(array);

        for (int num : array) {
            System.out.println(num);
        }
    }
}
```

이 코드는 array의 요소들을 오름차순으로 정렬합니다.

## ArrayList랑 배열 길이

다음은 배열의 길이를 알아내는 예시입니다:

```java
int[] array = new int[10]; // 길이가 10인 배열 생성
System.out.println(array.length); // 10 출력
```

반면에 `ArrayList`와 같은 컬렉션 클래스에서는 `.size()` 메서드를 사용하여 요소의 수를 알아낼 수 있습니다. 이는 동적으로 변경되는 데이터 구조에서 요소의 수를 알아내는 데 사용됩니다.

```java
ArrayList<Integer> list = new ArrayList<>(); // ArrayList 생성
list.add(1);
list.add(2);
list.add(3);
System.out.println(list.size()); // 3 출력
```

따라서 배열과 ArrayList는 요소의 수를 알아내는 방식이 서로 다르다는 것을 알 수 있습니다. 이는 배열이 고정 길이의 데이터 구조이고, ArrayList는 동적으로 크기가 변하는 데이터 구조라는 점에서 기인합니다.

## Set

```java
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Cherry");
        set.add("Apple"); // This will not be added as "Apple" is already in the set

        System.out.println(set); // Outputs: [Apple, Banana, Cherry]
    }
}
```

위의 예시에서 "Apple"은 처음에 한 번 추가되고, 두 번째로 추가될 때는 무시됩니다. 왜냐하면 `Set`은 중복 항목을 허용하지 않기 때문입니다.

**주요 메소드들**

- `add(E e)`: Set에 지정된 요소를 추가합니다. 만약 이미 Set에 요소가 존재한다면, 추가하지 않습니다. 요소가 성공적으로 추가되면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
- `remove(Object o)`: Set에서 지정된 요소를 제거합니다. 만약 요소가 성공적으로 제거되면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
- `contains(Object o)`: Set이 지정된 요소를 포함하고 있는지 확인합니다. 요소가 Set에 있다면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
- `size()`: Set의 크기(요소의 수)를 반환합니다.
- `isEmpty()`: Set이 비어있는지 확인합니다. Set이 비어있다면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
- `clear()`: Set에서 모든 요소를 제거합니다.
- `iterator()`: Set에서 반복자를 반환합니다. 반복자는 Set의 모든 요소를 순회하는 데 사용될 수 있습니다.
- `toArray()`: Set의 모든 요소를 포함하는 배열을 반환합니다. 이 배열은 Set에서 제공하는 순서를 유지합니다.
- `equals(Object o)`: 현재 Set와 지정된 객체가 같은지 확인합니다.
- `hashCode()`: Set의 해시 코드 값을 반환합니다.

위의 메소드들은 `Set` 인터페이스를 구현하는 모든 클래스(`HashSet`, `LinkedHashSet`, `TreeSet` 등)에서 사용할 수 있습니다.

## Map

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        String[] array = {"apple", "banana", "apple", "orange", "banana", "banana"};
        HashMap<String, Integer> countMap = new HashMap<>();

        for (String item : array) {
            // HashMap의 getOrDefault 메서드를 사용하여 해당 아이템의 현재 카운트를 가져오거나, 
            // 아이템이 처음 나온 경우에는 기본값으로 0을 사용합니다.
            Integer count = countMap.getOrDefault(item, 0);
            countMap.put(item, count + 1);
        }

        for (String key : countMap.keySet()) {
            System.out.println(key + ": " + countMap.get(key));
        }
    }
}

```

1. `put(K key, V value)`: 지정된 키에 지정된 값을 이 맵에 저장합니다. 이 맵이 이미 해당 키의 매핑을 포함하고 있으면, 이전 값을 새 값으로 대체합니다.
2. `get(Object key)`: 지정된 키에 매핑된 값을 반환합니다. 키에 대한 매핑이 없을 경우 null을 반환합니다.
3. `remove(Object key)`: 지정된 키에 매핑된 항목을 삭제합니다. 삭제된 값을 반환합니다.
4. `containsKey(Object key)`: 이 맵이 지정된 키의 매핑을 포함하고 있는지 확인합니다.
5. `containsValue(Object value)`: 이 맵이 지정된 값을 가진 매핑을 하나 이상 포함하고 있는지 확인합니다.
6. `size()`: 이 맵에 저장된 키-값 매핑의 수를 반환합니다.
7. `isEmpty()`: 이 맵이 비어있는 경우 `true`를 반환합니다.
8. `clear()`: 이 맵의 모든 매핑을 삭제합니다.
9. `keySet()`: 이 맵에 포함된 키들로 이루어진 `Set` 뷰를 반환합니다.
10. `values()`: 이 맵에 포함된 값들로 이루어진 `Collection` 뷰를 반환합니다.
11. `entrySet()`: 이 맵에 포함된 매핑들로 이루어진 `Set` 뷰를 반환합니다.
12. `getOrDefault(Object key, V defaultValue)`: 지정된 키에 매핑된 값을 반환하거나, 매핑이 없을 경우 디폴트 값을 반환합니다.

### Integer & int

`HashMap`에서는 `int` 대신 `Integer`를 사용하는 이유는 기본적으로 자바의 컬렉션 클래스들이 기본 데이터 타입 (int, double, boolean 등)을 직접적으로 지원하지 않기 때문입니다. 이들은 오직 객체만을 저장할 수 있습니다. 그래서 우리는 `Integer`, `Double`, `Boolean` 등의 wrapper 클래스를 사용합니다.

`Integer`는 `int`의 wrapper 클래스로서 `null` 값을 가질 수 있는 특징이 있습니다. 이는 아직 값을 할당받지 않은 상태를 표현하는 데 유용합니다.

그래서 `HashMap`에서 `get` 메서드를 호출하면, 값이 있을 경우 해당 `Integer` 객체를 반환하고, 값이 없을 경우 `null`을 반환합니다. 이렇게 `null`을 반환하는 기능을 활용하여 `getOrDefault` 메서드에서 기본값을 설정할 수 있게 되는 것입니다.

자바의 Auto-boxing과 Unboxing 특징으로 인해 우리는 `int`와 `Integer`를 자유롭게 서로 변환하여 사용할 수 있습니다. `Integer`를 `int`로 자동 변환하는 것을 unboxing이라 하며, 반대로 `int`를 `Integer`로 변환하는 것을 auto-boxing이라 합니다. 그래서 `int`와 `Integer`가 서로 변환이 가능해집니다.

아래 코드에서,

```java
Integer count = countMap.getOrDefault(item, 0);

```

우리는 `0`이라는 기본값(`int`)를 제공하고 있지만, 이것이 `Integer`로 자동 변환되어 `count`에 할당됩니다. 이는 자바의 auto-boxing 덕분입니다.

 자바의 제네릭(Generic)은 클래스 또는 인터페이스의 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법을 말합니다. 제네릭은 클래스나 메소드에서 사용할 내부 데이터 타입을 컴파일 시에 미리 지정하는 방식으로, 타입 안정성을 제공하고 형변환 번거로움을 줄여줍니다.

그러나 제네릭은 기본 데이터 타입을 허용하지 않습니다. 따라서 `int`, `char`, `boolean` 등과 같은 기본 데이터 타입 대신 해당 타입들의 래퍼 클래스를 사용해야 합니다. 예를 들어 `int`의 경우 `Integer`, `char`의 경우 `Character`, `boolean`의 경우 `Boolean` 등을 사용해야 합니다.

따라서 아래와 같은 제네릭 사용은 오류를 발생시킵니다:

```java
List<int> list = new ArrayList<>(); // 잘못된 코드

```

대신 다음과 같이 래퍼 클래스를 사용해야 합니다:

```java
List<Integer> list = new ArrayList<>(); // 올바른 코드

```

## Node 클래스화

```java
public class ListNode {
    int val; // 노드가 가지는 값
    ListNode next; // 다음 노드에 대한 참조

    ListNode(int val) { 
        this.val = val; 
    }  // 생성자
}


```

```java
class Node {
    int x;
    int y;

    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

```



```java
public class TreeNode {
    int val;
    TreeNode left; // 왼쪽 자식 노드에 대한 참조
    TreeNode right; // 오른쪽 자식 노드에 대한 참조

    TreeNode(int val) {
        this.val = val;
    }
}

```

## Stack

1. `push(E item)`: 스택의 맨 위(맨 마지막 위치)에 요소를 추가합니다. 추가된 요소를 반환합니다.
2. `pop()`: 스택의 맨 위에 있는 요소를 제거하고 그 요소를 반환합니다. 스택이 비어 있을 경우, `EmptyStackException`이 발생합니다.
3. `peek()`: 스택의 맨 위에 있는 요소를 제거하지 않고 반환합니다. 스택이 비어 있을 경우, `EmptyStackException`이 발생합니다.
4. `empty()`: 스택이 비어 있으면 `true`를, 그렇지 않으면 `false`를 반환합니다.
5. `search(Object o)`: 스택에서 주어진 객체를 찾아 그 위치를 반환합니다. 스택의 맨 위부터 아래로 탐색하며, 맨 위는 1로 시작합니다. 객체가 스택에 없으면 `-1`을 반환합니다.
6. `size()`: 스택에 있는 요소의 개수를 반환합니다.

이러한 메소드들을 사용하면 스택에 있는 요소를 추가, 제거, 조회하는 등의 작업을 할 수 있습니다. 스택은 LIFO(Last In First Out) 원칙에 따라 동작하기 때문에, `push()`로 추가한 마지막 요소가 `pop()` 또는 `peek()`을 통해 먼저 접근하거나 제거되는 점을 기억하시면 됩니다.

```java
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Stack 생성
        Stack<Integer> stack = new Stack<Integer>();

        // push(): 요소 추가
        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.println("Initial Stack: " + stack);

        // pop(): 요소 제거 및 반환
        int removedElement = stack.pop();
        System.out.println("Popped element: " + removedElement);
        System.out.println("Stack after pop: " + stack);

        // peek(): 맨 위의 요소 조회
        int top = stack.peek();
        System.out.println("Current top element: " + top);

        // empty(): 스택이 비어있는지 확인
        boolean isEmpty = stack.empty();
        System.out.println("Is the stack empty? " + isEmpty);

        // search(): 요소 위치 찾기
        int position = stack.search(2);
        System.out.println("Position of 2: " + position);

        // size(): 스택의 크기 확인
        int size = stack.size();
        System.out.println("Size of stack: " + size);
    }
}

```



## Queue

Queue 인터페이스의 주요 메서드에는 다음과 같은 것들이 있습니다:

- `add(E element)`: 큐의 끝에 요소를 추가합니다.
- `remove()`: 큐의 앞에서 요소를 삭제하고 반환합니다. 큐가 비어 있으면 예외를 발생시킵니다.
- `peek()`: 큐의 앞에서 요소를 삭제하지 않고 반환합니다. 큐가 비어 있으면 null을 반환합니다.
- `size()`: 큐의 크기(요소의 수)를 반환합니다.
- `poll()`: 앞의 요소 삭제 반환

다음은 Queue의 사용 예제입니다:

```java
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<Integer>();
        
        queue.add(1);  // queue에 1 추가
        queue.add(2);  // queue에 2 추가
        queue.add(3);  // queue에 3 추가

        System.out.println(queue.peek()); // queue의 앞쪽 요소 확인

```

## .map()

```java
import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String input = br.readLine();
        String[] stringList = input.split(" ");

        int[] inputList = Arrays.stream(stringList)
                                .mapToInt(Integer::parseInt)
                                .toArray();

        // 배열의 내용을 출력합니다.
        for (int num : inputList) {
            System.out.println(num);
        }
    }
}

```



```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        // String 리스트를 생성합니다.
        List<String> stringList = Arrays.asList("1", "2", "3", "4", "5");

        // map 메소드를 사용하여 stringList의 모든 요소를 Integer로 변환하고,
        // collect 메소드를 사용하여 다시 List<Integer>로 만듭니다.
        List<Integer> intList = stringList.stream()
                                          .map(x -> Integer.parseInt(x))
                                          .collect(Collectors.toList());

        // 변환된 int 리스트를 출력합니다.
        for (int num : intList) {
            System.out.println(num);
        }
    }
}

```

- Java 8의 Stream API는 컬렉션에서 연속된 요소를 처리하는 다양한 방법을 제공합니다. 그 중 `mapToInt`와 `map`은 스트림의 요소를 다른 형태로 변환하는 메소드입니다.

  - `mapToInt`: 주어진 함수를 스트림의 각 요소에 적용한 결과를 포함하는 새로운 `IntStream`을 반환합니다. `IntStream`은 int 형식의 요소로 구성된 시퀀스를 다루는 스트림입니다. `toArray` 메소드는 이 `IntStream`을 int 배열로 변환합니다.

  ```java
  List<String> strings = Arrays.asList("1", "2", "3");
  int[] numbers = strings.stream().mapToInt(Integer::parseInt).toArray(); // 결과: int 배열 [1, 2, 3]
  ```

  - `map`: 주어진 함수를 스트림의 각 요소에 적용한 결과를 포함하는 새로운 `Stream`을 반환합니다. 이후 `collect` 메소드를 사용하여 이 스트림을 다른 형태의 컬렉션으로 변환할 수 있습니다.

  ```java
  List<String> strings = Arrays.asList("1", "2", "3");
  List<Integer> numbers = strings.stream().map(Integer::parseInt).collect(Collectors.toList()); // 결과: List<Integer> [1, 2, 3]
  ```

  결론적으로, `mapToInt`와 `toArray`를 함께 사용하면 스트림의 각 요소를 int 값으로 변환하고 이를 int 배열로 모을 수 있습니다. 반면, `map`과 `collect`를 함께 사용하면 스트림의 각 요소를 다른 형태로 변환하고 이를 List나 Set 같은 컬렉션으로 모을 수 있습니다.

### lambda

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        // String 리스트를 생성합니다.
        List<String> stringList = Arrays.asList("1", "2", "3", "4", "5");

        // map 메소드를 사용하여 stringList의 모든 요소를 Integer로 변환하고,
        // collect 메소드를 사용하여 다시 List<Integer>로 만듭니다.
        List<Integer> intList = stringList.stream()
                                          .map(Integer::parseInt)
                                          .collect(Collectors.toList());

        // 변환된 int 리스트를 출력합니다.
        for (int num : intList) {
            System.out.println(num);
        }
    }
}

```

## 형 변환

`(int)`는 Java에서 형 변환(Type Casting)을 수행하는 문법입니다.

형 변환은 한 자료형의 값을 다른 자료형으로 변환하는 것을 의미합니다. 이는 두 가지 형태로 나타날 수 있습니다:

1. Widening Casting (자동 형 변환): 작은 데이터 타입을 큰 데이터 타입으로 변환할 때. 예를 들어, `int`를 `double`로 변환하는 것.
2. Narrowing Casting (명시적 형 변환): 큰 데이터 타입을 작은 데이터 타입으로 변환할 때. 예를 들어, `double`을 `int`로 변환하는 것. 이때는 데이터 손실이 일어날 수 있으므로, 프로그래머가 명시적으로 형 변환을 지시해야 합니다.

아래는 Narrowing Casting의 예시입니다:

```java
double myDouble = 9.78;
int myInt = (int) myDouble; // Narrowing Casting

System.out.println(myDouble);   // Outputs 9.78
System.out.println(myInt);      // Outputs 9

```

여기서 `(int)`는 `myDouble`의 값을 `int` 형으로 변환하라는 지시입니다. 이때 `myDouble`의 값 `9.78`에서 소수부분 `.78`이 손실되고, `myInt`는 손실된 값 `9`만을 저장하게 됩니다.

## min

`.min()`은 Java 8의 Stream API에 포함된 메소드로, 스트림의 요소 중 최소값을 찾습니다. 이 메소드는 OptionalInt 객체를 반환합니다.

Optional 클래스는 '값이 있을 수도, 없을 수도 있는' 컨테이너 객체입니다. 즉, 값이 존재하면 이 값을 가져올 수 있고, 값이 없으면 기본 값을 설정하거나 예외를 발생시킬 수 있습니다.

따라서 `.min()`의 결과가 값이 없을 경우를 대비해 `.getAsInt()` 메소드를 호출해서 int 값을 가져옵니다. 만약 `.min()`의 결과가 비어있는 Optional 객체라면, `.getAsInt()`는 NoSuchElementException을 발생시킵니다.

그러나 이 코드에서는 숫자의 배열이 항상 하나 이상의 요소를 포함하므로, `.min()`이 비어있는 Optional 객체를 반환하는 경우는 없습니다. 그래서 안전하게 `.getAsInt()`를 호출할 수 있습니다.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        int min = Arrays.stream(numbers).min().getAsInt();

        System.out.println("Minimum value: " + min); // 출력: "Minimum value: 1"
    }
}

```

## Math.pow()

```java
public class Main {
    public static void main(String[] args) {
        double base = 2;
        double exponent = 3;

        // 2의 3제곱을 계산합니다.
        double result = Math.pow(base, exponent);

        System.out.println(result);  // 출력: 8.0
    }
}

```

```java
int min = (int) Math.pow(10, 6);

```

## ||


Java에서 if문에 OR 연산자를 사용하려면 `||` 기호를 사용하면 됩니다.

다음은 그 예시입니다:

```java
int a = 10;
int b = 20;

if (a > 15 || b > 15) {
    System.out.println("Either a or b is greater than 15");
}
```

위 코드에서 `a > 15 || b > 15`는 "a가 15보다 크거나(bigger than) 또는(or) b가 15보다 크다"는 논리적인 표현입니다. a나 b 둘 중 하나라도 이 조건을 만족하면 if문의 본문이 실행됩니다.

이와 같이 `||`는 OR 연산을 나타내는 논리 연산자입니다. OR 연산은 둘 중 하나 이상의 피연산자가 참일 때 참을 반환합니다.

## StringBuilder

`StringBuilder`는 자바의 `java.lang` 패키지에 있는 클래스로, 문자열을 수정하거나 조작하는 연산을 수행할 때 사용합니다. 기본적으로 자바에서 문자열은 불변(Immutable)하기 때문에, 문자열에 대한 수정 연산이 빈번하게 일어나는 경우 매번 새로운 문자열 객체가 생성되어 메모리 사용이 비효율적일 수 있습니다. `StringBuilder`는 이러한 문제를 해결하기 위해 도입되었습니다.

`StringBuilder`는 내부적으로 변경 가능한 문자열을 관리하므로, 문자열에 대한 여러 조작을 수행해도 새로운 객체를 생성하지 않습니다. 따라서 대량의 문자열 조작이 필요한 경우 `StringBuilder`를 사용하면 훨씬 더 효율적인 코드를 작성할 수 있습니다.

아래는 `StringBuilder`의 사용 예시입니다:

```java
StringBuilder sb = new StringBuilder();

sb.append("Hello, ");
sb.append("World!");

System.out.println(sb.toString());  // 출력: Hello, World!
```

위 코드에서는 먼저 `StringBuilder` 객체를 생성하고, `append()` 메소드를 사용해 문자열을 추가합니다. 마지막으로 `toString()` 메소드를 이용해 최종적인 문자열을 얻습니다. 이렇게 `StringBuilder`를 이용하면 여러 개의 문자열을 연결하는 작업을 효율적으로 수행할 수 있습니다.

또한, `StringBuilder`는 `insert()`, `delete()`, `reverse()` 등의 메소드를 제공하여 문자열에 대한 다양한 조작을 지원합니다.

자바의 `String`은 불변(immutable) 객체입니다. 따라서 `String` 객체에 어떤 변경을 가하면, 원본 문자열을 수정하는 것이 아니라 새로운 `String` 객체를 생성합니다. 이렇게 문자열 연산을 여러 번 수행하면 많은 `String` 객체가 생성되고 이는 메모리 사용에 비효율적이 됩니다.

반면, `StringBuilder`는 가변(mutable) 객체로 설계되어 있어, 한번 생성된 `StringBuilder` 객체에 계속해서 문자열을 추가하거나 변경하는 것이 가능합니다. 그래서 문자열의 연결 등을 반복하는 작업에 있어서는 `StringBuilder`를 사용하는 것이 메모리와 연산 시간 면에서 더 효율적입니다.

그러나 이러한 특징이 항상 더 좋은 성능을 보장하는 것은 아닙니다. 예를 들어, 문자열 연결 연산이 몇 번 되지 않는다면, `StringBuilder`를 사용하는 것보다 그냥 `+` 연산자를 사용하는 것이 코드가 더 간결하고 이해하기 쉬울 수 있습니다.

따라서 상황에 따라 적절한 방법을 선택하는 것이 중요합니다.

## this

자바에서 `this` 키워드는 클래스 안에서 현재 인스턴스(오브젝트)를 참조하기 위해 사용됩니다. `this`를 사용하면 클래스의 메서드나 생성자에서 현재 인스턴스의 변수를 참조하거나 다른 메서드를 호출할 수 있습니다. `this`의 주요 사용 사례는 다음과 같습니다:

1. **현재 클래스의 인스턴스 변수를 참조하기 위해**: `this`는 현재 클래스의 인스턴스 변수를 참조하는 데 사용됩니다. 메서드나 생성자의 매개 변수 이름이 클래스의 인스턴스 변수 이름과 같을 때, 이는 혼란을 줄 수 있습니다. 이런 경우, `this` 키워드는 인스턴스 변수와 로컬 변수를 구분하는 데 사용됩니다.

   예시:

   ```java
   public class Person {
       private String name;
   
       public Person(String name) {
           this.name = name;  // Here, 'this' is used to refer to the instance variable 'name'
       }
   }
   ```

2. **현재 클래스의 메서드를 호출하기 위해**: `this`는 현재 클래스의 메서드를 호출하는 데도 사용될 수 있습니다.

   예시:

   ```java
   public class Calculator {
       private int result;
   
       public void add(int value) {
           this.result += value;  // Here, 'this' is used to call the method 'add'
       }
   }
   ```

3. **현재 클래스의 생성자를 호출하기 위해**: `this()`를 사용하여 같은 클래스의 다른 생성자를 호출할 수 있습니다.

   예시:

   ```java
   public class Rectangle {
       private int width;
       private int height;
   
       public Rectangle() {
           this(1, 1);  // Here, 'this' is used to call another constructor
       }
   
       public Rectangle(int width, int height) {
           this.width = width;
           this.height = height;
       }
   }
   ```

이처럼 `this` 키워드는 클래스 내부에서 현재 인스턴스를 참조하는 매우 중요한 방법입니다.

## @Override

자바에서 메소드 오버라이딩은 부모 클래스에서 이미 제공하는 메소드를 자식 클래스에서 재정의하여 사용하는 것을 말합니다. 이를 통해 자식 클래스는 부모 클래스의 메소드를 자신의 요구에 맞게 변경할 수 있습니다.

다음은 메소드 오버라이딩을 사용하는 간단한 예시입니다:

```java
// 부모 클래스
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound");
    }
}

// 자식 클래스
public class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("The cat meows");
    }
}

// 메인 클래스
public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();  // Create an Animal object
        Animal myCat = new Cat();  // Create a Cat object

        myAnimal.sound();  // Outputs "The animal makes a sound"
        myCat.sound();  // Outputs "The cat meows"
    }
}
```

위 코드에서, `Cat` 클래스는 `Animal` 클래스를 상속받아 `sound()` 메소드를 오버라이딩하고 있습니다. 이 때문에 `Cat` 객체에서 `sound()` 메소드를 호출하면 "The cat meows"라는 메시지가 출력됩니다.

`@Override` 어노테이션은 컴파일러에게 이 메소드가 부모 클래스의 메소드를 오버라이딩하고 있다는 것을 알려줍니다. 이 어노테이션을 사용하면 컴파일러가 오버라이딩 메소드의 이름, 파라미터 타입, 반환 타입이 부모 클래스의 메소드와 일치하는지 확인하므로 실수를 방지하는 데 도움이 됩니다.



자바에서 메소드를 오버라이딩할 때는 몇 가지 규칙이 있습니다. 오버라이딩의 기본적인 조건은 다음과 같습니다:

1. **메소드 이름이 같아야 합니다**: 부모 클래스의 메소드와 같은 이름의 메소드를 자식 클래스에서 정의해야 합니다.
2. **메소드 매개변수가 같아야 합니다**: 부모 클래스의 메소드와 자식 클래스의 메소드가 같은 타입과 개수의 매개변수를 가져야 합니다. 이를 메소드 시그니처라고 부르며, 오버라이딩할 때는 이 시그니처가 부모와 자식 클래스에서 동일해야 합니다.
3. **반환 타입이 같아야 합니다**: 부모 클래스의 메소드와 동일한 반환 타입을 가져야 합니다. 단, Java 5부터는 공변 반환 타입이 도입되어, 오버라이딩 메소드의 반환 타입이 부모 클래스 메소드의 반환 타입의 서브 타입이어도 허용됩니다.
4. **접근 수준이 같거나 더 넓어야 합니다**: 오버라이딩 메소드의 접근 제어자는 부모 클래스의 메소드와 같거나 더 넓은 범위로 설정해야 합니다. 예를 들어, 부모 클래스의 메소드가 `protected`로 선언되었다면, 오버라이딩 메소드는 `protected`나 `public`으로 선언해야 합니다.
5. **부모 클래스의 메소드가 final이 아니어야 합니다**: `final` 키워드가 붙은 메소드는 오버라이딩할 수 없습니다.
6. **부모 클래스의 메소드가 static이 아니어야 합니다**: `static` 메소드는 클래스 레벨에서 작동하므로 오버라이딩할 수 없습니다. `static` 메소드를 자식 클래스에서 같은 이름으로 다시 정의하는 것은 메소드 히딩(Method Hiding)이라고 합니다.

이런 조건을 지키면서 메소드를 오버라이딩하면, 부모 클래스의 메소드를 자식 클래스가 필요에 맞게 재정의하여 사용할 수 있습니다.

### super


자바에서 `super` 키워드는 자식 클래스에서 부모 클래스로 접근할 때 사용됩니다. `super`는 주로 두 가지 방식으로 사용됩니다:

1. **부모 클래스의 메소드를 호출하는데 사용**될 수 있습니다. 이는 자식 클래스에서 메소드를 오버라이딩했지만 부모 클래스의 원래 메소드를 여전히 호출해야 할 때 유용합니다.

```java
public class ParentClass {
    public void display() {
        System.out.println("This is the parent class display method");
    }
}

public class ChildClass extends ParentClass {
    public void display() {
        System.out.println("This is the child class display method");
    }

    public void callParentDisplay() {
        super.display();
    }
}

// 메인 클래스
public class Main {
    public static void main(String[] args) {
        ChildClass child = new ChildClass();
        child.display();  // 출력: "This is the child class display method"
        child.callParentDisplay();  // 출력: "This is the parent class display method"
    }
}
```

위 예시에서, `ChildClass`의 `callParentDisplay` 메소드는 `super.display();`를 사용하여 부모 클래스의 `display` 메소드를 호출합니다.

1. **부모 클래스의 생성자를 호출하는데 사용**될 수 있습니다. 자식 클래스의 생성자에서는 첫 번째 명령문으로 부모 클래스의 생성자를 호출할 수 있습니다.

```java
public class ParentClass {
    public ParentClass() {
        System.out.println("ParentClass constructor called");
    }
}

public class ChildClass extends ParentClass {
    public ChildClass() {
        super();  // 부모 클래스의 생성자를 호출합니다.
        System.out.println("ChildClass constructor called");
    }
}

// 메인 클래스
public class Main {
    public static void main(String[] args) {
        ChildClass child = new ChildClass();
        // 출력: "ParentClass constructor called"
        // 출력: "ChildClass constructor called"
    }
}
```

위 예시에서, `ChildClass`의 생성자는 `super();`를 사용하여 부모 클래스인 `ParentClass`의 생성자를 호출합니다.

따라서 `super`는 자식 클래스에서 부모 클래스의 메소드나 생성자를 명시적으로 호출할 때 사용하는 키워드입니다.

## final

자바에서 `final` 키워드는 "변경 불가능"이라는 의미를 가집니다. `final`은 변수, 메소드, 클래스에 사용될 수 있으며, 각각의 경우에 다음과 같은 의미를 가집니다:

1. **Final 변수**: `final` 변수는 한 번 초기화되면 그 값을 변경할 수 없습니다. 즉, `final` 변수는 상수(constant)로 간주됩니다. 예를 들어, `final int MAX_SPEED = 100;`은 MAX_SPEED 값을 나중에 변경할 수 없음을 의미합니다.
2. **Final 메소드**: `final` 메소드는 서브 클래스에서 오버라이드(재정의)할 수 없습니다. 이는 기능의 확장을 제한하고, 특정 메소드가 서브 클래스에서 변경되는 것을 막는데 사용됩니다.
3. **Final 클래스**: `final` 클래스는 상속할 수 없습니다. 즉, 다른 클래스가 `final` 클래스를 확장하려고 하면 컴파일 에러가 발생합니다. 이는 클래스의 설계를 변경하지 못하게 하는 효과가 있습니다. `java.lang.String` 클래스는 가장 잘 알려진 `final` 클래스의 예입니다.

`final` 키워드는 프로그래밍에서 불변성(immutability)을 확보하고, 코드의 안정성과 보안성을 높이는데 도움이 됩니다.

자바에서 `final` 키워드는 "변경 불가능"이라는 의미를 가집니다. `final`은 변수, 메소드, 클래스에 사용될 수 있으며, 각각의 경우에 다음과 같은 의미를 가집니다:

1. **Final 변수**: `final` 변수는 한 번 초기화되면 그 값을 변경할 수 없습니다. 즉, `final` 변수는 상수(constant)로 간주됩니다. 예를 들어, `final int MAX_SPEED = 100;`은 MAX_SPEED 값을 나중에 변경할 수 없음을 의미합니다.
2. **Final 메소드**: `final` 메소드는 서브 클래스에서 오버라이드(재정의)할 수 없습니다. 이는 기능의 확장을 제한하고, 특정 메소드가 서브 클래스에서 변경되는 것을 막는데 사용됩니다.
3. **Final 클래스**: `final` 클래스는 상속할 수 없습니다. 즉, 다른 클래스가 `final` 클래스를 확장하려고 하면 컴파일 에러가 발생합니다. 이는 클래스의 설계를 변경하지 못하게 하는 효과가 있습니다. `java.lang.String` 클래스는 가장 잘 알려진 `final` 클래스의 예입니다.

`final` 키워드는 프로그래밍에서 불변성(immutability)을 확보하고, 코드의 안정성과 보안성을 높이는데 도움이 됩니다.



`final` 키워드의 사용 예시는 다음과 같습니다:

1. **Final 변수**:

   ```java
   public class Circle {
       final double PI = 3.14159;
       double radius;
   
       public Circle(double radius) {
           this.radius = radius;
       }
   
       double calculateArea() {
           return PI * radius * radius;  // PI 값을 변경할 수 없습니다.
       }
   }
   ```

   위 예시에서 `PI`는 `final` 변수로 선언되어 있어 한 번 초기화된 후에는 그 값을 변경할 수 없습니다.

2. **Final 메소드**:

   ```java
   public class Vehicle {
       public final void startEngine() {
           System.out.println("Starting engine...");
           // 이 메소드는 자식 클래스에서 오버라이드 할 수 없습니다.
       }
   }
   
   public class Car extends Vehicle {
       @Override
       public void startEngine() {  // 컴파일 에러
           System.out.println("Starting car engine...");
       }
   }
   ```

   위 예시에서 `startEngine` 메소드는 `final`로 선언되어 있어서, `Car` 클래스에서 이를 오버라이드하려고 하면 컴파일 에러가 발생합니다.

3. **Final 클래스**:

   ```java
   public final class FinalClass {
       // 코드..
   }
   
   public class SomeClass extends FinalClass {  // 컴파일 에러
       // 코드..
   }
   ```

   위 예시에서 `FinalClass`는 `final` 클래스로 선언되어 있어서, 이를 상속하려는 `SomeClass`는 컴파일 에러를 발생시킵니다.

이처럼 `final` 키워드는 변수, 메소드, 클래스의 변경을 제한하는 데 사용됩니다.

## static

자바에서 `static` 키워드는 특정 멤버(변수, 메소드, 초기화 블록 등)가 객체(인스턴스)에 속하는 것이 아니라 클래스에 속하게 만듭니다. 즉, `static` 키워드가 붙은 멤버는 클래스 레벨에서 작동하며, 모든 인스턴스가 공유합니다.

1. **Static 변수**: `static` 변수(또는 클래스 변수)는 클래스에 속하며, 모든 인스턴스에서 이 변수를 공유합니다. `static` 변수는 클래스가 메모리에 로드될 때 한 번만 초기화되며, 클래스당 하나의 복사본만 있습니다.

   예시:

   ```java
   public class MyStaticClass {
       static int staticVar = 0;
   
       MyStaticClass() {
           staticVar++;
       }
   
       void printStaticVar() {
           System.out.println(staticVar);
       }
   }
   
   // 사용 예시
   MyStaticClass obj1 = new MyStaticClass();
   obj1.printStaticVar();  // 출력: 1
   
   MyStaticClass obj2 = new MyStaticClass();
   obj2.printStaticVar();  // 출력: 2
   ```

   위 예시에서 `staticVar`는 `static`으로 선언된 변수이므로, `MyStaticClass`의 모든 인스턴스에서 공유됩니다.

2. **Static 메소드**: `static` 메소드(또는 클래스 메소드)는 클래스에 속하며, 객체의 생성 없이 호출할 수 있습니다. `static` 메소드는 `static` 변수나 다른 `static` 메소드만 접근할 수 있습니다.

   예시:

   ```java
   public class MyStaticClass {
       static int staticVar = 0;
   
       static void incrementStaticVar() {
           staticVar++;
       }
   
       static void printStaticVar() {
           System.out.println(staticVar);
       }
   }
   
   // 사용 예시
   MyStaticClass.incrementStaticVar();
   MyStaticClass.printStaticVar();  // 출력: 1
   ```

   위 예시에서 `incrementStaticVar`와 `printStaticVar` 메소드는 `static`으로 선언되어 있으므로 객체의 생성 없이 직접 호출할 수 있습니다.

3. **Static 초기화 블록**: `static` 초기화 블록은 클래스가 JVM에 의해 로드될 때 한 번만 실행됩니다. 이 블록은 복잡한 `static` 변수의 초기화 또는 다른 `static` 초기화 작업에 사용됩니다.

   예시:

   ```java
   public class MyStaticClass {
       static int staticVar;
   
       // Static initialization block
       static {
           staticVar = doComplexCalculation();
       }
   
       static int doComplexCalculation() {
           // 복잡한 계산 코드...
           return result;
       }
   }
   ```

   위 예시에서 `static` 초기화 블록은 `staticVar`를 복잡한 계산 결과로 초기화하는 데 사용됩니다.

4. **Static 클래스**: `static` 클래스는 바깥 클래스 내부에 선언된 중첩 클래스만 될 수 있습니다. 이는 바깥 클래스와 독립적으로 동작하며, 바깥 클래스의 비-`static` 멤버에 접근할 수 없습니다.

   예시:

   ```java
   public class OuterClass {
       static int staticVar = 0;
   
       static class StaticNestedClass {
           void incrementStaticVar() {
               staticVar++;  // Can access static members of outer class
           }
       }
   }
   ```

   위 예시에서 `StaticNestedClass`는 `static`으로 선언된 중첩 클래스로, 바깥 클래스의 `static` 멤버에 접근할 수 있습니다.

### Overloading

자바에서 오버로딩(Overloading)은 같은 이름의 메소드를 여러 개 가지면서 매개변수의 유형과 개수가 다르도록 하는 기능을 말합니다. 이를 통해 하나의 메소드 이름을 사용하되, 제공하는 매개변수에 따라 다른 작업을 수행할 수 있습니다.

오버로딩의 규칙은 다음과 같습니다:

1. 메소드 이름은 같아야 합니다.
2. 매개변수의 개수 또는 타입이 달라야 합니다.
3. 반환 타입은 오버로딩을 구별하는데 사용되지 않습니다.

다음은 오버로딩의 예시입니다:

```java
public class OverloadingExample {

    void demo (int a) {
       System.out.println ("a: " + a);
    }

    void demo (int a, int b) {
       System.out.println ("a and b: " + a + "," + b);
    }

    double demo(double a) {
       System.out.println("double a: " + a);
       return a*a;
    }
}

public class Main {
    public static void main (String args []) {
        OverloadingExample obj = new OverloadingExample();
        double result;
        obj.demo(10);
        obj.demo(10, 20);
        result = obj.demo(5.5);
        System.out.println("O/P : " + result);
    }
}
```

이 예제에서 `demo` 메소드는 세 번 오버로딩 되었습니다. 첫 번째와 두 번째 `demo` 메소드는 void를 반환하며, 세 번째 `demo` 메소드는 double을 반환합니다. 이들 각각은 매개변수의 개수 또는 타입에 따라 다른 기능을 수행합니다.

## **Package** & Import

`package`는 비슷한 유형의 자바 클래스를 그룹화하는 방법을 제공합니다. 이는 이름 충돌을 방지하고, 코드의 유지 관리와 구조화를 향상시킵니다. 패키지 이름은 모두 소문자로 작성하고, 일반적으로는 도메인 이름을 반대로 사용하여 유니크함을 유지합니다. 예를 들어, "com.example.myapp"이 될 수 있습니다.

`package` 키워드를 사용하여 패키지를 선언합니다. 패키지 선언은 반드시 .java 파일의 첫 번째 문장이어야 합니다.

```java
package com.example.myapp;
```

이 코드는 `com.example.myapp` 패키지에 속한 클래스 또는 인터페이스를 선언합니다.

**Import**

다른 패키지에 있는 클래스를 사용하려면 그 클래스의 전체 패키지 이름을 사용해야 합니다. 예를 들어, `java.util` 패키지에 있는 `ArrayList`를 사용하려면 다음과 같이 써야 합니다:

```java
java.util.ArrayList list = new java.util.ArrayList();
```

이렇게 긴 이름을 매번 쓰는 것은 번거로울 수 있으므로, 자바는 `import` 문을 제공하여 다른 패키지의 클래스를 쉽게 참조할 수 있게 해줍니다. `import` 문은 소스 파일의 상단에 위치하며, 해당 파일에서 사용할 다른 패키지의 클래스 또는 인터페이스를 지정합니다. 예를 들어:

```java
import java.util.ArrayList;
```

이렇게 하면 해당 파일에서는 `ArrayList`를 직접 참조할 수 있습니다:

```java
ArrayList list = new ArrayList();
```

모든 클래스를 한 번에 가져오려면 와일드카드(*)를 사용할 수 있습니다:

```java
import java.util.*;
```

이렇게 하면 `java.util` 패키지의 모든 클래스를 직접 참조할 수 있습니다.

따라서 `package`는 현재 소스 코드가 어떤 패키지에 속하는지를 나타내며, `import`는 현재 소스 코드에서 다른 패키지의 클래스 또는 인터페이스를 쉽게 사용할 수 있도록 해줍니다.

```java
package org.opentutorials.javatutorials.packages.example1;

public class A {}
```

 아래 코드는 위에서 정의한 클래스 A를 클래스 B에서 사용하는 예제다. 정상적으로 동작한다. 

```java
package org.opentutorials.javatutorials.packages.example1;  

public class B {    
    public static void main(String[] args) {        
        A a = new A();    
    } 
} 
```

예제는 `A` 클래스와 `B` 클래스가 같은 패키지 `org.opentutorials.javatutorials.packages.example1`에 있기 때문에 `B` 클래스에서 `A` 클래스를 직접 사용할 수 있습니다.

패키지 내부에서는 패키지에 속한 모든 클래스를 다른 `import` 구문 없이 바로 사용할 수 있습니다. 이는 동일한 패키지 내에 있는 클래스들이 서로 밀접하게 관련되어 있기 때문에 이렇게 설계되었습니다.

따라서 위의 예제에서 `B` 클래스에서 `A` 클래스를 사용하려면 별도의 `import` 문 없이 `A`의 인스턴스를 바로 생성할 수 있습니다.

```java
A a = new A();
```

이렇게 `package` 선언은 해당 클래스가 어떤 패키지에 속하는지를 지정하고, 동일 패키지 내의 다른 클래스를 직접 참조할 수 있게 해줍니다.

반면에, 다른 패키지의 클래스를 사용하려면 `import`를 사용하거나, 클래스의 전체 패키지 이름을 사용해야 합니다. 예를 들어, `org.opentutorials.javatutorials.packages.example2` 패키지에 있는 `C` 클래스를 사용하려면 다음과 같이 해야 합니다.

```java
import org.opentutorials.javatutorials.packages.example2.C;
// 또는
org.opentutorials.javatutorials.packages.example2.C c = new org.opentutorials.javatutorials.packages.example2.C();
```

## throw

더 자세히 설명하겠습니다.

**throw**

`throw` 키워드는 프로그램에서 특정 조건에서 예외를 명시적으로 발생시키고자 할 때 사용됩니다. 이를 통해 예외 처리 루틴을 즉시 트리거 할 수 있습니다. `throw`는 실제로 예외 객체를 생성하고 이를 던집니다. `throw` 문은 `java.lang.Throwable` 클래스의 인스턴스를 던질 수 있습니다.

다음은 `throw` 사용의 예입니다:

```java
public void makePayment(double payment) {
    if (payment <= 0) {
        throw new IllegalArgumentException("Payment must be positive.");
    }
    // Payment processing code...
}
```

위의 메소드에서, 입력된 payment 값이 0 이하일 경우 `IllegalArgumentException`을 생성하고 던지며, 이는 일반적으로 프로그램의 다른 부분에서 잡아내어 처리됩니다.

**throws**

`throws` 키워드는 메소드 또는 생성자 선언에 사용되며, 해당 메소드나 생성자가 발생시킬 수 있는 예외를 나열합니다. 이 키워드는 호출자에게 이 메소드를 호출할 때 예외를 처리할 준비를 해야함을 알립니다.

예를 들어, 다음은 `IOException`을 던질 수 있는 메소드 선언입니다:

```java
public void writeToFile(String text) throws IOException {
    // File writing code...
}
```

위 메소드에서, 파일 쓰기 도중 문제가 발생하면 `IOException`이 발생할 수 있습니다. 이 메소드를 호출하는 코드는 `try-catch` 블록 내에서 이 메소드를 호출하거나, 또는 이 메소드가 던진 `IOException`을 다시 던지도록 선언해야 합니다.

**throw와 throws의 조합**

`throw`와 `throws`는 종종 함께 사용됩니다. 메소드 내에서 `throw`를 사용하여 예외를 던지고, `throws`를 사용하여 이 예외를 메소드 선언에 나열할 수 있습니다.

```java
public void makePayment(double payment) throws IllegalArgumentException {
    if (payment <= 0) {
        throw new IllegalArgumentException("Payment must be positive.");
    }
    // Payment processing code...
}
```

이 코드에서 `makePayment` 메소드는 `IllegalArgumentException`을 발생시킬 수 있음을 선언하고 있습니다. 이 메소드를 호출하는 코드는 이 예외를 처리하도록 작성되어야 합니다.

## Collections

아래는 `Collections` 클래스의 주요 메소드들과 각 메소드를 사용하는 예제 코드입니다.

### 정렬 관련

#### sort

```java
List<Integer> list = Arrays.asList(3, 1, 4, 1, 5, 9);
Collections.sort(list);
// list: [1, 1, 3, 4, 5, 9]
```

#### sort with Comparator

```java
List<String> list = Arrays.asList("apple", "banana", "cherry");
Collections.sort(list, Comparator.reverseOrder());
// list: ["cherry", "banana", "apple"]
```

### 검색 관련

#### binarySearch

```java
List<Integer> list = Arrays.asList(1, 3, 5, 7, 9);
int index = Collections.binarySearch(list, 5); // index = 2
```

### 원소 조작

#### reverse

```java
List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
Collections.reverse(list);
// list: [5, 4, 3, 2, 1]
```

#### shuffle

```java
Copy codeList<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
Collections.shuffle(list);
// list: (순서가 무작위로 바뀜)
```

#### swap

```java
List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
Collections.swap(list, 0, 4);
// list: [5, 2, 3, 4, 1]
```

### 기타 유용한 메소드

#### min, max

```
javaCopy codeList<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
int min = Collections.min(list); // min = 1
int max = Collections.max(list); // max = 5
```

#### frequency

```
javaCopy codeList<Integer> list = Arrays.asList(1, 1, 2, 3, 3, 3, 4);
int freq = Collections.frequency(list, 3); // freq = 3
```

#### disjoint

```
javaCopy codeList<Integer> list1 = Arrays.asList(1, 2, 3);
List<Integer> list2 = Arrays.asList(4, 5, 6);
boolean result = Collections.disjoint(list1, list2); // result = true
```

### 불변과 싱글톤 컬렉션 생성

#### unmodifiableList

```
javaCopy codeList<Integer> list = Arrays.asList(1, 2, 3);
List<Integer> unmodifiableList = Collections.unmodifiableList(list);
```

#### singletonList

```
javaCopy codeList<Integer> singletonList = Collections.singletonList(1);
// singletonList: [1]
```

이러한 메소드들은 종종 함께 사용되어 더 복잡한 작업을 수행합니다. 예제 코드는 각 메소드의 기본적인 사용법을 보여줍니다.





![User](./java_basic.assets/imageurl=https%253A%252F%252Flh3.googleusercontent.png)



스트림을 arraylist나 set으로 바꾸는것도 있지 않나



ChatGPT



네, Java 8 이상에서는 Stream API를 사용하여 컬렉션을 다룰 수 있으며, 스트림을 `ArrayList`나 `Set` 등으로 바꾸는 작업도 간단합니다.

### 스트림을 ArrayList로 바꾸기

스트림의 `collect` 메소드와 `Collectors.toList()` 를 사용하여 `ArrayList`로 바꿀 수 있습니다.

```
javaCopy codeimport java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.List;

// ...

Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5);
List<Integer> list = stream.collect(Collectors.toList());
```

### 스트림을 Set으로 바꾸기

스트림의 `collect` 메소드와 `Collectors.toSet()`을 사용하여 `Set`으로 바꿀 수 있습니다.

```
javaCopy codeimport java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.Set;

// ...

Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5);
Set<Integer> set = stream.collect(Collectors.toSet());
```

이렇게 하면 스트림의 원소가 `ArrayList`나 `Set`에 저장됩니다. `Collectors` 클래스는 이 외에도 다양한 유용한 메소드를 제공하여 스트림을 다양한 타입의 컬렉션으로 변환할 수 있습니다.
