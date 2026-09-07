# RendererPlatform

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

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
| `public get; BackendInfo` | [RendererBackendInfo](./rendererbackendinfo.md) |  |



---

## Methods

#### public [RenderCanvas](./graphics/rendercanvas.md) CreateWindowRenderCanvas([Window](../sdt4.managed.windowing/window.md) window, [DisplaySyncMode](./graphics/displaysyncmode.md) syncMode, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) bufferCount)


**Summary:**
Creates a new render canvas associated with the window

**Remarks:**
!!! warning
    If `window` already has a [RenderCanvas](./graphics/rendercanvas.md), it is invalidated!

**Parameters:**

- `window` ([Window](../sdt4.managed.windowing/window.md)): The window to create a render canvas out of.

- `syncMode` ([DisplaySyncMode](./graphics/displaysyncmode.md)): The vertical synchronisation policy of this window render canvas.

- `bufferCount` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): How many swap chain back buffers to create. This parameter is a hint and may be


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
#### public [MaterialInstance?](./graphics/materialinstance.md) CreateMaterialInstance([MaterialAsset](../sdt4.managed.core/asset/materialasset.md) material)


**Summary:**
Creates a material instance

**Parameters:**

- `material` ([MaterialAsset](../sdt4.managed.core/asset/materialasset.md)): Material to create an instance out of


**Returns:**

- [MaterialInstance?](./graphics/materialinstance.md): A new material instance based on `material`. If the renderer failed to allocate an instance, it will return null.

---


---