# ViewportRenderInstance

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
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
| `public get; set; RenderCanvas` | [RenderCanvas](../graphics/rendercanvas.md) | The render canvas attached to this viewport. This will throw an [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception) if [ViewportRenderInstance.OwnsCanvas](./viewportrenderinstance.md#ownscanvas) is false. |
| `public get; OwnsCanvas` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Denotes if the render canvas is owned by the viewport or not. If this is NOT owned by this viewport, the [ViewportRenderInstance.RenderCanvas](./viewportrenderinstance.md#rendercanvas) is invalid |



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
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetRenderArea([Vector2i](../../sdt4.managed.core/math/vector2i.md) extent, [Vector2i](../../sdt4.managed.core/math/vector2i.md) offset)


**Summary:**
Sets the render extent of the viewport on the canvas.

**Remarks:**
Invalid regions get clamped.

**Parameters:**

- `extent` ([Vector2i](../../sdt4.managed.core/math/vector2i.md)): 

- `offset` ([Vector2i](../../sdt4.managed.core/math/vector2i.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---