# RenderCanvas

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.
!!! important
    This class <strong>MUST</strong> be disposed manually.

## Definition

**Namespace:** `SDT4.Managed.Renderer.Graphics`  
**Assembly:** `SDT4.Managed.Renderer.dll`

```csharp
sealed class RenderCanvas
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RenderCanvas**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; IsValid` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | States if the render canvas is valid. Possible cases where the render canvas is invalid  includes if the object has been disposed, or if this is owned by a window and it has been resized. |
| `public get; IsAttached` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | States if the canvas is at least used by 1 IRenderCanvasAttacher; |
| `public get; SwapChainWindow` | [Window](../../sdt4.managed.windowing/window.md) | The window that defines this render canvas, if defined by a window. |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---
#### public virtual [String?](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String?](https://learn.microsoft.com/dotnet/api/system.string): 

---


---