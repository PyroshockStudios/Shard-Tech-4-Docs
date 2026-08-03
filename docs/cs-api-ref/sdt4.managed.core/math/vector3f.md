# Vector3f

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector3f
```
**Implements:**

##### [IVectorSpatial&lt;Single&gt;](./ivectorspatial`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector3f&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public y` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public z` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Vector3f](./vector3f.md) |  |
| `public get; set; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyToValuePtr([Single*](https://learn.microsoft.com/dotnet/api/system.single*) valuePtr)


**Summary:**
Copies the vector values into a scalar value pointer.

**Parameters:**

- `valuePtr` ([Single*](https://learn.microsoft.com/dotnet/api/system.single*)): Destination value pointer. Must be large enough to contain the values.


---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Length()

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

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
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetObjectData([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) info, [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) context)

**Parameters:**

- `info` ([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)): 

- `context` ([StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)): 


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector3f](./vector3f.md) other)

**Parameters:**

- `other` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---