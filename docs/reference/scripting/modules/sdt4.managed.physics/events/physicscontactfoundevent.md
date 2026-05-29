# PhysicsContactFoundEvent



## Definition

**Namespace:** `SDT4.Managed.Physics.Events`  
**Assembly:** `SDT4.Managed.Physics.dll`

```csharp
sealed class PhysicsContactFoundEvent
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Delegate](https://learn.microsoft.com/dotnet/api/system.delegate) ➔ [MulticastDelegate](https://learn.microsoft.com/dotnet/api/system.multicastdelegate) ➔  **PhysicsContactFoundEvent**
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

#### public virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Invoke([Actor](../../sdt4.managed.core/actor.md) other, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) shapeIndex, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) otherShapeIndex, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) persists, [PhysicsContactPatch[]](../physicscontactpatch.md) patches)

**Parameters:**

- `other` ([Actor](../../sdt4.managed.core/actor.md)): 

- `shapeIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `otherShapeIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `persists` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `patches` ([PhysicsContactPatch[]](../physicscontactpatch.md)): 


---
#### public virtual [IAsyncResult](https://learn.microsoft.com/dotnet/api/system.iasyncresult) BeginInvoke([Actor](../../sdt4.managed.core/actor.md) other, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) shapeIndex, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) otherShapeIndex, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) persists, [PhysicsContactPatch[]](../physicscontactpatch.md) patches, [AsyncCallback](https://learn.microsoft.com/dotnet/api/system.asynccallback) callback, [Object](https://learn.microsoft.com/dotnet/api/system.object) object)

**Parameters:**

- `other` ([Actor](../../sdt4.managed.core/actor.md)): 

- `shapeIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `otherShapeIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `persists` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `patches` ([PhysicsContactPatch[]](../physicscontactpatch.md)): 

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