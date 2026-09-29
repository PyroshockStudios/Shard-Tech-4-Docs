# SceneScript

## Summary
Represents a scriptable scene controller providing lifecycle callbacks across scene execution phases.

## Remarks
<para><b>Master Thread:</b> Operations on this type interact directly with scene and engine state, and must be executed exclusively on the Master Thread.</para>

## Definition

**Namespace:** `SDT4.Managed.Core.Script`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class SceneScript
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Scene](../scene.md) ➔  **SceneScript**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IDisposeTracker&lt;Scene&gt;](../utility/idisposetracker`1.md), [IScriptTarget](./iscripttarget.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; UniqueIdentifier` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the unique identifier for this scene script target, defaulting to [Guid.Empty](https://learn.microsoft.com/dotnet/api/system.guid#empty). |



---

## Methods

#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreBegin()


**Summary:**
Invoked when the scene starts, before any other scripts have begun execution.

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostBegin()


**Summary:**
Invoked when the scene starts, after all scene actors have been instantiated.

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreTick([Single](https://learn.microsoft.com/dotnet/api/system.single) dt)


**Summary:**
Invoked each frame prior to actor update ticking.

**Parameters:**

- `dt` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The delta time in seconds elapsed since the previous frame.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostTick([Single](https://learn.microsoft.com/dotnet/api/system.single) dt)


**Summary:**
Invoked each frame after actor update ticking has completed.

**Parameters:**

- `dt` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The delta time in seconds elapsed since the previous frame.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreStep([Single](https://learn.microsoft.com/dotnet/api/system.single) ts)


**Summary:**
Invoked each physics update prior to fixed-step evaluation.

**Parameters:**

- `ts` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The fixed timestep duration in seconds.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostStep([Single](https://learn.microsoft.com/dotnet/api/system.single) ts)


**Summary:**
Invoked each physics update after fixed-step evaluation has completed.

**Parameters:**

- `ts` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The fixed timestep duration in seconds.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreEnd()


**Summary:**
Invoked prior to scene termination and actor cleanup.

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostEnd()


**Summary:**
Invoked after scene termination and actor cleanup have completed.

---


---