# IRmlDataScalar

## Summary
A scalar data variable, that manages untyped variables.



## Definition

**Namespace:** `SDT4.Managed.UI.Rml.Data`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
interface IRmlDataScalar
```
**Implements:**

##### [IRmlData](./irmldata.md)
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

#### public [RmlVariant](../rmlvariant.md) Get()


**Summary:**
Called by the DOM when the value is accessed.

**Returns:**

- [RmlVariant](../rmlvariant.md): Value that can be read in the DOM. Return <c>[RmlVariant](../rmlvariant.md).Empty</c> if this should not be accessed.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Set([RmlVariant](../rmlvariant.md) data)


**Summary:**
Called by the DOM when the value has been modified (e.g. a checkbox has been checked)

**Parameters:**

- `data` ([RmlVariant](../rmlvariant.md)): 


---


---