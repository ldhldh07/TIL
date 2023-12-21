# React Query Render Optimizations

> **Disclaimer**
>
> Render optimizations are an advanced concept for any app. React Query already comes with very good optimizations and defaults out of the box, and most of the time, no further optimizations are needed. "Unneeded re-renders" is a topic that many people tend to put a lot of focus on, which is why I've decided to cover it. But I wanted to point out once again, that usually, for most apps, render optimizations probably don't matter as much as you'd think. Re-renders are a good thing. They make sure your app is up-to-date. I'd take an "unnecessary re-render" over a "missing render-that-should-have-been-there" all day every day. For more on this topic, please read:
>
> - [Fix the slow render before you fix the re-render](https://kentcdodds.com/blog/fix-the-slow-render-before-you-fix-the-re-render) by Kent C. Dodds
> - [this article by @ryanflorence about premature optimizations](https://reacttraining.com/blog/react-inline-functions-and-performance)

리액트 쿼리는 이미 아주 좋은 최적화를 기본 설정으로 제공한다. 그래도 대부분 추가적으로 최적화를 할 필요가 없음. 필요하지 않는 재 렌더링은 많은 사람들이 관심있어하는 주제라서 글을 쓴다. 하지만 대부분 그렇게 중요하진 않다. 리렌더링은 좋다. 최신의 상태로 유지시켜준다. 했어야 하는 리렌더링을 안하는 것보다는 불필요한 리렌더링을 하는 편이 낫다

참고

- [Fix the slow render before you fix the re-render](https://kentcdodds.com/blog/fix-the-slow-render-before-you-fix-the-re-render) by Kent C. Dodds
- [this article by @ryanflorence about premature optimizations](https://reacttraining.com/blog/react-inline-functions-and-performance)



> I've already written quite a bit about render optimizations when describing the select option in [#2: React Query Data Transformations](https://tkdodo.eu/blog/react-query-data-transformations). However, "Why does React Query re-render my component two times even though nothing changed in my data" is the question I probably needed to answer the most (apart from maybe: "Where can I find the v2 docs" 😅). So let me try to explain it in-depth.
>
> ## isFetching transition
>
> I haven't been entirely honest in the [last example](https://tkdodo.eu/blog/react-query-data-transformations#3-using-the-select-option) when I said that this component will only re-render if the length of todos change:
>
> count-component
>
> ```tsx
> export const useTodosQuery = (select) =>
>   useQuery({
>     queryKey: ['todos'],
>     queryFn: fetchTodos,
>     select,
>   })
> export const useTodosCount = () =>
>   useTodosQuery((data) => data.length)
> 
> function TodosCount() {
>   const todosCount = useTodosCount()
> 
>   return <div>{todosCount.data}</div>
> }
> ```
>
> Every time you make a background refetch, this component will re-render twice with the following query info:
>
> ```json
> { status: 'success', data: 2, isFetching: true }
> { status: 'success', data: 2, isFetching: false }
> ```
>
> That is because React Query exposes a lot of meta information for each query, and `isFetching` is one of them. This flag will always be true when a request is in-flight. This is quite useful if you want to display a background loading indicator. But it's also kinda unnecessary if you don't do that.

2번 글에서 이미 렌더링 최적화에 대해 이야기함. 하지만 리액트 쿼리가 데이터가 그대로여도 리렌더링을 두번 하는 것에 대해 이야기할 것.

## isFetching transition

이전 게시글에서 길이가 바뀔때만 리렌더링된다고 했는데 사실 정직한 이야기가 아니었다.

count-component

```ts
export const useTodosQuery = (select) =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    select,
  })
export const useTodosCount = () =>
  useTodosQuery((data) => data.length)

function TodosCount() {
  const todosCount = useTodosCount()

  return <div>{todosCount.data}</div>
}
```

배경에서 `refetch`를 할 때마다, 컴포넌트는 두번 재렌더링 된다.

```json
{ status: 'success', data: 2, isFetching: true }
{ status: 'success', data: 2, isFetching: false }
```

리액트 쿼리가 많은 meta infomation에 노출되고 그 중 하나가 `isFetching` 이 flag는 request가 in-filght일때 true이다. 로딩 indicator 띄울때 유용하고, 그렇지 않을때는 필요 없다.

> ### notifyOnChangeProps
>
> For this use-case, React Query has the `notifyOnChangeProps` option. It can be set on a per-observer level to tell React Query: Please only inform this observer about changes if one of these props change. By setting this option to `['data']`, we will find the optimized version we seek:
>
> optimized-with-notifyOnChangeProps
>
> ```ts
> export const useTodosQuery = (select, notifyOnChangeProps) =>
>   useQuery({
>     queryKey: ['todos'],
>     queryFn: fetchTodos,
>     select,
>     notifyOnChangeProps,
>   })
> export const useTodosCount = () =>
>   useTodosQuery((data) => data.length, ['data'])
> ```
>
> You can see this in action in the [optimistic-updates-typescript](https://github.com/tannerlinsley/react-query/blob/9023b0d1f01567161a8c13da5d8d551a324d6c23/examples/optimistic-updates-typescript/pages/index.tsx#L35-L48) example in the docs.

## notifyOnChangeProps

이 유즈케이스에서 `notifyOnChangeProps` 옵션을 제공한다.

per-observer 레벨에서 설정할 수 있다. RQ에게 이 속성들 중 하나가 변경될 경우 그 observer에게 알려주세요라고 시킬 수 있다. `['data']`를이 옵션에 설정하면 우리가 원하는 가장 최적화된 버전을 얻을 수 있다.

```ts
export const useTodosQuery = (select, notifyOnChangeProps) =>
  useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    select,
    notifyOnChangeProps,
  })
export const useTodosCount = () =>
  useTodosQuery((data) => data.length, ['data'])
```

[optimistic-updates-typescript](https://github.com/tannerlinsley/react-query/blob/9023b0d1f01567161a8c13da5d8d551a324d6c23/examples/optimistic-updates-typescript/pages/index.tsx#L35-L48) 여기서 이 동작 볼 수 있음

> ### Staying in sync
>
> While the above code works well, it can get out of sync quite easily. What if we want to react to the `error`, too? Or we start to use the `isLoading` flag? We have to keep the `notifyOnChangeProps` list in sync with whichever fields we are actually using in our components. If we forget to do that, and we only observe the `data` property, but get an `error` that we also display, our component will not re-render and is thus outdated. This is especially troublesome if we hard-code this in our custom hook, because the hook does not know what the component will actually use:
>
> outdated-component
>
> ```tsx
> export const useTodosCount = () =>
>   useTodosQuery((data) => data.length, ['data'])
> 
> function TodosCount() {
>   // 🚨 we are using error,
>   // but we are not getting notified if error changes!
>   const { error, data } = useTodosCount()
> 
>   return (
>     <div>
>       {error ? error : null}
>       {data ? data : null}
>     </div>
>   )
> }
> ```
>
> As I have hinted in the disclaimer in the beginning, I think this is way worse than the occasional unneeded re-render. Of course, we can pass the option to the custom hook, but this still feels quite manual and boilerplate-y. Is there a way to do this automatically? Turns out, there is:

## Staying in sync

이전 코드가 잘 작동하면서도 동기화에서 잘 벗어날 수 있다. 에러에 반응하고 로딩중이라는 flag를 띄우려면 어케 해야할까. `notifyOnChangeProps`를 컴포넌트에서 사용하는 필드와 동기화 해야한다. 그걸 빼먹으면 데이터 속성을 관찰만 하고 에러가 발생하면 리렌더링되지 않고 outdated된 컴포넌트가 되어버림. 특히 커스텀훅을 하드코딩했을 때 더 문제가 된다. 훅에서는 컴포넌트에 대해서 알지 못하기 때문. 

```ts
export const useTodosCount = () =>
  useTodosQuery((data) => data.length, ['data'])

function TodosCount() {
  // 🚨 we are using error,
  // but we are not getting notified if error changes!
  const { error, data } = useTodosCount()

  return (
    <div>
      {error ? error : null}
      {data ? data : null}
    </div>
  )
}
```

이건 불필요한 리렌더링보다 안좋은 상황

커스텀 훅에 그런 옵션을 넘길 수 있지만 이거는 수동적이고 boilerplate스럽다. 이 다음 내용에서 해결

> ### Tracked Queries
>
> I'm quite proud of this feature, given that it was my first major contribution to the library. If you set `notifyOnChangeProps` to `'tracked'`, React Query will keep track of the fields you are using during render, and will use this to compute the list. This will optimize exactly the same way as specifying the list manually, except that you don't have to think about it. You can also turn this on globally for all your queries:
>
> tracked-queries
>
> ```tsx
> const queryClient = new QueryClient({
>   defaultOptions: {
>     queries: {
>       notifyOnChangeProps: 'tracked',
>     },
>   },
> })
> function App() {
>   return (
>     <QueryClientProvider client={queryClient}>
>       <Example />
>     </QueryClientProvider>
>   )
> }
> ```
>
> With this, you never have to think about re-renders again. Of course, tracking the usages has a bit of an overhead as well, so make sure you use this wisely. There are also some limitations to tracked queries, which is why this is an opt-in feature:
>
> - If you use [object rest destructuring](https://github.com/tc39/proposal-object-rest-spread/blob/6ee4ce3cdda246746fc46fb149bb8b43c28e704d/Rest.md), you are effectively observing all fields. Normal destructuring is fine, just don't do this:
>
> problematic-rest-destructuring
>
> ```ts
> // 🚨 will track all fields
> const { isLoading, ...queryInfo } = useQuery(...)
> 
> // ✅ this is totally fine
> const { isLoading, data } = useQuery(...)
> ```
>
> - Tracked queries only work "during render". If you only access fields during effects, they will not be tracked. This is quite the edge case though because of dependency arrays:
>
> tracking-effects
>
> ```ts
> const queryInfo = useQuery(...)
> 
> // 🚨 will not corectly track data
> React.useEffect(() => {
>     console.log(queryInfo.data)
> })
> 
> // ✅ fine because the dependency array is accessed during render
> React.useEffect(() => {
>     console.log(queryInfo.data)
> }, [queryInfo.data])
> ```
>
> - Tracked queries don't reset on each render, so if you track a field once, you'll track it for the lifetime of the observer:
>
> no-reset
>
> ```ts
> const queryInfo = useQuery(...)
> 
> if (someCondition()) {
>     // 🟡 we will track the data field if someCondition was true in any previous render cycle
>     return <div>{queryInfo.data}</div>
> }
> ```
>
> **Update**
>
> Starting with v4, tracked queries are turned on per default in React Query, and you can opt out of the feature with `notifyOnChangeProps: 'all'`.

## Tracked Queries

`notifyOnChangeProps` 옵션을 `tracked`로 설정한다면, 렌더링 중에 사용하는 필드를 계속 추적한다. 그리고 이걸 리스트를 계산하는데 사용한다. 생각을 할 필요가 없을 때를 제외하고는, 수동으로 목록을 지정하는 것이랑 정확히 똑같이 동기화가 된다. 또한 이걸 모든 쿼리들에 전역적으로 켤 수도 있다.

tracked-queries

```ts
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      notifyOnChangeProps: 'tracked',
    },
  },
})
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Example />
    </QueryClientProvider>
  )
}
```

이렇게 하면 리렌더링에 대한 상각을 안해도 됨. 물론 약간의 오버헤드가 있으니 현명하게 사용해야함.

이 `tracked queryies`를 사용할 때는 약간의 제한이 있음. 이게 `opt-in`기능이기 때문 (사용자가 명시해서 활성화해야 하는 옵션)

만약 `object rest destructing` (전개 연산자`...`)을 사용한다면, 사실상 모든 필드를 관찰하게 된다.  `Nomal destructing`은 좋은데, 이렇게는 하지 마라.

problematic-rest-destructuring

```ts
// 🚨 will track all fields
const { isLoading, ...queryInfo } = useQuery(...)

// ✅ this is totally fine
const { isLoading, data } = useQuery(...)
```

`tracked queries`는 렌더링할때만 작동한다. 만약 필드에만 접근한다면, tracked되지 않음. 이건 dependency arrays가 원인인 엣지 케이스임. 

tracking-effects

```ts
const queryInfo = useQuery(...)

// 🚨 will not corectly track data
React.useEffect(() => {
    console.log(queryInfo.data)
})

// ✅ fine because the dependency array is accessed during render
React.useEffect(() => {
    console.log(queryInfo.data)
}, [queryInfo.data])
```

tracked queries는 매 렌더마다 리셋되지 않는다. 그렇기에 만약 필드를 한번 추적했으면 observer의 lifetime동안 그것을 추적할 것이다.

no-reset

```ts
const queryInfo = useQuery(...)

if (someCondition()) {
    // 🟡 we will track the data field if someCondition was true in any previous render cycle
    return <div>{queryInfo.data}</div>
}
```

### Update

v4부터는 기본으로 켜져 있음.  `notifyOnChangeProps: 'all'`로 끌 수 있음.

>## Structural sharing
>
>A different, but no less important render optimization that React Query has turned on out of the box is *structural sharing*. This feature makes sure that we keep referential identity of our `data` on every level. As an example, suppose you have the following data structure:
>
>```json
>[
>  { "id": 1, "name": "Learn React", "status": "active" },
>  { "id": 2, "name": "Learn React Query", "status": "todo" }
>]
>```
>
>Now suppose we transition our first todo into the *done* state, and we make a background refetch. We'll get a completely new json from our backend:
>
>```diff
>Copycopy code to clipboard
>1[
>2-  { "id": 1, "name": "Learn React", "status": "active" },
>3+  { "id": 1, "name": "Learn React", "status": "done" },
>4  { "id": 2, "name": "Learn React Query", "status": "todo" }
>5]
>```
>
>Now React Query will attempt to compare the old state and the new and keep as much of the previous state as possible. In our example, the todos array will be new, because we updated a todo. The object with id 1 will also be new, but the object for id 2 will be the same reference as the one in the previous state - React Query will just copy it over to the new result because nothing has changed in it.
>
>This comes in very handy when using selectors for partial subscriptions:
>
>optimized-selectors
>
>```ts
>Copyoptimized-selectors: copy code to clipboard
>1// ✅ will only re-render if _something_ within todo with id:2 changes
>2// thanks to structural sharing
>3const { data } = useTodo(2)
>```
>
>As I've hinted before, for selectors, structural sharing will be done twice: Once on the result returned from the `queryFn` to determine if anything changed at all, and then once more on the *result* of the selector function. In some instances, especially when having very large datasets, structural sharing *can* be a bottleneck. It also only works on json-serializable data. If you don't need this optimization, you can turn it off by setting `structuralSharing: false` on any query.
>
>Have a look at the [replaceEqualDeep tests](https://github.com/tannerlinsley/react-query/blob/80cecef22c3e088d6cd9f8fbc5cd9e2c0aab962f/src/core/tests/utils.test.tsx#L97-L304) if you want to learn more about what happens under the hood.

## Structural sharing

구조적인 공유는 리액트 쿼리가 out of the box(별도의 설치 없이 사용할 수 있는)로 제공하는 중요한 렌더링 동기화 기법이다.

이 기능은 우리가 모든 레벨에서 참조 정체성을 지킬 수 있도록 해줍니다. 만약 이런 데이터 구조를 따른다고 가정하면

```ㅓ내ㅜ
[
  { "id": 1, "name": "Learn React", "status": "active" },
  { "id": 2, "name": "Learn React Query", "status": "todo" }
]
```

첫번째 todo를 done으로 바꾸고 refetch하면 우리는 백엔드에서 완전히 새로운 json을 받는다ㅓ.

```diff
[
-  { "id": 1, "name": "Learn React", "status": "active" },
+  { "id": 1, "name": "Learn React", "status": "done" },
  { "id": 2, "name": "Learn React Query", "status": "todo" }
]
```

이때 RQ가 이전과 지금의 상태를 비교해서 가능한 이전 상태를 많이 유지한다. 이 예에서 todos 배열은 업데이트했기에 새롭다. id 1인 객체는 또한 새롭고 id 2인 객체는 이전의 참조를 유지함. 



이는 selector로 부분 subscribe할 때 유용하다.

optimized-selectors

```ts
// ✅ will only re-render if _something_ within todo with id:2 changes
// thanks to structural sharing
const { data } = useTodo(2)
```

selector에서 구조적 공유는 두번 일어난다. 결과가 queryFn에서 반환될때 바뀌었는지 확인을 위해 한번 , selector function의 결과에 한번

큰 데이터셋을 가질때, 병목현상을 일으킬 수 있음. json-seriializable인 데이터에만 작용함. 최적화가 필요 없다면 `structuralSharing: false`를 아무 쿼리에나 설정