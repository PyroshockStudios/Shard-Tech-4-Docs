# WindowCursorEnterEventArgs

## Summary
Provides data for events fired when the mouse cursor enters or leaves the window client area.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct WindowCursorEnterEventArgs
```
**Implements:**

##### [IEquatable&lt;WindowCursorEnterEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Window` | [Window](../../../sdt4.managed.windowing/window.md) | The [WindowCursorEnterEventArgs.Window](./windowcursorentereventargs.md#window) whose boundaries were crossed by the cursor. |
| `public get; set; Entered` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | <see langword="true" /> if the cursor entered the window; <see langword="false" /> if it exited. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([WindowCursorEnterEventArgs](./windowcursorentereventargs.md) other)

**Parameters:**

- `other` ([WindowCursorEnterEventArgs](./windowcursorentereventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Window](../../../sdt4.managed.windowing/window.md) Window, out [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Entered)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Window` ([Window](../../../sdt4.managed.windowing/window.md)): 

- `Entered` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---


---