# Vector4i

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector4i
```
**Implements:**

##### [IVectorSpatial&lt;Int32&gt;](./ivectorspatial`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector4i&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public y` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public z` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public w` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |

---


## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Vector4i](./vector4i.md) |  |
| `public get; set; Item` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |

---


## Methods

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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Vector4i](./vector4i.md) other)

**Parameters:**

- `other` ([Vector4i](./vector4i.md)): 


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