# Window

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the same thread the window was created.
    The default window provided by the engine is created on the master thread.
    
!!! important
    This class <strong>MUST</strong> be disposed manually.

## Definition

**Namespace:** `SDT4.Managed.Windowing`  
**Assembly:** `SDT4.Managed.Windowing.dll`

```csharp
sealed class Window
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Window**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IDisposeTracker&lt;Window&gt;](../sdt4.managed.core/utility/idisposetracker`1.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; InternalWindowPtr` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) |  |
| `public get; WindowMonitor` | [Monitor](./monitor.md) | The monitor that the window resides in.  This is <strong>NULL</strong> if the window is not in fullscreen mode! |
| `public get; set; Size` | [Vector2i](../sdt4.managed.core/math/vector2i.md) | Size of the window in pixels |
| `public get; FramebufferSize` | [Vector2i](../sdt4.managed.core/math/vector2i.md) | The renderable framebuffer region of the window in pixels |
| `public get; set; Position` | [Vector2i](../sdt4.managed.core/math/vector2i.md) | Position of the window relative to the workspace |
| `public get; set; Borderless` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | If the window has the title bar visible or not. |
| `public get; set; Resizable` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | If the window has the title bar visible or not. |


##### `Size` Remarks
!!! warning
    Do not use [Window.Size](./window.md#size) for determining the size of the renderable region. 
    Use [Window.FramebufferSize](./window.md#framebuffersize) to determine appropriate renderable regions for render targets.


---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Maximize()


**Summary:**
Maximises the window

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Minimize()


**Summary:**
Minimises the window

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Restore()


**Summary:**
Restores the window after minimisation.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Close()


**Summary:**
Closes window immediately

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetMonitor([Monitor?](./monitor.md) monitor, [VideoMode](./videomode.md) mode)


**Summary:**
Sets the <em>fullscreen</em> display monitor with the specified window mode. If monitor is <strong>NULL</strong> then it will revert to windowed mode.

**Parameters:**

- `monitor` ([Monitor?](./monitor.md)): The monitor to place the window in fullscreen, null if revert to windowed.

- `mode` ([VideoMode](./videomode.md)): Closest video mode to choose. Colour bits are ignored, and refresh rate is only applicable in fullscreen mode


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---