# WindowResizeCallback

## Summary




## Definition

**Namespace:** `SDT4.Managed.Input`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
sealed class WindowResizeCallback
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Delegate](https://learn.microsoft.com/dotnet/api/system.delegate) ➔ [MulticastDelegate](https://learn.microsoft.com/dotnet/api/system.multicastdelegate) ➔  **WindowResizeCallback**
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

#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Invoke([Vector2f](../sdt4.managed.core/math/vector2f.md) newSize)

**Parameters:**

- `newSize` ([Vector2f](../sdt4.managed.core/math/vector2f.md)): 


---
#### public virtual [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) BeginInvoke([Vector2f](../sdt4.managed.core/math/vector2f.md) newSize, [AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback) callback, [Object](https://learn.microsoft.com/dotnet/api/system.object) object)

**Parameters:**

- `newSize` ([Vector2f](../sdt4.managed.core/math/vector2f.md)): 

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