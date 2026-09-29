# Vector

## Summary
The math class containing vector math operations



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
static class Vector
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Vector**
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



---

## Methods

#### public static [Vector2f](./vector2f.md) NormalizeAngle([Vector2f](./vector2f.md) v)


**Summary:**
Normalises the angular components of a 2D vector in radians to the range [-pi, pi].

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): The vector containing angles in radians.


**Returns:**

- [Vector2f](./vector2f.md): A vector containing normalised angles.

---
#### public static [Vector3f](./vector3f.md) NormalizeAngle([Vector3f](./vector3f.md) v)


**Summary:**
Normalises the angular components of a 3D vector in radians to the range [-pi, pi].

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): The vector containing angles in radians.


**Returns:**

- [Vector3f](./vector3f.md): A vector containing normalised angles.

---
#### public static [Vector4f](./vector4f.md) NormalizeAngle([Vector4f](./vector4f.md) v)


**Summary:**
Normalises the angular components of a 4D vector in radians to the range [-pi, pi].

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): The vector containing angles in radians.


**Returns:**

- [Vector4f](./vector4f.md): A vector containing normalised angles.

---
#### public static [Vector2f](./vector2f.md) DeltaAngle([Vector2f](./vector2f.md) current, [Vector2f](./vector2f.md) target)


**Summary:**
Calculates the shortest angular difference in radians between corresponding components of two 2D vectors.

**Parameters:**

- `current` ([Vector2f](./vector2f.md)): The current angles in radians.

- `target` ([Vector2f](./vector2f.md)): The target angles in radians.


**Returns:**

- [Vector2f](./vector2f.md): A vector containing angular differences in the range [-pi, pi].

---
#### public static [Vector3f](./vector3f.md) DeltaAngle([Vector3f](./vector3f.md) current, [Vector3f](./vector3f.md) target)


**Summary:**
Calculates the shortest angular difference in radians between corresponding components of two 3D vectors.

**Parameters:**

- `current` ([Vector3f](./vector3f.md)): The current angles in radians.

- `target` ([Vector3f](./vector3f.md)): The target angles in radians.


**Returns:**

- [Vector3f](./vector3f.md): A vector containing angular differences in the range [-pi, pi].

---
#### public static [Vector4f](./vector4f.md) DeltaAngle([Vector4f](./vector4f.md) current, [Vector4f](./vector4f.md) target)


**Summary:**
Calculates the shortest angular difference in radians between corresponding components of two 4D vectors.

**Parameters:**

- `current` ([Vector4f](./vector4f.md)): The current angles in radians.

- `target` ([Vector4f](./vector4f.md)): The target angles in radians.


**Returns:**

- [Vector4f](./vector4f.md): A vector containing angular differences in the range [-pi, pi].

---
#### public static [Vector2d](./vector2d.md) NormalizeAngle([Vector2d](./vector2d.md) v)


**Summary:**
Normalises the angular components of a double-precision 2D vector in radians to the range [-pi, pi].

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): The vector containing angles in radians.


**Returns:**

- [Vector2d](./vector2d.md): A vector containing normalised angles.

---
#### public static [Vector3d](./vector3d.md) NormalizeAngle([Vector3d](./vector3d.md) v)


**Summary:**
Normalises the angular components of a double-precision 3D vector in radians to the range [-pi, pi].

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): The vector containing angles in radians.


**Returns:**

- [Vector3d](./vector3d.md): A vector containing normalised angles.

---
#### public static [Vector4d](./vector4d.md) NormalizeAngle([Vector4d](./vector4d.md) v)


**Summary:**
Normalises the angular components of a double-precision 4D vector in radians to the range [-pi, pi].

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): The vector containing angles in radians.


**Returns:**

- [Vector4d](./vector4d.md): A vector containing normalised angles.

---
#### public static [Vector2d](./vector2d.md) DeltaAngle([Vector2d](./vector2d.md) current, [Vector2d](./vector2d.md) target)


**Summary:**
Calculates the shortest angular difference in radians between corresponding components of two double-precision 2D vectors.

**Parameters:**

- `current` ([Vector2d](./vector2d.md)): The current angles in radians.

- `target` ([Vector2d](./vector2d.md)): The target angles in radians.


**Returns:**

- [Vector2d](./vector2d.md): A vector containing angular differences in the range [-pi, pi].

---
#### public static [Vector3d](./vector3d.md) DeltaAngle([Vector3d](./vector3d.md) current, [Vector3d](./vector3d.md) target)


**Summary:**
Calculates the shortest angular difference in radians between corresponding components of two double-precision 3D vectors.

**Parameters:**

- `current` ([Vector3d](./vector3d.md)): The current angles in radians.

- `target` ([Vector3d](./vector3d.md)): The target angles in radians.


**Returns:**

- [Vector3d](./vector3d.md): A vector containing angular differences in the range [-pi, pi].

---
#### public static [Vector4d](./vector4d.md) DeltaAngle([Vector4d](./vector4d.md) current, [Vector4d](./vector4d.md) target)


**Summary:**
Calculates the shortest angular difference in radians between corresponding components of two double-precision 4D vectors.

**Parameters:**

- `current` ([Vector4d](./vector4d.md)): The current angles in radians.

- `target` ([Vector4d](./vector4d.md)): The target angles in radians.


**Returns:**

- [Vector4d](./vector4d.md): A vector containing angular differences in the range [-pi, pi].

---
#### public static [Vector2f](./vector2f.md) ToDeg([Vector2f](./vector2f.md) rad)


**Summary:**
Converts the components of a 2D vector from radians to degrees.

**Parameters:**

- `rad` ([Vector2f](./vector2f.md)): The vector containing angles in radians.


**Returns:**

- [Vector2f](./vector2f.md): A vector containing angles in degrees.

---
#### public static [Vector3f](./vector3f.md) ToDeg([Vector3f](./vector3f.md) rad)


**Summary:**
Converts the components of a 3D vector from radians to degrees.

**Parameters:**

- `rad` ([Vector3f](./vector3f.md)): The vector containing angles in radians.


**Returns:**

- [Vector3f](./vector3f.md): A vector containing angles in degrees.

---
#### public static [Vector4f](./vector4f.md) ToDeg([Vector4f](./vector4f.md) rad)


**Summary:**
Converts the components of a 4D vector from radians to degrees.

**Parameters:**

- `rad` ([Vector4f](./vector4f.md)): The vector containing angles in radians.


**Returns:**

- [Vector4f](./vector4f.md): A vector containing angles in degrees.

---
#### public static [Vector2f](./vector2f.md) ToRad([Vector2f](./vector2f.md) deg)


**Summary:**
Converts the components of a 2D vector from degrees to radians.

**Parameters:**

- `deg` ([Vector2f](./vector2f.md)): The vector containing angles in degrees.


**Returns:**

- [Vector2f](./vector2f.md): A vector containing angles in radians.

---
#### public static [Vector3f](./vector3f.md) ToRad([Vector3f](./vector3f.md) deg)


**Summary:**
Converts the components of a 3D vector from degrees to radians.

**Parameters:**

- `deg` ([Vector3f](./vector3f.md)): The vector containing angles in degrees.


**Returns:**

- [Vector3f](./vector3f.md): A vector containing angles in radians.

---
#### public static [Vector4f](./vector4f.md) ToRad([Vector4f](./vector4f.md) deg)


**Summary:**
Converts the components of a 4D vector from degrees to radians.

**Parameters:**

- `deg` ([Vector4f](./vector4f.md)): The vector containing angles in degrees.


**Returns:**

- [Vector4f](./vector4f.md): A vector containing angles in radians.

---
#### public static [Vector2d](./vector2d.md) ToDeg([Vector2d](./vector2d.md) rad)


**Summary:**
Converts the components of a double-precision 2D vector from radians to degrees.

**Parameters:**

- `rad` ([Vector2d](./vector2d.md)): The vector containing angles in radians.


**Returns:**

- [Vector2d](./vector2d.md): A vector containing angles in degrees.

---
#### public static [Vector3d](./vector3d.md) ToDeg([Vector3d](./vector3d.md) rad)


**Summary:**
Converts the components of a double-precision 3D vector from radians to degrees.

**Parameters:**

- `rad` ([Vector3d](./vector3d.md)): The vector containing angles in radians.


**Returns:**

- [Vector3d](./vector3d.md): A vector containing angles in degrees.

---
#### public static [Vector4d](./vector4d.md) ToDeg([Vector4d](./vector4d.md) rad)


**Summary:**
Converts the components of a double-precision 4D vector from radians to degrees.

**Parameters:**

- `rad` ([Vector4d](./vector4d.md)): The vector containing angles in radians.


**Returns:**

- [Vector4d](./vector4d.md): A vector containing angles in degrees.

---
#### public static [Vector2d](./vector2d.md) ToRad([Vector2d](./vector2d.md) deg)


**Summary:**
Converts the components of a double-precision 2D vector from degrees to radians.

**Parameters:**

- `deg` ([Vector2d](./vector2d.md)): The vector containing angles in degrees.


**Returns:**

- [Vector2d](./vector2d.md): A vector containing angles in radians.

---
#### public static [Vector3d](./vector3d.md) ToRad([Vector3d](./vector3d.md) deg)


**Summary:**
Converts the components of a double-precision 3D vector from degrees to radians.

**Parameters:**

- `deg` ([Vector3d](./vector3d.md)): The vector containing angles in degrees.


**Returns:**

- [Vector3d](./vector3d.md): A vector containing angles in radians.

---
#### public static [Vector4d](./vector4d.md) ToRad([Vector4d](./vector4d.md) deg)


**Summary:**
Converts the components of a double-precision 4D vector from degrees to radians.

**Parameters:**

- `deg` ([Vector4d](./vector4d.md)): The vector containing angles in degrees.


**Returns:**

- [Vector4d](./vector4d.md): A vector containing angles in radians.

---
#### public static [Vector2b](./vector2b.md) Approximately([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b)


**Summary:**
Performs a component-wise approximate equality check between two 2D vectors using single-precision tolerance.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): The first vector operand.

- `b` ([Vector2f](./vector2f.md)): The second vector operand.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component equality.

---
#### public static [Vector2b](./vector2b.md) Approximately([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) tolerance)


**Summary:**
Performs a component-wise approximate equality check between two 2D vectors within a given tolerance.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): The first vector operand.

- `b` ([Vector2f](./vector2f.md)): The second vector operand.

- `tolerance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximal amount of error allowed.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component equality.

---
#### public static [Vector3b](./vector3b.md) Approximately([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Performs a component-wise approximate equality check between two 3D vectors using single-precision tolerance.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The first vector operand.

- `b` ([Vector3f](./vector3f.md)): The second vector operand.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component equality.

---
#### public static [Vector3b](./vector3b.md) Approximately([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) tolerance)


**Summary:**
Performs a component-wise approximate equality check between two 3D vectors within a given tolerance.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The first vector operand.

- `b` ([Vector3f](./vector3f.md)): The second vector operand.

- `tolerance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximal amount of error allowed.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component equality.

---
#### public static [Vector4b](./vector4b.md) Approximately([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b)


**Summary:**
Performs a component-wise approximate equality check between two 4D vectors using single-precision tolerance.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): The first vector operand.

- `b` ([Vector4f](./vector4f.md)): The second vector operand.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component equality.

---
#### public static [Vector4b](./vector4b.md) Approximately([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) tolerance)


**Summary:**
Performs a component-wise approximate equality check between two 4D vectors within a given tolerance.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): The first vector operand.

- `b` ([Vector4f](./vector4f.md)): The second vector operand.

