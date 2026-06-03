# Matrix3x3f

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Matrix3x3f
```
**Implements:**

##### [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public x` | [Vector3f](./vector3f.md) |  |
| `public y` | [Vector3f](./vector3f.md) |  |
| `public z` | [Vector3f](./vector3f.md) |  |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Item` | [Vector3f](./vector3f.md) |  |



---

## Methods

#### public [Matrix3x3f](./matrix3x3f.md) Transpose()

**Returns:**

- [Matrix3x3f](./matrix3x3f.md): 

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
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetObjectData([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) info, [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) context)

**Parameters:**

- `info` ([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)): 

- `context` ([StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)): 


---


---