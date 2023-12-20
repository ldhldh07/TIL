# React Query Data Transformations

> ## Data Transformation
>
> Let's face it - most of us are *not* using GraphQL. If you do, then you can be very happy because you have the luxury of requesting your data in the format that you desire.
>
> If you are working with REST though, you are constrained by what the backend returns. So how and where do you best transform data when working with react-query? The only answer worth a damn in software development applies here as well:
>
> > It depends.
>
> — Every developer, always
>
> Here are 3+1 approaches on where you *can* transform data with their respective pros and cons:

QraphQL은 원하는 데이터 요청을 할 때 더 고급 기능을 제공, 하지만 대부분 우리는 REST 사용하고 REST는 백엔드가 반환하는 것에 제한되어있음.

RQ에서 어떻게 변환할지, 어디에서 변환할지는 항상 개바개임

그 3+1가지의 접근법과 장단점 소개



>### 0. On the backend
>
>This is my favourite approach, if you can afford it. If the backend returns data in exactly the structure we want, there is nothing we need to do. While this might sound unrealistic in many cases, e.g. when working with public REST APIs, it is also quite possible to achieve in enterprise applications. If you are in control of the backend and have an endpoint that returns data for your exact use-case, prefer to deliver the data the way you expect it.
>
>🟢  no work on the frontend
>🔴  not always possible

## 0. 벡엔드에서 하는 경우

가장 선호하는 방식

백엔드에서 원하는 구조대로 데이터를 리턴한다면 우리는 아무것도 안해도 된다.

public REST APIs에서는 비현실적인 이야기이지만, 업체 에플리케이션에서는 할 수 있음

백엔드를 컨틀로해서 정확한 유스-케이스에 맞춰진 데이터를 반환하는 엔드포인트를 가지도록 한다,

🟢 프론트엔드에서 하는게 아님

🔴 항상 가능한 것은 아님

>### 1. In the queryFn
>
>The `queryFn` is the function that you pass to `useQuery`. It expects you to return a Promise, and the resulting data winds up in the query cache. But it doesn't mean that you have to absolutely return data in the structure that the backend delivers here. You can transform it before doing so:
>
>```ts
>const fetchTodos = async (): Promise<Todos> => {
>  const response = await axios.get('todos')
>  const data: Todos = response.data
>
>  return data.map((todo) => todo.name.toUpperCase())
>}
>
>export const useTodosQuery = () =>
>  useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos,
>  })
>```
>
>On the frontend, you can then work with this data "as if it came like this from the backend". No where in your code will you actually work with todo names that are *not* upper-cased. You will also *not* have access to the original structure. If you look at the react-query-devtools, you will see the transformed structure. If you look at the network trace, you'll see the original structure. This might be confusing, so keep that in mind.
>
>Also, there is no optimization that react-query can do for you here. Every time a fetch is executed, your transformation will run. If it's expensive, consider one of the other alternatives. Some companies also have a shared api layer that abstracts data fetching, so you might not have access to this layer to do your transformations.
>
>🟢  very "close to the backend" in terms of co-location
>🟡  the transformed structure winds up in the cache, so you don't have access to the original structure
>🔴  runs on every fetch
>🔴  not feasible if you have a shared api layer that you cannot freely modify

## 1. queryFn에서 변환

`queryFn`은 `useQuery`에 넘기는 함수입니다. Promise 객체를 반환하는 것으로 기대되고, 이 반환된 데이터는 쿼리 캐시로 저장. 백엔드에서 넘어온 그대로 넘길 필요는 없기 때문에 넘기기 전에 변환할 수 있다.

변환되기 전의 데이터를 코드에서는 볼 수 있음

```ts
const fetchTodos = async (): Promise<Todos> => {
  const response = await axios.get('todos')
  const data: Todos = response.data

  return data.map((todo) => todo.name.toUpperCase())
}

export const useTodosQuery = () =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
  })
```

프론트엔드에서 이렇게 백엔드에서 온 데이터 변형 가능

기존의 구조에는 접근 불가능하다, react-query-devtools로도 볼 수 없음

네트워크 추적하면 볼 수 있는데 혼란을 불러올 수 있다.



여기서 리액트 쿼리가 할 수 있는 최적화는 없고, 불러올때마다 계속 변환작업을 거침. 이 과정이 비용이 든다면, 다른 옵션을 선택하는 것이 낫다. 어떤 회사에서는 이 과정을 추상화하는 공유된 api layer를 사용해서 이걸 자유롭게 수정하지 못한다

🟢 백엔드와의 결합도 측면에서 '가깝다' 

🟡 변형된 구조가 캐시에 저장되므로 원래 구조에 접근할 수 없음 

