# RendererPlatform

## Summary




## Definition

**Namespace:** `SDT4.Managed.Renderer`  
**Assembly:** `SDT4.Managed.Renderer.dll`

```csharp
sealed class RendererPlatform
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RendererPlatform**
**Implements:**

##### [IRenderingCapability](../sdt4.managed.core/capabilities/irenderingcapability.md), [ICapability](../sdt4.managed.core/capabilities/icapability.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Rhi` | [IRhiBackend](./irhibackend.md) |  |



---

## Methods

#### public [RenderCanvas](./graphics/rendercanvas.md) CreateWindowRenderCanvas([Window](../sdt4.managed.windowing/window.md) window)


**Summary:**
Creates a new render canvas associated with the window

**Remarks:**
!!! warning
    If `window` already has a scene render instance, the existing [RenderCanvas](./graphics/rendercanvas.md) is invalidated!

**Parameters:**

- `window` ([Window](../sdt4.managed.windowing/window.md)): 


**Returns:**

- [RenderCanvas](./graphics/rendercanvas.md): 

---
#### public [SceneRenderInstance](./xrp/scenerenderinstance.md) CreateSceneRenderer([Scene](../sdt4.managed.core/scene.md) scene)


**Summary:**
Creates a new render instance that allows rendering the scene. Only <strong>ONE</strong> is allowed be created per scene.

**Remarks:**
If `scene` already has a scene render instance, an [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception) is thrown.

**Parameters:**

- `scene` ([Scene](../sdt4.managed.core/scene.md)): Scene to base the render instance


**Returns:**

- [SceneRenderInstance](./xrp/scenerenderinstance.md): A new render instance for the scene.

---
#### public [MaterialInstance?](./graphics/materialinstance.md) CreateMaterialInstance([IMaterialAsset](../sdt4.managed.core/asset/imaterialasset.md) material)


**Summary:**
Creates a material instance

**Parameters:**

- `material` ([IMaterialAsset](../sdt4.managed.core/asset/imaterialasset.md)): Material to create an instance out of


**Returns:**

- [MaterialInstance?](./graphics/materialinstance.md): A new material instance based on `material`. If the renderer failed to allocate an instance, it will return null.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DestroyMaterialInstance([MaterialInstance](./graphics/materialinstance.md) instance)


**Summary:**
Releases a material instance

**Parameters:**

- `instance` ([MaterialInstance](./graphics/materialinstance.md)): Instance to free


---


---