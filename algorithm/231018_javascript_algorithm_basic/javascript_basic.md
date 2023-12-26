## 자료구조

1. **배열 (Array)**

   ```js
   let arr = [1, 2, 3, 4, 5];
   arr.push(6); // [1, 2, 3, 4, 5, 6]
   arr.pop();   // [1, 2, 3, 4, 5]
   ```

2. **스택 (Stack)**

   - 배열을 사용하여 스택처럼 활용할 수 있습니다.

   ```js
   let stack = [];
   stack.push(1);  // [1]
   stack.push(2);  // [1, 2]
   stack.pop();    // [1]
   ```

3. **큐 (Queue)**

   - 배열을 사용하여 큐처럼 활용할 수 있습니다.

   ```javascript
   let queue = [];
   queue.push(1);      // [1]
   queue.push(2);      // [1, 2]
   let item = queue.shift(); // item = 1, queue = [2]
   ```

4. **해시 테이블 (Hash Table)**

   - 자바스크립트의 객체나 Map 객체를 사용

   ```js
   let obj = {};
   obj["key1"] = "value1";
   
   let map = new Map();
   map.set("key2", "value2");
   ```

5. **세트 (Set)**

   ```js
   let mySet = new Set();
   mySet.add(1);
   mySet.add(2);
   mySet.add(2);  // 중복된 값은 추가되지 않음
   ```

6. **그래프 (Graph)**

   - 자바스크립트에서는 직접적인 그래프 자료구조를 제공하지 않으므로, 객체나 배열 등을 조합하여 사용합니다.

자바스크립트는 다른 전통적인 언어들에 비해 직접적으로 다양한 자료구조를 제공하지는 않습니다. 그러나 그만큼 배열과 객체가 유연하게 작동하므로, 이를 활용해 다양한 자료구조를 간단히 표현하거나 구현할 수 있습니다.

## 연산자

1. **삼항 연산자 (Conditional Operator) `? :`**

   - 이 연산자는 세 부분으로 구성됩니다: 조건식, 참일 때의 값, 거짓일 때의 값.

   ```javascript
   let value = (x > 10) ? "greater than 10" : "less than or equal to 10";
   ```

2. **Nullish Coalescing Operator `??`**

   - 왼쪽 피연산자가 `null` 또는 `undefined`일 경우 오른쪽 피연산자를 반환합니다. 그렇지 않으면 왼쪽 피연산자를 반환합니다.

   ```javascript
   let value = someVariable ?? "default";
   ```

3. **Optional Chaining `?.`**

   - 객체의 속성이 존재하지 않을 수 있는 경우에 사용됩니다. 만약 객체나 그 속성이 `undefined` 또는 `null`이면 바로 `undefined`를 반환합니다.

   ```javascript
   let value = someObject?.someProperty?.someMethod();
   ```

이 외에도 JavaScript에는 여러 연산자들이 있습니다만, `?`, `??`, 그리고 `?.`와 같이 짧고 특별한 형태를 가진 연산자는 위의 것들이 주요한 것들입니다.

## ??

JavaScript에서 `??`는 **nullish coalescing 연산자**라고 합니다.

`??` 연산자는 왼쪽 피연산자가 null 또는 undefined일 때 오른쪽 피연산자를 반환하고, 그렇지 않을 경우 왼쪽 피연산자를 반환합니다.

이 연산자는 `||` 연산자와 유사해 보이지만, 중요한 차이점이 있습니다. `||` 연산자는 왼쪽 피연산자가 falsy일 때 오른쪽 피연산자를 반환하는 반면, `??` 연산자는 오직 null 또는 undefined일 때만 오른쪽 피연산자를 반환합니다.

예제:

```javascript
let value;

console.log(value ?? "default"); // "default" 출력

value = null;
console.log(value ?? "default"); // "default" 출력

value = 0;
console.log(value ?? "default"); // 0 출력

value = "";
console.log(value ?? "default"); // "" (빈 문자열) 출력

value = false;
console.log(value ?? "default"); // false 출력
```



```javascript
let value;

console.log(value || "default"); // "default" 출력

value = null;
console.log(value || "default"); // "default" 출력

value = 0;
console.log(value || "default"); // "default" 출력 (주의: 0은 falsy 값입니다)

value = "";
console.log(value || "default"); // "default" 출력

value = false;
console.log(value || "default"); // "default" 출력
```

위 예제에서 볼 수 있듯이, `value`가 null 또는 undefined이 아니면 `??` 연산자는 왼쪽 피연산자의 값을 그대로 반환합니다.

## 슬라이싱

자바스크립트에서 배열의 일부분을 가져오려면 `slice` 메서드를 사용하면 됩니다. 문자열에 대해서도 `slice` 메서드를 사용할 수 있습니다.

1. **배열에서 슬라이싱**:

```js
let numbers = [0, 1, 2, 3, 4, 5];
let sliced = numbers.slice(1, 4); // 시작 인덱스와 종료 인덱스를 지정
console.log(sliced); // [1, 2, 3]을 출력합니다.
```

1. **문자열에서 슬라이싱**:

```js
let string = "Hello, World!";
let slicedString = string.slice(0, 5);
console.log(slicedString); // "Hello"를 출력합니다.
```

`slice` 메서드의 특징:

- `slice` 메서드는 원본 배열 또는 문자열을 수정하지 않습니다. 대신 새로운 배열 또는 문자열을 반환합니다.
- 시작 인덱스는 포함되고, 종료 인덱스는 포함되지 않습니다. 예를 들어, `slice(1, 4)`는 인덱스 1에서 3까지의 항목을 가져옵니다.
- 종료 인덱스를 생략하면 시작 인덱스부터 배열의 끝까지 슬라이싱됩니다.
- 인덱스가 음수인 경우 배열의 끝에서부터의 위치를 나타냅니다. 예: `slice(-3)`은 배열의 마지막 세 항목을 가져옵니다.

이러한 방법을 사용하여 자바스크립트에서 슬라이싱을 적용할 수 있습니다.

## max, min, sum

자바스크립트에서 배열의 최대값, 최소값 및 합계를 구하는 방법을 알아보겠습니다.

1. **최대값 (max) 구하기**:

```js
let numbers = [1, 4, 2, 9, 7, 5];
let max = Math.max(...numbers);
console.log(max);  // 9
```

1. **최소값 (min) 구하기**:

```js
let min = Math.min(...numbers);
console.log(min);  // 1
```

1. **합계 (sum) 구하기**:

```js
let sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log(sum);  // 28
```

여기서 사용된 `...`는 스프레드 연산자로, 배열의 요소들을 개별 인자로 펼쳐서 함수에 전달합니다.

`reduce`는 배열의 각 요소에 대해 함수를 실행하고, 단일 결과 값을 반환합니다. 첫 번째 매개변수는 누산기로, 이전 호출의 반환 값이며, 두 번째 매개변수는 현재 요소의 값입니다. 초기값 `0`은 누산기의 초기 값으로 제공됩니다.

이 방법을 사용하여 자바스크립트에서 배열의 최대값, 최소값 및 합계를 쉽게 구할 수 있습니다.
