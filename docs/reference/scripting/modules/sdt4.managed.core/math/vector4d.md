# Vector4d

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector4d
```
**Implements:**

##### [IVectorSpatial&lt;Double&gt;](./ivectorspatial`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |

---


## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; x` | [Double](https://learn.microsoft.com/dotnet/api/system.double) |  |
| `public get; y` | [Double](https://learn.microsoft.com/dotnet/api/system.double) |  |
| `public get; z` | [Double](https://learn.microsoft.com/dotnet/api/system.double) |  |
| `public get; w` | [Double](https://learn.microsoft.com/dotnet/api/system.double) |  |
| `public get; Item` | [Double](https://learn.microsoft.com/dotnet/api/system.double) |  |

---


## Methods

#### public [Double](https://learn.microsoft.com/dotnet/api/system.double) Length()

**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

##### Summary
In format of (x, y, z, w)

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


---