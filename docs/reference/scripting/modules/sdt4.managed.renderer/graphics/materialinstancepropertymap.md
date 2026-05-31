# MaterialInstancePropertyMap



## Definition

**Namespace:** `SDT4.Managed.Renderer.Graphics`  
**Assembly:** `SDT4.Managed.Renderer.dll`

```csharp
sealed class MaterialInstancePropertyMap
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **MaterialInstancePropertyMap**
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |


---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Item` | [MaterialInstanceProperty](./materialinstanceproperty.md) |  |
| `public set; Item` | [ITexture2D](../../sdt4.managed.core/asset/itexture2d.md) |  |


---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Single](https://learn.microsoft.com/dotnet/api/system.single) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Vector2f](../../sdt4.managed.core/math/vector2f.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Vector2f](../../sdt4.managed.core/math/vector2f.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Vector3f](../../sdt4.managed.core/math/vector3f.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Vector3f](../../sdt4.managed.core/math/vector3f.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Vector4f](../../sdt4.managed.core/math/vector4f.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Vector4f](../../sdt4.managed.core/math/vector4f.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [UInt32](https://learn.microsoft.com/dotnet/api/system.uint32) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([UInt32](https://learn.microsoft.com/dotnet/api/system.uint32)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [ITexture2D](../../sdt4.managed.core/asset/itexture2d.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([ITexture2D](../../sdt4.managed.core/asset/itexture2d.md)): 


---
#### public [IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) QueryProperties()

**Returns:**

- [IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---