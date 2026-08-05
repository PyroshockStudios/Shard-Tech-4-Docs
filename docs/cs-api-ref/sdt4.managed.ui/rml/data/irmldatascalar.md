# IRMLDataScalar

## Summary
A scalar data variable, that manages untyped variables.



## Definition

**Namespace:** `SDT4.Managed.UI.RML.Data`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
interface IRMLDataScalar
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

#### public [RMLVariant](../rmlvariant.md) Get()


**Summary:**
Called by the DOM when the value is accessed.

**Returns:**

- [RMLVariant](../rmlvariant.md): Value that can be read in the DOM. Return <c>[RMLVariant](../rmlvariant.md).Empty</c> if this should not be accessed.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Set([RMLVariant](../rmlvariant.md) data)


**Summary:**
Called by the DOM when the value has been modified (e.g. a checkbox has been checked)

**Parameters:**

- `data` ([RMLVariant](../rmlvariant.md)): 


---


---