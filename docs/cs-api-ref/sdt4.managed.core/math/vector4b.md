# Vector4b

## Summary
Represents a 4D boolean vector supporting component-wise logical operations.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector4b
```
**Implements:**

##### [IVectorComparable&lt;Vector4b&gt;](./ivectorcomparable`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector4b&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | The X boolean component. |
| `public y` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | The Y boolean component. |
| `public z` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | The Z boolean component. |
| `public w` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | The W boolean component. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; False` | [Vector4b](./vector4b.md) | Gets a vector with all components set to <see langword="false" />. |
| `public static get; True` | [Vector4b](./vector4b.md) | Gets a vector with all components set to <see langword="true" />. |
| `public get; set; Item` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets or sets the component at the specified zero-based index. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) All()


**Summary:**
Determines whether all components evaluate to <see langword="true" />.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Any()


**Summary:**
Determines whether any component evaluates to <see langword="true" />.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector4b](./vector4b.md) other)


**Summary:**
Determines whether the specified vector is equal to the current vector.

**Parameters:**

- `other` ([Vector4b](./vector4b.md)): 


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