- `tolerance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximal amount of error allowed.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component equality.

---
#### public static [Vector2b](./vector2b.md) IsBetween([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) min, [Vector2f](./vector2f.md) max)


**Summary:**
Determines component-wise whether a 2D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): The vector to test.

- `min` ([Vector2f](./vector2f.md)): The inclusive lower bound vector.

- `max` ([Vector2f](./vector2f.md)): The inclusive upper bound vector.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component containment.

---
#### public static [Vector3b](./vector3b.md) IsBetween([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) min, [Vector3f](./vector3f.md) max)


**Summary:**
Determines component-wise whether a 3D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): The vector to test.

- `min` ([Vector3f](./vector3f.md)): The inclusive lower bound vector.

- `max` ([Vector3f](./vector3f.md)): The inclusive upper bound vector.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component containment.

---
#### public static [Vector4b](./vector4b.md) IsBetween([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) min, [Vector4f](./vector4f.md) max)


**Summary:**
Determines component-wise whether a 4D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): The vector to test.

- `min` ([Vector4f](./vector4f.md)): The inclusive lower bound vector.

- `max` ([Vector4f](./vector4f.md)): The inclusive upper bound vector.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component containment.

---
#### public static [Vector2b](./vector2b.md) IsBetweenExcl([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) min, [Vector2f](./vector2f.md) max)


**Summary:**
Determines component-wise whether a 2D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): The vector to test.

- `min` ([Vector2f](./vector2f.md)): The exclusive lower bound vector.

- `max` ([Vector2f](./vector2f.md)): The exclusive upper bound vector.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector3b](./vector3b.md) IsBetweenExcl([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) min, [Vector3f](./vector3f.md) max)


**Summary:**
Determines component-wise whether a 3D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): The vector to test.

- `min` ([Vector3f](./vector3f.md)): The exclusive lower bound vector.

- `max` ([Vector3f](./vector3f.md)): The exclusive upper bound vector.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector4b](./vector4b.md) IsBetweenExcl([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) min, [Vector4f](./vector4f.md) max)


**Summary:**
Determines component-wise whether a 4D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): The vector to test.

- `min` ([Vector4f](./vector4f.md)): The exclusive lower bound vector.

- `max` ([Vector4f](./vector4f.md)): The exclusive upper bound vector.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector2b](./vector2b.md) Approximately([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b)


**Summary:**
Performs a component-wise approximate equality check between two double-precision 2D vectors.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): The first vector operand.

- `b` ([Vector2d](./vector2d.md)): The second vector operand.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component equality.

---
#### public static [Vector2b](./vector2b.md) Approximately([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) tolerance)


**Summary:**
Performs a component-wise approximate equality check between two double-precision 2D vectors within a given tolerance.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): The first vector operand.

- `b` ([Vector2d](./vector2d.md)): The second vector operand.

- `tolerance` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximal amount of error allowed.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component equality.

---
#### public static [Vector3b](./vector3b.md) Approximately([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Performs a component-wise approximate equality check between two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The first vector operand.

- `b` ([Vector3d](./vector3d.md)): The second vector operand.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component equality.

---
#### public static [Vector3b](./vector3b.md) Approximately([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) tolerance)


**Summary:**
Performs a component-wise approximate equality check between two double-precision 3D vectors within a given tolerance.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The first vector operand.

- `b` ([Vector3d](./vector3d.md)): The second vector operand.

- `tolerance` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximal amount of error allowed.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component equality.

---
#### public static [Vector4b](./vector4b.md) Approximately([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b)


**Summary:**
Performs a component-wise approximate equality check between two double-precision 4D vectors.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): The first vector operand.

- `b` ([Vector4d](./vector4d.md)): The second vector operand.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component equality.

---
#### public static [Vector4b](./vector4b.md) Approximately([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) tolerance)


**Summary:**
Performs a component-wise approximate equality check between two double-precision 4D vectors within a given tolerance.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): The first vector operand.

- `b` ([Vector4d](./vector4d.md)): The second vector operand.

- `tolerance` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximal amount of error allowed.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component equality.

---
#### public static [Vector2b](./vector2b.md) IsBetween([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) min, [Vector2d](./vector2d.md) max)


**Summary:**
Determines component-wise whether a double-precision 2D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): The vector to test.

- `min` ([Vector2d](./vector2d.md)): The inclusive lower bound vector.

- `max` ([Vector2d](./vector2d.md)): The inclusive upper bound vector.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component containment.

---
#### public static [Vector3b](./vector3b.md) IsBetween([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) min, [Vector3d](./vector3d.md) max)


**Summary:**
Determines component-wise whether a double-precision 3D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): The vector to test.

- `min` ([Vector3d](./vector3d.md)): The inclusive lower bound vector.

- `max` ([Vector3d](./vector3d.md)): The inclusive upper bound vector.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component containment.

---
#### public static [Vector4b](./vector4b.md) IsBetween([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) min, [Vector4d](./vector4d.md) max)


**Summary:**
Determines component-wise whether a double-precision 4D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): The vector to test.

- `min` ([Vector4d](./vector4d.md)): The inclusive lower bound vector.

- `max` ([Vector4d](./vector4d.md)): The inclusive upper bound vector.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component containment.

---
#### public static [Vector2b](./vector2b.md) IsBetweenExcl([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) min, [Vector2d](./vector2d.md) max)


**Summary:**
Determines component-wise whether a double-precision 2D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): The vector to test.

- `min` ([Vector2d](./vector2d.md)): The exclusive lower bound vector.

- `max` ([Vector2d](./vector2d.md)): The exclusive upper bound vector.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector3b](./vector3b.md) IsBetweenExcl([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) min, [Vector3d](./vector3d.md) max)


**Summary:**
Determines component-wise whether a double-precision 3D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): The vector to test.

- `min` ([Vector3d](./vector3d.md)): The exclusive lower bound vector.

- `max` ([Vector3d](./vector3d.md)): The exclusive upper bound vector.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector4b](./vector4b.md) IsBetweenExcl([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) min, [Vector4d](./vector4d.md) max)


**Summary:**
Determines component-wise whether a double-precision 4D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): The vector to test.

- `min` ([Vector4d](./vector4d.md)): The exclusive lower bound vector.

- `max` ([Vector4d](./vector4d.md)): The exclusive upper bound vector.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector2b](./vector2b.md) IsBetween([Vector2i](./vector2i.md) v, [Vector2i](./vector2i.md) min, [Vector2i](./vector2i.md) max)


**Summary:**
Determines component-wise whether an integer 2D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector2i](./vector2i.md)): The vector to test.

- `min` ([Vector2i](./vector2i.md)): The inclusive lower bound vector.

- `max` ([Vector2i](./vector2i.md)): The inclusive upper bound vector.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component containment.

---
#### public static [Vector3b](./vector3b.md) IsBetween([Vector3i](./vector3i.md) v, [Vector3i](./vector3i.md) min, [Vector3i](./vector3i.md) max)


**Summary:**
Determines component-wise whether an integer 3D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector3i](./vector3i.md)): The vector to test.

- `min` ([Vector3i](./vector3i.md)): The inclusive lower bound vector.

- `max` ([Vector3i](./vector3i.md)): The inclusive upper bound vector.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component containment.

---
#### public static [Vector4b](./vector4b.md) IsBetween([Vector4i](./vector4i.md) v, [Vector4i](./vector4i.md) min, [Vector4i](./vector4i.md) max)


**Summary:**
Determines component-wise whether an integer 4D vector lies within an inclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector4i](./vector4i.md)): The vector to test.

- `min` ([Vector4i](./vector4i.md)): The inclusive lower bound vector.

- `max` ([Vector4i](./vector4i.md)): The inclusive upper bound vector.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component containment.

---
#### public static [Vector2b](./vector2b.md) IsBetweenExcl([Vector2i](./vector2i.md) v, [Vector2i](./vector2i.md) min, [Vector2i](./vector2i.md) max)


**Summary:**
Determines component-wise whether an integer 2D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector2i](./vector2i.md)): The vector to test.

- `min` ([Vector2i](./vector2i.md)): The exclusive lower bound vector.

- `max` ([Vector2i](./vector2i.md)): The exclusive upper bound vector.


**Returns:**

- [Vector2b](./vector2b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector3b](./vector3b.md) IsBetweenExcl([Vector3i](./vector3i.md) v, [Vector3i](./vector3i.md) min, [Vector3i](./vector3i.md) max)


**Summary:**
Determines component-wise whether an integer 3D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector3i](./vector3i.md)): The vector to test.

- `min` ([Vector3i](./vector3i.md)): The exclusive lower bound vector.

- `max` ([Vector3i](./vector3i.md)): The exclusive upper bound vector.


**Returns:**

- [Vector3b](./vector3b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector4b](./vector4b.md) IsBetweenExcl([Vector4i](./vector4i.md) v, [Vector4i](./vector4i.md) min, [Vector4i](./vector4i.md) max)


**Summary:**
Determines component-wise whether an integer 4D vector lies strictly within an exclusive range defined by two boundary vectors.

**Parameters:**

- `v` ([Vector4i](./vector4i.md)): The vector to test.

- `min` ([Vector4i](./vector4i.md)): The exclusive lower bound vector.

- `max` ([Vector4i](./vector4i.md)): The exclusive upper bound vector.


**Returns:**

- [Vector4b](./vector4b.md): A boolean vector indicating component strict containment.

---
#### public static [Vector3f](./vector3f.md) Cross([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Calculates the cross product of two single-precision 3D vectors.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The first vector operand.

- `b` ([Vector3f](./vector3f.md)): The second vector operand.


**Returns:**

- [Vector3f](./vector3f.md): A vector perpendicular to both operands.

---
#### public static [Vector3d](./vector3d.md) Cross([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Calculates the cross product of two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The first vector operand.

- `b` ([Vector3d](./vector3d.md)): The second vector operand.


**Returns:**

- [Vector3d](./vector3d.md): A vector perpendicular to both operands.

---
#### public static [Vector3i](./vector3i.md) Cross([Vector3i](./vector3i.md) a, [Vector3i](./vector3i.md) b)


**Summary:**
Calculates the cross product of two integer 3D vectors.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): The first vector operand.

- `b` ([Vector3i](./vector3i.md)): The second vector operand.


**Returns:**

- [Vector3i](./vector3i.md): A vector perpendicular to both operands.

---
#### public static [Vector2f](./vector2f.md) SmoothDamp([Vector2f](./vector2f.md) current, [Vector2f](./vector2f.md) target, ref [Vector2f](./vector2f.md) currentVelocity, [Single](https://learn.microsoft.com/dotnet/api/system.single) smoothTime, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a single-precision 2D vector towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Vector2f](./vector2f.md)): The current position vector.

- `target` ([Vector2f](./vector2f.md)): The target position vector.

- `currentVelocity` ([Vector2f](./vector2f.md)): A reference to the current velocity vector, modified by the method.

- `smoothTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The approximate time required to reach the target.

- `maxSpeed` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum component movement speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Vector2f](./vector2f.md): The smoothed vector position.

---
#### public static [Vector3f](./vector3f.md) SmoothDamp([Vector3f](./vector3f.md) current, [Vector3f](./vector3f.md) target, ref [Vector3f](./vector3f.md) currentVelocity, [Single](https://learn.microsoft.com/dotnet/api/system.single) smoothTime, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a single-precision 3D vector towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Vector3f](./vector3f.md)): The current position vector.

- `target` ([Vector3f](./vector3f.md)): The target position vector.

