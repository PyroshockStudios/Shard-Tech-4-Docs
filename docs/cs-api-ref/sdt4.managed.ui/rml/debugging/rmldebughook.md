# RmlDebugHook

## Summary
The class for specifying debug overlays

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml.Debugging`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
static class RmlDebugHook
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RmlDebugHook**
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
| `public static get; IsActive` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Returns if the debug hook is active. |



---

## Methods

#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) AttachHook([ViewportRenderInstance](../../../sdt4.managed.renderer/xrp/viewportrenderinstance.md) viewport)


**Summary:**
Attaches this debug overlay hook permanently. This can only be called from a standalone runtime. 

**Remarks:**
!!! note
    When running a scene via the embedded view in the editor, the debug hook is persistently attached,
    and will always throw [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)

!!! important
    The debug hook can only be attached once, once it is attached, it can no longer be attached.
    Make sure to attach this to a valid viewport render instance that never goes out of scope!

**Parameters:**

- `viewport` ([ViewportRenderInstance](../../../sdt4.managed.renderer/xrp/viewportrenderinstance.md)): The viewport to attach this render instance to. This must have a window associated with it.


---


---