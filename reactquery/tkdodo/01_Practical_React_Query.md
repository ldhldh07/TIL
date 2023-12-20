[원본] (https://tkdodo.eu/blog/practical-react-query)

# Practical React Query

>When GraphQL and especially [Apollo Client](https://www.apollographql.com/docs/react/) became popular in ca. 2018, there was a lot of fuss about it completely replacing redux, and the question [Is Redux dead yet?](https://dev.to/markerikson/redux---not-dead-yet-1d9k) has been asked a lot.
>
>I distinctly remember not understanding what this was all about. Why would some data fetching library replace your global state manager? What does one even have to do with the other?
>
>I was under the impression that GraphQL clients like Apollo would only fetch the data for you, similar to what e.g. [axios](https://github.com/axios/axios) does for REST, and that you would still obviously need some way of making that data accessible to your application.
>
>I couldn't have been more wrong.

Apollo 클라이언트가 화제가 되었을 때, data fetching library가 상태 관리자를 대체한다는 이야기를 이해하지 못함.

단순히 데이터를 가져오면 애플리케이션에서 그걸 또 가져오는 방식이 필요하다고 생각

>## Client State vs. Server State
>
>What Apollo gives you is not just the ability to describe which data you want and to fetch that data, it also comes with a *cache* for that server data. This means that you can just use the same `useQuery` hook in multiple components, and it will only fetch data once and then subsequently return it from the cache.
>
>
>
>This sounds *very* familiar with what we, and probably many other teams as well, have mainly been using `redux` for: Fetch data from the server and make it available everywhere.
>
>
>
>So it seems that we have always been treating this *server state* like any other *client state*. Except that when it comes to *server state* (think: A list of articles that you fetch, the details of a User you want to display, ...), your app does not own it. We have only borrowed it to display the most recent version of it on the screen for the user. It is the server who owns the data.
>
>
>
>To me, that introduced a paradigm shift in how to think about data. If we can leverage the cache to display data that we do not own, there isn't really much left that is real client state that *also* needs to be made available to the whole app. That made me understand why many think that Apollo can replace redux in lots of instances.

Apollo는 서버 데이터에 대한 캐시를 제공

이런식으로 데이터를 캐시로 이용한다면, 전역적으로 사용해야하는 client state는 별로 많지 않아짐

>## React Query
>
>I have never had the chance to use GraphQL. We have an existing REST API, don't really experience problems with over-fetching, it just works, etc. Clearly, there aren't enough pain points for us to warrant a switch, especially given that you'd also have to adapt the backend, which isn't quite so simple.
>
>Yet I still envied the simplicity of how data fetching can look like on the frontend, including the handling of loading and error states. If only there were something similar in React for REST APIs...
>
>Enter [React Query](https://tanstack.com/query/latest/).
>
>Made by the open sourcerer [Tanner Linsley](https://github.com/tannerlinsley) in late 2019, React Query takes the good parts of Apollo and brings them to REST. It works with any function that returns a Promise and embraces the *stale-while-revalidate* caching strategy. The library operates on sane defaults that try to keep your data as fresh as possible while at the same time showing data to the user as early as possible, making it feel near instant at times and thus providing a great UX. On top of that, it is also very flexible and lets you customize various settings for when the defaults are not enough.
>
>This article is not going to be an introduction to React Query though.
>
>I think the docs are great at explaining Guides & Concepts, there are [Videos](https://tanstack.com/query/latest/docs/react/videos) from various Talks that you can watch, and Tanner has a React Query [Essentials Course](https://learn.tanstack.com/) you can take if you want to get familiar with the library.
>
>I want to focus more on some practical tips that go beyond the docs, which might be useful when you are already working with the library. These are things I have picked up over the last couple of months when I was not only actively using the library at work, but also got involved in the React Query community, answering questions on Discord and in GitHub Discussions.

그 아폴로의 좋은점을 REST로 가져온 것이 리액트쿼리

>### The Defaults explained
>
>I believe the React Query [Defaults](https://tanstack.com/query/latest/docs/react/guides/important-defaults) are very well chosen, but they can catch you off guard from time to time, especially at the beginning.
>
>First of all: React Query does *not* invoke the `queryFn` on every re-render, even with the default `staleTime` of zero. Your app can re-render for various reasons at any time, so fetching every time would be insane!
>
>> Always code for re-renders, and a lot of them. I like to call it render resiliency.
>
>— Tanner Linsley
>
>If you see a refetch that you are not expecting, it is likely because you just focused the window and React Query is doing a `refetchOnWindowFocus`, which is a great feature for production: If the user goes to a different browser tab, and then comes back to your app, a background refetch will be triggered automatically, and data on the screen will be updated if something has changed on the server in the meantime. All of this happens without a loading spinner being shown, and your component will not re-render if the data is the same as you currently have in the cache.
>
>During development, this will probably be triggered more frequently, especially because focusing between the Browser DevTools and your app will also cause a fetch, so be aware of that.
>
>**Update**
>
>Since React Query v5, `refechOnWindowFocus` no longer listens to the `focus` event - the `visibilitychange` event is used exclusively. This means you'll get fewer unwanted re-fetches in development mode, while still retaining the trigger for most production cases. It also fixes a bunch of issues as [shown here](https://github.com/TanStack/query/pull/4805).
>
>Secondly, there seems to be a bit of confusion between `gcTime` and `staleTime`, so let me try to clear that up:
>
>- `staleTime`: The duration until a query transitions from fresh to stale. As long as the query is fresh, data will always be read from the cache only - no network request will happen! If the query is stale (which per default is: instantly), you will still get data from the cache, but a background refetch can happen [under certain conditions](https://tanstack.com/query/latest/docs/react/guides/caching).
>- `gcTime`: The duration until inactive queries will be removed from the cache. This defaults to 5 minutes. Queries transition to the inactive state as soon as there are no observers registered, so when all components which use that query have unmounted.
>
>Most of the time, if you want to change one of these settings, it's the `staleTime` that needs adjusting. I have rarely ever needed to tamper with the `gcTime`. There is a good [explanation by example](https://tanstack.com/query/latest/docs/react/guides/caching#basic-example) in the docs as well.
>
>**Update**
>
>`gcTime` was previously known as `cacheTime`, but it got renamed in v5 to better reflect what it's doing.



`React Query`는 리렌더링할때마다 쿼리를 호출하지 않는다 (`staleTime`이 0이라 할지라도)

Tanner Linsley씨가 이야기하는 `render resiliency` 렌더 회복력 - 여러번의 리렌더에 버틸 수 있는 코드

예를 들어 `refetchOnWindowFocus`는 사용자가 다른 브라우저탭으로 이용했다가 앱으로 돌아올 때 리패치가 되는 기능이다. 

캐시랑 똑같은 경우에 로딩 spinner 안보여지고 리렌더링이 안된다.

### `gcTime`과 `staleTime`의 차이

- `staleTime`: 쿼리가 `fresh`에서 `stale`로 전환되는 시간, * stale: 구식의. 쿼리가 fresh 상태에서는 네트워크로 요청하지 않고 캐시에서 읽음. stale상태에서는 여전히 캐시에서 데이터를 받지만, 특정 조건하에서는 다시 `refetch`가 이루어짐.

- `gcTime`: 비활성화된 쿼리가 캐시에서 삭제될때까지의 시간.*비활성화 상태 : 모든 쿼리가 `unmount`. 보통은 gcTime을 조정할 일이 없음 기본값- 5분

>### Use the React Query DevTools
>
>This will help you immensely in understanding the state a query is in. The DevTools will also tell you what data is currently in the cache, so you'll have an easier time debugging. In addition to that, I have found that it helps to throttle your network connection in the browser DevTools if you want to better recognize background refetches, since dev-servers are usually pretty fast.
>
>### Treat the query key like a dependency array
>
>I am referring to the dependency array of the [useEffect](https://reactjs.org/docs/hooks-reference.html#conditionally-firing-an-effect) hook here, which I assume you are familiar with.
>
>Why are these two similar?
>
>Because React Query will trigger a refetch whenever the query key changes. So when we pass a variable parameter to our `queryFn`, we almost always want to fetch data when that value changes. Instead of orchestrating complex effects to manually trigger a refetch, we can utilize the query key:

```typescript
type State = 'all' | 'open' | 'done'
type Todo = {
  id: number
  state: State
}
type Todos = ReadonlyArray<Todo>

const fetchTodos = async (state: State): Promise<Todos> => {
  const response = await axios.get(`todos/${state}`)
  return response.data
}

export const useTodosQuery = (state: State) =>
  useQuery({
    queryKey: ['todos', state],
    queryFn: () => fetchTodos(state),
  })
```

`useEffect`와 비슷하다 쿼리키가 변경될때마다 `refetch`하는 것이 useEffect에서 dependency 배열을 참조하는 것과 유사



>#### A new cache entry
>
>Because the query key is used as a key for the cache, you will get a new cache entry when you switch from 'all' to 'done', and that will result in a hard loading state (probably showing a loading spinner) when you switch for the first time. This is certainly not ideal, so if possible, we can try to pre-fill the newly created cache entry with [initialData](https://tanstack.com/query/latest/docs/react/guides/initial-query-data#initial-data-from-cache). The above example is perfect for that, because we can do some client side pre-filtering on our todos:
>
>```typescript
>type State = 'all' | 'open' | 'done'
>type Todo = {
>  id: number
>  state: State
>}
>type Todos = ReadonlyArray<Todo>
>
>const fetchTodos = async (state: State): Promise<Todos> => {
>  const response = await axios.get(`todos/${state}`)
>  return response.data
>}
>
>export const useTodosQuery = (state: State) =>
>  useQuery({
>    queryKey: ['todos', state],
>    queryFn: () => fetchTodos(state),
>    /// 추가된 부분
>    initialData: () => {
>      const allTodos = queryClient.getQueryData<Todos>([
>        'todos',
>        'all',
>      ])
>      const filteredData =
>        allTodos?.filter((todo) => todo.state === state) ?? []
>
>      return filteredData.length > 0 ? filteredData : undefined
>    },
>  	/// 추가된 부분
>  })
>```

`initialData`로 스위치 할 때 로딩 대신 모든 데이터로 최적화할 수 있음

캐시에서 해당 state에 해당하는 모든 항목을 불러오고

쿼리키가 변경되면 새로운 캐시를 만들어서 새 캐시에넣고 업데이트된 목록을 보여줄 수 있음

>### Keep server and client state separate
>
>This goes hand in hand with [putting-props-to-use-state](https://tkdodo.eu/blog/putting-props-to-use-state), an article I have written last month: If you get data from `useQuery`, try not to put that data into local state. The main reason is that you implicitly opt out of all background updates that React Query does for you, because the state "copy" will not update with it.
>
>This is fine if you want to e.g. fetch some default values for a Form, and render your Form once you have data. Background updates are very unlikely to yield something new, and even if, your Form has already been initialized. So if you do that on purpose, make sure to *not* fire off unnecessary background refetches by setting `staleTime`:
>
>```jsx
>/// initial-form-data
>const App = () => {
>  const { data } = useQuery({
>    queryKey: ['key'],
>    queryFn,
>    staleTime: Infinity,
>  })
>
>  return data ? <MyForm initialData={data} /> : null
>}
>
>const MyForm = ({ initialData }) => {
>  const [data, setData] = React.useState(initialData)
>  ...
>}
>```
>
>This concept will be a bit harder to follow through when you display data that you also want to allow the user to edit, but it has many advantages. I have prepared a little codesandbox example:
>
><iframe src="https://codesandbox.io/embed/inspiring-mayer-rp3jx?fontsize=14&amp;hidenavigation=1&amp;theme=dark&amp;view=preview" title="separate-server-and-client-state" allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts" style="box-sizing: inherit; color: rgb(45, 55, 72); font-family: Inter, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, &quot;Noto Sans&quot;, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; width: 877px; height: 600px; border: 0px; border-radius: 4px; overflow: hidden;"></iframe>
>
>The important part of this demo is that we never put the value that we get from React Query into local state. This makes sure that we always see the latest data, because there is no local "copy" of it.

RQ로 불러온 값은 local State에 넣지 말아야 최신 데이터로 표시할 수 있음

로컬 스테이트에 넣으면 최신으로 안바뀜 : 코드박스 - 랜덤 숫자가 안바뀜

>### The enabled option is very powerful
>
>The `useQuery` hook has many options that you can pass in to customize its behaviour, and the `enabled` option is a very powerful one that *enables* you to do many cool things (pun intended). Here is a short list of things that we were able to accomplish thanks to this option:
>
>- [Dependent Queries](https://tanstack.com/query/latest/docs/react/guides/dependent-queries)
>  Fetch data in one query and have a second query only run once we have successfully obtained data from the first query.
>- Turn queries on and off
>  We have one query that polls data regularly thanks to `refetchInterval`, but we can temporarily pause it if a Modal is open to avoid updates in the back of the screen.
>- Wait for user input
>  Have some filter criteria in the query key, but disable it for as long as the user has not applied their filters.
>- Disable a query after some user input
>  e.g. if we then have a draft value that should take precedence over the server data. See the above example.

`enabled` 옵션들

- `Dependent Queries`: 첫번째 쿼리를 성공했을때만 두번째 쿼리를 가져움
- `Turn queries on and off` : `refetchInterval`을 사용했을 때, 주기적으로 데이터를 가져오는데, 모달이 열려 있을 때는 잠깐 멈춰놓을 수 있음
- `Wait for user input`: 쿼리 키에 필터 기준을 적용할 때, 사용자가 필터를 적용할 때까지 비활성화
- `Disable a query after some user input` : 서버 데이터보다 우선해야할 draft value 가 있으면 사용

>### Don't use the queryCache as a local state manager
>
>If you tamper with the queryCache (`queryClient.setQueryData`), it should only be for optimistic updates or for writing data that you receive from the backend after a mutation. Remember that every background refetch might override that data, so [use](https://reactjs.org/docs/hooks-state.html) [something](https://zustand.surge.sh/) [else](https://redux.js.org/) for local state.

로컬 상태 관리자로 캐시 사용하지 마세요

`setQueryData`는 서버에서 받은 데이터를 변형해서 넣을 때나 낙관적인 업데이트가 있을 때 사용되는 것이고 local state로 쓰기 위한 것이 아니다

>### Create custom hooks
>
>Even if it's only for wrapping one `useQuery` call, creating a custom hook usually pays off because:
>
>- You can keep the actual data fetching out of the ui, but co-located with your `useQuery` call.
>- You can keep all usages of one query key (and potentially type definitions) in one file.
>- If you need to tweak some settings or add some data transformation, you can do that in one place.
>
>You have already seen an example of that in the [todos queries above](https://tkdodo.eu/blog/practical-react-query#treat-the-query-key-like-a-dependency-array).

useQuery를 래핑한 custom hooks를 만들기

- ui랑 분리하여 관련된 위치에 호출
- 하나의 파일로 동일 쿼리의 여러 사용을 유지할 수 있음
- 쿼리를 조정해야할때 하나의 파일에서 가능

