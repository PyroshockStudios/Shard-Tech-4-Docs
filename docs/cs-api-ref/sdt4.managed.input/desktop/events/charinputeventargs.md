# CharInputEventArgs

## Summary
Provides data for text input events containing a decoded Unicode character.



## Definition

**Namespace:** `SDT4.Managed.Input.Desktop.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct CharInputEventArgs
```
**Implements:**

##### [IEquatable&lt;CharInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event (typically a <c>WindowInput</c> instance or <see langword="null" />). |
| `public get; set; Unicode` | [Rune](https://learn.microsoft.com/dotnet/api/system.text.rune) | The 32-bit Unicode scalar value ([Rune](https://learn.microsoft.com/dotnet/api/system.text.rune)) entered by the user. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([CharInputEventArgs](./charinputeventargs.md) other)

**Parameters:**

- `other` ([CharInputEventArgs](./charinputeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Rune](https://learn.microsoft.com/dotnet/api/system.text.rune) Unicode)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `Unicode` ([Rune](https://learn.microsoft.com/dotnet/api/system.text.rune)): 


---


---