- `currentVelocity` ([Vector3f](./vector3f.md)): A reference to the current velocity vector, modified by the method.

- `smoothTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The approximate time required to reach the target.

- `maxSpeed` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum component movement speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Vector3f](./vector3f.md): The smoothed vector position.

---
#### public static [Vector4f](./vector4f.md) SmoothDamp([Vector4f](./vector4f.md) current, [Vector4f](./vector4f.md) target, ref [Vector4f](./vector4f.md) currentVelocity, [Single](https://learn.microsoft.com/dotnet/api/system.single) smoothTime, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a single-precision 4D vector towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Vector4f](./vector4f.md)): The current position vector.

- `target` ([Vector4f](./vector4f.md)): The target position vector.

- `currentVelocity` ([Vector4f](./vector4f.md)): A reference to the current velocity vector, modified by the method.

- `smoothTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The approximate time required to reach the target.

- `maxSpeed` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum component movement speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Vector4f](./vector4f.md): The smoothed vector position.

---
#### public static [Vector2d](./vector2d.md) SmoothDamp([Vector2d](./vector2d.md) current, [Vector2d](./vector2d.md) target, ref [Vector2d](./vector2d.md) currentVelocity, [Double](https://learn.microsoft.com/dotnet/api/system.double) smoothTime, [Double](https://learn.microsoft.com/dotnet/api/system.double) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a double-precision 2D vector towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Vector2d](./vector2d.md)): The current position vector.

- `target` ([Vector2d](./vector2d.md)): The target position vector.

- `currentVelocity` ([Vector2d](./vector2d.md)): A reference to the current velocity vector, modified by the method.

- `smoothTime` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The approximate time required to reach the target.

- `maxSpeed` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximum component movement speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Vector2d](./vector2d.md): The smoothed vector position.

---
#### public static [Vector3d](./vector3d.md) SmoothDamp([Vector3d](./vector3d.md) current, [Vector3d](./vector3d.md) target, ref [Vector3d](./vector3d.md) currentVelocity, [Double](https://learn.microsoft.com/dotnet/api/system.double) smoothTime, [Double](https://learn.microsoft.com/dotnet/api/system.double) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a double-precision 3D vector towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Vector3d](./vector3d.md)): The current position vector.

- `target` ([Vector3d](./vector3d.md)): The target position vector.

- `currentVelocity` ([Vector3d](./vector3d.md)): A reference to the current velocity vector, modified by the method.

- `smoothTime` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The approximate time required to reach the target.

- `maxSpeed` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximum component movement speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Vector3d](./vector3d.md): The smoothed vector position.

---
#### public static [Vector4d](./vector4d.md) SmoothDamp([Vector4d](./vector4d.md) current, [Vector4d](./vector4d.md) target, ref [Vector4d](./vector4d.md) currentVelocity, [Double](https://learn.microsoft.com/dotnet/api/system.double) smoothTime, [Double](https://learn.microsoft.com/dotnet/api/system.double) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a double-precision 4D vector towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Vector4d](./vector4d.md)): The current position vector.

- `target` ([Vector4d](./vector4d.md)): The target position vector.

- `currentVelocity` ([Vector4d](./vector4d.md)): A reference to the current velocity vector, modified by the method.

- `smoothTime` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The approximate time required to reach the target.

- `maxSpeed` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximum component movement speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Vector4d](./vector4d.md): The smoothed vector position.

---
#### public static [Int32](https://learn.microsoft.com/dotnet/api/system.int32) DistanceSq([Vector2i](./vector2i.md) a, [Vector2i](./vector2i.md) b)


**Summary:**
Calculates the squared Euclidean distance between two integer 2D vectors.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): The first vector.

- `b` ([Vector2i](./vector2i.md)): The second vector.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The squared distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Vector2i](./vector2i.md) a, [Vector2i](./vector2i.md) b)


**Summary:**
Calculates the Euclidean distance between two integer 2D vectors.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): The first vector.

- `b` ([Vector2i](./vector2i.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The distance as a single-precision floating-point value.

---
#### public static [Int32](https://learn.microsoft.com/dotnet/api/system.int32) DistanceSq([Vector3i](./vector3i.md) a, [Vector3i](./vector3i.md) b)


**Summary:**
Calculates the squared Euclidean distance between two integer 3D vectors.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): The first vector.

- `b` ([Vector3i](./vector3i.md)): The second vector.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The squared distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Vector3i](./vector3i.md) a, [Vector3i](./vector3i.md) b)


**Summary:**
Calculates the Euclidean distance between two integer 3D vectors.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): The first vector.

- `b` ([Vector3i](./vector3i.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The distance as a single-precision floating-point value.

---
#### public static [Int32](https://learn.microsoft.com/dotnet/api/system.int32) DistanceSq([Vector4i](./vector4i.md) a, [Vector4i](./vector4i.md) b)


**Summary:**
Calculates the squared Euclidean distance between two integer 4D vectors.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): The first vector.

- `b` ([Vector4i](./vector4i.md)): The second vector.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The squared distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Vector4i](./vector4i.md) a, [Vector4i](./vector4i.md) b)


**Summary:**
Calculates the Euclidean distance between two integer 4D vectors.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): The first vector.

