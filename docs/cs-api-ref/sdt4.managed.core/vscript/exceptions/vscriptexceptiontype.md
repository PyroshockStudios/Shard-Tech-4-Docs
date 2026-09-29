# VScriptExceptionType

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.VScript.Exceptions`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
enum VScriptExceptionType
```

---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `Generic` | [VScriptExceptionType](./vscriptexceptiontype.md) | General unhandled script error or custom user message. |
| `InvalidArgument` | [VScriptExceptionType](./vscriptexceptiontype.md) | A passed argument or pin value is invalid or out of acceptable bounds. |
| `NullReference` | [VScriptExceptionType](./vscriptexceptiontype.md) | A required object, entity, or reference is null or unassigned. |
| `IndexOutOfBounds` | [VScriptExceptionType](./vscriptexceptiontype.md) | An array index, collection lookup, or slot ID was outside valid boundaries. |
| `InvalidState` | [VScriptExceptionType](./vscriptexceptiontype.md) | The operation cannot proceed due to the current game/object state (e.g., acting on a dead entity). |
| `NotFound` | [VScriptExceptionType](./vscriptexceptiontype.md) | An asset, resource, dictionary key, or sub-object could not be found. |
| `NotSupported` | [VScriptExceptionType](./vscriptexceptiontype.md) | A requested operation is not implemented or not supported in this context. |
| `MathError` | [VScriptExceptionType](./vscriptexceptiontype.md) | A division by zero, NaN, or arithmetic overflow occurred during execution. |
| `Timeout` | [VScriptExceptionType](./vscriptexceptiontype.md) | A timeout or deadline expired while waiting for an external event or condition. |
| `AssertionFailed` | [VScriptExceptionType](./vscriptexceptiontype.md) | A critical runtime assertion failed. |
| `NotImplemented` | [VScriptExceptionType](./vscriptexceptiontype.md) | This function is not implemented |
| `MissingReturn` | [VScriptExceptionType](./vscriptexceptiontype.md) | This function is missing a return value |
| `ForeignException` | [VScriptExceptionType](./vscriptexceptiontype.md) | This exception is a rethrown non-visual script exception |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |



---

## Methods



---