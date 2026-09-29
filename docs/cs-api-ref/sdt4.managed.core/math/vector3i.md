# Vector3i

## Summary
Represents a 3D 32-bit signed integer vector.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector3i
```
**Implements:**

##### [IVectorSpatial&lt;Int32, Single, Vector3i, Vector3f&gt;](./ivectorspatial`4.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector3i&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | The X integer component of the vector. |
| `public y` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | The Y integer component of the vector. |
| `public z` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | The Z integer component of the vector. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Vector3i](./vector3i.md) | Gets a vector with all components set to zero. |
| `public static get; One` | [Vector3i](./vector3i.md) | Gets a vector with all components set to one. |
| `public get; set; Item` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Gets or sets the component at the specified zero-based index. |
| `public get; IsNormalized` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the squared length equals 1. |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyToValuePtr([Int32*](https://learn.microsoft.com/dotnet/api/system.int32*) valuePtr)


**Summary:**
Copies the vector values into a scalar value pointer.

**Parameters:**

- `valuePtr` ([Int32*](https://learn.microsoft.com/dotnet/api/system.int32*)): Destination value pointer. Must be large enough to contain the values.


---
#### public [Int32](https://learn.microsoft.com/dotnet/api/system.int32) LengthSq()


**Summary:**
Calculates the squared magnitude of the vector.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Length()


**Summary:**
Calculates the magnitude of the vector as a single-precision float.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public [Vector3f](./vector3f.md) Normalized()


**Summary:**
Returns a normalised single-precision vector scaled to unit length.

**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a string representation of the vector.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is equal to the current vector.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector3i](./vector3i.md) other)


**Summary:**
Determines whether the specified vector is equal to the current vector.

**Parameters:**

- `other` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this vector.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetObjectData([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) info, [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) context)


**Summary:**
Populates serialisation information with vector component data.

**Parameters:**

- `info` ([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)): 

- `context` ([StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)): 


---


---