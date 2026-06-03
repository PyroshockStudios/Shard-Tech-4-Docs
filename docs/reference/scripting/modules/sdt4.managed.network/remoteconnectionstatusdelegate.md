# RemoteConnectionStatusDelegate

## Summary




## Definition

**Namespace:** `SDT4.Managed.Network`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
sealed class RemoteConnectionStatusDelegate
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Delegate](https://learn.microsoft.com/dotnet/api/system.delegate) ➔ [MulticastDelegate](https://learn.microsoft.com/dotnet/api/system.multicastdelegate) ➔  **RemoteConnectionStatusDelegate**
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

#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Invoke([RemoteConnectionStatus](./remoteconnectionstatus.md) status)

**Parameters:**

- `status` ([RemoteConnectionStatus](./remoteconnectionstatus.md)): 


---
#### public virtual [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) BeginInvoke([RemoteConnectionStatus](./remoteconnectionstatus.md) status, [AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback) callback, [Object](https://learn.microsoft.com/dotnet/api/system.object) object)

**Parameters:**

- `status` ([RemoteConnectionStatus](./remoteconnectionstatus.md)): 

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