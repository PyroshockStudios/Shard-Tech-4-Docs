# RMLEvent



## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RMLEvent
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RMLEvent**
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
| `public get; Type` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Get the event type. |
| `public get; set; CurrentTarget` | [RMLElement](./rmlelement.md) | Get/Set the current element in the propagation. |
| `public get; Target` | [RMLElement](./rmlelement.md) | The original target of the event |
| `public get; EventPhase` | [RMLEventPhase](./rmleventphase.md) | Indicates which phase of the event flow is being processed. |
| `public get; Interruptible` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns true if the event can be interrupted, that is, stopped from propagating. |
| `public get; Propagating` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns true if the event is still propagating. |
| `public get; ImmediatePropagating` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns true if the event is still immediate propagating. |
| `public get; Parameters` | [RMLEventParameters](./rmleventparameters.md) | The list of parameters provided by the event. This map is only valid during the execution of the event listener callback |


---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) StopPropagation()

Stops propagation of the event if it is interruptible, but finish all listeners on the current element.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) StopImmediatePropagation()

Stops propagation of the event if it is interruptible, including to any other listeners on the current element.

---


---