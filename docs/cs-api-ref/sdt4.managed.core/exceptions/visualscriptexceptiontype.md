# VisualScriptExceptionType

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Exceptions`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
enum VisualScriptExceptionType
```

---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `Generic` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | General unhandled script error or custom user message. |
| `InvalidArgument` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | A passed argument or pin value is invalid or out of acceptable bounds. |
| `NullReference` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | A required object, entity, or reference is null or unassigned. |
| `IndexOutOfBounds` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | An array index, collection lookup, or slot ID was outside valid boundaries. |
| `InvalidState` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | The operation cannot proceed due to the current game/object state (e.g., acting on a dead entity). |
| `NotFound` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | An asset, resource, dictionary key, or sub-object could not be found. |
| `NotSupported` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | A requested operation is not implemented or not supported in this context. |
| `MathError` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | A division by zero, NaN, or arithmetic overflow occurred during execution. |
| `Timeout` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | A timeout or deadline expired while waiting for an external event or condition. |
| `AssertionFailed` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | A critical runtime assertion failed. |
| `NotImplemented` | [VisualScriptExceptionType](./visualscriptexceptiontype.md) | This function is not implemented |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |



---

## Methods



---