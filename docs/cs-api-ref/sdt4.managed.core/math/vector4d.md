# Vector4d

## Summary
Represents a 4D double-precision floating-point vector.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector4d
```
**Implements:**

##### [IVectorSpatial&lt;Double, Double, Vector4d, Vector4d&gt;](./ivectorspatial`4.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector4d&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The X component of the vector. |
| `public y` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The Y component of the vector. |
| `public z` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The Z component of the vector. |
| `public w` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The W component of the vector. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Vector4d](./vector4d.md) | Gets a vector with all components set to zero. |
| `public static get; One` | [Vector4d](./vector4d.md) | Gets a vector with all components set to one. |
| `public get; set; Item` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | Gets or sets the component at the specified zero-based index. |
| `public get; IsNormalized` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the vector is normalised to unit length within tolerance. |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyToValuePtr([Double*](https://learn.microsoft.com/dotnet/api/system.double*) valuePtr)


**Summary:**
Copies the vector values into a scalar value pointer.

**Parameters:**

- `valuePtr` ([Double*](https://learn.microsoft.com/dotnet/api/system.double*)): Destination value pointer. Must be large enough to contain the values.


---
#### public [Double](https://learn.microsoft.com/dotnet/api/system.double) LengthSq()


**Summary:**
Calculates the squared magnitude of the vector.

**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public [Double](https://learn.microsoft.com/dotnet/api/system.double) Length()


**Summary:**
Calculates the magnitude of the vector.

**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public [Vector4d](./vector4d.md) Normalized()


**Summary:**
Returns a normalised copy of the vector scaled to unit length.

**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a culture-invariant string representation of the vector.

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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector4d](./vector4d.md) other)


**Summary:**
Determines whether the specified vector is equal to the current vector.

**Parameters:**

- `other` ([Vector4d](./vector4d.md)): 


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