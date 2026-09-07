# MouseButtonEventArgs

## Summary
Provides data for mouse button press and release events.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct MouseButtonEventArgs
```
**Implements:**

##### [IEquatable&lt;MouseButtonEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Button` | [MouseButton](../mousebutton.md) | The specific mouse button that triggered the event. |
| `public get; set; Modifiers` | [InputModifiers](../inputmodifiers.md) | Bitfield flags indicating the state of keyboard modifier keys when the mouse action occurred. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([MouseButtonEventArgs](./mousebuttoneventargs.md) other)

**Parameters:**

- `other` ([MouseButtonEventArgs](./mousebuttoneventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [MouseButton](../mousebutton.md) Button, out [InputModifiers](../inputmodifiers.md) Modifiers)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Button` ([MouseButton](../mousebutton.md)): 

- `Modifiers` ([InputModifiers](../inputmodifiers.md)): 


---


---