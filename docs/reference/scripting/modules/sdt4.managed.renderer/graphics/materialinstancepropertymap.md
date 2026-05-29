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
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Float2](../../sdt4.managed.core/math/float2.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Float2](../../sdt4.managed.core/math/float2.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Float3](../../sdt4.managed.core/math/float3.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Float3](../../sdt4.managed.core/math/float3.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetParameter([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Float4](../../sdt4.managed.core/math/float4.md) value)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([Float4](../../sdt4.managed.core/math/float4.md)): 


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