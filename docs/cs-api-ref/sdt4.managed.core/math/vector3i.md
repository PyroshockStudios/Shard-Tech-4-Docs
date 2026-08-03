# Vector3i

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector3i
```
**Implements:**

##### [IVectorSpatial&lt;Int32&gt;](./ivectorspatial`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector3i&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public y` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public z` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Vector3i](./vector3i.md) |  |
| `public get; set; Item` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyToValuePtr([Int32*](https://learn.microsoft.com/dotnet/api/system.int32*) valuePtr)


**Summary:**
Copies the vector values into a scalar value pointer.

**Parameters:**

- `valuePtr` ([Int32*](https://learn.microsoft.com/dotnet/api/system.int32*)): Destination value pointer. Must be large enough to contain the values.


---
#### public [Int32](https://learn.microsoft.com/dotnet/api/system.int32) Length()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector3i](./vector3i.md) other)

**Parameters:**

- `other` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetObjectData([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) info, [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) context)

**Parameters:**

- `info` ([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)): 

- `context` ([StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)): 


---


---