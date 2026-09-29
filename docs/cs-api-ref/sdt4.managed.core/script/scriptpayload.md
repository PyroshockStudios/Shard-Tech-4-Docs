# ScriptPayload

## Summary
Represents payload data supplied during actor script initialisation and creation control.



## Definition

**Namespace:** `SDT4.Managed.Core.Script`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class ScriptPayload
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **ScriptPayload**
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
| `public get; set; Veto` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets or sets a value indicating whether the creation of this actor should be cancelled. |
| `public get; protected set; State` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | Gets custom initialisation data passed via <c>SpawnPrefab</c>, or <see langword="null" /> if the actor is being loaded from a level file. |



---

## Methods



---