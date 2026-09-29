# Quaternion

## Summary
Represents a four-dimensional complex number utilised for 3D spatial rotations.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Quaternion
```
**Implements:**

##### [IVectorSpatial&lt;Single, Single, Quaternion, Quaternion&gt;](./ivectorspatial`4.md), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IEquatable&lt;Quaternion&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public w` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The real or scalar component of the quaternion. |
| `public x` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The X imaginary vector component of the quaternion. |
| `public y` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The Y imaginary vector component of the quaternion. |
| `public z` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The Z imaginary vector component of the quaternion. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Zero` | [Quaternion](./quaternion.md) | Gets a quaternion with all components set to zero. |
| `public static get; Identity` | [Quaternion](./quaternion.md) | Gets the identity quaternion representing no rotation (w: 1, x: 0, y: 0, z: 0). |
| `public get; IsNormalized` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether this quaternion is normalised to unit length within tolerance. |



---

## Methods

#### public static [Quaternion](./quaternion.md) RotateAround([Quaternion](./quaternion.md) q, [Vector3f](./vector3f.md) axis, [Single](https://learn.microsoft.com/dotnet/api/system.single) angle)


**Summary:**
Rotates an existing quaternion around a specified axis by an angle in radians.

**Parameters:**

- `q` ([Quaternion](./quaternion.md)): The base orientation quaternion to rotate.

- `axis` ([Vector3f](./vector3f.md)): The normalised axis of rotation.

- `angle` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The rotation angle in radians.


**Returns:**

- [Quaternion](./quaternion.md): The resulting rotated orientation quaternion.

---
#### public static [Quaternion](./quaternion.md) FromAxisAngle([Vector3f](./vector3f.md) axis, [Single](https://learn.microsoft.com/dotnet/api/system.single) angle)


**Summary:**
Creates a rotation quaternion representing a rotation around a specified axis by an angle in radians.

**Parameters:**

- `axis` ([Vector3f](./vector3f.md)): The normalised axis of rotation.

- `angle` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The rotation angle in radians.


**Returns:**

- [Quaternion](./quaternion.md): A new rotation quaternion.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyToValuePtr([Single*](https://learn.microsoft.com/dotnet/api/system.single*) valuePtr)


**Summary:**
Copies the vector values into a scalar value pointer.

**Parameters:**

- `valuePtr` ([Single*](https://learn.microsoft.com/dotnet/api/system.single*)): Destination value pointer. Must be large enough to contain the values.


---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) LengthSq()


**Summary:**
Calculates the squared length (squared Euclidean norm) of the quaternion.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The squared length.

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) Length()


**Summary:**
Calculates the length (Euclidean norm) of the quaternion.

**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The length.

---
#### public [Quaternion](./quaternion.md) Normalized()


**Summary:**
Returns a normalised copy of this quaternion scaled to unit length.

**Returns:**

- [Quaternion](./quaternion.md): The normalised quaternion, or [Quaternion.Zero](./quaternion.md#zero) if the length is zero.

---
#### public [Quaternion](./quaternion.md) Conjugate()


**Summary:**
Returns the complex conjugate of this quaternion, negating its vector components (x, y, z).

**Returns:**

- [Quaternion](./quaternion.md): The conjugate quaternion.

---
#### public [Quaternion](./quaternion.md) Inverse()


**Summary:**
Calculates the multiplicative inverse of this quaternion.

**Returns:**

- [Quaternion](./quaternion.md): The inverted quaternion.

---
#### public static [Quaternion](./quaternion.md) FromRotationMatrix([Matrix3x3f](./matrix3x3f.md) m)


**Summary:**
Constructs an orientation quaternion from a 3x3 orthonormal rotation matrix.

**Parameters:**

- `m` ([Matrix3x3f](./matrix3x3f.md)): The 3x3 rotation matrix.


**Returns:**

- [Quaternion](./quaternion.md): The corresponding unit quaternion.

---
#### public [EulerAngle](./eulerangle.md) ToEulerAngle([EulerOrder](./eulerorder.md) order)


**Summary:**
Converts this quaternion into intrinsic Euler angles according to the specified rotation sequence.

**Parameters:**

- `order` ([EulerOrder](./eulerorder.md)): The desired sequence of axis rotations. Defaults to [EulerAngle.DefaultOrder](./eulerangle.md#defaultorder).


**Returns:**

- [EulerAngle](./eulerangle.md): An [EulerAngle](./eulerangle.md) structure representing the orientation.

---
#### public [Matrix3x3f](./matrix3x3f.md) ToRotationMatrix()


**Summary:**
Converts this quaternion into an equivalent 3x3 orthonormal rotation matrix.

**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A 3x3 rotation matrix representing the same orientation.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a string representation of the quaternion.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A formatted string displaying the quaternion components.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is a [Quaternion](./quaternion.md) and is equal to the current instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is a [Quaternion](./quaternion.md) and matches all components; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Quaternion](./quaternion.md) other)


**Summary:**
Determines whether the specified [Quaternion](./quaternion.md) is equal to the current instance.

**Parameters:**

- `other` ([Quaternion](./quaternion.md)): The quaternion to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if all corresponding components are equal; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this quaternion.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetObjectData([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) info, [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) context)


**Summary:**
Populates a [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) with the data needed to serialise the quaternion.

**Parameters:**

- `info` ([SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)): The [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) to populate with data.

- `context` ([StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)): The destination for this serialisation.


---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) DistanceSq([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b)


**Summary:**
Calculates the squared Euclidean distance between two quaternions in 4D component space.

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): The first quaternion.

- `b` ([Quaternion](./quaternion.md)): The second quaternion.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The squared Euclidean distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b)


