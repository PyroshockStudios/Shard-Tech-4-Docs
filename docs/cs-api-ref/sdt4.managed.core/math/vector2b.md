# Vector2b

## Summary
Represents a 2D boolean vector supporting component-wise logical operations.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector2b
```
**Implements:**

##### [IVectorComparable&lt;Vector2b&gt;](./ivectorcomparable`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector2b&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | The X boolean component. |
| `public y` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | The Y boolean component. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; False` | [Vector2b](./vector2b.md) | Gets a vector with all components set to <see langword="false" />. |
| `public static get; True` | [Vector2b](./vector2b.md) | Gets a vector with all components set to <see langword="true" />. |
| `public get; set; Item` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets or sets the boolean component at the specified zero-based index. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) All()


**Summary:**
Determines whether all components evaluate to <see langword="true" />.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if both X and Y are <see langword="true" />; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Any()


**Summary:**
Determines whether any component evaluates to <see langword="true" />.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if at least one component is <see langword="true" />; otherwise, <see langword="false" />.

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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector2b](./vector2b.md) other)


**Summary:**
Determines whether the specified vector is equal to the current vector.

**Parameters:**

- `other` ([Vector2b](./vector2b.md)): 


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