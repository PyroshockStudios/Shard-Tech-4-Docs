# OffThreadTask

## Summary
A task wrapper that explicitly forbids awaiting or blocking on the Master Thread.
Prevents deadlocks where work scheduled on the master thread is awaited by the master thread itself.



## Definition

**Namespace:** `SDT4.Managed.Core.Threading`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct OffThreadTask
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



---

## Methods

#### public [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) AsTask()

**Returns:**

- [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Wait()

---
#### public [OffThreadAwaiter](./offthreadawaiter.md) GetAwaiter()

**Returns:**

- [OffThreadAwaiter](./offthreadawaiter.md): 

---


---