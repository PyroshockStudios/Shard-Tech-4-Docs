# WindowFocusChangeEventArgs

## Summary
Provides data for window input focus gain or loss events.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct WindowFocusChangeEventArgs
```
**Implements:**

##### [IEquatable&lt;WindowFocusChangeEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Window` | [Window](../../../sdt4.managed.windowing/window.md) | The [WindowFocusChangeEventArgs.Window](./windowfocuschangeeventargs.md#window) whose focus state has changed. |
| `public get; set; Focused` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | <see langword="true" /> if the window gained input focus; <see langword="false" /> if it lost focus. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([WindowFocusChangeEventArgs](./windowfocuschangeeventargs.md) other)

**Parameters:**

- `other` ([WindowFocusChangeEventArgs](./windowfocuschangeeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Window](../../../sdt4.managed.windowing/window.md) Window, out [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Focused)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Window` ([Window](../../../sdt4.managed.windowing/window.md)): 

- `Focused` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---


---