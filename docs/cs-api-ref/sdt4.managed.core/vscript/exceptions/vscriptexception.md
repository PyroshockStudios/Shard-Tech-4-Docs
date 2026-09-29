# VScriptException

## Summary
Exception class for Visual Script.

## Remarks
!!! note
    Should not be thrown from handwritten C# code. Prefer to use System exceptions or custom exceptions.

## Definition

**Namespace:** `SDT4.Managed.Core.VScript.Exceptions`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class VScriptException
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Exception](https://learn.microsoft.com/dotnet/api/system.exception) ➔  **VScriptException**
**Implements:**

##### [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; ExceptionType` | [VScriptExceptionType](./vscriptexceptiontype.md) | The category/type of exception thrown. |
| `public get; SourceFile` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; NodeId` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) | The V-Script node ID the exception was thrown from. |
| `public get; ForeignException` | [Exception](https://learn.microsoft.com/dotnet/api/system.exception) | The foreign exception that was rethrown |



---

## Methods



---