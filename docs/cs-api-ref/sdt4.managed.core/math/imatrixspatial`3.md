# IMatrixSpatial&lt;&gt;

## Summary
Defines a contract for square spatial transformation matrices operating over numeric component and vector types.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
interface IMatrixSpatial<>
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
| `public static get; Zero` | TMatrixType | Gets a matrix with all elements set to zero. |
| `public static get; Identity` | TMatrixType | Gets the multiplicative identity matrix. |
| `public get; Item` | TComponentType | Gets the scalar component at the specified zero-based row and column indices. |
| `public get; Item` | TVectorType | Gets the row vector at the specified zero-based index. |
| `public get; IsOrthoNormal` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the matrix is orthonormal, where its basis vectors are orthogonal unit vectors. |



---

## Methods

#### public TComponentType Determinant()


**Summary:**
Calculates the determinant of the matrix.

**Returns:**

- TComponentType: The scalar determinant value.

---
#### public TMatrixType Transposed()


**Summary:**
Returns a transposed copy of the matrix with its rows and columns swapped.

**Returns:**

- TMatrixType: The transposed matrix.

---
#### public TMatrixType Inverse()


**Summary:**
Calculates the multiplicative inverse of the matrix.

**Returns:**

- TMatrixType: The inverted matrix.

---
#### public TVectorType GetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row)


**Summary:**
Retrieves the row vector at the specified zero-based index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index.


**Returns:**

- TVectorType: The vector representing the row.

---
#### public TVectorType GetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col)


**Summary:**
Retrieves the column vector at the specified zero-based index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index.


**Returns:**

- TVectorType: The vector representing the column.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row, TVectorType vec)


**Summary:**
Sets the row vector at the specified zero-based index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index.

- `vec` (TVectorType): The vector to assign to the row.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col, TVectorType vec)


**Summary:**
Sets the column vector at the specified zero-based index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index.

- `vec` (TVectorType): The vector to assign to the column.


---


---