# OffThreadAwaiter

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Threading`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct OffThreadAwaiter
```
**Implements:**

##### [ICriticalNotifyCompletion](https://learn.microsoft.com/dotnet/api/system.runtime.compilerservices.icriticalnotifycompletion), [INotifyCompletion](https://learn.microsoft.com/dotnet/api/system.runtime.compilerservices.inotifycompletion)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; IsCompleted` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) OnCompleted([Action](https://learn.microsoft.com/dotnet/api/system.action) continuation)

**Parameters:**

- `continuation` ([Action](https://learn.microsoft.com/dotnet/api/system.action)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnsafeOnCompleted([Action](https://learn.microsoft.com/dotnet/api/system.action) continuation)

**Parameters:**

- `continuation` ([Action](https://learn.microsoft.com/dotnet/api/system.action)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetResult()

---


---