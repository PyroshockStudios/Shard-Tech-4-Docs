# ViewportRenderInstance

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Thread.RunLater](../../sdt4.managed.core/thread.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Renderer.XRP`  
**Assembly:** `SDT4.Managed.Renderer.dll`

```csharp
sealed class ViewportRenderInstance
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **ViewportRenderInstance**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IRenderCanvasAttacher](../graphics/irendercanvasattacher.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; RenderCanvas` | [RenderCanvas](../graphics/rendercanvas.md) |  |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetCameraActor([Actor](../../sdt4.managed.core/actor.md) actor)


**Summary:**
Attaches the camera of an actor to this render instance

**Remarks:**
If `actor` is not owned by the scene render instance that provided

**Parameters:**

- `actor` ([Actor](../../sdt4.managed.core/actor.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetViewport([Vector2f](../../sdt4.managed.core/math/vector2f.md) extent, [Vector2f](../../sdt4.managed.core/math/vector2f.md) offset)


**Summary:**
Sets the render extent of the viewport on the canvas.

**Remarks:**
Invalid regions get clamped.

**Parameters:**

- `extent` ([Vector2f](../../sdt4.managed.core/math/vector2f.md)): 

- `offset` ([Vector2f](../../sdt4.managed.core/math/vector2f.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---


---