🔴 모든 fetch에 실행됨 

🔴 공유 API 계층이 있고, 이를 자유롭게 수정할 수 없는 경우에는 실행 불가능"

>### 2. In the render function
>
>As advised in [Part 1](https://tkdodo.eu/blog/practical-react-query), if you create custom hooks, you can easily do transformations there:
>
>render-transformation
>
>```ts
>const fetchTodos = async (): Promise<Todos> => {
>  const response = await axios.get('todos')
>  return response.data
>}
>
>export const useTodosQuery = () => {
>  const queryInfo = useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos,
>  })
>
>  return {
>    ...queryInfo,
>    data: queryInfo.data?.map((todo) => todo.name.toUpperCase()),
>  }
>}
>```
>
>As it stands, this will not only run every time your fetch function runs, but actually on every render (even those that do not involve data fetching). This is likely not a problem at all, but if it is, you can optimize with `useMemo`. Be careful to define your dependencies *as narrow as possible*. `data` inside the queryInfo will be referentially stable unless something really changed (in which case you want to recompute your transformation), but the `queryInfo` itself will *not*. If you add `queryInfo` as your dependency, the transformation will again run on every render:
>
>useMemo-dependencies
>
>```ts
>export const useTodosQuery = () => {
>  const queryInfo = useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos
>  })
>
>  return {
>    ...queryInfo,
>    // 🚨 don't do this - the useMemo does nothing at all here!
>    data: React.useMemo(
>      () => queryInfo.data?.map((todo) => todo.name.toUpperCase()),
>      [queryInfo]
>    ),
>
>    // ✅ correctly memoizes by queryInfo.data
>    data: React.useMemo(
>      () => queryInfo.data?.map((todo) => todo.name.toUpperCase()),
>      [queryInfo.data]
>    ),
>  }
>}
>```
>
>Especially if you have additional logic in your custom hook to combine with your data transformation, this is a good option. Be aware that data can be potentially undefined, so use optional chaining when working with it.
>
>**Update**
>
>Since React Query has [tracked queries](https://tkdodo.eu/blog/react-query-render-optimizations#tracked-queries) turned on per default since v4, spreading `...queryInfo` is no longer recommended, because it invokes getters on all properties.
>
>🟢  optimizable via useMemo
>🟡  exact structure cannot be inspected in the devtools
>🔴  a bit more convoluted syntax
>🔴  data can be potentially undefined
>🔴  not recommended with tracked queries

## 2. 렌더링 함수에서 변환

custom hooks를 만들어 쉽게 변환할 수도 있다

render-transformation

```ts
const fetchTodos = async (): Promise<Todos> => {
  const response = await axios.get('todos')
  return response.data
}

export const useTodosQuery = () => {
  const queryInfo = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
  })

  return {
    ...queryInfo,
    data: queryInfo.data?.map((todo) => todo.name.toUpperCase()),
  }
}
```

이렇게 할 시 렌더링될 때마다 변환작업이 실행되기 때문에 `useMemo`로 최적화할 수 있다

data는 가능한 dependencies를 최소화하도록 해라.실제로 변화할 때를 제외하고는 안정적일 것이다. 하지만 `queryInfo`자체로는 그렇지 않다. queryInfo를 의존성에 추가하면 렌더링할때마다 변환작업이 이루어짐.



useMemo-dependencies

```ts
export const useTodosQuery = () => {
  const queryInfo = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos
  })

  return {
    ...queryInfo,
    // 🚨 don't do this - the useMemo does nothing at all here!
    data: React.useMemo(
      () => queryInfo.data?.map((todo) => todo.name.toUpperCase()),
      [queryInfo]
    ),

    // ✅ correctly memoizes by queryInfo.data
    data: React.useMemo(
      () => queryInfo.data?.map((todo) => todo.name.toUpperCase()),
      [queryInfo.data]
    ),
  }
}
```

특히, 이 훅과 조합되는 변환작업이 있들 때 이 방법이 좋다

만약 undefined될 수 있다면 `optional chaining`을 사용해라

> 업데이트
>
> v4부터 tracked queries를 가지기 때문에 `...queryInfo`를 펼치는 것은 더이상 추천하지 않음
>
> 접근할 때마다 모든 속성에 getter를 데려옴
>
> *추적 쿼리 기능이라는 것은 queryInfo에 접근할 때마다 getter함수 호출한다는 것

🟢 useMemo를 통해 최적화 가능 

🟡 개발자 도구에서 정확한 구조를 검사할 수 없음 

🔴 다소 복잡한 문법 

🔴 데이터가 potenitally undefined일 수 있음 

🔴 추적 쿼리와 함께 사용하기에는 권장되지 않음

>### 3. using the select option
>
>v3 introduced built-in selectors, which can also be used to transform data:
>
>select-transformation
>
>```ts
>export const useTodosQuery = () =>
>  useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos,
>    select: (data) => data.map((todo) => todo.name.toUpperCase()),
>  })
>```
>
>selectors will only be called if `data` exists, so you don't have to care about `undefined` here. Selectors like the one above will also run on every render, because the functional identity changes (it's an inline function). If your transformation is expensive, you can memoize it either with useCallback, or by extracting it to a stable function reference:
>
>select-memoizations
>
>```ts
>const transformTodoNames = (data: Todos) =>
>  data.map((todo) => todo.name.toUpperCase())
>
>export const useTodosQuery = () =>
>  useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos,
>    // ✅ uses a stable function reference
>    select: transformTodoNames,
>  })
>
>export const useTodosQuery = () =>
>  useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos,
>    // ✅ memoizes with useCallback
>    select: React.useCallback(
>      (data: Todos) => data.map((todo) => todo.name.toUpperCase()),
>      []
>    ),
>  })
>```
>
>Further, the select option can also be used to subscribe to only parts of the data. This is what makes this approach truly unique. Consider the following example:
>
>select-partial-subscriptions
>
>```js
>export const useTodosQuery = (select) =>
>  useQuery({
>    queryKey: ['todos'],
>    queryFn: fetchTodos,
>    select,
>  })
>
>export const useTodosCount = () =>
>  useTodosQuery((data) => data.length)
>export const useTodo = (id) =>
>  useTodosQuery((data) => data.find((todo) => todo.id === id))
>```
>
>Here, we've created a [useSelector](https://react-redux.js.org/api/hooks#useselector) like API by passing a custom selector to our `useTodosQuery`. The custom hooks still works like before, as `select` will be `undefined` if you don't pass it, so the whole state will be returned.
>
>But if you pass a selector, you are now only subscribed to the result of the selector function. This is quite powerful, because it means that even if we update the name of a todo, our component that only subscribes to the count via `useTodosCount` will *not* rerender. The count hasn't changed, so react-query can choose to *not* inform this observer about the update 🥳 (Please note that this is a bit simplified here and technically not entirely true - I will talk in more detail about render optimizations in Part 3).
>
>🟢  best optimizations
>🟢  allows for partial subscriptions
>🟡  structure can be different for every observer
>🟡  structural sharing is performed twice (I will also talk about this in more detail in [Part 3](https://tkdodo.eu/blog/react-query-render-optimizations))

v3에는 빌트인된 selector가 있어서 이걸로 변환할 수도 있다

```ts
export const useTodosQuery = () =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    select: (data) => data.map((todo) => todo.name.toUpperCase()),
  })
```

selector는 data가 존재할 때만 호출됨

그래서 undefined를 걱정할 필요가 없다.

이 셀렉터는 모든 렌더링마다 실행된다. 인라인 함수라 함수적인 정체성이 바뀌기 때문

이 작업이 비용이 많이 든다면 useCallback을 쓰거나 안정적인 함수참조로 추출한다면 최적화할 수 있다.

```ts
const transformTodoNames = (data: Todos) =>
  data.map((todo) => todo.name.toUpperCase())

export const useTodosQuery = () =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    // ✅ uses a stable function reference
    select: transformTodoNames,
  })

export const useTodosQuery = () =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    // ✅ memoizes with useCallback
    select: React.useCallback(
      (data: Todos) => data.map((todo) => todo.name.toUpperCase()),
      []
    ),
  })
```

데이터의 일부분만  subscribe할 수도 있다. 이 방법의 특이한 부분이다.

```ts
export const useTodosQuery = (select) =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    select,
  })

export const useTodosCount = () =>
  useTodosQuery((data) => data.length)
export const useTodo = (id) =>
  useTodosQuery((data) => data.find((todo) => todo.id === id))
```

`useSelector `같은 방식으로 `useTodosQuery` api를 만들었다. 넘기지 않으면 `select`가 `undefined`가 되기 때문에 이전에 사용하던대로 전체 state가 반환된다.



만약 selector를 전달하면 그 결과에만 subscribe한다. `todo`를 업데이트해도 다시 렌더링되지 않는다. 갯수가 변겨되지 않으면 react-query는 observer에게 업데이트된걸 알리지 않아도 된다. 이 부분에 대해서는 part3 렌더링 최적화에서 좀 더 자세히 이야기 한다.

🟢 최적화 측면에서 최고 

🟢 부분 구독을 허용 

🟡 각 관찰자마다 구조가 다를 수 있음 

🟡 구조적 공유가 두 번 수행됨 (이 부분도 Part 3에서 더 자세히 이야기할 것입니다)