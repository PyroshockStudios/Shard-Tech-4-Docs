# SceneRenderInstance

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
sealed class SceneRenderInstance
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **SceneRenderInstance**
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



---

## Methods

#### public [ViewportRenderInstance](./viewportrenderinstance.md) CreateViewportRenderer([String](https://learn.microsoft.com/dotnet/api/system.string) uniqueName, [RenderCanvas](../graphics/rendercanvas.md) renderCanvas)


**Summary:**
Creates a viewport from a canvas.

**Remarks:**
`uniqueName` <strong>MUST</strong> be unique, otherwise an [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception) is thrown. 
`renderCanvas` <strong>MUST</strong> be valid, otherwise an [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception) is thrown.

**Parameters:**

- `uniqueName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `renderCanvas` ([RenderCanvas](../graphics/rendercanvas.md)): 


**Returns:**

- [ViewportRenderInstance](./viewportrenderinstance.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---


---