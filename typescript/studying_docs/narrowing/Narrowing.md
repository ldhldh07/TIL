### Narrowing

```typescript
function padLeft(padding: number | string, input: string): string {
  throw new Error("Not implemented yet!");
}
```

`padding`이 `number`라면 

```typescript
function padLeft(padding: number | string, input: string) {
  return " ".repeat(padding) + input;
`Argument of type 'string | number' is not assignable to parameter of type 'number'.
  Type 'string' is not assignable to type 'number'.`
}
```

repeat이 number에 쓰는 것이기 때문에 오류

```typescript
function padLeft(padding: number | string, input: string) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + input;
  }
  return padding + input;
}
```

if(typeof )를 이용해서 narrowing