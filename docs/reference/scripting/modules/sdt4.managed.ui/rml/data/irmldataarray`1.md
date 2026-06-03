# IRMLDataArray&lt;&gt;

## Summary




## Definition

**Namespace:** `SDT4.Managed.UI.RML.Data`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
interface IRMLDataArray<>
```
**Implements:**

##### [IRMLData](./irmldata.md)
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

#### public [Int32](https://learn.microsoft.com/dotnet/api/system.int32) Size()


**Summary:**
Called by the DOM when it wants to know the size of the array.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): Array size

---
#### public T Get([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index)


**Summary:**
Called by the DOM when it wants to retrieve data at an array.
This may be a scalar variable (such as a [RMLVariant](../rmlvariant.md)) or another structure (like [IRMLDataStruct](./irmldatastruct.md) or [IRMLDataArray](./irmldataarray.md))

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): Index of array


**Returns:**

- T: Boxed variable. If you wish to return a scalar, this must be wrapped in [IRMLDataScalar](./irmldatascalar.md). <seealso cref="T:SDT4.Managed.UI.RML.Data.IRMLDataArray" />

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Set([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index, T value)


**Summary:**
Sets variables for scalar arrays. This function can be disregarded if only non-scalars are accessed through arrays,
unless you want to know that such a variable has been modified. If it's a reference type, it will be accurately modified anyway.
This <strong>MUST</strong> be handled for both [RMLVariant](../rmlvariant.md) and [IRMLDataScalar](./irmldatascalar.md) (due to there being no way to infer the underlying reference type)

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): Index of array

- `value` (T): Value that was sent from RmlUi


---


---