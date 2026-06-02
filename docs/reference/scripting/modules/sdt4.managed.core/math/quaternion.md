# Quaternion

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Quaternion
```
**Implements:**

##### [IVectorSpatial&lt;Single&gt;](./ivectorspatial`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Quaternion&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public w` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public x` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public y` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public z` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |

---


## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public static get; Identity` | [Quaternion](./quaternion.md) |  |

---


## Methods

#### public [Quaternion](./quaternion.md) Conjugate()

**Returns:**

- [Quaternion](./quaternion.md): 

---
#### public [Quaternion](./quaternion.md) Inverse()

**Returns:**

- [Quaternion](./quaternion.md): 

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Length()

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Dot([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b)

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): 

- `b` ([Quaternion](./quaternion.md)): 


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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Quaternion](./quaternion.md) other)

**Parameters:**

- `other` ([Quaternion](./quaternion.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---