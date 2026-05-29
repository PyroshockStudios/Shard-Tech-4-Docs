# Mesh3DComponentExtensions



## Definition

**Namespace:** `SDT4.Managed.Renderer.Extensions`  
**Assembly:** `SDT4.Managed.Renderer.dll`

```csharp
static class Mesh3DComponentExtensions
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Mesh3DComponentExtensions**
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


---

## Methods

#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) BindMaterialInstance([Mesh3DComponent](../../sdt4.managed.core/components/mesh3dcomponent.md) component, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) slot, [MaterialInstance](../graphics/materialinstance.md) instance)

Binds the given material instance to this mesh.

**Parameters:**

- `component` ([Mesh3DComponent](../../sdt4.managed.core/components/mesh3dcomponent.md)): 

- `slot` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): index to bind

- `instance` ([MaterialInstance](../graphics/materialinstance.md)): material instance to bind


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): True if binding succeeded. If the engine runs out of available slots, it will return false.

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindMaterialInstance([Mesh3DComponent](../../sdt4.managed.core/components/mesh3dcomponent.md) component, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) slot)

Unbinds the material instance from this slot

**Parameters:**

- `component` ([Mesh3DComponent](../../sdt4.managed.core/components/mesh3dcomponent.md)): 

- `slot` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): index to remove the bound material instance


---


---