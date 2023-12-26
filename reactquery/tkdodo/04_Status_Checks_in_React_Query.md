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
- 

