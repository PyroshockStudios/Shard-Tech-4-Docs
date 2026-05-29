# RmlEventListener

Event listener

## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RmlEventListener
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Delegate](https://learn.microsoft.com/dotnet/api/system.delegate) ➔ [MulticastDelegate](https://learn.microsoft.com/dotnet/api/system.multicastdelegate) ➔  **RmlEventListener**
**Implements:**

##### [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)
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

#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Invoke([RMLEvent](./rmlevent.md) event)

**Parameters:**

- `event` ([RMLEvent](./rmlevent.md)): 


---
#### public virtual [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) BeginInvoke([RMLEvent](./rmlevent.md) event, [AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback) callback, [Object](https://learn.microsoft.com/dotnet/api/system.object) object)

**Parameters:**

- `event` ([RMLEvent](./rmlevent.md)): 

- `callback` ([AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback)): 

- `object` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult): 

---
#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) EndInvoke([IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) result)

**Parameters:**

- `result` ([IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult)): 


---


---