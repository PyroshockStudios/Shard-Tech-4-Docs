# Matrix

## Summary
Provides utility methods and constants for matrix transformations, conversions, and decompositions.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
static class Matrix
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Matrix**
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public static Storage` | [MatrixStorage](./matrixstorage.md) | Defines the memory layout layout convention utilised for matrix storage. |
| `public static Access` | [MatrixStorage](./matrixstorage.md) | Defines the indexing and element access convention utilised for matrices. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |



---

## Methods

#### public static [Matrix3x3f](./matrix3x3f.md) ToMatrix3x3([Matrix4x4f](./matrix4x4f.md) mat)


**Summary:**
Extracts the upper-left 3x3 rotation and scale submatrix from a 4x4 matrix.

**Parameters:**

- `mat` ([Matrix4x4f](./matrix4x4f.md)): The 4x4 source matrix.


**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A 3x3 matrix representing the linear portion of the transformation.

---
#### public static [Matrix4x4f](./matrix4x4f.md) ToMatrix4x4([Matrix3x3f](./matrix3x3f.md) mat)


**Summary:**
Promotes a 3x3 matrix to an affine 4x4 matrix with zero translation and homogeneous coordinates.

**Parameters:**

- `mat` ([Matrix3x3f](./matrix3x3f.md)): The 3x3 source matrix.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A 4x4 transformation matrix.

---
#### public static [EulerAngle](./eulerangle.md) ToEulerAngle([Matrix3x3f](./matrix3x3f.md) mat, [EulerOrder](./eulerorder.md) order)


**Summary:**
Decomposes a 3x3 rotation matrix into Euler angles according to a specified rotation sequence.

**Parameters:**

- `mat` ([Matrix3x3f](./matrix3x3f.md)): The orthonormal 3x3 rotation matrix to extract angles from.

- `order` ([EulerOrder](./eulerorder.md)): The rotational axis application sequence. Defaults to [EulerAngle.DefaultOrder](./eulerangle.md#defaultorder).


**Returns:**

- [EulerAngle](./eulerangle.md): An [EulerAngle](./eulerangle.md) structure representing the decomposed orientation.

---
#### public static [Quaternion](./quaternion.md) ToQuaternion([Matrix3x3f](./matrix3x3f.md) mat)


**Summary:**
Converts a 3x3 orthonormal rotation matrix into an equivalent rotation quaternion.

**Parameters:**

- `mat` ([Matrix3x3f](./matrix3x3f.md)): The 3x3 rotation matrix.


**Returns:**

- [Quaternion](./quaternion.md): A normalised [Quaternion](./quaternion.md) representing the rotation.

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) Decompose([Matrix4x4f](./matrix4x4f.md) mat, out [Vector3f](./vector3f.md) translation, out [Quaternion](./quaternion.md) rotation, out [Vector3f](./vector3f.md) scale)


**Summary:**
Decomposes an affine 4x4 transformation matrix into its translation, rotation, and scale components.

**Parameters:**

- `mat` ([Matrix4x4f](./matrix4x4f.md)): The 4x4 matrix to decompose.

- `translation` ([Vector3f](./vector3f.md)): When this method returns, contains the translation vector.

- `rotation` ([Quaternion](./quaternion.md)): When this method returns, contains the orientation quaternion.

- `scale` ([Vector3f](./vector3f.md)): When this method returns, contains the scale vector.


---
#### public static [Matrix4x4f](./matrix4x4f.md) MakeTranslation([Vector3f](./vector3f.md) translation)


**Summary:**
Creates a 4x4 translation transformation matrix from a displacement vector.

**Parameters:**

- `translation` ([Vector3f](./vector3f.md)): The displacement vector along the X, Y, and Z axes.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A translation matrix.

---
#### public static [Matrix4x4f](./matrix4x4f.md) MakeRotation([Quaternion](./quaternion.md) rotation)


**Summary:**
Creates a 4x4 rotation transformation matrix from an orientation quaternion.

**Parameters:**

- `rotation` ([Quaternion](./quaternion.md)): The rotation quaternion.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A rotation matrix.

---
#### public static [Matrix4x4f](./matrix4x4f.md) MakeRotation([EulerAngle](./eulerangle.md) rotation)


**Summary:**
Creates a 4x4 rotation transformation matrix from an euler rotation.

**Parameters:**

- `rotation` ([EulerAngle](./eulerangle.md)): The euler rotation.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A rotation matrix.

---
#### public static [Matrix4x4f](./matrix4x4f.md) MakeScale([Vector3f](./vector3f.md) scale)


**Summary:**
Creates a 4x4 scaling transformation matrix from a scale vector.

**Parameters:**

- `scale` ([Vector3f](./vector3f.md)): The scaling factors along the X, Y, and Z axes.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): A scale matrix.

---
#### public static [Matrix4x4f](./matrix4x4f.md) Translate([Matrix4x4f](./matrix4x4f.md) mat, [Vector3f](./vector3f.md) translation)


**Summary:**
Applies a translation transformation to an existing 4x4 matrix by pre-multiplying a translation matrix.

**Parameters:**

- `mat` ([Matrix4x4f](./matrix4x4f.md)): The base transformation matrix.

- `translation` ([Vector3f](./vector3f.md)): The displacement vector to apply.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): The resulting transformed matrix.

---
#### public static [Matrix4x4f](./matrix4x4f.md) Rotate([Matrix4x4f](./matrix4x4f.md) mat, [Quaternion](./quaternion.md) rotation)


**Summary:**
Applies a rotation transformation to an existing 4x4 matrix by pre-multiplying a rotation matrix.

**Parameters:**

- `mat` ([Matrix4x4f](./matrix4x4f.md)): The base transformation matrix.

- `rotation` ([Quaternion](./quaternion.md)): The orientation quaternion to apply.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): The resulting transformed matrix.

---
#### public static [Matrix4x4f](./matrix4x4f.md) Scale([Matrix4x4f](./matrix4x4f.md) mat, [Vector3f](./vector3f.md) scale)


**Summary:**
Applies a scale transformation to an existing 4x4 matrix by pre-multiplying a scale matrix.

**Parameters:**

- `mat` ([Matrix4x4f](./matrix4x4f.md)): The base transformation matrix.

- `scale` ([Vector3f](./vector3f.md)): The scaling factors to apply.


**Returns:**

- [Matrix4x4f](./matrix4x4f.md): The resulting transformed matrix.

---


---