# MouseScrollEventArgs

## Summary
Provides data for mouse wheel or touchpad scrolling events.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct MouseScrollEventArgs
```
**Implements:**

##### [IEquatable&lt;MouseScrollEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; DeltaX` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The horizontal scroll offset (e.g., tilting the scroll wheel or a two-finger horizontal swipe). |
| `public get; set; DeltaY` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The vertical scroll offset (e.g., rotating the scroll wheel or a two-finger vertical swipe). |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([MouseScrollEventArgs](./mousescrolleventargs.md) other)

**Parameters:**

- `other` ([MouseScrollEventArgs](./mousescrolleventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Double](https://learn.microsoft.com/dotnet/api/system.double) DeltaX, out [Double](https://learn.microsoft.com/dotnet/api/system.double) DeltaY)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `DeltaX` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `DeltaY` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


---


---