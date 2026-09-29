# IVectorSpatial&lt;&gt;

## Summary
Defines a contract for spatial vectors providing geometric length and normalisation operations.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
interface IVectorSpatial<>
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
| `public static get; Zero` | TVectorType | Gets a vector with all components initialised to zero. |
| `public get; IsNormalized` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the vector is normalised to unit length within tolerance. |



---

## Methods

#### public TComponentType LengthSq()


**Summary:**
Calculates the squared length (squared magnitude) of the vector.

**Returns:**

- TComponentType: The squared magnitude of the vector.

---
#### public TLengthType Length()


**Summary:**
Calculates the length (magnitude) of the vector.

**Returns:**

- TLengthType: The magnitude of the vector.

---
#### public TNormalizedType Normalized()


**Summary:**
Returns a normalised copy of the vector scaled to unit length.

**Returns:**

- TNormalizedType: The normalised vector.

---


---