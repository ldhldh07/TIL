# Testing React Query

> Questions around the testing topic come up quite often together with React Query, so I'll try to answer some of them here. I think one reason for that is that testing "smart" components (also called [container components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)) is not the easiest thing to do. With the rise of hooks, this split has been largely deprecated. It is now encouraged to consume hooks directly where you need them rather than doing a mostly arbitrary split and drill props down.
>
> I think this is generally a very good improvement for colocation and code readability, but we now have more components that consume dependencies outside of "just props".
>
> They might `useContext`. They might `useSelector`. Or they might `useQuery`.
>
> Those components are technically no longer pure, because calling them in different environments leads to different results. When testing them, you need to carefully setup those surrounding environments to get things working.

테스팅 주제에 대한 질문들이 많다. '스마트' 컴포넌트(컨테이너 컴포넌트)를 테스팅하는 것이 어렵기 때문이다.

훅이 생기면서 이런 분리는 deprecated됐다. 이제는 임의로 분리하고 props down하는 대신 훅을 사용하는 것이 독려된다. 



이는 가독성이랑 colocation(하나의 위치에 모아놓는것)측면에서 아주 좋은 발전이라고 생각한다. 하지만 우리는 'just props'외의 의존성을 사용하는 더 많은 컴퍼넌트들을 가지고 있다.

그건 `useContext`, `useSelector`, `useQuery`가 있다.

다른 환경에서 호출했을 때, 다른 결과를 불러온다는 점에서 이 컴퍼넌트들은 pure하지 않다. 이것들을 테스팅할때, 이것들을 작동하게 하는 주변 환경들을 신중하게 셋업해야한다.

