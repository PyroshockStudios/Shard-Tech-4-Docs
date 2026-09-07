# WindowInput

## Summary
Provides window-specific and static global input handling for desktop platforms,
including event-based callbacks and polling mechanisms for keyboard, mouse, and window state changes.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Input.Desktop`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
sealed class WindowInput
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **WindowInput**
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

#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsKeyDown([KeyCode](./keycode.md) keyInput)


**Summary:**
Queries the native backend to determine whether the specified keyboard key is currently held down.

**Parameters:**

- `keyInput` ([KeyCode](./keycode.md)): The key code to poll.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the key is currently down; otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsMouseButtonDown([MouseButton](./mousebutton.md) mouseInput)


**Summary:**
Queries the native backend to determine whether the specified mouse button is currently held down.

**Parameters:**

- `mouseInput` ([MouseButton](./mousebutton.md)): The mouse button to poll.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the button is currently down; otherwise, <see langword="false" />.

---
#### public static [Vector2i](../../sdt4.managed.core/math/vector2i.md) GetMousePosition()


**Summary:**
Retrieves the current screen/window coordinate of the mouse cursor from the native backend.

**Returns:**

- [Vector2i](../../sdt4.managed.core/math/vector2i.md): A [Vector2i](../../sdt4.managed.core/math/vector2i.md) containing the cursor's current X and Y coordinates.

---
#### public static [Vector2i](../../sdt4.managed.core/math/vector2i.md) GetMouseDelta()


**Summary:**
Retrieves the last mouse delta that occurred.

**Returns:**

- [Vector2i](../../sdt4.managed.core/math/vector2i.md): A [Vector2i](../../sdt4.managed.core/math/vector2i.md) containing the cursor's delta X and Y coordinates.

---


---