- `b` ([Vector4i](./vector4i.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The distance as a single-precision floating-point value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) DistanceSq([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b)


**Summary:**
Calculates the squared Euclidean distance between two single-precision 2D vectors.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): The first vector.

- `b` ([Vector2f](./vector2f.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The squared distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b)


**Summary:**
Calculates the Euclidean distance between two single-precision 2D vectors.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): The first vector.

- `b` ([Vector2f](./vector2f.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) DistanceSq([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Calculates the squared Euclidean distance between two single-precision 3D vectors.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The first vector.

- `b` ([Vector3f](./vector3f.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The squared distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Calculates the Euclidean distance between two single-precision 3D vectors.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The first vector.

- `b` ([Vector3f](./vector3f.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) DistanceSq([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b)


**Summary:**
Calculates the squared Euclidean distance between two single-precision 4D vectors.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): The first vector.

- `b` ([Vector4f](./vector4f.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The squared distance.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Distance([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b)


**Summary:**
Calculates the Euclidean distance between two single-precision 4D vectors.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): The first vector.

- `b` ([Vector4f](./vector4f.md)): The second vector.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The distance.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) DistanceSq([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b)


**Summary:**
Calculates the squared Euclidean distance between two double-precision 2D vectors.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): The first vector.

- `b` ([Vector2d](./vector2d.md)): The second vector.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The squared distance.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Distance([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b)


**Summary:**
Calculates the Euclidean distance between two double-precision 2D vectors.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): The first vector.

- `b` ([Vector2d](./vector2d.md)): The second vector.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The distance.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) DistanceSq([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Calculates the squared Euclidean distance between two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The first vector.

- `b` ([Vector3d](./vector3d.md)): The second vector.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The squared distance.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Distance([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Calculates the Euclidean distance between two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The first vector.

- `b` ([Vector3d](./vector3d.md)): The second vector.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The distance.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) DistanceSq([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b)


**Summary:**
Calculates the squared Euclidean distance between two double-precision 4D vectors.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): The first vector.

- `b` ([Vector4d](./vector4d.md)): The second vector.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The squared distance.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Distance([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b)


**Summary:**
Calculates the Euclidean distance between two double-precision 4D vectors.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): The first vector.

- `b` ([Vector4d](./vector4d.md)): The second vector.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The distance.

---
#### public static [Int32](https://learn.microsoft.com/dotnet/api/system.int32) Dot([Vector2i](./vector2i.md) a, [Vector2i](./vector2i.md) b)


**Summary:**
Calculates the dot product of two integer 2D vectors.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): The first vector operand.

- `b` ([Vector2i](./vector2i.md)): The second vector operand.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The scalar dot product.

---
#### public static [Int32](https://learn.microsoft.com/dotnet/api/system.int32) Dot([Vector3i](./vector3i.md) a, [Vector3i](./vector3i.md) b)


**Summary:**
Calculates the dot product of two integer 3D vectors.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): The first vector operand.

- `b` ([Vector3i](./vector3i.md)): The second vector operand.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The scalar dot product.

---
#### public static [Int32](https://learn.microsoft.com/dotnet/api/system.int32) Dot([Vector4i](./vector4i.md) a, [Vector4i](./vector4i.md) b)


**Summary:**
Calculates the dot product of two integer 4D vectors.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): The first vector operand.

- `b` ([Vector4i](./vector4i.md)): The second vector operand.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The scalar dot product.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Dot([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b)


**Summary:**
Calculates the dot product of two single-precision 2D vectors.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): The first vector operand.

- `b` ([Vector2f](./vector2f.md)): The second vector operand.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The scalar dot product.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Dot([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Calculates the dot product of two single-precision 3D vectors.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The first vector operand.

- `b` ([Vector3f](./vector3f.md)): The second vector operand.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The scalar dot product.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Dot([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b)


**Summary:**
Calculates the dot product of two single-precision 4D vectors.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): The first vector operand.

- `b` ([Vector4f](./vector4f.md)): The second vector operand.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The scalar dot product.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Dot([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b)


**Summary:**
Calculates the dot product of two double-precision 2D vectors.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): The first vector operand.

- `b` ([Vector2d](./vector2d.md)): The second vector operand.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The scalar dot product.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Dot([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Calculates the dot product of two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The first vector operand.

- `b` ([Vector3d](./vector3d.md)): The second vector operand.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The scalar dot product.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Dot([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b)


**Summary:**
Calculates the dot product of two double-precision 4D vectors.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): The first vector operand.

- `b` ([Vector4d](./vector4d.md)): The second vector operand.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The scalar dot product.

---
#### public static [Vector2f](./vector2f.md) Clamp([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) min, [Vector2f](./vector2f.md) max)


**Summary:**
Clamps the components of a 2D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 

- `min` ([Vector2f](./vector2f.md)): 

- `max` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Clamp([Vector2f](./vector2f.md) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Clamps the components of a 2D vector to a scalar range.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Clamp([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) min, [Vector3f](./vector3f.md) max)


**Summary:**
Clamps the components of a 3D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 

- `min` ([Vector3f](./vector3f.md)): 

- `max` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Clamp([Vector3f](./vector3f.md) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Clamps the components of a 3D vector to a scalar range.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Clamp([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) min, [Vector4f](./vector4f.md) max)


**Summary:**
Clamps the components of a 4D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 

- `min` ([Vector4f](./vector4f.md)): 

- `max` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Clamp([Vector4f](./vector4f.md) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Clamps the components of a 4D vector to a scalar range.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Min([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b)


**Summary:**
Returns the component-wise minimum of two 2D vectors.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Min([Vector2f](./vector2f.md) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the component-wise minimum between a 2D vector and a scalar value.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Min([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Returns the component-wise minimum of two 3D vectors.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Min([Vector3f](./vector3f.md) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the component-wise minimum between a 3D vector and a scalar value.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Min([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b)


**Summary:**
Returns the component-wise minimum of two 4D vectors.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Min([Vector4f](./vector4f.md) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the component-wise minimum between a 4D vector and a scalar value.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Max([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b)


**Summary:**
Returns the component-wise maximum of two 2D vectors.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Max([Vector2f](./vector2f.md) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the component-wise maximum between a 2D vector and a scalar value.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Max([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b)


**Summary:**
Returns the component-wise maximum of two 3D vectors.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Max([Vector3f](./vector3f.md) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the component-wise maximum between a 3D vector and a scalar value.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Max([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b)


**Summary:**
Returns the component-wise maximum of two 4D vectors.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Max([Vector4f](./vector4f.md) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the component-wise maximum between a 4D vector and a scalar value.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Ceil([Vector2f](./vector2f.md) f)


**Summary:**
Computes the smallest integral values greater than or equal to each component of a 2D vector.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Ceil([Vector3f](./vector3f.md) f)


**Summary:**
Computes the smallest integral values greater than or equal to each component of a 3D vector.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Ceil([Vector4f](./vector4f.md) f)


**Summary:**
Computes the smallest integral values greater than or equal to each component of a 4D vector.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Floor([Vector2f](./vector2f.md) f)


**Summary:**
Computes the largest integral values less than or equal to each component of a 2D vector.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Floor([Vector3f](./vector3f.md) f)


**Summary:**
Computes the largest integral values less than or equal to each component of a 3D vector.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Floor([Vector4f](./vector4f.md) f)


**Summary:**
Computes the largest integral values less than or equal to each component of a 4D vector.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Round([Vector2f](./vector2f.md) f)


**Summary:**
Rounds each component of a 2D vector to the nearest integral value.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Round([Vector3f](./vector3f.md) f)


**Summary:**
Rounds each component of a 3D vector to the nearest integral value.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Round([Vector4f](./vector4f.md) f)


**Summary:**
Rounds each component of a 4D vector to the nearest integral value.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Saturate([Vector2f](./vector2f.md) v)


**Summary:**
Clamps each component of a 2D vector to the range [0, 1].

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Saturate([Vector3f](./vector3f.md) v)


**Summary:**
Clamps each component of a 3D vector to the range [0, 1].

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Saturate([Vector4f](./vector4f.md) v)


**Summary:**
Clamps each component of a 4D vector to the range [0, 1].

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Wrap([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) min, [Vector2f](./vector2f.md) max)


**Summary:**
Wraps each component of a 2D vector into the specified boundary ranges.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 

- `min` ([Vector2f](./vector2f.md)): 

- `max` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Wrap([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) min, [Vector3f](./vector3f.md) max)


**Summary:**
Wraps each component of a 3D vector into the specified boundary ranges.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 

- `min` ([Vector3f](./vector3f.md)): 

- `max` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Wrap([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) min, [Vector4f](./vector4f.md) max)


**Summary:**
Wraps each component of a 4D vector into the specified boundary ranges.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 

- `min` ([Vector4f](./vector4f.md)): 

- `max` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) PingPong([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) min, [Vector2f](./vector2f.md) max)


**Summary:**
Oscillates each component of a 2D vector between the specified bounds.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 

- `min` ([Vector2f](./vector2f.md)): 

- `max` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) PingPong([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) min, [Vector3f](./vector3f.md) max)


**Summary:**
Oscillates each component of a 3D vector between the specified bounds.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 

- `min` ([Vector3f](./vector3f.md)): 

- `max` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) PingPong([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) min, [Vector4f](./vector4f.md) max)


**Summary:**
Oscillates each component of a 4D vector between the specified bounds.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 

- `min` ([Vector4f](./vector4f.md)): 

- `max` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2d](./vector2d.md) Clamp([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) min, [Vector2d](./vector2d.md) max)


**Summary:**
Clamps the components of a double-precision 2D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 

- `min` ([Vector2d](./vector2d.md)): 

- `max` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Clamp([Vector2d](./vector2d.md) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Clamps the components of a double-precision 2D vector to a scalar range.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Clamp([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) min, [Vector3d](./vector3d.md) max)


**Summary:**
Clamps the components of a double-precision 3D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 

- `min` ([Vector3d](./vector3d.md)): 

- `max` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Clamp([Vector3d](./vector3d.md) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Clamps the components of a double-precision 3D vector to a scalar range.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Clamp([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) min, [Vector4d](./vector4d.md) max)


**Summary:**
Clamps the components of a double-precision 4D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 

- `min` ([Vector4d](./vector4d.md)): 

- `max` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Clamp([Vector4d](./vector4d.md) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Clamps the components of a double-precision 4D vector to a scalar range.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Min([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b)


**Summary:**
Returns the component-wise minimum of two double-precision 2D vectors.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Min([Vector2d](./vector2d.md) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the component-wise minimum between a double-precision 2D vector and a scalar value.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Min([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Returns the component-wise minimum of two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Min([Vector3d](./vector3d.md) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the component-wise minimum between a double-precision 3D vector and a scalar value.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Min([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b)


**Summary:**
Returns the component-wise minimum of two double-precision 4D vectors.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Min([Vector4d](./vector4d.md) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the component-wise minimum between a double-precision 4D vector and a scalar value.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Max([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b)


**Summary:**
Returns the component-wise maximum of two double-precision 2D vectors.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Max([Vector2d](./vector2d.md) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the component-wise maximum between a double-precision 2D vector and a scalar value.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Max([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b)


**Summary:**
Returns the component-wise maximum of two double-precision 3D vectors.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Max([Vector3d](./vector3d.md) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the component-wise maximum between a double-precision 3D vector and a scalar value.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Max([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b)


**Summary:**
Returns the component-wise maximum of two double-precision 4D vectors.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Max([Vector4d](./vector4d.md) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the component-wise maximum between a double-precision 4D vector and a scalar value.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Ceil([Vector2d](./vector2d.md) f)


**Summary:**
Computes the smallest integral values greater than or equal to each component of a double-precision 2D vector.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Ceil([Vector3d](./vector3d.md) f)


**Summary:**
Computes the smallest integral values greater than or equal to each component of a double-precision 3D vector.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Ceil([Vector4d](./vector4d.md) f)


**Summary:**
Computes the smallest integral values greater than or equal to each component of a double-precision 4D vector.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Floor([Vector2d](./vector2d.md) f)


**Summary:**
Computes the largest integral values less than or equal to each component of a double-precision 2D vector.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Floor([Vector3d](./vector3d.md) f)


**Summary:**
Computes the largest integral values less than or equal to each component of a double-precision 3D vector.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Floor([Vector4d](./vector4d.md) f)


**Summary:**
Computes the largest integral values less than or equal to each component of a double-precision 4D vector.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Round([Vector2d](./vector2d.md) f)


**Summary:**
Rounds each component of a double-precision 2D vector to the nearest integral value.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Round([Vector3d](./vector3d.md) f)


**Summary:**
Rounds each component of a double-precision 3D vector to the nearest integral value.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Round([Vector4d](./vector4d.md) f)


**Summary:**
Rounds each component of a double-precision 4D vector to the nearest integral value.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Saturate([Vector2d](./vector2d.md) v)


**Summary:**
Clamps each component of a double-precision 2D vector to the range [0, 1].

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Saturate([Vector3d](./vector3d.md) v)


**Summary:**
Clamps each component of a double-precision 3D vector to the range [0, 1].

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Saturate([Vector4d](./vector4d.md) v)


**Summary:**
Clamps each component of a double-precision 4D vector to the range [0, 1].

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Wrap([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) min, [Vector2d](./vector2d.md) max)


**Summary:**
Wraps each component of a double-precision 2D vector into the specified boundary ranges.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 

- `min` ([Vector2d](./vector2d.md)): 

- `max` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Wrap([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) min, [Vector3d](./vector3d.md) max)


**Summary:**
Wraps each component of a double-precision 3D vector into the specified boundary ranges.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 

- `min` ([Vector3d](./vector3d.md)): 

- `max` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Wrap([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) min, [Vector4d](./vector4d.md) max)


**Summary:**
Wraps each component of a double-precision 4D vector into the specified boundary ranges.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 

- `min` ([Vector4d](./vector4d.md)): 

- `max` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) PingPong([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) min, [Vector2d](./vector2d.md) max)


**Summary:**
Oscillates each component of a double-precision 2D vector between the specified bounds.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 

- `min` ([Vector2d](./vector2d.md)): 

- `max` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) PingPong([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) min, [Vector3d](./vector3d.md) max)


**Summary:**
Oscillates each component of a double-precision 3D vector between the specified bounds.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 

- `min` ([Vector3d](./vector3d.md)): 

- `max` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) PingPong([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) min, [Vector4d](./vector4d.md) max)


**Summary:**
Oscillates each component of a double-precision 4D vector between the specified bounds.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 

- `min` ([Vector4d](./vector4d.md)): 

- `max` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2i](./vector2i.md) Clamp([Vector2i](./vector2i.md) v, [Vector2i](./vector2i.md) min, [Vector2i](./vector2i.md) max)


**Summary:**
Clamps the components of an integer 2D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector2i](./vector2i.md)): 

- `min` ([Vector2i](./vector2i.md)): 

- `max` ([Vector2i](./vector2i.md)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector2i](./vector2i.md) Clamp([Vector2i](./vector2i.md) v, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) min, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) max)


**Summary:**
Clamps the components of an integer 2D vector to a scalar range.

**Parameters:**

- `v` ([Vector2i](./vector2i.md)): 

- `min` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `max` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector3i](./vector3i.md) Clamp([Vector3i](./vector3i.md) v, [Vector3i](./vector3i.md) min, [Vector3i](./vector3i.md) max)


**Summary:**
Clamps the components of an integer 3D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector3i](./vector3i.md)): 

- `min` ([Vector3i](./vector3i.md)): 

- `max` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector3i](./vector3i.md) Clamp([Vector3i](./vector3i.md) v, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) min, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) max)


**Summary:**
Clamps the components of an integer 3D vector to a scalar range.

**Parameters:**

- `v` ([Vector3i](./vector3i.md)): 

- `min` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `max` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector4i](./vector4i.md) Clamp([Vector4i](./vector4i.md) v, [Vector4i](./vector4i.md) min, [Vector4i](./vector4i.md) max)


**Summary:**
Clamps the components of an integer 4D vector to the range defined by boundary vectors.

**Parameters:**

- `v` ([Vector4i](./vector4i.md)): 

- `min` ([Vector4i](./vector4i.md)): 

- `max` ([Vector4i](./vector4i.md)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector4i](./vector4i.md) Clamp([Vector4i](./vector4i.md) v, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) min, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) max)


**Summary:**
Clamps the components of an integer 4D vector to a scalar range.

**Parameters:**

- `v` ([Vector4i](./vector4i.md)): 

- `min` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `max` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector2i](./vector2i.md) Min([Vector2i](./vector2i.md) a, [Vector2i](./vector2i.md) b)


**Summary:**
Returns the component-wise minimum of two integer 2D vectors.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): 

- `b` ([Vector2i](./vector2i.md)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector2i](./vector2i.md) Min([Vector2i](./vector2i.md) a, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) b)


**Summary:**
Returns the component-wise minimum between an integer 2D vector and a scalar value.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): 

- `b` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector3i](./vector3i.md) Min([Vector3i](./vector3i.md) a, [Vector3i](./vector3i.md) b)


**Summary:**
Returns the component-wise minimum of two integer 3D vectors.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): 

- `b` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector3i](./vector3i.md) Min([Vector3i](./vector3i.md) a, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) b)


**Summary:**
Returns the component-wise minimum between an integer 3D vector and a scalar value.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): 

- `b` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector4i](./vector4i.md) Min([Vector4i](./vector4i.md) a, [Vector4i](./vector4i.md) b)


**Summary:**
Returns the component-wise minimum of two integer 4D vectors.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): 

- `b` ([Vector4i](./vector4i.md)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector4i](./vector4i.md) Min([Vector4i](./vector4i.md) a, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) b)


**Summary:**
Returns the component-wise minimum between an integer 4D vector and a scalar value.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): 

- `b` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector2i](./vector2i.md) Max([Vector2i](./vector2i.md) a, [Vector2i](./vector2i.md) b)


**Summary:**
Returns the component-wise maximum of two integer 2D vectors.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): 

- `b` ([Vector2i](./vector2i.md)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector2i](./vector2i.md) Max([Vector2i](./vector2i.md) a, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) b)


**Summary:**
Returns the component-wise maximum between an integer 2D vector and a scalar value.

**Parameters:**

- `a` ([Vector2i](./vector2i.md)): 

- `b` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector3i](./vector3i.md) Max([Vector3i](./vector3i.md) a, [Vector3i](./vector3i.md) b)


**Summary:**
Returns the component-wise maximum of two integer 3D vectors.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): 

- `b` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector3i](./vector3i.md) Max([Vector3i](./vector3i.md) a, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) b)


**Summary:**
Returns the component-wise maximum between an integer 3D vector and a scalar value.

**Parameters:**

- `a` ([Vector3i](./vector3i.md)): 

- `b` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector4i](./vector4i.md) Max([Vector4i](./vector4i.md) a, [Vector4i](./vector4i.md) b)


**Summary:**
Returns the component-wise maximum of two integer 4D vectors.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): 

