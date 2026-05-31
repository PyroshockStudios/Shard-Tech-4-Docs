# PacketListenerDelegate



## Definition

**Namespace:** `SDT4.Managed.Network`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
sealed class PacketListenerDelegate
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Delegate](https://learn.microsoft.com/dotnet/api/system.delegate) ➔ [MulticastDelegate](https://learn.microsoft.com/dotnet/api/system.multicastdelegate) ➔  **PacketListenerDelegate**
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

#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Invoke([IRemoteConnection](./iremoteconnection.md) connection, [IEnumerable&lt;Byte&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) bytes)

**Parameters:**

- `connection` ([IRemoteConnection](./iremoteconnection.md)): 

- `bytes` ([IEnumerable&lt;Byte&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)): 


---
#### public virtual [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) BeginInvoke([IRemoteConnection](./iremoteconnection.md) connection, [IEnumerable&lt;Byte&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) bytes, [AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback) callback, [Object](https://learn.microsoft.com/dotnet/api/system.object) object)

**Parameters:**

- `connection` ([IRemoteConnection](./iremoteconnection.md)): 

- `bytes` ([IEnumerable&lt;Byte&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)): 

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