> ## Mocking network requests
>
> Since React Query is an async server state management library, your components will likely make requests to a backend. When testing, this backend is not available to actually deliver data, and even if, you likely don't want to make your tests dependent on that.
>
> There are tons of articles out there on how to mock data with jest. You can mock your api client if you have one. You can mock fetch or axios directly. I can only second what Kent C. Dodds has written in his article [Stop mocking fetch](https://kentcdodds.com/blog/stop-mocking-fetch):
>
> Use [mock service worker](https://mswjs.io/) by [@ApiMocking](https://twitter.com/ApiMocking)
>
> It can be your single source of truth when it comes to mocking your apis:
>
> - works in node for testing
> - supports REST and GraphQL
> - has a [storybook addon](https://storybook.js.org/addons/msw-storybook-addon) so you can write stories for your components that `useQuery`
> - works in the browser for development purposes, and you'll still see the requests going out in the browser devtools
> - works with cypress, similar to fixtures
>
> ------
>
> With our network layer being taken care of, we can start talking about React Query specific things to keep an eye on:

## Mocking network requests

리액트 쿼리는 비동기 서버 상태 관리 라이브러리이다. 그 때문에 너의 컴포넌트는 백엔드에서 requests를 만든다.

테스팅을 할 때, 이 백엔드는 실제로 데이터를 전ㄷ달하지 않고, 심지어 있다고 해도 테스트는 그것에 의존하지 않고 하고 싶을 것이다.

jest로 데이터를 mock하는 방법에 대한 다양한 글들이 있다. 하나를 가지고 있다면 api 클라이언트를 mock할 수 있다. fetch나 axios를 직접 mock할 수 있다. kenk C.dodds가 한말에 동의한다.

> Use [mock service worker](https://mswjs.io/) by [@ApiMocking](https://twitter.com/ApiMocking)

이것은 너의 apis를 mocking할때 하나의 진실이 될 수 있다.

- 테스팅은 노드에서 작동한다.
- REST와 GraphQL을 지원한다.
- `useQuery`를 사용하는 컴퍼넌트에 대한 스토리를 쓸 수 있는 스트리북 애드온이 있다.
- 개발 목적으로 브라우저 내에서 작동한다. 그리고 브라우저 개발자 도구에서 requests가 나가는 것을 여전히 볼 수 있다.
- fixtures와 유사하게 cypress와 함께 작동한다.
- 네트워크 계층에서 처리가 되면, 우리는 지켜봐야할 RQ의 구체적인 것들에 대해 이야기를 시작할 수 있다.

> ## QueryClientProvider
>
> Whenever you use React Query, you need a QueryClientProvider and give it a queryClient - a vessel which holds the `QueryCache`. The cache will in turn hold the data of your queries.
>
> I prefer to give each test its own QueryClientProvider and create a `new QueryClient` for each test. That way, tests are completely isolated from each other. A different approach might be to clear the cache after each test, but I like to keep shared state between tests as minimal as possible. Otherwise, you might get unexpected and flaky results if you run your tests in parallel.
>
> ### For custom hooks
>
> If you are testing custom hooks, I'm quite certain you're using [react-hooks-testing-library](https://react-hooks-testing-library.com/). It's the easiest thing there is to test hooks. With that library, we can wrap our hook in a [wrapper](https://react-hooks-testing-library.com/reference/api#wrapper), which is a React component to wrap the test component in when rendering. I think this is the perfect place to create the QueryClient, because it will be executed once per test:
>
> wrapper
>
> ```tsx
> const createWrapper = () => {
>   // ✅ creates a new QueryClient for each test
>   const queryClient = new QueryClient()
>   return ({ children }) => (
>     <QueryClientProvider client={queryClient}>
>       {children}
>     </QueryClientProvider>
>   )
> }
> 
> test('my first test', async () => {
>   const { result } = renderHook(() => useCustomHook(), {
>     wrapper: createWrapper(),
>   })
> })
> ```
>
> ### For components
>
> If you want to test a Component that uses a `useQuery` hook, you also need to wrap that Component in QueryClientProvider. A small wrapper around `render` from [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/) seems like a good choice. Have a look at how React Query does it [internally for their tests](https://github.com/tannerlinsley/react-query/blob/ead2e5dd5237f3d004b66316b5f36af718286d2d/src/react/tests/utils.tsx#L6-L17).

## QueryClientProvider

RQ를 사용할 때마다, QueryClientProvider가 필요하고 그것에 queryClient를 제공해야 한다. queryClient는 `QueryCache`를 가지고 있는 그릇이다. 이 캐시는 결국 너의 쿼리들의 데이터를 가지고 있을 것이다. 



나는 테스트마다 고유의 QueryClientProvider를 주고 `new QueryClient`를 만드는 것을 선호한다. 이 방법을 쓴다면, 테스트들은 서로 독립될 수 있다. 다른 접근법은 매번 테스트때마다 캐시를 삭제하는 것이다. 하지만 테스트 간 공유하는 것은 최소한 작게 하고자 한다. 그렇지 않으면 테스트를 병렬로 돌렸을 때, 예상치 못하고 불안정한 결과를 얻을 것이다. 

### For custom hooks

커스텀 훅을 위해서, 만약 커스텀 훅들을 테스트 해본다면, `react-hooks-testing-library`를 사용할것이라고 꽤나 확신한다. 이것은 훅을 테스트할 수 있는 가장 쉬운 방법이다. 이 라이브러리는 우리가 우리의 훅을 렌더링하는 동안 테스트 컴퍼넌트를 싸기 위한 리액트 컴퍼넌트인 wrapper로 감쌀 수 있다. 

이곳이 QueryClient를 생성하기 가장 완벽한 장소라고 생각한다. 테스트 마다 한번만 실행되기 때문이다.

**wrapper**

```tsx
const createWrapper = () => {
  // ✅ creates a new QueryClient for each test
  const queryClient = new QueryClient()
  return ({ children }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  )
}

test('my first test', async () => {
  const { result } = renderHook(() => useCustomHook(), {
    wrapper: createWrapper(),
  })
})
```

### For components

만약 `useQuery`훅을 사용하는 컴퍼넌트를 테스트해보고 싶다면, QueryClientProvider로 컴퍼넌트를 감싸야 한다.

react-testing-library의 `render`를 감싸는 작은 wrapper가 좋다.

어떻게 RQ가 그들의 테스트에서 내부적으로 작동하는지 봐라.

> ## Turn off retries
>
> It's one of the most common "gotchas" with React Query and testing: The library defaults to three retries with exponential backoff, which means that your tests are likely to timeout if you want to test an erroneous query. The easiest way to turn retries off is, again, via the `QueryClientProvider`. Let's extend the above example:
>
> no-retries
>
> ```tsx
> Copyno-retries: copy code to clipboard1const createWrapper = () => {2  const queryClient = new QueryClient({3    defaultOptions: {4      queries: {5        // ✅ turns retries off6        retry: false,7      },8    },9  })10
> 11  return ({ children }) => (12    <QueryClientProvider client={queryClient}>13      {children}14    </QueryClientProvider>15  )16}17
> 18test("my first test", async () => {19  const { result } = renderHook(() => useCustomHook(), {20    wrapper: createWrapper()21  })22}
> ```
>
> This will set the defaults for all queries in the component tree to "no retries". It is important to know that this will only work if your actual `useQuery` has no explicit retries set. If you have a query that wants 5 retries, this will still take precedence, because defaults are only taken as a fallback.
>
> ### setQueryDefaults
>
> The best advice I can give you for this problem is: Don't set these options on `useQuery` directly. Try to use and override the defaults as much as possible, and if you really need to change something for specific queries, use [queryClient.setQueryDefaults](https://react-query.tanstack.com/reference/QueryClient#queryclientsetquerydefaults).
>
> So for example, instead of setting retry on `useQuery`:
>
> not-on-useQuery
>
> ```tsx
> const createWrapper = () => {
>   const queryClient = new QueryClient({
>     defaultOptions: {
>       queries: {
>         // ✅ turns retries off
>         retry: false,
>       },
>     },
>   })
> 
>   return ({ children }) => (
>     <QueryClientProvider client={queryClient}>
>       {children}
>     </QueryClientProvider>
>   )
> }
> 
> test("my first test", async () => {
>   const { result } = renderHook(() => useCustomHook(), {
>     wrapper: createWrapper()
>   })
> }
> ```
>
> Set it like this:
>
> setQueryDefaults
>
> ```tsx
> const queryClient = new QueryClient()
> 
> function App() {
>   return (
>     <QueryClientProvider client={queryClient}>
>       <Example />
>     </QueryClientProvider>
>   )
> }
> 
> function Example() {
>   // 🚨 you cannot override this setting for tests!
>   const queryInfo = useQuery({
>     queryKey: ['todos'],
>     queryFn: fetchTodos,
>     retry: 5,
>   })
> }
> ```
>
> Here, all queries will retry two times, only *todos* will retry five times, and I still have the option to turn it off for all queries in my tests 🙌.
>
> ### ReactQueryConfigProvider
>
> Of course, this only works for known query keys. Sometimes, you really want to set some configs on a subset of your component tree. In v2, React Query had a [ReactQueryConfigProvider](https://react-query-v2.tanstack.com/docs/api#reactqueryconfigprovider) for that exact use-case. You can achieve the same thing in v3 with a couple of lines of codes:
>
> ReactQueryConfigProvider
>
> ```jsx
> const queryClient = new QueryClient({
>   defaultOptions: {
>     queries: {
>       retry: 2,
>     },
>   },
> })
> 
> // ✅ only todos will retry 5 times
> queryClient.setQueryDefaults(['todos'], { retry: 5 })
> 
> function App() {
>   return (
>     <QueryClientProvider client={queryClient}>
>       <Example />
>     </QueryClientProvider>
>   )
> }
> ```
>
> You can see this in action in this [codesandbox example](https://codesandbox.io/s/react-query-config-provider-v3-lt00f).
>
> 

## Turn off retries

이것은 리액트 쿼리와 테스트에서의 일반적인 "gotchas" 중 하나이다. *gotchas: 문법적으로는 작동하지만 직관에 반하고, 예상치 못하거나 원하지 않는 결과를 초래하는 것. 이 라이브러리는 기본적으로 기하급수적인 backoff와 함께 세번의 재시도를 한다. 이는 잘못된 쿼리를 테스트하려할 때 시간초과가 될 가능성이 크다는 뜻이다.

retries를 끄는 가장 시운 방법은 QueryClientProvider를 이용하는 것이다. 위의 예시를 확장해보자.

**no-retires**

```tsx
const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        // ✅ turns retries off
        retry: false,
      },
    },
  })

  return ({ children }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  )
}

test("my first test", async () => {
  const { result } = renderHook(() => useCustomHook(), {
    wrapper: createWrapper()
  })
}
```

이렇게 하면 컴포넌트 트리에 있는 모든 쿼리들에 대해 `no retires`로 기본값을 설정한다. 실제 `useQuery`가 분명한 재시도 셋을 가지고 있지 않을때만 작동한다는 것을 아는 것은 중요하다.만약 다섯번의 재시도를 원하는 쿼리를 가진 경우, 이것은 여전히 우선순위를 가진다. 기본값은 오직 대체수단으로만 사용되기 때문이다.

### setQueryDefaults

이 옵션을 useQuery에 직접적으로 설정하지 말아야 한다. 가능한 기본값을 사용하고 override하려고 해라. 특정 쿼리에만 변경하는것이 정말 필요하다면 `queryClient.setQueryDefaults`를 사용해라.

예를 들어 `useQuery`에 재시도를 설정하는 대신

**not-on-useQuery**

```tsx
const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Example />
    </QueryClientProvider>
  )
}

function Example() {
  // 🚨 you cannot override this setting for tests!
  const queryInfo = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    retry: 5,
  })
}
```

이렇게 해라

**setQueryDefaults**

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 2,
    },
  },
})

// ✅ only todos will retry 5 times
queryClient.setQueryDefaults(['todos'], { retry: 5 })

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Example />
    </QueryClientProvider>
  )
}
```

이렇게 한다면, 모든 쿼리들은 두번 재시도하고 오직 'todos'만 5번 재시도할 것이다. 그리고 여전히 모든 쿼리에 대해 이를 끌 수 있는 옵션을 가진다.

> ### ReactQueryConfigProvider
>
> Of course, this only works for known query keys. Sometimes, you really want to set some configs on a subset of your component tree. In v2, React Query had a [ReactQueryConfigProvider](https://react-query-v2.tanstack.com/docs/api#reactqueryconfigprovider) for that exact use-case. You can achieve the same thing in v3 with a couple of lines of codes:
>
> ReactQueryConfigProvider
>
> ```jsx
> const ReactQueryConfigProvider = ({ children, defaultOptions }) => {
>   const client = useQueryClient()
>   const [newClient] = React.useState(
>     () =>
>       new QueryClient({
>         queryCache: client.getQueryCache(),
>         muationCache: client.getMutationCache(),
>         defaultOptions,
>       })
>   )
> 
>   return (
>     <QueryClientProvider client={newClient}>
>       {children}
>     </QueryClientProvider>
>   )
> }
> ```
>
> You can see this in action in this [codesandbox example](https://codesandbox.io/s/react-query-config-provider-v3-lt00f).

## ReactQueryConfigProvider

이것은 알려진 쿼리 키에만 작동한다. 컴퍼넌트 트리의 subset에 어떤 configs를 설정하고 싶을 수 있다. v2에서는 RQ는 이런 유스케이스를 위해  ReactQueryConfigProvider를 가진다. v3에서는 이런 코드 몇줄로 같은 것을 해낼 수 있다.

**ReactQueryConfigProvider**

```tsx
const ReactQueryConfigProvider = ({ children, defaultOptions }) => {
  const client = useQueryClient()
  const [newClient] = React.useState(
    () =>
      new QueryClient({
        queryCache: client.getQueryCache(),
        muationCache: client.getMutationCache(),
        defaultOptions,
      })
  )

  return (
    <QueryClientProvider client={newClient}>
      {children}
    </QueryClientProvider>
  )
}
```

이 코드샌드박스 예제에서 확인할 수 있다 [codesandbox example](https://codesandbox.io/s/react-query-config-provider-v3-lt00f).

>## Always await the query
>
>Since React Query is async by nature, when running the hook, you won't immediately get a result. It usually will be in loading state and without data to check. The [async utilities](https://react-hooks-testing-library.com/reference/api#async-utilities) from react-hooks-testing-library offer a lot of ways to solve this problem. For the simplest case, we can just wait until the query has transitioned to success state:
>
>waitFor
>
>```tsx
>const createWrapper = () => {
>  const queryClient = new QueryClient({
>    defaultOptions: {
>      queries: {
>        retry: false,
>      },
>    },
>  })
>  return ({ children }) => (
>    <QueryClientProvider client={queryClient}>
>      {children}
>    </QueryClientProvider>
>  )
>}
>
>test("my first test", async () => {
>  const { result, waitFor } = renderHook(() => useCustomHook(), {
>    wrapper: createWrapper()
>  })
>
>  // ✅ wait until the query has transitioned to success state
>  await waitFor(() => result.current.isSuccess)
>
>  expect(result.current.data).toBeDefined()
>}
>```
>
>> **Update**
>>
>> [@testing-library/react v13.1.0](https://github.com/testing-library/react-testing-library/releases/tag/v13.1.0) also has a new [renderHook](https://testing-library.com/docs/react-testing-library/api/#renderhook) that you can use. However, it doesn't return its own `waitFor` util, so you'll have to use the one you can [import from @testing-library/react](https://testing-library.com/docs/dom-testing-library/api-async/#waitfor) instead. The API is a bit different, as it doesn't allow to return a `boolean`, but expects a `Promise` instead. That means we must adapt our code slightly:
>>
>> new-render-hook
>>
>> ```tsx
>> import { waitFor, renderHook } from '@testing-library/react'
>> 
>> test("my first test", async () => {
>>   const { result } = renderHook(() => useCustomHook(), {
>>     wrapper: createWrapper()
>>   })
>> 
>>   // ✅ return a Promise via expect to waitFor
>>   await waitFor(() => expect(result.current.isSuccess).toBe(true))
>> 
>>   expect(result.current.data).toBeDefined()
>> }
>> ```

## Always await the query

리액트 쿼리는 본질적으로 비동기적이기 때문에, 훅을 돌리고 바로 결과를 얻지 못합니다. 보통은 로딩 상태에 있고 확인할 데이터가 없습니다. react-hooks-testing-library의 비동기 utilities들은 이 문제를 해결할 수 있는 많은 방법들을 제공합니다. 가장 간단한 경우에 우리는 쿼리가 success state로 전환될 때까지 단지 기다립니다.

**waitFor**

```tsx
const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        retry: false,
      },
    },
  })
  return ({ children }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  )
}