- `b` ([Vector4i](./vector4i.md)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector4i](./vector4i.md) Max([Vector4i](./vector4i.md) a, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) b)


**Summary:**
Returns the component-wise maximum between an integer 4D vector and a scalar value.

**Parameters:**

- `a` ([Vector4i](./vector4i.md)): 

- `b` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector2f](./vector2f.md) Sqrt([Vector2f](./vector2f.md) f)


**Summary:**
Returns the square root of each component in a 2D vector.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Sqrt([Vector3f](./vector3f.md) f)


**Summary:**
Returns the square root of each component in a 3D vector.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Sqrt([Vector4f](./vector4f.md) f)


**Summary:**
Returns the square root of each component in a 4D vector.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Pow([Vector2f](./vector2f.md) f, [Vector2f](./vector2f.md) p)


**Summary:**
Raises each component of a 2D vector to the power specified by a component vector.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 

- `p` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Pow([Vector2f](./vector2f.md) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Raises each component of a 2D vector to a scalar power.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Pow([Vector3f](./vector3f.md) f, [Vector3f](./vector3f.md) p)


**Summary:**
Raises each component of a 3D vector to the power specified by a component vector.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 

- `p` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Pow([Vector3f](./vector3f.md) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Raises each component of a 3D vector to a scalar power.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Pow([Vector4f](./vector4f.md) f, [Vector4f](./vector4f.md) p)


**Summary:**
Raises each component of a 4D vector to the power specified by a component vector.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 

- `p` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Pow([Vector4f](./vector4f.md) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Raises each component of a 4D vector to a scalar power.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Exp([Vector2f](./vector2f.md) power)


**Summary:**
Returns e raised to the power of each component in a 2D vector.

**Parameters:**

- `power` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Exp([Vector3f](./vector3f.md) power)


**Summary:**
Returns e raised to the power of each component in a 3D vector.

**Parameters:**

- `power` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Exp([Vector4f](./vector4f.md) power)


**Summary:**
Returns e raised to the power of each component in a 4D vector.

**Parameters:**

- `power` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Log([Vector2f](./vector2f.md) f, [Vector2f](./vector2f.md) p)


**Summary:**
Calculates the logarithm of each component of a 2D vector in the specified base vector components.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 

- `p` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Log([Vector2f](./vector2f.md) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Calculates the logarithm of each component of a 2D vector in a specified scalar base.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Log([Vector2f](./vector2f.md) f)


**Summary:**
Calculates the natural (base e) logarithm of each component of a 2D vector.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Log([Vector3f](./vector3f.md) f, [Vector3f](./vector3f.md) p)


**Summary:**
Calculates the logarithm of each component of a 3D vector in the specified base vector components.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 

- `p` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Log([Vector3f](./vector3f.md) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Calculates the logarithm of each component of a 3D vector in a specified scalar base.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Log([Vector3f](./vector3f.md) f)


**Summary:**
Calculates the natural (base e) logarithm of each component of a 3D vector.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Log([Vector4f](./vector4f.md) f, [Vector4f](./vector4f.md) p)


**Summary:**
Calculates the logarithm of each component of a 4D vector in the specified base vector components.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 

- `p` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Log([Vector4f](./vector4f.md) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Calculates the logarithm of each component of a 4D vector in a specified scalar base.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Log([Vector4f](./vector4f.md) f)


**Summary:**
Calculates the natural (base e) logarithm of each component of a 4D vector.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Log10([Vector2f](./vector2f.md) f)


**Summary:**
Calculates the base-10 logarithm of each component of a 2D vector.

**Parameters:**

- `f` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Log10([Vector3f](./vector3f.md) f)


**Summary:**
Calculates the base-10 logarithm of each component of a 3D vector.

**Parameters:**

- `f` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Log10([Vector4f](./vector4f.md) f)


**Summary:**
Calculates the base-10 logarithm of each component of a 4D vector.

**Parameters:**

- `f` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2d](./vector2d.md) Sqrt([Vector2d](./vector2d.md) f)


**Summary:**
Returns the square root of each component in a double-precision 2D vector.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Sqrt([Vector3d](./vector3d.md) f)


**Summary:**
Returns the square root of each component in a double-precision 3D vector.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Sqrt([Vector4d](./vector4d.md) f)


**Summary:**
Returns the square root of each component in a double-precision 4D vector.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Pow([Vector2d](./vector2d.md) f, [Vector2d](./vector2d.md) p)


**Summary:**
Raises each component of a double-precision 2D vector to the power specified by a component vector.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 

- `p` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Pow([Vector2d](./vector2d.md) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Raises each component of a double-precision 2D vector to a scalar power.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Pow([Vector3d](./vector3d.md) f, [Vector3d](./vector3d.md) p)


**Summary:**
Raises each component of a double-precision 3D vector to the power specified by a component vector.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 

- `p` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Pow([Vector3d](./vector3d.md) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Raises each component of a double-precision 3D vector to a scalar power.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Pow([Vector4d](./vector4d.md) f, [Vector4d](./vector4d.md) p)


**Summary:**
Raises each component of a double-precision 4D vector to the power specified by a component vector.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 

- `p` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Pow([Vector4d](./vector4d.md) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Raises each component of a double-precision 4D vector to a scalar power.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Exp([Vector2d](./vector2d.md) power)


**Summary:**
Returns e raised to the power of each component in a double-precision 2D vector.

**Parameters:**

- `power` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Exp([Vector3d](./vector3d.md) power)


**Summary:**
Returns e raised to the power of each component in a double-precision 3D vector.

**Parameters:**

- `power` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Exp([Vector4d](./vector4d.md) power)


**Summary:**
Returns e raised to the power of each component in a double-precision 4D vector.

**Parameters:**

- `power` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Log([Vector2d](./vector2d.md) f, [Vector2d](./vector2d.md) p)


**Summary:**
Calculates the logarithm of each component of a double-precision 2D vector in the specified base vector components.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 

- `p` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Log([Vector2d](./vector2d.md) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Calculates the logarithm of each component of a double-precision 2D vector in a specified scalar base.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Log([Vector2d](./vector2d.md) f)


**Summary:**
Calculates the natural (base e) logarithm of each component of a double-precision 2D vector.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Log([Vector3d](./vector3d.md) f, [Vector3d](./vector3d.md) p)


**Summary:**
Calculates the logarithm of each component of a double-precision 3D vector in the specified base vector components.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 

- `p` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Log([Vector3d](./vector3d.md) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Calculates the logarithm of each component of a double-precision 3D vector in a specified scalar base.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Log([Vector3d](./vector3d.md) f)


**Summary:**
Calculates the natural (base e) logarithm of each component of a double-precision 3D vector.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Log([Vector4d](./vector4d.md) f, [Vector4d](./vector4d.md) p)


**Summary:**
Calculates the logarithm of each component of a double-precision 4D vector in the specified base vector components.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 

- `p` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Log([Vector4d](./vector4d.md) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Calculates the logarithm of each component of a double-precision 4D vector in a specified scalar base.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Log([Vector4d](./vector4d.md) f)


**Summary:**
Calculates the natural (base e) logarithm of each component of a double-precision 4D vector.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Log10([Vector2d](./vector2d.md) f)


**Summary:**
Calculates the base-10 logarithm of each component of a double-precision 2D vector.

**Parameters:**

- `f` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Log10([Vector3d](./vector3d.md) f)


**Summary:**
Calculates the base-10 logarithm of each component of a double-precision 3D vector.

**Parameters:**

- `f` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Log10([Vector4d](./vector4d.md) f)


**Summary:**
Calculates the base-10 logarithm of each component of a double-precision 4D vector.

**Parameters:**

- `f` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2f](./vector2f.md) Lerp([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Linearly interpolates between two 2D vectors by a scalar interpolation factor.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Vector2f](./vector2f.md)): 

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Lerp([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b, [Vector2f](./vector2f.md) t)


**Summary:**
Linearly interpolates component-wise between two 2D vectors by a component interpolation factor.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Vector2f](./vector2f.md)): 

- `t` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Lerp([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Linearly interpolates between two 3D vectors by a scalar interpolation factor.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Vector3f](./vector3f.md)): 

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Lerp([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b, [Vector3f](./vector3f.md) t)


**Summary:**
Linearly interpolates component-wise between two 3D vectors by a component interpolation factor.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Vector3f](./vector3f.md)): 

- `t` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Lerp([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Linearly interpolates between two 4D vectors by a scalar interpolation factor.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Vector4f](./vector4f.md)): 

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Lerp([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b, [Vector4f](./vector4f.md) t)


**Summary:**
Linearly interpolates component-wise between two 4D vectors by a component interpolation factor.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Vector4f](./vector4f.md)): 

- `t` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) InvLerp([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b, [Vector2f](./vector2f.md) x)


**Summary:**
Calculates the component-wise inverse linear interpolation factor for a 2D vector within a boundary range.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): 

- `b` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) InvLerp([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b, [Vector3f](./vector3f.md) x)


**Summary:**
Calculates the component-wise inverse linear interpolation factor for a 3D vector within a boundary range.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): 

- `b` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) InvLerp([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b, [Vector4f](./vector4f.md) x)


**Summary:**
Calculates the component-wise inverse linear interpolation factor for a 4D vector within a boundary range.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): 

- `b` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Map([Vector2f](./vector2f.md) srcStart, [Vector2f](./vector2f.md) srcEnd, [Vector2f](./vector2f.md) targetStart, [Vector2f](./vector2f.md) targetEnd, [Vector2f](./vector2f.md) x)


**Summary:**
Remaps each component of a 2D vector from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Vector2f](./vector2f.md)): 

- `srcEnd` ([Vector2f](./vector2f.md)): 

- `targetStart` ([Vector2f](./vector2f.md)): 

- `targetEnd` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Map([Vector3f](./vector3f.md) srcStart, [Vector3f](./vector3f.md) srcEnd, [Vector3f](./vector3f.md) targetStart, [Vector3f](./vector3f.md) targetEnd, [Vector3f](./vector3f.md) x)


**Summary:**
Remaps each component of a 3D vector from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Vector3f](./vector3f.md)): 

- `srcEnd` ([Vector3f](./vector3f.md)): 

- `targetStart` ([Vector3f](./vector3f.md)): 

