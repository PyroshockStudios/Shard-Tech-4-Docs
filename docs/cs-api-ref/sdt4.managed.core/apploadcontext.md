# AppLoadContext

## Summary
Contains the application load information when the game initially loads.



## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class AppLoadContext
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **AppLoadContext**
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
| `public get; Args` | [String[]](https://learn.microsoft.com/dotnet/api/system.string) | The application arguments used when launching |
| `public get; Env` | [IReadOnlyDictionary&lt;String, String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2) | The environment variables available when launching the application |
| `public get; InstanceReadyTask` | [Task&lt;AppInstance&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) | Task containing the app instance once the components are ready. |
| `public get; GameReadyTask` | [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) | Task that finishes once the opening screen finishes playing. In the event of [AppLoadContext.InstanceReadyTask](./apploadcontext.md#instancereadytask)  throws an exception, this task throws a [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception). |


##### `Args` Remarks
!!! warning
    This includes engine specific arguments such as -rhi, 
    refer to the engine manual to avoid usage of certain argument names

##### `InstanceReadyTask` Remarks
!!! warning
    This task may throw a [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception) in case of the application 
    failing to load any components. In this situation, the application cannot be loaded and 
    the app must be restarted by the user.

##### `GameReadyTask` Remarks
!!! note
    In the case of a headless application, this task is <strong>NULL</strong>.


---

## Methods

#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---


---