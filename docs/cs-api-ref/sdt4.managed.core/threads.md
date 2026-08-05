# Threads

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
static class Threads
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Threads**
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
| `public static get; protected static set; MasterThreadId` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | The managed master thread ID. |
| `public static get; IsCurrentMasterThread` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | States if the current executing thread is the master thread. |



---

## Methods

#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) AssertMasterThread()


**Summary:**
Asserts that the current thread is the master thread.

**Remarks:**
!!! info
    Debug only: This method is stripped in release builds

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) AssertMatchThread([Int32](https://learn.microsoft.com/dotnet/api/system.int32) target)


**Summary:**
Asserts that the current thread matches the target thread ID.

**Remarks:**
!!! info
    Debug only: This method is stripped in release builds

**Parameters:**

- `target` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) RunLater([ThreadStart](https://learn.microsoft.com/dotnet/api/system.threading.threadstart) thread)


**Summary:**
Queues a subroutine to be executed on the master thread during the next engine tick.

**Parameters:**

- `thread` ([ThreadStart](https://learn.microsoft.com/dotnet/api/system.threading.threadstart)): Runnable function to call.


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) RunOnMaster([ThreadStart](https://learn.microsoft.com/dotnet/api/system.threading.threadstart) thread)


**Summary:**
Executes a subroutine on the master thread. If already on the master thread, executes immediately (blocking).

**Parameters:**

- `thread` ([ThreadStart](https://learn.microsoft.com/dotnet/api/system.threading.threadstart)): Runnable function to call.


---
#### public static [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) RunLaterAsync([Action](https://learn.microsoft.com/dotnet/api/system.action) action)


**Summary:**
Queues a subroutine to be executed on the master thread during the next engine tick 
and allows you to await its completion.

**Parameters:**

- `action` ([Action](https://learn.microsoft.com/dotnet/api/system.action)): 


**Returns:**

- [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task): 

---
#### public static [Task&lt;T&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) RunLaterAsync&lt;T&gt;([Func&lt;T&gt;](https://learn.microsoft.com/dotnet/api/system.func-1) function)


**Summary:**
Queues a subroutine to be executed on the master thread during the next engine tick, 
awaits its completion, and returns the result.

**Parameters:**

- `function` ([Func&lt;T&gt;](https://learn.microsoft.com/dotnet/api/system.func-1)): 


**Returns:**

- [Task&lt;T&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1): 

---


---