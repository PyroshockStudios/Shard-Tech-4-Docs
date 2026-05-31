# Vector3f



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Vector3f
```
**Implements:**

##### [IVectorSpacial&lt;Single&gt;](./ivectorspacial`1.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Vector3f&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |


---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; x` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; y` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; z` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |


---

## Methods

#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Length()

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

In format of (x, y, z)

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