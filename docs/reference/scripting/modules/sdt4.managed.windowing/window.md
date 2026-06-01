# Window

## Summary




## Definition

**Namespace:** `SDT4.Managed.Windowing`  
**Assembly:** `SDT4.Managed.Windowing.dll`

```csharp
sealed class Window
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Window**
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
| `public get; NativeWindow` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) |  |
| `public get; WindowMonitor` | [Monitor](./monitor.md) | The monitor that the window resides in.  This is <strong>NULL</strong> if the window is not in fullscreen mode! |
| `public get; set; Size` | [Vector2f](../sdt4.managed.core/math/vector2f.md) | Size of the window in pixels |
| `public get; FramebufferSize` | [Vector2f](../sdt4.managed.core/math/vector2f.md) | The renderable framebuffer region of the window in pixels |
| `public get; set; Position` | [Vector2f](../sdt4.managed.core/math/vector2f.md) | Position of the window relative to the workspace |
| `public get; set; Borderless` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | If the window has the title bar visible or not. |
| `public get; set; Resizable` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | If the window has the title bar visible or not. |

---
##### `Size` Remarks
!!! warning
    Do not use <see cref="P:SDT4.Managed.Windowing.Window.Size" /> for determining the size of the renderable region. 
    Use <see cref="P:SDT4.Managed.Windowing.Window.FramebufferSize" /> to determine appropriate renderable regions for render targets.



## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Maximize()

##### Summary
Maximises the window

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Minimize()

##### Summary
Minimises the window

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Restore()

##### Summary
Restores the window after minimisation.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Close()

##### Summary
Closes window immediately

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetMonitor([Monitor?](./monitor.md) monitor, [VideoMode](./videomode.md) mode)

##### Summary
Sets the <em>fullscreen</em> display monitor with the specified window mode. If monitor is <strong>NULL</strong> then it will revert to windowed mode.

**Parameters:**

- `monitor` ([Monitor?](./monitor.md)): The monitor to place the window in fullscreen, null if revert to windowed.

- `mode` ([VideoMode](./videomode.md)): Closest video mode to choose. Colour bits are ignored, and refresh rate is only applicable in fullscreen mode


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---


---