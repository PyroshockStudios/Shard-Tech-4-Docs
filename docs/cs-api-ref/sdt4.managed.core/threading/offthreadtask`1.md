# OffThreadTask&lt;&gt;

## Summary
A generic task wrapper that explicitly forbids awaiting or blocking on the Master Thread.



## Definition

**Namespace:** `SDT4.Managed.Core.Threading`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct OffThreadTask<>
```
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Result` | T |  |



---

## Methods

#### public [Task&lt;T&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) AsTask()

**Returns:**

- [Task&lt;T&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Wait()

---
#### public [OffThreadAwaiter&lt;T&gt;](./offthreadawaiter`1.md) GetAwaiter()

**Returns:**

- [OffThreadAwaiter&lt;T&gt;](./offthreadawaiter`1.md): 

---


---