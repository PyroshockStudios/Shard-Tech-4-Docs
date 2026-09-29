# Matrix3x3f

## Summary
Represents a 3x3 single-precision floating-point matrix arranged in row-major layout.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Matrix3x3f
```
**Implements:**

##### [IMatrixSpatial&lt;Single, Vector3f, Matrix3x3f&gt;](./imatrixspatial`3.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Matrix3x3f&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public m00` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 0. |
| `public m01` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 1. |
| `public m02` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 0, column 2. |
| `public m10` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 0. |
| `public m11` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 1. |
| `public m12` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 1, column 2. |
| `public m20` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 0. |
| `public m21` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 1. |
| `public m22` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Value at row 2, column 2. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Matrix3x3f](./matrix3x3f.md) | Gets a 3x3 matrix with all elements set to zero. |
| `public static get; Identity` | [Matrix3x3f](./matrix3x3f.md) | Gets the 3x3 multiplicative identity matrix. |
| `public get; Item` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the element at the specified row and column indices. |
| `public get; Item` | [Vector3f](./vector3f.md) | Gets the row vector at the specified index. |
| `public get; IsOrthoNormal` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the matrix basis vectors are mutually orthogonal and normalised to unit length. |



---

## Methods

#### public static [Matrix3x3f](./matrix3x3f.md) FromColumns([Vector3f](./vector3f.md) col0, [Vector3f](./vector3f.md) col1, [Vector3f](./vector3f.md) col2)


**Summary:**
Constructs a 3x3 matrix from column vectors.

**Parameters:**

- `col0` ([Vector3f](./vector3f.md)): The first column vector.

- `col1` ([Vector3f](./vector3f.md)): The second column vector.

- `col2` ([Vector3f](./vector3f.md)): The third column vector.


**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A matrix containing the column vectors.

---
#### public static [Matrix3x3f](./matrix3x3f.md) FromRows([Vector3f](./vector3f.md) row0, [Vector3f](./vector3f.md) row1, [Vector3f](./vector3f.md) row2)


**Summary:**
Constructs a 3x3 matrix from row vectors.

**Parameters:**

- `row0` ([Vector3f](./vector3f.md)): The first row vector.

- `row1` ([Vector3f](./vector3f.md)): The second row vector.

- `row2` ([Vector3f](./vector3f.md)): The third row vector.


**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A matrix containing the row vectors.

---
#### public [Vector3f](./vector3f.md) GetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col)


**Summary:**
Retrieves the column vector at the specified index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index (0 to 2).


**Returns:**

- [Vector3f](./vector3f.md): The column vector.

---
#### public [Vector3f](./vector3f.md) GetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row)


**Summary:**
Retrieves the row vector at the specified index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index (0 to 2).


**Returns:**

- [Vector3f](./vector3f.md): The row vector.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetColumn([Int32](https://learn.microsoft.com/dotnet/api/system.int32) col, [Vector3f](./vector3f.md) vec)


**Summary:**
Sets the column vector at the specified index.

**Parameters:**

- `col` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based column index (0 to 2).

- `vec` ([Vector3f](./vector3f.md)): The vector to assign to the column.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetRow([Int32](https://learn.microsoft.com/dotnet/api/system.int32) row, [Vector3f](./vector3f.md) vec)


**Summary:**
Sets the row vector at the specified index.

**Parameters:**

- `row` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based row index (0 to 2).

- `vec` ([Vector3f](./vector3f.md)): The vector to assign to the row.


---
#### public [Matrix4x4f](./matrix4x4f.md) ToMatrix4x4()


**Summary:**
Promotes this 3x3 matrix to an affine 4x4 matrix with zero translation and homogeneous coordinates.

**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A 4x4 transformation matrix.

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Determinant()


**Summary:**
Calculates the scalar determinant of the 3x3 matrix.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The determinant value.

---
#### public [Matrix3x3f](./matrix3x3f.md) Transposed()


**Summary:**
Returns a transposed copy of the matrix with rows and columns swapped.

**Returns:**

- [Matrix3x3f](./matrix3x3f.md): The transposed matrix.

---
#### public [Matrix3x3f](./matrix3x3f.md) Inverse()


**Summary:**
Calculates the multiplicative inverse of the matrix.

**Returns:**

- [Matrix3x3f](./matrix3x3f.md): The inverted matrix.

---
#### public [EulerAngle](./eulerangle.md) ToEulerAngle([EulerOrder](./eulerorder.md) order)


**Summary:**
Decomposes this rotation matrix into Euler angles according to a specified rotation sequence.

**Parameters:**

- `order` ([EulerOrder](./eulerorder.md)): The rotational axis sequence to extract. Defaults to [EulerAngle.DefaultOrder](./eulerangle.md#defaultorder).


**Returns:**

- [EulerAngle](./eulerangle.md): The resulting [EulerAngle](./eulerangle.md).

---
#### public [Quaternion](./quaternion.md) ToQuaternion()


**Summary:**
Converts this orthonormal rotation matrix into an equivalent rotation quaternion.

**Returns:**

- [Quaternion](./quaternion.md): A normalised [Quaternion](./quaternion.md).

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Matrix3x3f](./matrix3x3f.md) other)


**Summary:**
Determines whether the specified [Matrix3x3f](./matrix3x3f.md) is equal to the current instance.

**Parameters:**

- `other` ([Matrix3x3f](./matrix3x3f.md)): The matrix to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if all corresponding elements are equal; otherwise, <see langword="false" />.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is a [Matrix3x3f](./matrix3x3f.md) and is equal to the current instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is a [Matrix3x3f](./matrix3x3f.md) and matches all elements; otherwise, <see langword="false" />.

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