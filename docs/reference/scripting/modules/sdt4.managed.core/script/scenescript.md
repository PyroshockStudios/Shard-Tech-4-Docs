# SceneScript

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Script`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class SceneScript
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Scene](../scene.md) ➔  **SceneScript**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IScriptTarget](./iscripttarget.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; UniqueIdentifier` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) |  |



---

## Methods

#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreBegin()


**Summary:**
Called when the scene starts, before any other scripts have been called

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostBegin()


**Summary:**
Called when the scene starts, after all actors have been instantiated

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreTick([Single](https://learn.microsoft.com/dotnet/api/system.single) dt)

**Parameters:**

- `dt` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostTick([Single](https://learn.microsoft.com/dotnet/api/system.single) dt)

**Parameters:**

- `dt` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreStep([Single](https://learn.microsoft.com/dotnet/api/system.single) ts)

**Parameters:**

- `ts` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostStep([Single](https://learn.microsoft.com/dotnet/api/system.single) ts)

**Parameters:**

- `ts` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPreEnd()

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnPostEnd()

---


---