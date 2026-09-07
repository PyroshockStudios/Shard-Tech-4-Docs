# WindowDropEventArgs

## Summary
Provides data for external drag-and-drop operations onto a window surface.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct WindowDropEventArgs
```
**Implements:**

##### [IEquatable&lt;WindowDropEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Window` | [Window](../../../sdt4.managed.windowing/window.md) | The [WindowDropEventArgs.Window](./windowdropeventargs.md#window) on which the external items were dropped. |
| `public get; set; DroppedPaths` | [String[]](https://learn.microsoft.com/dotnet/api/system.string) | An array of absolute file system paths representing the dropped files or directories. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([WindowDropEventArgs](./windowdropeventargs.md) other)

**Parameters:**

- `other` ([WindowDropEventArgs](./windowdropeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Window](../../../sdt4.managed.windowing/window.md) Window, out [String[]](https://learn.microsoft.com/dotnet/api/system.string) DroppedPaths)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Window` ([Window](../../../sdt4.managed.windowing/window.md)): 

- `DroppedPaths` ([String[]](https://learn.microsoft.com/dotnet/api/system.string)): 


---


---