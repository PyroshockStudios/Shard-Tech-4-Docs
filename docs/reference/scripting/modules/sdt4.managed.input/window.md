# Window

## Summary




## Definition

**Namespace:** `SDT4.Managed.Input`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
sealed class Window
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Window**
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
| `public static get; WindowMonitor` | [Monitor](./monitor.md) | The monitor that the window resides in.  This is <strong>NULL</strong> if the window is not in fullscreen mode! |
| `public get; set; Resolution` | [Vector2f](../sdt4.managed.core/math/vector2f.md) | Resolution of the window in pixels |
| `public get; set; Position` | [Vector2f](../sdt4.managed.core/math/vector2f.md) | Position of the window relative to the workspace |
| `public get; set; Borderless` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | If the window has the title bar visible or not. |

---


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
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddWindowResizeCallback([WindowResizeCallback](./windowresizecallback.md) resizeCallback)

##### Summary
Registers a callback for whenever the window resizes.

**Parameters:**

- `resizeCallback` ([WindowResizeCallback](./windowresizecallback.md)): Delegate function to be called when window resizes.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveWindowResizeCallback([WindowResizeCallback](./windowresizecallback.md) resizeCallback)

##### Summary
Removes a previously registered callback for whenever the window resizes.
If NO such delegate was registered, an <em>IndexOutOfRangeException</em> is thrown.

**Parameters:**

- `resizeCallback` ([WindowResizeCallback](./windowresizecallback.md)): Exact delegate that was registered.


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsKeyDown([KeyInput](./keyinput.md) key)

**Parameters:**

- `key` ([KeyInput](./keyinput.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsMouseButtonDown([MouseInput](./mouseinput.md) mouseBtn)

**Parameters:**

- `mouseBtn` ([MouseInput](./mouseinput.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Vector2f](../sdt4.managed.core/math/vector2f.md) GetMousePosition()

**Returns:**

- [Vector2f](../sdt4.managed.core/math/vector2f.md): 

---


---