- `targetEnd` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Map([Vector4f](./vector4f.md) srcStart, [Vector4f](./vector4f.md) srcEnd, [Vector4f](./vector4f.md) targetStart, [Vector4f](./vector4f.md) targetEnd, [Vector4f](./vector4f.md) x)


**Summary:**
Remaps each component of a 4D vector from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Vector4f](./vector4f.md)): 

- `srcEnd` ([Vector4f](./vector4f.md)): 

- `targetStart` ([Vector4f](./vector4f.md)): 

- `targetEnd` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2d](./vector2d.md) Lerp([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) t)


**Summary:**
Linearly interpolates between two double-precision 2D vectors by a scalar interpolation factor.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Vector2d](./vector2d.md)): 

- `t` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Lerp([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b, [Vector2d](./vector2d.md) t)


**Summary:**
Linearly interpolates component-wise between two double-precision 2D vectors by a component interpolation factor.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Vector2d](./vector2d.md)): 

- `t` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Lerp([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) t)


**Summary:**
Linearly interpolates between two double-precision 3D vectors by a scalar interpolation factor.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Vector3d](./vector3d.md)): 

- `t` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Lerp([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b, [Vector3d](./vector3d.md) t)


**Summary:**
Linearly interpolates component-wise between two double-precision 3D vectors by a component interpolation factor.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Vector3d](./vector3d.md)): 

- `t` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Lerp([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) t)


**Summary:**
Linearly interpolates between two double-precision 4D vectors by a scalar interpolation factor.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Vector4d](./vector4d.md)): 

- `t` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Lerp([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b, [Vector4d](./vector4d.md) t)


**Summary:**
Linearly interpolates component-wise between two double-precision 4D vectors by a component interpolation factor.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Vector4d](./vector4d.md)): 

- `t` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) InvLerp([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b, [Vector2d](./vector2d.md) x)


**Summary:**
Calculates the component-wise inverse linear interpolation factor for a double-precision 2D vector within a boundary range.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): 

- `b` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) InvLerp([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b, [Vector3d](./vector3d.md) x)


**Summary:**
Calculates the component-wise inverse linear interpolation factor for a double-precision 3D vector within a boundary range.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): 

- `b` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) InvLerp([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b, [Vector4d](./vector4d.md) x)


**Summary:**
Calculates the component-wise inverse linear interpolation factor for a double-precision 4D vector within a boundary range.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): 

- `b` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Map([Vector2d](./vector2d.md) srcStart, [Vector2d](./vector2d.md) srcEnd, [Vector2d](./vector2d.md) targetStart, [Vector2d](./vector2d.md) targetEnd, [Vector2d](./vector2d.md) x)


**Summary:**
Remaps each component of a double-precision 2D vector from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Vector2d](./vector2d.md)): 

- `srcEnd` ([Vector2d](./vector2d.md)): 

- `targetStart` ([Vector2d](./vector2d.md)): 

- `targetEnd` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Map([Vector3d](./vector3d.md) srcStart, [Vector3d](./vector3d.md) srcEnd, [Vector3d](./vector3d.md) targetStart, [Vector3d](./vector3d.md) targetEnd, [Vector3d](./vector3d.md) x)


**Summary:**
Remaps each component of a double-precision 3D vector from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Vector3d](./vector3d.md)): 

- `srcEnd` ([Vector3d](./vector3d.md)): 

- `targetStart` ([Vector3d](./vector3d.md)): 

- `targetEnd` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Map([Vector4d](./vector4d.md) srcStart, [Vector4d](./vector4d.md) srcEnd, [Vector4d](./vector4d.md) targetStart, [Vector4d](./vector4d.md) targetEnd, [Vector4d](./vector4d.md) x)


**Summary:**
Remaps each component of a double-precision 4D vector from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Vector4d](./vector4d.md)): 

- `srcEnd` ([Vector4d](./vector4d.md)): 

- `targetStart` ([Vector4d](./vector4d.md)): 

- `targetEnd` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2f](./vector2f.md) MoveTowards([Vector2f](./vector2f.md) a, [Vector2f](./vector2f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Moves a single-precision 2D vector towards a destination vector by a maximum step delta without overshooting.

**Parameters:**

- `a` ([Vector2f](./vector2f.md)): The starting position vector.

- `b` ([Vector2f](./vector2f.md)): The destination target vector.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum displacement distance permitted.


**Returns:**

- [Vector2f](./vector2f.md): The updated vector position.

---
#### public static [Vector3f](./vector3f.md) MoveTowards([Vector3f](./vector3f.md) a, [Vector3f](./vector3f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Moves a single-precision 3D vector towards a destination vector by a maximum step delta without overshooting.

**Parameters:**

- `a` ([Vector3f](./vector3f.md)): The starting position vector.

- `b` ([Vector3f](./vector3f.md)): The destination target vector.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum displacement distance permitted.


**Returns:**

- [Vector3f](./vector3f.md): The updated vector position.

---
#### public static [Vector4f](./vector4f.md) MoveTowards([Vector4f](./vector4f.md) a, [Vector4f](./vector4f.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Moves a single-precision 4D vector towards a destination vector by a maximum step delta without overshooting.

**Parameters:**

- `a` ([Vector4f](./vector4f.md)): The starting position vector.

- `b` ([Vector4f](./vector4f.md)): The destination target vector.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum displacement distance permitted.


**Returns:**

- [Vector4f](./vector4f.md): The updated vector position.

---
#### public static [Vector2d](./vector2d.md) MoveTowards([Vector2d](./vector2d.md) a, [Vector2d](./vector2d.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Moves a double-precision 2D vector towards a destination vector by a maximum step delta without overshooting.

**Parameters:**

- `a` ([Vector2d](./vector2d.md)): The starting position vector.

- `b` ([Vector2d](./vector2d.md)): The destination target vector.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum displacement distance permitted.


**Returns:**

- [Vector2d](./vector2d.md): The updated vector position.

---
#### public static [Vector3d](./vector3d.md) MoveTowards([Vector3d](./vector3d.md) a, [Vector3d](./vector3d.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Moves a double-precision 3D vector towards a destination vector by a maximum step delta without overshooting.

**Parameters:**

- `a` ([Vector3d](./vector3d.md)): The starting position vector.

- `b` ([Vector3d](./vector3d.md)): The destination target vector.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum displacement distance permitted.


**Returns:**

- [Vector3d](./vector3d.md): The updated vector position.

---
#### public static [Vector4d](./vector4d.md) MoveTowards([Vector4d](./vector4d.md) a, [Vector4d](./vector4d.md) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Moves a double-precision 4D vector towards a destination vector by a maximum step delta without overshooting.

**Parameters:**

- `a` ([Vector4d](./vector4d.md)): The starting position vector.

- `b` ([Vector4d](./vector4d.md)): The destination target vector.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum displacement distance permitted.


**Returns:**

- [Vector4d](./vector4d.md): The updated vector position.

---
#### public static [Vector2f](./vector2f.md) Project([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) onto)


**Summary:**
Projects a single-precision 2D vector onto another target vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): The vector to project.

- `onto` ([Vector2f](./vector2f.md)): The vector to project onto.


**Returns:**

- [Vector2f](./vector2f.md): The orthogonal vector projection of `v` onto `onto`, or zero if `onto` has zero magnitude.

---
#### public static [Vector3f](./vector3f.md) Project([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) onto)


**Summary:**
Projects a single-precision 3D vector onto another target vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): The vector to project.

- `onto` ([Vector3f](./vector3f.md)): The vector to project onto.


**Returns:**

- [Vector3f](./vector3f.md): The orthogonal vector projection of `v` onto `onto`, or zero if `onto` has zero magnitude.

---
#### public static [Vector4f](./vector4f.md) Project([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) onto)


**Summary:**
Projects a single-precision 4D vector onto another target vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): The vector to project.

- `onto` ([Vector4f](./vector4f.md)): The vector to project onto.


**Returns:**

- [Vector4f](./vector4f.md): The orthogonal vector projection of `v` onto `onto`, or zero if `onto` has zero magnitude.

---
#### public static [Vector2d](./vector2d.md) Project([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) onto)


**Summary:**
Projects a double-precision 2D vector onto another target vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): The vector to project.

- `onto` ([Vector2d](./vector2d.md)): The vector to project onto.


**Returns:**

- [Vector2d](./vector2d.md): The orthogonal vector projection of `v` onto `onto`, or zero if `onto` has zero magnitude.

---
#### public static [Vector3d](./vector3d.md) Project([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) onto)


**Summary:**
Projects a double-precision 3D vector onto another target vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): The vector to project.

- `onto` ([Vector3d](./vector3d.md)): The vector to project onto.


**Returns:**

- [Vector3d](./vector3d.md): The orthogonal vector projection of `v` onto `onto`, or zero if `onto` has zero magnitude.

---
#### public static [Vector4d](./vector4d.md) Project([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) onto)


**Summary:**
Projects a double-precision 4D vector onto another target vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): The vector to project.

- `onto` ([Vector4d](./vector4d.md)): The vector to project onto.


**Returns:**

- [Vector4d](./vector4d.md): The orthogonal vector projection of `v` onto `onto`, or zero if `onto` has zero magnitude.

---
#### public static [Vector2f](./vector2f.md) Reflect([Vector2f](./vector2f.md) v, [Vector2f](./vector2f.md) normal)


**Summary:**
Reflects an incident single-precision 2D vector off a surface defined by a surface normal.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): The incident direction vector.

- `normal` ([Vector2f](./vector2f.md)): The normalised surface normal vector.


**Returns:**

- [Vector2f](./vector2f.md): The reflected direction vector.

---
#### public static [Vector3f](./vector3f.md) Reflect([Vector3f](./vector3f.md) v, [Vector3f](./vector3f.md) normal)


**Summary:**
Reflects an incident single-precision 3D vector off a surface defined by a surface normal.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): The incident direction vector.

- `normal` ([Vector3f](./vector3f.md)): The normalised surface normal vector.


**Returns:**

- [Vector3f](./vector3f.md): The reflected direction vector.

---
#### public static [Vector4f](./vector4f.md) Reflect([Vector4f](./vector4f.md) v, [Vector4f](./vector4f.md) normal)


**Summary:**
Reflects an incident single-precision 4D vector off a surface defined by a surface normal.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): The incident direction vector.

- `normal` ([Vector4f](./vector4f.md)): The normalised surface normal vector.


**Returns:**

- [Vector4f](./vector4f.md): The reflected direction vector.

---
#### public static [Vector2d](./vector2d.md) Reflect([Vector2d](./vector2d.md) v, [Vector2d](./vector2d.md) normal)


**Summary:**
Reflects an incident double-precision 2D vector off a surface defined by a surface normal.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): The incident direction vector.

- `normal` ([Vector2d](./vector2d.md)): The normalised surface normal vector.


**Returns:**

- [Vector2d](./vector2d.md): The reflected direction vector.

---
#### public static [Vector3d](./vector3d.md) Reflect([Vector3d](./vector3d.md) v, [Vector3d](./vector3d.md) normal)


**Summary:**
Reflects an incident double-precision 3D vector off a surface defined by a surface normal.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): The incident direction vector.

- `normal` ([Vector3d](./vector3d.md)): The normalised surface normal vector.


**Returns:**

- [Vector3d](./vector3d.md): The reflected direction vector.

---
#### public static [Vector4d](./vector4d.md) Reflect([Vector4d](./vector4d.md) v, [Vector4d](./vector4d.md) normal)


**Summary:**
Reflects an incident double-precision 4D vector off a surface defined by a surface normal.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): The incident direction vector.

