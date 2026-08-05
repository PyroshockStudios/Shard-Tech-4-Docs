# NativeEngineException

## Summary
Exception class for unexpected engine failure. Hopefully this never needs to be triggered,
however this is thrown if an unexpected invalid state is reached, that would never in normal circumstances.

## Remarks
!!! important
    It is highly likely that either a memory corruption occurred (however it is more likely for a
    [ExecutionEngineException](https://learn.microsoft.com/dotnet/api/system.executionengineexception) to be thrown in that scenario) or a bug in the engine.
    Please report bugs to <a href="mailto:support@pyroshockstudios.com">support@pyroshockstudios.com</a>
    with reproducible steps if this exception occurs frequently!

## Definition

**Namespace:** `SDT4.Managed.Core.Exceptions`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class NativeEngineException
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Exception](https://learn.microsoft.com/dotnet/api/system.exception) ➔  **NativeEngineException**
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
| `public get; ManagedModule` | [String](https://learn.microsoft.com/dotnet/api/system.string) | C# Module the exception occurred in. This is almost always tied to a specific C++ module. Note: This should never be null, however if it is, it indicates even stronger corruption. |



---

## Methods



---