**Summary:**
Calculates the Euclidean distance between two quaternions in 4D component space.

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): The first quaternion.

- `b` ([Quaternion](./quaternion.md)): The second quaternion.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The Euclidean distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Dot([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b)


**Summary:**
Calculates the dot product of two quaternions.

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): The first quaternion operand.

- `b` ([Quaternion](./quaternion.md)): The second quaternion operand.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The scalar dot product.

---
#### public static [Quaternion](./quaternion.md) FromEulerAngle([EulerAngle](./eulerangle.md) euler)


**Summary:**
Creates a rotation quaternion from an intrinsic [EulerAngle](./eulerangle.md) according to its specified rotation order.

**Parameters:**

- `euler` ([EulerAngle](./eulerangle.md)): The Euler angle angles and axis sequence.


**Returns:**

- [Quaternion](./quaternion.md): A rotation quaternion representing the combined rotations.

---
#### public static [EulerAngle](./eulerangle.md) ToEulerAngle([Quaternion](./quaternion.md) quat, [EulerOrder](./eulerorder.md) order)


**Summary:**
Decomposes an orientation quaternion into intrinsic Euler angles according to the specified axis rotation sequence.

**Parameters:**

- `quat` ([Quaternion](./quaternion.md)): The orientation quaternion to decompose.

- `order` ([EulerOrder](./eulerorder.md)): The desired sequence of axis rotations. Defaults to [EulerAngle.DefaultOrder](./eulerangle.md#defaultorder).


**Returns:**

- [EulerAngle](./eulerangle.md): An [EulerAngle](./eulerangle.md) instance containing pitch, yaw, and roll angles in radians.

---
#### public static [Quaternion](./quaternion.md) Nlerp([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Performs a normalised linear interpolation between two quaternions.

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): The starting orientation quaternion.

- `b` ([Quaternion](./quaternion.md)): The destination orientation quaternion.

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The interpolation factor, where 0 represents `a` and 1 represents `b`.


**Returns:**

- [Quaternion](./quaternion.md): The normalised interpolated quaternion.

---
#### public static [Quaternion](./quaternion.md) Slerp([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Performs spherical linear interpolation between two quaternions, maintaining constant angular velocity along the shortest arc.

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): The starting orientation quaternion.

- `b` ([Quaternion](./quaternion.md)): The destination orientation quaternion.

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The interpolation factor, where 0 represents `a` and 1 represents `b`.


**Returns:**

- [Quaternion](./quaternion.md): The spherically interpolated quaternion.

---
#### public static [Quaternion](./quaternion.md) LookAt([Vector3f](./vector3f.md) eye, [Vector3f](./vector3f.md) target)


**Summary:**
Creates a rotation quaternion that points from an eye position towards a target position, assuming a default up direction of (0, 1, 0).

**Parameters:**

- `eye` ([Vector3f](./vector3f.md)): The source position vector.

- `target` ([Vector3f](./vector3f.md)): The target point to look towards.


**Returns:**

- [Quaternion](./quaternion.md): A rotation quaternion facing the target.

---
#### public static [Quaternion](./quaternion.md) LookAt([Vector3f](./vector3f.md) origin, [Vector3f](./vector3f.md) target, [Vector3f](./vector3f.md) up)


**Summary:**
Creates a rotation quaternion that points from an origin position towards a target position with a specified upwards reference direction.

**Parameters:**

- `origin` ([Vector3f](./vector3f.md)): The source position vector.

- `target` ([Vector3f](./vector3f.md)): The target point to look towards.

- `up` ([Vector3f](./vector3f.md)): The upwards reference direction.


**Returns:**

- [Quaternion](./quaternion.md): A rotation quaternion facing the target.

---
#### public static [Matrix3x3f](./matrix3x3f.md) ToRotationMatrix([Quaternion](./quaternion.md) q)


**Summary:**
Converts a rotation quaternion into an equivalent 3x3 orthonormal rotation matrix.

**Parameters:**

- `q` ([Quaternion](./quaternion.md)): The unit orientation quaternion to convert.


**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A 3x3 rotation matrix representing the same orientation.

---
#### public static [Vector3f](./vector3f.md) RotateVector([Quaternion](./quaternion.md) quat, [Vector3f](./vector3f.md) vec)


**Summary:**
Rotates a 3D vector by an orientation quaternion.

**Parameters:**

- `quat` ([Quaternion](./quaternion.md)): The rotation quaternion to apply.

- `vec` ([Vector3f](./vector3f.md)): The vector to rotate.


**Returns:**

- [Vector3f](./vector3f.md): The rotated vector.

---
#### public static [Vector3f](./vector3f.md) RotateVector([Vector3f](./vector3f.md) vec, [Quaternion](./quaternion.md) quat)


**Summary:**
Rotates a 3D vector by the inverse of an orientation quaternion.

**Parameters:**

- `vec` ([Vector3f](./vector3f.md)): The vector to rotate.

- `quat` ([Quaternion](./quaternion.md)): The rotation quaternion whose inverse will be applied.


**Returns:**

- [Vector3f](./vector3f.md): The unrotated or inversely rotated vector.

---
#### public static [Quaternion](./quaternion.md) RotateTowards([Quaternion](./quaternion.md) a, [Quaternion](./quaternion.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Rotates an orientation quaternion towards a target orientation by an angular step not exceeding a maximum delta.

**Parameters:**

- `a` ([Quaternion](./quaternion.md)): The starting orientation quaternion.

- `b` ([Quaternion](./quaternion.md)): The destination orientation quaternion.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum angular step permitted during rotation.


**Returns:**

- [Quaternion](./quaternion.md): The resulting orientation quaternion rotated towards `b`.

---


---