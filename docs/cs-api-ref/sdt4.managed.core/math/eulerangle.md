# EulerAngle

## Summary
Represents a 3D rotation expressed as intrinsic Euler angles (pitch, yaw, and roll) with a specified rotation order.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct EulerAngle
```
**Implements:**

##### [IEquatable&lt;EulerAngle&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public static DefaultOrder` | [EulerOrder](./eulerorder.md) | The default intrinsic rotation order ([EulerOrder.YXZ](./eulerorder.md#yxz)). |
| `public x` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The pitch rotation angle in radians (rotation about the X-axis). |
| `public y` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The yaw rotation angle in radians (rotation about the Y-axis). |
| `public z` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The roll rotation angle in radians (rotation about the Z-axis). |
| `public Order` | [EulerOrder](./eulerorder.md) | The sequence in which the rotational axes are evaluated. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Pitch` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the pitch angle in radians (equivalent to [EulerAngle.x](./eulerangle.md#x)). |
| `public get; Yaw` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the yaw angle in radians (equivalent to [EulerAngle.y](./eulerangle.md#y)). |
| `public get; Roll` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the roll angle in radians (equivalent to [EulerAngle.z](./eulerangle.md#z)). |



---

## Methods

#### public [Quaternion](./quaternion.md) ToQuaternion()


**Summary:**
Converts this Euler angle representation into an equivalent orientation [Quaternion](./quaternion.md).

**Returns:**

- [Quaternion](./quaternion.md): A quaternion representing the rotation.

---
#### public [Matrix3x3f](./matrix3x3f.md) ToRotationMatrix()


**Summary:**
Converts this Euler angle representation into a [Matrix3x3f](./matrix3x3f.md).

**Returns:**

- [Matrix3x3f](./matrix3x3f.md): A matrix representing the rotation.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([EulerAngle](./eulerangle.md) other)


**Summary:**
Determines whether the specified [EulerAngle](./eulerangle.md) is equal to the current instance.

**Parameters:**

- `other` ([EulerAngle](./eulerangle.md)): The Euler angle to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if all angles and the rotation order match; otherwise, <see langword="false" />.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is an [EulerAngle](./eulerangle.md) and is equal to the current instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is an [EulerAngle](./eulerangle.md) and matches all angles and rotation order; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this Euler angle instance.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a culture-invariant string representation of the Euler angles in degrees, alongside its rotation order.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A formatted string displaying rotation order, pitch, yaw, and roll in degrees.

---


---