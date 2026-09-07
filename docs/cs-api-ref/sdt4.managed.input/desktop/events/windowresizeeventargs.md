# WindowResizeEventArgs

## Summary
Provides data for events fired when the window gets resized.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct WindowResizeEventArgs
```
**Implements:**

##### [IEquatable&lt;WindowResizeEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Window` | [Window](../../../sdt4.managed.windowing/window.md) | The [WindowResizeEventArgs.Window](./windowresizeeventargs.md#window) whose boundaries were crossed by the cursor. |
| `public get; set; Size` | [Vector2i](../../../sdt4.managed.core/math/vector2i.md) | The new window size, after resizing. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([WindowResizeEventArgs](./windowresizeeventargs.md) other)

**Parameters:**

- `other` ([WindowResizeEventArgs](./windowresizeeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Window](../../../sdt4.managed.windowing/window.md) Window, out [Vector2i](../../../sdt4.managed.core/math/vector2i.md) Size)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Window` ([Window](../../../sdt4.managed.windowing/window.md)): 

- `Size` ([Vector2i](../../../sdt4.managed.core/math/vector2i.md)): 


---


---