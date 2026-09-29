# Matrix4x4f

## Summary
Represents a 4x4 single-precision floating-point matrix arranged in row-major layout, commonly utilised for 3D affine transformations.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Matrix4x4f
```
**Implements:**

##### [IMatrixSpatial&lt;Single, Vector4f, Matrix4x4f&gt;](./imatrixspatial`3.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Matrix4x4f&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public m00` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 0. |
| `public m01` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 1. |
| `public m02` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 2. |
| `public m03` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 3. |
| `public m10` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 0. |
| `public m11` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 1. |
| `public m12` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 2. |
| `public m13` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 3. |
| `public m20` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 0. |
| `public m21` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 1. |
| `public m22` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 2. |
| `public m23` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 3. |
| `public m30` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 3, column 0. |
| `public m31` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 3, column 1. |
| `public m32` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 3, column 2. |
| `public m33` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 3, column 3. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Matrix4x4f](./matrix4x4f.md) | Gets a 4x4 matrix with all elements set to zero. |
| `public static get; Identity` | [Matrix4x4f](./matrix4x4f.md) | Gets the 4x4 multiplicative identity matrix. |
| `public get; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the element at the specified row and column indices. |
| `public get; Item` | [Vector4f](./vector4f.md) | Gets the row vector at the specified index. |
| `public get; IsOrthoNormal` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether all 4 basis vectors are mutually orthogonal and normalised to unit length. |
| `public get; IsOrthoNormal3x3` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the upper-left 3x3 rotational submatrix is orthonormal. |



---

## Methods

#### public static [Matrix4x4f](./matrix4x4f.md) FromColumns([Vector4f](./vector4f.md) col0, [Vector4f](./vector4f.md) col1, [Vector4f](./vector4f.md) col2, [Vector4f](./vector4f.md) col3)


**Summary:**
Constructs a 4x4 matrix from column vectors.

**Parameters:**

- `col0` ([Vector4f](./vector4f.md)): The first column vector.

- `col1` ([Vector4f](./vector4f.md)): The second column vector.

- `col2` ([Vector4f](./vector4f.md)): The third column vector.

- `col3` ([Vector4f](./vector4f.md)): The fourth column vector.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A matrix containing the column vectors.

---
#### public static [Matrix4x4f](./matrix4x4f.md) FromRows([Vector4f](./vector4f.md) row0, [Vector4f](./vector4f.md) row1, [Vector4f](./vector4f.md) row2, [Vector4f](./vector4f.md) row3)


**Summary:**
Constructs a 4x4 matrix from row vectors.

**Parameters:**

- `row0` ([Vector4f](./vector4f.md)): The first row vector.

- `row1` ([Vector4f](./vector4f.md)): The second row vector.

- `row2` ([Vector4f](./vector4f.md)): The third row vector.

- `row3` ([Vector4f](./vector4f.md)): The fourth row vector.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A matrix containing the row vectors.

---
#### public [Vector4f](./vector4f.md) GetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col)


**Summary:**
Retrieves the column vector at the specified index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index (0 to 3).


**Returns:**

- [Vector4f](./vector4f.md): The column vector.

---
#### public [Vector4f](./vector4f.md) GetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row)


**Summary:**
Retrieves the row vector at the specified index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index (0 to 3).


**Returns:**

- [Vector4f](./vector4f.md): The row vector.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col, [Vector4f](./vector4f.md) vec)


**Summary:**
Sets the column vector at the specified index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index (0 to 3).

- `vec` ([Vector4f](./vector4f.md)): The vector to assign to the column.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row, [Vector4f](./vector4f.md) vec)


**Summary:**
Sets the row vector at the specified index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index (0 to 3).

- `vec` ([Vector4f](./vector4f.md)): The vector to assign to the row.


---
#### public [Matrix3x3f](./matrix3x3f.md) ToMatrix3x3()


**Summary:**
Extracts the upper-left 3x3 submatrix containing the rotational and scaling components.

**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A 3x3 matrix.

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Determinant()


**Summary:**
Calculates the scalar determinant of the 4x4 matrix.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The determinant value.

---
#### public [Matrix4x4f](./matrix4x4f.md) Transposed()


**Summary:**
Returns a transposed copy of the matrix with rows and columns swapped.

**Returns:**

- [Matrix4x4f](./matrix4x4f.md): The transposed matrix.

---
#### public [Matrix4x4f](./matrix4x4f.md) Inverse()


**Summary:**
Calculates the multiplicative inverse of the matrix.

**Returns:**

- [Matrix4x4f](./matrix4x4f.md): The inverted matrix.

---
#### public [EulerAngle](./eulerangle.md) ToEulerAngle([EulerOrder](./eulerorder.md) order)


**Summary:**
Decomposes the upper-left 3x3 rotation portion of this matrix into Euler angles according to a specified rotation sequence.

**Parameters:**

- `order` ([EulerOrder](./eulerorder.md)): The rotational axis sequence to extract. Defaults to [EulerAngle.DefaultOrder](./eulerangle.md#defaultorder).


**Returns:**

- [EulerAngle](./eulerangle.md): The resulting [EulerAngle](./eulerangle.md).

---
#### public [Quaternion](./quaternion.md) ToQuaternion()


**Summary:**
Converts the upper-left 3x3 rotation portion of this matrix into an equivalent rotation quaternion.

**Returns:**

- [Quaternion](./quaternion.md): A normalised [Quaternion](./quaternion.md).

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Matrix4x4f](./matrix4x4f.md) other)


**Summary:**
Determines whether the specified [Matrix4x4f](./matrix4x4f.md) is equal to the current instance.

**Parameters:**

- `other` ([Matrix4x4f](./matrix4x4f.md)): The matrix to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if all corresponding elements are equal; otherwise, <see langword="false" />.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is a [Matrix4x4f](./matrix4x4f.md) and is equal to the current instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is a [Matrix4x4f](./matrix4x4f.md) and matches all elements; otherwise, <see langword="false" />.

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