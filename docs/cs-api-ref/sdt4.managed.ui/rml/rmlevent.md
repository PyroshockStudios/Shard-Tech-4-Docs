# RmlEvent

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.
!!! important
    The event object is ONLY valid during events. Otherwise, any access will result in a [ObjectDisposedException](https://learn.microsoft.com/dotnet/api/system.objectdisposedexception)

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RmlEvent
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RmlEvent**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Type` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Get the event type. |
| `public get; set; CurrentTarget` | [RmlElement?](./rmlelement.md) | Get/Set the current element in the propagation. |
| `public get; Target` | [RmlElement](./rmlelement.md) | The original target of the event |
| `public get; EventPhase` | [RmlEventPhase](./rmleventphase.md) | Indicates which phase of the event flow is being processed. |
| `public get; Interruptible` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns true if the event can be interrupted, that is, stopped from propagating. |
| `public get; Propagating` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns true if the event is still propagating. |
| `public get; ImmediatePropagating` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns true if the event is still immediate propagating. |
| `public get; Parameters` | [RmlEventParameters](./rmleventparameters.md) | The list of parameters provided by the event. This map is only valid during the execution of the event listener callback |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) StopPropagation()


**Summary:**
Stops propagation of the event if it is interruptible, but finish all listeners on the current element.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) StopImmediatePropagation()


**Summary:**
Stops propagation of the event if it is interruptible, including to any other listeners on the current element.

---
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
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---


---