- `normal` ([Vector4d](./vector4d.md)): The normalised surface normal vector.


**Returns:**

- [Vector4d](./vector4d.md): The reflected direction vector.

---
#### public static [Vector2f](./vector2f.md) Sign([Vector2f](./vector2f.md) value)


**Summary:**
Returns the component-wise sign of a single-precision 2D vector (1.0f, -1.0f, or 0.0f).

**Parameters:**

- `value` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Sign([Vector3f](./vector3f.md) value)


**Summary:**
Returns the component-wise sign of a single-precision 3D vector (1.0f, -1.0f, or 0.0f).

**Parameters:**

- `value` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Sign([Vector4f](./vector4f.md) value)


**Summary:**
Returns the component-wise sign of a single-precision 4D vector (1.0f, -1.0f, or 0.0f).

**Parameters:**

- `value` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Abs([Vector2f](./vector2f.md) value)


**Summary:**
Returns the component-wise absolute values of a single-precision 2D vector.

**Parameters:**

- `value` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Abs([Vector3f](./vector3f.md) value)


**Summary:**
Returns the component-wise absolute values of a single-precision 3D vector.

**Parameters:**

- `value` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Abs([Vector4f](./vector4f.md) value)


**Summary:**
Returns the component-wise absolute values of a single-precision 4D vector.

**Parameters:**

- `value` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2d](./vector2d.md) Sign([Vector2d](./vector2d.md) value)


**Summary:**
Returns the component-wise sign of a double-precision 2D vector (1.0d, -1.0d, or 0.0d).

**Parameters:**

- `value` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Sign([Vector3d](./vector3d.md) value)


**Summary:**
Returns the component-wise sign of a double-precision 3D vector (1.0d, -1.0d, or 0.0d).

**Parameters:**

- `value` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Sign([Vector4d](./vector4d.md) value)


**Summary:**
Returns the component-wise sign of a double-precision 4D vector (1.0d, -1.0d, or 0.0d).

**Parameters:**

- `value` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Abs([Vector2d](./vector2d.md) value)


**Summary:**
Returns the component-wise absolute values of a double-precision 2D vector.

**Parameters:**

- `value` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Abs([Vector3d](./vector3d.md) value)


**Summary:**
Returns the component-wise absolute values of a double-precision 3D vector.

**Parameters:**

- `value` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Abs([Vector4d](./vector4d.md) value)


**Summary:**
Returns the component-wise absolute values of a double-precision 4D vector.

**Parameters:**

- `value` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2i](./vector2i.md) Sign([Vector2i](./vector2i.md) value)


**Summary:**
Returns the component-wise sign of an integer 2D vector (1, -1, or 0).

**Parameters:**

- `value` ([Vector2i](./vector2i.md)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector3i](./vector3i.md) Sign([Vector3i](./vector3i.md) value)


**Summary:**
Returns the component-wise sign of an integer 3D vector (1, -1, or 0).

**Parameters:**

- `value` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector4i](./vector4i.md) Sign([Vector4i](./vector4i.md) value)


**Summary:**
Returns the component-wise sign of an integer 4D vector (1, -1, or 0).

**Parameters:**

- `value` ([Vector4i](./vector4i.md)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector2i](./vector2i.md) Abs([Vector2i](./vector2i.md) value)


**Summary:**
Returns the component-wise absolute values of an integer 2D vector.

**Parameters:**

- `value` ([Vector2i](./vector2i.md)): 


**Returns:**

- [Vector2i](./vector2i.md): 

---
#### public static [Vector3i](./vector3i.md) Abs([Vector3i](./vector3i.md) value)


**Summary:**
Returns the component-wise absolute values of an integer 3D vector.

**Parameters:**

- `value` ([Vector3i](./vector3i.md)): 


**Returns:**

- [Vector3i](./vector3i.md): 

---
#### public static [Vector4i](./vector4i.md) Abs([Vector4i](./vector4i.md) value)


**Summary:**
Returns the component-wise absolute values of an integer 4D vector.

**Parameters:**

- `value` ([Vector4i](./vector4i.md)): 


**Returns:**

- [Vector4i](./vector4i.md): 

---
#### public static [Vector2f](./vector2f.md) Step([Vector2f](./vector2f.md) edge, [Vector2f](./vector2f.md) x)


**Summary:**
Evaluates a component-wise step function where each component evaluates to 1.0f if exceeding the edge vector component; otherwise 0.0f.

**Parameters:**

- `edge` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) Step([Single](https://learn.microsoft.com/dotnet/api/system.single) edge, [Vector2f](./vector2f.md) x)


**Summary:**
Evaluates a step function across a 2D vector comparing each component against a scalar threshold edge.

**Parameters:**

- `edge` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Step([Vector3f](./vector3f.md) edge, [Vector3f](./vector3f.md) x)


**Summary:**
Evaluates a component-wise step function where each component evaluates to 1.0f if exceeding the edge vector component; otherwise 0.0f.

**Parameters:**

- `edge` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) Step([Single](https://learn.microsoft.com/dotnet/api/system.single) edge, [Vector3f](./vector3f.md) x)


**Summary:**
Evaluates a step function across a 3D vector comparing each component against a scalar threshold edge.

**Parameters:**

- `edge` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Step([Vector4f](./vector4f.md) edge, [Vector4f](./vector4f.md) x)


**Summary:**
Evaluates a component-wise step function where each component evaluates to 1.0f if exceeding the edge vector component; otherwise 0.0f.

**Parameters:**

- `edge` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) Step([Single](https://learn.microsoft.com/dotnet/api/system.single) edge, [Vector4f](./vector4f.md) x)


**Summary:**
Evaluates a step function across a 4D vector comparing each component against a scalar threshold edge.

**Parameters:**

- `edge` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) LinearStep([Vector2f](./vector2f.md) edgeMin, [Vector2f](./vector2f.md) edgeMax, [Vector2f](./vector2f.md) x)


**Summary:**
Performs component-wise clamped linear interpolation across 2D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector2f](./vector2f.md)): 

- `edgeMax` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) LinearStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector2f](./vector2f.md) x)


**Summary:**
Performs component-wise clamped linear interpolation for a 2D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) LinearStep([Vector3f](./vector3f.md) edgeMin, [Vector3f](./vector3f.md) edgeMax, [Vector3f](./vector3f.md) x)


**Summary:**
Performs component-wise clamped linear interpolation across 3D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector3f](./vector3f.md)): 

- `edgeMax` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) LinearStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector3f](./vector3f.md) x)


**Summary:**
Performs component-wise clamped linear interpolation for a 3D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) LinearStep([Vector4f](./vector4f.md) edgeMin, [Vector4f](./vector4f.md) edgeMax, [Vector4f](./vector4f.md) x)


**Summary:**
Performs component-wise clamped linear interpolation across 4D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector4f](./vector4f.md)): 

- `edgeMax` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) LinearStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector4f](./vector4f.md) x)


**Summary:**
Performs component-wise clamped linear interpolation for a 4D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) SmoothStep([Vector2f](./vector2f.md) edgeMin, [Vector2f](./vector2f.md) edgeMax, [Vector2f](./vector2f.md) x)


**Summary:**
Performs smooth Hermite interpolation component-wise across 2D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector2f](./vector2f.md)): 

- `edgeMax` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) SmoothStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector2f](./vector2f.md) x)


**Summary:**
Performs smooth Hermite interpolation for a 2D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) SmoothStep([Vector3f](./vector3f.md) edgeMin, [Vector3f](./vector3f.md) edgeMax, [Vector3f](./vector3f.md) x)


**Summary:**
Performs smooth Hermite interpolation component-wise across 3D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector3f](./vector3f.md)): 

- `edgeMax` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) SmoothStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector3f](./vector3f.md) x)


**Summary:**
Performs smooth Hermite interpolation for a 3D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) SmoothStep([Vector4f](./vector4f.md) edgeMin, [Vector4f](./vector4f.md) edgeMax, [Vector4f](./vector4f.md) x)


**Summary:**
Performs smooth Hermite interpolation component-wise across 4D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector4f](./vector4f.md)): 

- `edgeMax` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) SmoothStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector4f](./vector4f.md) x)


**Summary:**
Performs smooth Hermite interpolation for a 4D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) HardStep([Vector2f](./vector2f.md) edgeMin, [Vector2f](./vector2f.md) edgeMax, [Vector2f](./vector2f.md) x)


**Summary:**
Evaluates a clamped hard step function component-wise across 2D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector2f](./vector2f.md)): 

- `edgeMax` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector2f](./vector2f.md) HardStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector2f](./vector2f.md) x)


**Summary:**
Evaluates a clamped hard step function for a 2D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) HardStep([Vector3f](./vector3f.md) edgeMin, [Vector3f](./vector3f.md) edgeMax, [Vector3f](./vector3f.md) x)


**Summary:**
Evaluates a clamped hard step function component-wise across 3D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector3f](./vector3f.md)): 

- `edgeMax` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector3f](./vector3f.md) HardStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector3f](./vector3f.md) x)


**Summary:**
Evaluates a clamped hard step function for a 3D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) HardStep([Vector4f](./vector4f.md) edgeMin, [Vector4f](./vector4f.md) edgeMax, [Vector4f](./vector4f.md) x)


**Summary:**
Evaluates a clamped hard step function component-wise across 4D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector4f](./vector4f.md)): 

- `edgeMax` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector4f](./vector4f.md) HardStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Vector4f](./vector4f.md) x)


**Summary:**
Evaluates a clamped hard step function for a 4D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2d](./vector2d.md) Step([Vector2d](./vector2d.md) edge, [Vector2d](./vector2d.md) x)


**Summary:**
Evaluates a component-wise step function where each component evaluates to 1.0d if exceeding the edge vector component; otherwise 0.0d.

**Parameters:**

- `edge` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) Step([Double](https://learn.microsoft.com/dotnet/api/system.double) edge, [Vector2d](./vector2d.md) x)


**Summary:**
Evaluates a step function across a double-precision 2D vector comparing each component against a scalar threshold edge.

**Parameters:**

- `edge` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Step([Vector3d](./vector3d.md) edge, [Vector3d](./vector3d.md) x)


**Summary:**
Evaluates a component-wise step function where each component evaluates to 1.0d if exceeding the edge vector component; otherwise 0.0d.

**Parameters:**

- `edge` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) Step([Double](https://learn.microsoft.com/dotnet/api/system.double) edge, [Vector3d](./vector3d.md) x)


**Summary:**
Evaluates a step function across a double-precision 3D vector comparing each component against a scalar threshold edge.

**Parameters:**

- `edge` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Step([Vector4d](./vector4d.md) edge, [Vector4d](./vector4d.md) x)


**Summary:**
Evaluates a component-wise step function where each component evaluates to 1.0d if exceeding the edge vector component; otherwise 0.0d.

**Parameters:**

- `edge` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) Step([Double](https://learn.microsoft.com/dotnet/api/system.double) edge, [Vector4d](./vector4d.md) x)


**Summary:**
Evaluates a step function across a double-precision 4D vector comparing each component against a scalar threshold edge.

**Parameters:**

- `edge` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) LinearStep([Vector2d](./vector2d.md) edgeMin, [Vector2d](./vector2d.md) edgeMax, [Vector2d](./vector2d.md) x)


**Summary:**
Performs component-wise clamped linear interpolation across double-precision 2D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector2d](./vector2d.md)): 

- `edgeMax` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) LinearStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector2d](./vector2d.md) x)


