# WindowExtensions

## Summary




## Definition

**Namespace:** `SDT4.Managed.Input`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
static class WindowExtensions
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **WindowExtensions**
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

---


## Methods

#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) AddWindowResizeCallback([Window](../sdt4.managed.windowing/window.md) window, [WindowResizeCallback](./windowresizecallback.md) resizeCallback)

##### Summary
Registers a callback for whenever the window resizes.

**Parameters:**

- `window` ([Window](../sdt4.managed.windowing/window.md)): 

- `resizeCallback` ([WindowResizeCallback](./windowresizecallback.md)): Delegate function to be called when window resizes.


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveWindowResizeCallback([Window](../sdt4.managed.windowing/window.md) window, [WindowResizeCallback](./windowresizecallback.md) resizeCallback)

##### Summary
Removes a previously registered callback for whenever the window resizes.
If NO such delegate was registered, an <em>IndexOutOfRangeException</em> is thrown.

**Parameters:**

- `window` ([Window](../sdt4.managed.windowing/window.md)): 

- `resizeCallback` ([WindowResizeCallback](./windowresizecallback.md)): Exact delegate that was registered.


---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsKeyDown([Window](../sdt4.managed.windowing/window.md) window, [KeyInput](./keyinput.md) key)

**Parameters:**

- `window` ([Window](../sdt4.managed.windowing/window.md)): 

- `key` ([KeyInput](./keyinput.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsMouseDown([Window](../sdt4.managed.windowing/window.md) window, [MouseInput](./mouseinput.md) mouseBtn)

**Parameters:**

- `window` ([Window](../sdt4.managed.windowing/window.md)): 

- `mouseBtn` ([MouseInput](./mouseinput.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public static [Vector2i](../sdt4.managed.core/math/vector2i.md) GetMousePosition()

**Returns:**

- [Vector2i](../sdt4.managed.core/math/vector2i.md): 

---


---