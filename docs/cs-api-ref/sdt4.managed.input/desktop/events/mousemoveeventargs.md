# MouseMoveEventArgs

## Summary
Provides data for mouse motion events, including absolute coordinates and frame-to-frame movement delta.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct MouseMoveEventArgs
```
**Implements:**

##### [IEquatable&lt;MouseMoveEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Window` | [Window](../../../sdt4.managed.windowing/window.md) | The [MouseMoveEventArgs.Window](./mousemoveeventargs.md#window) where this event occurred. |
| `public get; set; Position` | [Vector2i](../../../sdt4.managed.core/math/vector2i.md) | The current cursor position in window client-space coordinates. |
| `public get; set; AbsolutePosition` | [Vector2i](../../../sdt4.managed.core/math/vector2i.md) | The current cursor position in absolute coordinates. |
| `public get; set; Delta` | [Vector2i](../../../sdt4.managed.core/math/vector2i.md) | The relative movement delta since the last recorded mouse event. |



---

## Methods

#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([MouseMoveEventArgs](./mousemoveeventargs.md) other)

**Parameters:**

- `other` ([MouseMoveEventArgs](./mousemoveeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Window](../../../sdt4.managed.windowing/window.md) Window, out [Vector2i](../../../sdt4.managed.core/math/vector2i.md) Position, out [Vector2i](../../../sdt4.managed.core/math/vector2i.md) AbsolutePosition, out [Vector2i](../../../sdt4.managed.core/math/vector2i.md) Delta)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Window` ([Window](../../../sdt4.managed.windowing/window.md)): 

- `Position` ([Vector2i](../../../sdt4.managed.core/math/vector2i.md)): 

- `AbsolutePosition` ([Vector2i](../../../sdt4.managed.core/math/vector2i.md)): 

- `Delta` ([Vector2i](../../../sdt4.managed.core/math/vector2i.md)): 


---


---