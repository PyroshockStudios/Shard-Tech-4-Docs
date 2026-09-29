# Vector4f

## Summary
Represents a 4D single-precision floating-point vector.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector4f
```
**Implements:**

##### [IVectorSpatial&lt;Single, Single, Vector4f, Vector4f&gt;](./ivectorspatial`4.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector4f&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The X component of the vector. |
| `public y` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The Y component of the vector. |
| `public z` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The Z component of the vector. |
| `public w` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The W component of the vector. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Vector4f](./vector4f.md) | Gets a vector with all components set to zero. |
| `public static get; One` | [Vector4f](./vector4f.md) | Gets a vector with all components set to one. |
| `public get; set; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the component at the specified zero-based index. |
| `public get; IsNormalized` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the vector is normalised to unit length within tolerance. |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyToValuePtr([Single*](https://learn.microsoft.com/dotnet/api/system.single*) valuePtr)


**Summary:**
Copies the vector values into a scalar value pointer.

**Parameters:**

- `valuePtr` ([Single*](https://learn.microsoft.com/dotnet/api/system.single*)): Destination value pointer. Must be large enough to contain the values.


---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) LengthSq()


**Summary:**
Calculates the squared magnitude of the vector.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Length()


**Summary:**
Calculates the magnitude of the vector.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public [Vector4f](./vector4f.md) Normalized()


**Summary:**
Returns a normalised copy of the vector scaled to unit length.

**Returns:**

- [Vector4f](./vector4f.md): 

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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector4f](./vector4f.md) other)


**Summary:**
Determines whether the specified vector is equal to the current vector.

**Parameters:**

- `other` ([Vector4f](./vector4f.md)): 


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