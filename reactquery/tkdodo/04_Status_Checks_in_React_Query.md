# Status Checks in React Query

> One advantage of React Query is the easy access to status fields of the query. You instantly know if your query is loading or if it's erroneous. For this, the library exposes a bunch of boolean flags, which are mostly derived from the internal state machine. Looking at [the types](https://github.com/TanStack/query/blob/87358d73582b369f06cc81d0dfa135323df7d43d/packages/query-core/src/types.ts#L441), your query can be in one of the following states:
>
> - `success`: Your query was successful, and you have `data` for it
> - `error`: Your query did not work, and an `error` is set
> - `pending`: Your query has no data
>
> Note that the `isFetching` flag is *not* part of the internal state machine - it is an additional flag that will be true whenever a request is in-flight. You can be fetching and success, you can be fetching and error - but you cannot be loading and success at the same time. The state machine makes sure of that.
>
> **Update**
>
> Before v5, `pending` was named `loading`, and before v4, there was a fourth state called `idle`.
>
> Also, the `isFetching` flag is derived from a secondary `fetchStatus` - just like the `isPaused` flag. You can read more about this in [#13: Offline React Query](https://tkdodo.eu/blog/offline-react-query).

리액트 쿼리의 장점은 쿼리의 상태 필드에 대해 쉽게 접근할 수 있다는 것이다. 쿼리가 로딩 중인지, 에러가 났는지 바로 알 수 있다. 이 라이브러리는 내부 state machinde에서 비롯된 다수의 boolean flag를 제공한다. 쿼리는 뒤에 나오는 states중의 하나의 상태이다.

- success : 쿼리가 성공적이고, `data`를 가진다.
- error: 쿼리가 작동하지 않았다. `error`가 세팅된다.
- Pending: 쿼리에 데이터가 없다

`isFetching` 플래그는 내부적인 상태 머신의 일부가 아니라는 것에 주목해야 한다. request가 진행중일때마다 true가 되는 추가적인 플래그이다.

fetching하 고 성공할수도 있고, fetching하고 실패할 수도 있다. 하지만 로딩중이면서 동시에 성공을 할 수는 없다. 이 state machine은 그것을 확실하게 해준다.

**Update**

v5 이전에는 pending이 loading이었다. 그리고 v4이전에는 idle이라는 4번째 상테가 있었다. 또한, `isFetching` 플래그는 `isPaused`처럼 두번째 ` fetchStatus`에서 온다. 이것에 대해서는 #13에서 자세히 확인할 수 있다.

> ## The standard example
>
> Most examples look something like this:
>
> standard-example
>
> ```jsx
> const todos = useTodos()
> 
> if (todos.isPending) {
>   return 'Loading...'
> }
> if (todos.error) {
>   return 'An error has occurred: ' + todos.error.message
> }
> 
> return <div>{todos.data.map(renderTodo)}</div>
> ```
>
> Here, we check for pending and error first, and then display our data. This is probably fine for some use-cases, but not for others. Many data fetching solutions, especially hand-crafted ones, have no refetch mechanism, or only refetch on explicit user interactions.
>
> But React Query does.
>
> It refetches quite aggressively per default, and does so without the user actively requesting a refetch. The concepts of `refetchOnMount`, `refetchOnWindowFocus` and `refetchOnReconnect` are great for keeping your data accurate, but they might cause a confusing ux if such an automatic background refetch fails.

## The standard example

대부분의 예시는 이것과 같다

**standard-example**

```jsx
const todos = useTodos()

if (todos.isPending) {
  return 'Loading...'
}
if (todos.error) {
  return 'An error has occurred: ' + todos.error.message
}

return <div>{todos.data.map(renderTodo)}</div>

```

여기서 우리는 먼저 대기중을 확인하고 그 다음에 데이터를 보이게 합니다. 이건 어떤 유스케이스들에서는 괜찮지만 다른 유스케이스에서는 아닙니다. 많은 데이터를 가져오는 해결법들은 refetch 메커니즘이 없거나 또는 단지 명시적인 사용자 인터렉션에서만 refetch를 합니다.

하지만 RQ는 합니다.

기본적으로 적극적으로 refetch를 합니다. 그리고 사용자가 활발하게 refetch를 요구하지 않아도 그렇게 합니다. 



`refetchOnMount`, `refetchOnWindowFocus`, `refetchOnReconnect`와 같은 컨셉들은 데이터 정확성을 지키는데 좋습니다. 하지만 그들은 자동적인 배경 refetch가 실패할 경우 ux에 혼란을 줄 수 있습니다. 

>## Background errors
>
>In many situations, if a background refetch fails, it could be silently ignored. But the code above does not do that. Let's look at two examples:
>
>- The user opens a page, and the initial query loads successfully. They are working on the page for some time, then switch browser tabs to check emails. They come back some minutes later, and React Query will do a background refetch. Now that fetch fails.
>- Our user is on page with a list view, and they click on one item to drill down to the detail view. This works fine, so they go back to the list view. Once they go to the detail view again, they will see data from the cache. This is great - except if the background refetch fails.
>
>In both situations, our query will be in the following state:
>
>```json
>{
>  "status": "error",
>  "error": { "message": "Something went wrong" },
>  "data": [{ ... }]
>}
>```
>
>As you can see, we will have *both* an error *and* the stale data available. This is what makes React Query great - it embraces the stale-while-revalidate caching mechanism, which means it will always give you data if it exists, even if it's stale.
>
>Now it's up to us to decide what we display. Is it important to show the error? Is it enough to show the stale data only, if we have any? Should we show both, maybe with a little *background error* indicator?
>
>There is no clear answer to this question - it depends on your exact use-case. However, given the two above examples, I think it would be a somewhat confusing user experience if data would be replaced with an error screen.
>
>This is even more relevant when we take into account that React Query will retry failed queries three times per default with exponential backoff, so it might take a couple of seconds until the stale data is replaced with the error screen. If you also have no background fetching indicator, this can be really perplexing.
>
>This is why I usually check for data-availability first:
>
>data-first
>
>```jsx
>const todos = useTodos()
>
>if (todos.data) {
>  return <div>{todos.data.map(renderTodo)}</div>
>}
>if (todos.error) {
>  return 'An error has occurred: ' + todos.error.message
>}
>
>return 'Loading...'
>```
>
>Again, there is no clear principle of what is right, as it is highly dependent on the use-case. Everyone should be aware of the consequences that aggressive refetching has, and we have to structure our code accordingly rather than strictly following the simple todo-examples 😉.
>
>Special thanks go to [Niek Bosch](https://github.com/boschni) who first highlighted to me why this pattern of status checking can be harmful in some situations.

## Background errors

많은 상황에서 만약 refetch가 실패한다면, 그것은 조용하게 무시됩니다. 하지만 위의 코드는 안그럽니다. 두가지 예시를 보여드리겠습니다.

1. 사용자가 페이지를 열고 초기 쿼리가 성공적으로 로드가 됩니다. 그들은 어느 정도 페이지 위에서 작동합니다. 그리고 이메일을 확인하기 위해 탭을 변경합니다. 그들은 좀 후에 리액트 쿼리는 배경에 refetch를 합니다. 그리고 fetch를 실패합니다.
2. List view에 있는 사용자가 하나의 아이템을 클릭하고 상세 뷰로 넘어갑니다. 이것은 잘 작동합니다. 그래서 그들은 list view로 돌아갑니다. 그들은 캐시에 있는 데이터를 봅니다. 이것은 좋습니다 - refetch가 실패했을 때를 제외합니다.

두 상황에서 쿼리는 이런 상태입니다.

```json
{
  "status": "error",
  "error": { "message": "뭔가 잘못됐습니다" },
  "data": [{ ... }]
}
```

error와 stale된 데이터를 모두 가지고 있다. 이것이 react query을 대단하게 만들어준다. 이것은 'stale-while-revaliate' 캐싱 매커니즘을 수용한다. 그래서 데이터가 오래됐더라도 존재한다면 항상 제공합니다.



이제 우리가 어떤 것을 표시할지 결정해야 한다. 에러를 보여주는 것이 중요한지, 가지고 있다면 stale된 데이터를 보여줘야할지, 작은 에러 표시와 함께 둘다 보여줘야 할지?

명확한 정답은 없다. 너의 정확한 유스 케이스에 달려있다. 하지만 위 두개의 케이스를 봤을떄, 나는 데이터 대신 에러 메세지가 있다면 사용자 경험이 혼란을 줄 것이라고 본다.

이것은 리액트 쿼리가 기본적으로 실패한 쿼리를 exponential backoff를 사용해서 기본으로 세번 재시도 하기 때문에 더욱 중요하다. 그래서 stale된 데이터가 에러 스크린으로 대체되기까지 몇 초 걸릴 수 있다. 만약 배경에서 fetching을 표시하지 않는다면, 이것은 좀 당혹스러울 수 있다.



이것은 data-availability를 우선으로 두는 이유입니다.

**data-first**

```jsx
const todos = useTodos()

if (todos.data) {
  return <div>{todos.data.map(renderTodo)}</div>
}
if (todos.error) {
  return 'An error has occurred: ' + todos.error.message
}

return 'Loading...'
```

확실한 원칙은 없습니다. 유스-케이스에 달려있습니다. 모두 적극적인 refetching의 결과를 알아야 합니다. 그리고 간단한 할일 예제들을 따르기보다는 고유의 구조를 갖추는 것이 좋습니다.