test("my first test", async () => {
  const { result, waitFor } = renderHook(() => useCustomHook(), {
    wrapper: createWrapper()
  })

  // ✅ wait until the query has transitioned to success state
  await waitFor(() => result.current.isSuccess)

  expect(result.current.data).toBeDefined()
}
```

### Update

[@testing-library/react v13.1.0](https://github.com/testing-library/react-testing-library/releases/tag/v13.1.0)은 또한 사용할 수 있는 renderHook을 가지고 있습니다. 하지만 자체적인 waitFor유틸을 반환하지 않습니다. @testing-library/react에서 import해서 그것을 사용할 수 있습니다. API는 다소 다르다. 그것은 boolean으로 반환하는 것이 아니라 `Promise`로 반환한다. 그것은 우리가 반드시 아까 코드에서 수정해야 한다.

**new-render-hook**

```tsx
import { waitFor, renderHook } from '@testing-library/react'

test("my first test", async () => {
  const { result } = renderHook(() => useCustomHook(), {
    wrapper: createWrapper()
  })

  // ✅ return a Promise via expect to waitFor
  await waitFor(() => expect(result.current.isSuccess).toBe(true))

  expect(result.current.data).toBeDefined()
}
```

>  Putting it all together
>
> I've set up a quick repository where all of this comes nicely together: mock-service-worker, react-testing-library and the mentioned wrapper. It contains four tests - basic failure and success tests for custom hooks and components. Have a look here: https://github.com/TkDodo/testing-react-query

### Putting it all together

이 mock-service-worker랑 react-testing-library 그리고 wrapper가 다 잘 쓰인 레포를 하나 만들었다. 참고:

https://github.com/TkDodo/testing-react-query