**Summary:**
Performs component-wise clamped linear interpolation for a double-precision 2D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) LinearStep([Vector3d](./vector3d.md) edgeMin, [Vector3d](./vector3d.md) edgeMax, [Vector3d](./vector3d.md) x)


**Summary:**
Performs component-wise clamped linear interpolation across double-precision 3D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector3d](./vector3d.md)): 

- `edgeMax` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) LinearStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector3d](./vector3d.md) x)


**Summary:**
Performs component-wise clamped linear interpolation for a double-precision 3D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) LinearStep([Vector4d](./vector4d.md) edgeMin, [Vector4d](./vector4d.md) edgeMax, [Vector4d](./vector4d.md) x)


**Summary:**
Performs component-wise clamped linear interpolation across double-precision 4D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector4d](./vector4d.md)): 

- `edgeMax` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) LinearStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector4d](./vector4d.md) x)


**Summary:**
Performs component-wise clamped linear interpolation for a double-precision 4D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) SmoothStep([Vector2d](./vector2d.md) edgeMin, [Vector2d](./vector2d.md) edgeMax, [Vector2d](./vector2d.md) x)


**Summary:**
Performs smooth Hermite interpolation component-wise across double-precision 2D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector2d](./vector2d.md)): 

- `edgeMax` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) SmoothStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector2d](./vector2d.md) x)


**Summary:**
Performs smooth Hermite interpolation for a double-precision 2D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) SmoothStep([Vector3d](./vector3d.md) edgeMin, [Vector3d](./vector3d.md) edgeMax, [Vector3d](./vector3d.md) x)


**Summary:**
Performs smooth Hermite interpolation component-wise across double-precision 3D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector3d](./vector3d.md)): 

- `edgeMax` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) SmoothStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector3d](./vector3d.md) x)


**Summary:**
Performs smooth Hermite interpolation for a double-precision 3D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) SmoothStep([Vector4d](./vector4d.md) edgeMin, [Vector4d](./vector4d.md) edgeMax, [Vector4d](./vector4d.md) x)


**Summary:**
Performs smooth Hermite interpolation component-wise across double-precision 4D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector4d](./vector4d.md)): 

- `edgeMax` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) SmoothStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector4d](./vector4d.md) x)


**Summary:**
Performs smooth Hermite interpolation for a double-precision 4D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) HardStep([Vector2d](./vector2d.md) edgeMin, [Vector2d](./vector2d.md) edgeMax, [Vector2d](./vector2d.md) x)


**Summary:**
Evaluates a clamped hard step function component-wise across double-precision 2D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector2d](./vector2d.md)): 

- `edgeMax` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector2d](./vector2d.md) HardStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector2d](./vector2d.md) x)


**Summary:**
Evaluates a clamped hard step function for a double-precision 2D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) HardStep([Vector3d](./vector3d.md) edgeMin, [Vector3d](./vector3d.md) edgeMax, [Vector3d](./vector3d.md) x)


**Summary:**
Evaluates a clamped hard step function component-wise across double-precision 3D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector3d](./vector3d.md)): 

- `edgeMax` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector3d](./vector3d.md) HardStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector3d](./vector3d.md) x)


**Summary:**
Evaluates a clamped hard step function for a double-precision 3D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) HardStep([Vector4d](./vector4d.md) edgeMin, [Vector4d](./vector4d.md) edgeMax, [Vector4d](./vector4d.md) x)


**Summary:**
Evaluates a clamped hard step function component-wise across double-precision 4D boundary vector ranges.

**Parameters:**

- `edgeMin` ([Vector4d](./vector4d.md)): 

- `edgeMax` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector4d](./vector4d.md) HardStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Vector4d](./vector4d.md) x)


**Summary:**
Evaluates a clamped hard step function for a double-precision 4D vector across a scalar boundary range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2f](./vector2f.md) Sin([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the sine of each component in a 2D vector in radians.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Sin([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the sine of each component in a 3D vector in radians.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Sin([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the sine of each component in a 4D vector in radians.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Cos([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the cosine of each component in a 2D vector in radians.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Cos([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the cosine of each component in a 3D vector in radians.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Cos([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the cosine of each component in a 4D vector in radians.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Tan([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the tangent of each component in a 2D vector in radians.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Tan([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the tangent of each component in a 3D vector in radians.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Tan([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the tangent of each component in a 4D vector in radians.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Asin([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the angle in radians whose sine is each component of a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Asin([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the angle in radians whose sine is each component of a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Asin([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the angle in radians whose sine is each component of a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Acos([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the angle in radians whose cosine is each component of a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Acos([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the angle in radians whose cosine is each component of a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Acos([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the angle in radians whose cosine is each component of a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Atan([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the angle in radians whose tangent is each component of a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Atan([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the angle in radians whose tangent is each component of a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Atan([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the angle in radians whose tangent is each component of a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Atan2([Vector2f](./vector2f.md) y, [Vector2f](./vector2f.md) x)


**Summary:**
Calculates component-wise the angle in radians whose tangent is the quotient of corresponding components from two 2D vectors.

**Parameters:**

- `y` ([Vector2f](./vector2f.md)): 

- `x` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Atan2([Vector3f](./vector3f.md) y, [Vector3f](./vector3f.md) x)


**Summary:**
Calculates component-wise the angle in radians whose tangent is the quotient of corresponding components from two 3D vectors.

**Parameters:**

- `y` ([Vector3f](./vector3f.md)): 

- `x` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Atan2([Vector4f](./vector4f.md) y, [Vector4f](./vector4f.md) x)


**Summary:**
Calculates component-wise the angle in radians whose tangent is the quotient of corresponding components from two 4D vectors.

**Parameters:**

- `y` ([Vector4f](./vector4f.md)): 

- `x` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Sinh([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the hyperbolic sine of each component in a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Sinh([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the hyperbolic sine of each component in a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Sinh([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the hyperbolic sine of each component in a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Cosh([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the hyperbolic cosine of each component in a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Cosh([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the hyperbolic cosine of each component in a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Cosh([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the hyperbolic cosine of each component in a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Tanh([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the hyperbolic tangent of each component in a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Tanh([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the hyperbolic tangent of each component in a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Tanh([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the hyperbolic tangent of each component in a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Asinh([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the angle whose hyperbolic sine is each component of a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Asinh([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the angle whose hyperbolic sine is each component of a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Asinh([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the angle whose hyperbolic sine is each component of a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Acosh([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the angle whose hyperbolic cosine is each component of a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Acosh([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the angle whose hyperbolic cosine is each component of a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Acosh([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the angle whose hyperbolic cosine is each component of a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2f](./vector2f.md) Atanh([Vector2f](./vector2f.md) v)


**Summary:**
Calculates the angle whose hyperbolic tangent is each component of a 2D vector.

**Parameters:**

- `v` ([Vector2f](./vector2f.md)): 


**Returns:**

- [Vector2f](./vector2f.md): 

---
#### public static [Vector3f](./vector3f.md) Atanh([Vector3f](./vector3f.md) v)


**Summary:**
Calculates the angle whose hyperbolic tangent is each component of a 3D vector.

**Parameters:**

- `v` ([Vector3f](./vector3f.md)): 


**Returns:**

- [Vector3f](./vector3f.md): 

---
#### public static [Vector4f](./vector4f.md) Atanh([Vector4f](./vector4f.md) v)


**Summary:**
Calculates the angle whose hyperbolic tangent is each component of a 4D vector.

**Parameters:**

- `v` ([Vector4f](./vector4f.md)): 


**Returns:**

- [Vector4f](./vector4f.md): 

---
#### public static [Vector2d](./vector2d.md) Sin([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the sine of each component in a double-precision 2D vector in radians.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Sin([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the sine of each component in a double-precision 3D vector in radians.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Sin([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the sine of each component in a double-precision 4D vector in radians.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Cos([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the cosine of each component in a double-precision 2D vector in radians.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Cos([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the cosine of each component in a double-precision 3D vector in radians.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Cos([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the cosine of each component in a double-precision 4D vector in radians.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Tan([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the tangent of each component in a double-precision 2D vector in radians.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Tan([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the tangent of each component in a double-precision 3D vector in radians.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Tan([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the tangent of each component in a double-precision 4D vector in radians.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Asin([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the angle in radians whose sine is each component of a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Asin([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the angle in radians whose sine is each component of a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Asin([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the angle in radians whose sine is each component of a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Acos([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the angle in radians whose cosine is each component of a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Acos([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the angle in radians whose cosine is each component of a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Acos([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the angle in radians whose cosine is each component of a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Atan([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the angle in radians whose tangent is each component of a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Atan([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the angle in radians whose tangent is each component of a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Atan([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the angle in radians whose tangent is each component of a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Atan2([Vector2d](./vector2d.md) y, [Vector2d](./vector2d.md) x)


**Summary:**
Calculates component-wise the angle in radians whose tangent is the quotient of corresponding components from two double-precision 2D vectors.

**Parameters:**

- `y` ([Vector2d](./vector2d.md)): 

- `x` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Atan2([Vector3d](./vector3d.md) y, [Vector3d](./vector3d.md) x)


**Summary:**
Calculates component-wise the angle in radians whose tangent is the quotient of corresponding components from two double-precision 3D vectors.

**Parameters:**

- `y` ([Vector3d](./vector3d.md)): 

- `x` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Atan2([Vector4d](./vector4d.md) y, [Vector4d](./vector4d.md) x)


**Summary:**
Calculates component-wise the angle in radians whose tangent is the quotient of corresponding components from two double-precision 4D vectors.

**Parameters:**

- `y` ([Vector4d](./vector4d.md)): 

- `x` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Sinh([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the hyperbolic sine of each component in a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Sinh([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the hyperbolic sine of each component in a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Sinh([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the hyperbolic sine of each component in a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Cosh([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the hyperbolic cosine of each component in a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Cosh([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the hyperbolic cosine of each component in a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Cosh([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the hyperbolic cosine of each component in a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Tanh([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the hyperbolic tangent of each component in a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Tanh([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the hyperbolic tangent of each component in a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Tanh([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the hyperbolic tangent of each component in a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Asinh([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the angle whose hyperbolic sine is each component of a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Asinh([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the angle whose hyperbolic sine is each component of a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Asinh([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the angle whose hyperbolic sine is each component of a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Acosh([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the angle whose hyperbolic cosine is each component of a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Acosh([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the angle whose hyperbolic cosine is each component of a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Acosh([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the angle whose hyperbolic cosine is each component of a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---
#### public static [Vector2d](./vector2d.md) Atanh([Vector2d](./vector2d.md) v)


**Summary:**
Calculates the angle whose hyperbolic tangent is each component of a double-precision 2D vector.

**Parameters:**

- `v` ([Vector2d](./vector2d.md)): 


**Returns:**

- [Vector2d](./vector2d.md): 

---
#### public static [Vector3d](./vector3d.md) Atanh([Vector3d](./vector3d.md) v)


**Summary:**
Calculates the angle whose hyperbolic tangent is each component of a double-precision 3D vector.

**Parameters:**

- `v` ([Vector3d](./vector3d.md)): 


**Returns:**

- [Vector3d](./vector3d.md): 

---
#### public static [Vector4d](./vector4d.md) Atanh([Vector4d](./vector4d.md) v)


**Summary:**
Calculates the angle whose hyperbolic tangent is each component of a double-precision 4D vector.

**Parameters:**

- `v` ([Vector4d](./vector4d.md)): 


**Returns:**

- [Vector4d](./vector4d.md): 

---


---