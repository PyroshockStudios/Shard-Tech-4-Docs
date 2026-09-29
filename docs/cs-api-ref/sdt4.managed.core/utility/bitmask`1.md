# Bitmask&lt;&gt;

## Summary
Represents a generic bitmask wrapper over an underlying binary integer type, providing bitwise query and manipulation operations.



## Definition

**Namespace:** `SDT4.Managed.Core.Utility`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Bitmask<>
```
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
| `public static get; Capacity` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Gets the total bit capacity of the underlying integer type. |
| `public get; set; Item` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Indexes into a bit of the mask. Can query, set or clear bits. |
| `public get; NumSetBits` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Gets the number of set bits (population count) in this mask. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) HasBit([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index)


**Summary:**
Determines whether the bit at the specified zero-based index is set.

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based bit position to test.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the bit is set; otherwise, <see langword="false" />.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetBit([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index)


**Summary:**
Sets the bit at the specified zero-based index to 1.

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based bit position to set.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) ClearBit([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index)


**Summary:**
Clears the bit at the specified zero-based index to 0.

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based bit position to clear.


---


---