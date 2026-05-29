# GamepadConnectionStateDelegate



## Definition

**Namespace:** `SDT4.Managed.Input`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
sealed class GamepadConnectionStateDelegate
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Delegate](https://learn.microsoft.com/dotnet/api/system.delegate) ➔ [MulticastDelegate](https://learn.microsoft.com/dotnet/api/system.multicastdelegate) ➔  **GamepadConnectionStateDelegate**
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

#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Invoke([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) firstConnection, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex)

**Parameters:**

- `firstConnection` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public virtual [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) BeginInvoke([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) firstConnection, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex, [AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback) callback, [Object](https://learn.microsoft.com/dotnet/api/system.object) object)

**Parameters:**

- `firstConnection` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

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