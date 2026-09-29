# Matrix2x2f

## Summary
Represents a 2x2 single-precision floating-point matrix arranged in row-major layout.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Matrix2x2f
```
**Implements:**

##### [IMatrixSpatial&lt;Single, Vector2f, Matrix2x2f&gt;](./imatrixspatial`3.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Matrix2x2f&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public m00` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 0. |
| `public m01` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 1. |
| `public m10` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 0. |
| `public m11` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 1. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Matrix2x2f](./matrix2x2f.md) | Gets a 2x2 matrix with all elements set to zero. |
| `public static get; Identity` | [Matrix2x2f](./matrix2x2f.md) | Gets the 2x2 multiplicative identity matrix. |
| `public get; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the element at the specified row and column indices. |
| `public get; Item` | [Vector2f](./vector2f.md) | Gets the row vector at the specified index. |
| `public get; IsOrthoNormal` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the matrix basis vectors are mutually orthogonal and normalised to unit length. |



---

## Methods

#### public static [Matrix2x2f](./matrix2x2f.md) FromColumns([Vector2f](./vector2f.md) col0, [Vector2f](./vector2f.md) col1)


**Summary:**
Constructs a 2x2 matrix from column vectors.

**Parameters:**

- `col0` ([Vector2f](./vector2f.md)): The first column vector.

- `col1` ([Vector2f](./vector2f.md)): The second column vector.


**Returns:**

- [Matrix2x2f](./matrix2x2f.md): A matrix containing the column vectors.

---
#### public static [Matrix2x2f](./matrix2x2f.md) FromRows([Vector2f](./vector2f.md) row0, [Vector2f](./vector2f.md) row1)


**Summary:**
Constructs a 2x2 matrix from row vectors.

**Parameters:**

- `row0` ([Vector2f](./vector2f.md)): The first row vector.

- `row1` ([Vector2f](./vector2f.md)): The second row vector.


**Returns:**

- [Matrix2x2f](./matrix2x2f.md): A matrix containing the row vectors.

---
#### public [Vector2f](./vector2f.md) GetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col)


**Summary:**
Retrieves the column vector at the specified index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index (0 to 1).


**Returns:**

- [Vector2f](./vector2f.md): The column vector.

---
#### public [Vector2f](./vector2f.md) GetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row)


**Summary:**
Retrieves the row vector at the specified index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index (0 to 1).


**Returns:**

- [Vector2f](./vector2f.md): The row vector.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col, [Vector2f](./vector2f.md) vec)


**Summary:**
Sets the column vector at the specified index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index (0 to 1).

- `vec` ([Vector2f](./vector2f.md)): The vector to assign to the column.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row, [Vector2f](./vector2f.md) vec)


**Summary:**
Sets the row vector at the specified index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index (0 to 1).

- `vec` ([Vector2f](./vector2f.md)): The vector to assign to the row.


---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Determinant()


**Summary:**
Calculates the scalar determinant of the 2x2 matrix.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The determinant value.

---
#### public [Matrix2x2f](./matrix2x2f.md) Transposed()


**Summary:**
Returns a transposed copy of the matrix with rows and columns swapped.

**Returns:**

- [Matrix2x2f](./matrix2x2f.md): The transposed matrix.

---
#### public [Matrix2x2f](./matrix2x2f.md) Inverse()


**Summary:**
Calculates the multiplicative inverse of the matrix.

**Returns:**

- [Matrix2x2f](./matrix2x2f.md): The inverted matrix.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Matrix2x2f](./matrix2x2f.md) other)


**Summary:**
Determines whether the specified [Matrix2x2f](./matrix2x2f.md) is equal to the current instance.

**Parameters:**

- `other` ([Matrix2x2f](./matrix2x2f.md)): The matrix to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if all corresponding elements are equal; otherwise, <see langword="false" />.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is a [Matrix2x2f](./matrix2x2f.md) and is equal to the current instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is a [Matrix2x2f](./matrix2x2f.md) and matches all elements; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this matrix.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a culture-invariant string representation of the matrix.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A formatted string displaying the matrix rows.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetObjectData([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) info, [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) context)


**Summary:**
Populates a [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) with the data needed to serialise the matrix.

**Parameters:**

- `info` ([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)): The [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) to populate with data.

- `context` ([StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)): The destination for this serialisation.


---


---