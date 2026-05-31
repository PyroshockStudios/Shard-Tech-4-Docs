# AppLoadContext

Contains the application load information when the game initially loads.

## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct AppLoadContext
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
| `public get; Args` | [String[]](https://learn.microsoft.com/dotnet/api/system.string) | The application arguments used when launching !!! warning     This includes engine specific arguments such as -rhi,      refer to the engine manual to avoid usage of certain argument names |
| `public get; Env` | [String[]](https://learn.microsoft.com/dotnet/api/system.string) | The environment variables available when launching the application |
| `public get; InstanceReadyTask` | [Task&lt;AppInstance&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) | Task containing the app instance once the components are ready.  !!! warning     This task may throw a <see cref="T:System.InvalidOperationException" /> in case of the application      failing to load any components. In this situation, the application cannot be loaded and      the app must be restarted by the user. |
| `public get; GameReadyTask` | [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) | Task that finishes once the opening screen finishes playing. In the event of <see cref="P:SDT4.Managed.Core.AppLoadContext.InstanceReadyTask" />  throws an exception, this task throws a <see cref="T:System.InvalidOperationException" />.  !!! note     In the case of a headless application, this task is <strong>NULL</strong>. |


---

## Methods



---