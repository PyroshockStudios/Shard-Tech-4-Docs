# Scalar

## Summary
The math class containing scalar math operations



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
static class Scalar
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Scalar**
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

#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) NormalizeAngle([Single](https://learn.microsoft.com/dotnet/api/system.single) angle)


**Summary:**
Normalises an angle in radians to the range [-pi, pi].

**Parameters:**

- `angle` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The angle in radians.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The normalised angle in radians.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) DeltaAngle([Single](https://learn.microsoft.com/dotnet/api/system.single) current, [Single](https://learn.microsoft.com/dotnet/api/system.single) target)


**Summary:**
Calculates the shortest angular difference in radians from a current angle to a target angle.

**Parameters:**

- `current` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The current angle in radians.

- `target` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The target angle in radians.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The angular difference in radians within [-pi, pi].

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) NormalizeAngle([Double](https://learn.microsoft.com/dotnet/api/system.double) angle)


**Summary:**
Normalises an angle in radians to the range [-pi, pi].

**Parameters:**

- `angle` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The angle in radians.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The normalised angle in radians.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) DeltaAngle([Double](https://learn.microsoft.com/dotnet/api/system.double) current, [Double](https://learn.microsoft.com/dotnet/api/system.double) target)


**Summary:**
Calculates the shortest angular difference in radians from a current angle to a target angle.

**Parameters:**

- `current` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The current angle in radians.

- `target` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The target angle in radians.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The angular difference in radians within [-pi, pi].

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) ToDeg([Single](https://learn.microsoft.com/dotnet/api/system.single) rad)


**Summary:**
Converts an angle from radians to degrees.

**Parameters:**

- `rad` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The angle in radians.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The angle converted to degrees.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) ToRad([Single](https://learn.microsoft.com/dotnet/api/system.single) deg)


**Summary:**
Converts an angle from degrees to radians.

**Parameters:**

- `deg` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The angle in degrees.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The angle converted to radians.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) ToDeg([Double](https://learn.microsoft.com/dotnet/api/system.double) rad)


**Summary:**
Converts an angle from radians to degrees.

**Parameters:**

- `rad` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The angle in radians.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The angle converted to degrees.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) ToRad([Double](https://learn.microsoft.com/dotnet/api/system.double) deg)


**Summary:**
Converts an angle from degrees to radians.

**Parameters:**

- `deg` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The angle in degrees.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The angle converted to radians.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Approximately([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Determines whether two single-precision floating-point values are approximately equal within precision tolerance.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The first scalar value.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The second scalar value.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the absolute difference is less than [Constants.EpsilonF](./constants.md#epsilonf); otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Approximately([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) tolerance)


**Summary:**
Determines whether two double-precision floating-point values are approximately equal within a given tolerance.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The first scalar value.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The second scalar value.

- `tolerance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximal amount of error allowed.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the absolute difference is less than `tolerance` otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsBetween([Single](https://learn.microsoft.com/dotnet/api/system.single) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Determines whether a value lies within an inclusive range.

**Parameters:**

- `v` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The value to test.

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The inclusive minimum bound.

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The inclusive maximum bound.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `v` is between `min` and `max` inclusive; otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsBetweenExcl([Single](https://learn.microsoft.com/dotnet/api/system.single) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Determines whether a value lies strictly within an exclusive range.

**Parameters:**

- `v` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The value to test.

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The exclusive minimum bound.

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The exclusive maximum bound.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `v` is strictly greater than `min` and strictly less than `max`; otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Approximately([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Determines whether two double-precision floating-point values are approximately equal within precision tolerance.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The first scalar value.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The second scalar value.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the absolute difference is less than [Constants.EpsilonD](./constants.md#epsilond); otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Approximately([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) tolerance)


**Summary:**
Determines whether two double-precision floating-point values are approximately equal within a given tolerance.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The first scalar value.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The second scalar value.

- `tolerance` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximal amount of error allowed.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the absolute difference is less than `tolerance` otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsBetween([Double](https://learn.microsoft.com/dotnet/api/system.double) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Determines whether a value lies within an inclusive range.

**Parameters:**

- `v` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The value to test.

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The inclusive minimum bound.

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The inclusive maximum bound.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `v` is between `min` and `max` inclusive; otherwise, <see langword="false" />.

---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsBetweenExcl([Double](https://learn.microsoft.com/dotnet/api/system.double) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Determines whether a value lies strictly within an exclusive range.

**Parameters:**

- `v` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The value to test.

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The exclusive minimum bound.

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The exclusive maximum bound.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `v` is strictly greater than `min` and strictly less than `max`; otherwise, <see langword="false" />.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) SmoothDamp([Single](https://learn.microsoft.com/dotnet/api/system.single) current, [Single](https://learn.microsoft.com/dotnet/api/system.single) target, ref [Single](https://learn.microsoft.com/dotnet/api/system.single) currentVelocity, [Single](https://learn.microsoft.com/dotnet/api/system.single) smoothTime, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a single-precision scalar value towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The current scalar value.

- `target` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The target destination value.

- `currentVelocity` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): A reference to the current velocity, updated by the method.

- `smoothTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The approximate time required to reach the target.

- `maxSpeed` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The smoothed scalar value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) SmoothDamp([Double](https://learn.microsoft.com/dotnet/api/system.double) current, [Double](https://learn.microsoft.com/dotnet/api/system.double) target, ref [Double](https://learn.microsoft.com/dotnet/api/system.double) currentVelocity, [Double](https://learn.microsoft.com/dotnet/api/system.double) smoothTime, [Double](https://learn.microsoft.com/dotnet/api/system.double) maxSpeed, [Single](https://learn.microsoft.com/dotnet/api/system.single) deltaTime)


**Summary:**
Smoothly transitions a double-precision scalar value towards a target over time using critically damped spring dynamics.

**Parameters:**

- `current` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The current scalar value.

- `target` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The target destination value.

- `currentVelocity` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): A reference to the current velocity, updated by the method.

- `smoothTime` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The approximate time required to reach the target.

- `maxSpeed` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximum speed allowed.

- `deltaTime` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The elapsed time since the previous update.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The smoothed scalar value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Clamp([Single](https://learn.microsoft.com/dotnet/api/system.single) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Clamps a single-precision value to a specified inclusive range.

**Parameters:**

- `v` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The value to clamp.

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The lower bound.

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The upper bound.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The clamped scalar value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Min([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the smaller of two single-precision values.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The first scalar value.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The second scalar value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The smaller value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Max([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b)


**Summary:**
Returns the larger of two single-precision values.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The first scalar value.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The second scalar value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The larger value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Ceil([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Computes the smallest integral value that is greater than or equal to the specified single-precision number.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The ceiling value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Floor([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Computes the largest integral value that is less than or equal to the specified single-precision number.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The floor value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Round([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Rounds a single-precision value to the nearest integer.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The rounded value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Saturate([Single](https://learn.microsoft.com/dotnet/api/system.single) v)


**Summary:**
Clamps a single-precision value to the range [0, 1].

**Parameters:**

- `v` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The value to saturate.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The saturated value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Wrap([Single](https://learn.microsoft.com/dotnet/api/system.single) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Wraps a single-precision value into the range [min, max).

**Parameters:**

- `v` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The inclusive minimum bound.

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The exclusive maximum bound.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The wrapped scalar value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) PingPong([Single](https://learn.microsoft.com/dotnet/api/system.single) v, [Single](https://learn.microsoft.com/dotnet/api/system.single) min, [Single](https://learn.microsoft.com/dotnet/api/system.single) max)


**Summary:**
Oscillates a single-precision value back and forth between a minimum and maximum range.

**Parameters:**

- `v` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The progressing value.

- `min` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The minimum bound.

- `max` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum bound.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The oscillated value within [min, max].

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Clamp([Double](https://learn.microsoft.com/dotnet/api/system.double) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Clamps a double-precision value to a specified inclusive range.

**Parameters:**

- `v` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The value to clamp.

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The lower bound.

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The upper bound.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The clamped scalar value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Min([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the smaller of two double-precision values.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The first scalar value.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The second scalar value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The smaller value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Max([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b)


**Summary:**
Returns the larger of two double-precision values.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The first scalar value.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The second scalar value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The larger value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Ceil([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Computes the smallest integral value that is greater than or equal to the specified double-precision number.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The ceiling value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Floor([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Computes the largest integral value that is less than or equal to the specified double-precision number.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The floor value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Round([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Rounds a double-precision value to the nearest integer.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The rounded value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Saturate([Double](https://learn.microsoft.com/dotnet/api/system.double) v)


**Summary:**
Clamps a double-precision value to the range [0, 1].

**Parameters:**

- `v` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The value to saturate.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The saturated value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Wrap([Double](https://learn.microsoft.com/dotnet/api/system.double) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Wraps a double-precision value into the range [min, max).

**Parameters:**

- `v` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The inclusive minimum bound.

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The exclusive maximum bound.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The wrapped scalar value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) PingPong([Double](https://learn.microsoft.com/dotnet/api/system.double) v, [Double](https://learn.microsoft.com/dotnet/api/system.double) min, [Double](https://learn.microsoft.com/dotnet/api/system.double) max)


**Summary:**
Oscillates a double-precision value back and forth between a minimum and maximum range.

**Parameters:**

- `v` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The progressing value.

- `min` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The minimum bound.

- `max` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The maximum bound.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The oscillated value within [min, max].

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Sqrt([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the square root of a single-precision number.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The square root.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Pow([Single](https://learn.microsoft.com/dotnet/api/system.single) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Raises a single-precision value to a specified power.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The base number.

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The exponent.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The value of `f` raised to `p`.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Exp([Single](https://learn.microsoft.com/dotnet/api/system.single) power)


**Summary:**
Returns e raised to the specified single-precision power.

**Parameters:**

- `power` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The exponent.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The mathematical constant e raised to `power`.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Log([Single](https://learn.microsoft.com/dotnet/api/system.single) f, [Single](https://learn.microsoft.com/dotnet/api/system.single) p)


**Summary:**
Computes the logarithm of a single-precision number in a specified base.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The number whose logarithm is to be computed.

- `p` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The logarithmic base.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The logarithm of `f` in base `p`.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Log([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Computes the natural (base e) logarithm of a single-precision number.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The natural logarithm.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Log10([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Computes the base-10 logarithm of a single-precision number.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The base-10 logarithm.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Sqrt([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the square root of a double-precision number.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The square root.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Pow([Double](https://learn.microsoft.com/dotnet/api/system.double) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Raises a double-precision value to a specified power.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The base number.

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The exponent.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The value of `f` raised to `p`.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Exp([Double](https://learn.microsoft.com/dotnet/api/system.double) power)


**Summary:**
Returns e raised to the specified double-precision power.

**Parameters:**

- `power` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The exponent.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The mathematical constant e raised to `power`.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Log([Double](https://learn.microsoft.com/dotnet/api/system.double) f, [Double](https://learn.microsoft.com/dotnet/api/system.double) p)


**Summary:**
Computes the logarithm of a double-precision number in a specified base.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The number whose logarithm is to be computed.

- `p` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The logarithmic base.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The logarithm of `f` in base `p`.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Log([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Computes the natural (base e) logarithm of a double-precision number.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The natural logarithm.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Log10([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Computes the base-10 logarithm of a double-precision number.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The base-10 logarithm.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Lerp([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Performs a linear interpolation between two single-precision values.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The starting value.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The destination value.

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The interpolation factor.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The interpolated scalar value.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) LerpAngle([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) t)


**Summary:**
Interpolates linearly between two angles in radians, correctly wrapping around circle boundaries along the shortest path.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The starting angle in radians.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The destination angle in radians.

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The interpolation factor.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The interpolated angle in radians.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) InvLerp([Single](https://learn.microsoft.com/dotnet/api/system.single) a, [Single](https://learn.microsoft.com/dotnet/api/system.single) b, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Calculates the inverse linear interpolation factor of a single-precision value within a given range.

**Parameters:**

- `a` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The start of the range.

- `b` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The end of the range.

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The value to query.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The linear interpolation factor t such that Lerp(a, b, t) == x.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Map([Single](https://learn.microsoft.com/dotnet/api/system.single) srcStart, [Single](https://learn.microsoft.com/dotnet/api/system.single) srcEnd, [Single](https://learn.microsoft.com/dotnet/api/system.single) targetStart, [Single](https://learn.microsoft.com/dotnet/api/system.single) targetEnd, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Remaps a single-precision value from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The start bound of the source range.

- `srcEnd` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The end bound of the source range.

- `targetStart` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The start bound of the target range.

- `targetEnd` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The end bound of the target range.

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The value to remap.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The mapped value within the target range.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Lerp([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) t)


**Summary:**
Performs a linear interpolation between two double-precision values.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The starting value.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The destination value.

- `t` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The interpolation factor.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The interpolated scalar value.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) LerpAngle([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) t)


**Summary:**
Interpolates linearly between two angles in radians, correctly wrapping around circle boundaries along the shortest path.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The starting angle in radians.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The destination angle in radians.

- `t` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The interpolation factor.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The interpolated angle in radians.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) InvLerp([Double](https://learn.microsoft.com/dotnet/api/system.double) a, [Double](https://learn.microsoft.com/dotnet/api/system.double) b, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Calculates the inverse linear interpolation factor of a double-precision value within a given range.

**Parameters:**

- `a` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The start of the range.

- `b` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The end of the range.

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The value to query.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The linear interpolation factor t such that Lerp(a, b, t) == x.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Map([Double](https://learn.microsoft.com/dotnet/api/system.double) srcStart, [Double](https://learn.microsoft.com/dotnet/api/system.double) srcEnd, [Double](https://learn.microsoft.com/dotnet/api/system.double) targetStart, [Double](https://learn.microsoft.com/dotnet/api/system.double) targetEnd, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Remaps a double-precision value from an input range to a corresponding target range.

**Parameters:**

- `srcStart` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The start bound of the source range.

- `srcEnd` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The end bound of the source range.

- `targetStart` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The start bound of the target range.

- `targetEnd` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The end bound of the target range.

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The value to remap.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The mapped value within the target range.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) MoveTowards([Single](https://learn.microsoft.com/dotnet/api/system.single) current, [Single](https://learn.microsoft.com/dotnet/api/system.single) target, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Advances a single-precision value towards a target by a maximum step delta without overshooting.

**Parameters:**

- `current` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The current value.

- `target` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The target value to reach.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum step size allowed.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The updated value moving towards `target`.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) MoveTowardsAngle([Single](https://learn.microsoft.com/dotnet/api/system.single) current, [Single](https://learn.microsoft.com/dotnet/api/system.single) target, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDelta)


**Summary:**
Advances an angle in radians towards a target angle along the shortest circular path by a maximum step delta.

**Parameters:**

- `current` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The current angle in radians.

- `target` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The target angle in radians.

- `maxDelta` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The maximum angular step permitted in radians.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The updated angle in radians moving towards `target`.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Sign([Single](https://learn.microsoft.com/dotnet/api/system.single) value)


**Summary:**
Returns the sign of a single-precision value, returning 1.0f for positive, -1.0f for negative, and 0.0f for zero.

**Parameters:**

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 1.0f, -1.0f, or 0.0f indicating the sign.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Abs([Single](https://learn.microsoft.com/dotnet/api/system.single) value)


**Summary:**
Returns the absolute value of a single-precision number.

**Parameters:**

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The non-negative magnitude of `value`.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Sign([Double](https://learn.microsoft.com/dotnet/api/system.double) value)


**Summary:**
Returns the sign of a double-precision value, returning 1.0d for positive, -1.0d for negative, and 0.0d for zero.

**Parameters:**

- `value` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 1.0d, -1.0d, or 0.0d indicating the sign.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Abs([Double](https://learn.microsoft.com/dotnet/api/system.double) value)


**Summary:**
Returns the absolute value of a double-precision number.

**Parameters:**

- `value` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The non-negative magnitude of `value`.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Step([Single](https://learn.microsoft.com/dotnet/api/system.single) edge, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Generates a step function, returning 1.0f if the value exceeds the threshold edge; otherwise 0.0f.

**Parameters:**

- `edge` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The threshold value.

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value to evaluate.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 1.0f if `x` &gt; `edge`; otherwise, 0.0f.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) LinearStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Performs a clamped linear interpolation mapping an input value between two boundary edges to [0, 1].

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The lower threshold edge.

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The upper threshold edge.

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The normalised linear interpolation factor clamped to [0, 1].

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) SmoothStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Performs smooth Hermite interpolation between 0 and 1 when an input value lies within the range [edgeMin, edgeMax].

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The lower threshold edge.

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The upper threshold edge.

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): A smoothly interpolated S-curve factor between 0.0f and 1.0f.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) HardStep([Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMin, [Single](https://learn.microsoft.com/dotnet/api/system.single) edgeMax, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Evaluates a scaled, clamped hard step function across a range.

**Parameters:**

- `edgeMin` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The lower threshold edge.

- `edgeMax` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The scaling multiplier factor.

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The input value.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The calculated hard step value clamped at a lower bound of zero.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Step([Double](https://learn.microsoft.com/dotnet/api/system.double) edge, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Generates a step function, returning 1.0d if the value exceeds the threshold edge; otherwise 0.0d.

**Parameters:**

- `edge` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The threshold value.

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value to evaluate.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 1.0d if `x` &gt; `edge`; otherwise, 0.0d.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) LinearStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Performs a clamped linear interpolation mapping an input value between two boundary edges to [0, 1].

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The lower threshold edge.

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The upper threshold edge.

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The normalised linear interpolation factor clamped to [0, 1].

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) SmoothStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Performs smooth Hermite interpolation between 0 and 1 when an input value lies within the range [edgeMin, edgeMax].

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The lower threshold edge.

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The upper threshold edge.

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): A smoothly interpolated S-curve factor between 0.0d and 1.0d.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) HardStep([Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMin, [Double](https://learn.microsoft.com/dotnet/api/system.double) edgeMax, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Evaluates a scaled, clamped hard step function across a range.

**Parameters:**

- `edgeMin` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The lower threshold edge.

- `edgeMax` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The scaling multiplier factor.

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): The input value.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The calculated hard step value clamped at a lower bound of zero.

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Sin([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the sine of the specified angle in radians.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Cos([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the cosine of the specified angle in radians.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Tan([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the tangent of the specified angle in radians.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Asin([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the angle in radians whose sine is the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Acos([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the angle in radians whose cosine is the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Atan([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the angle in radians whose tangent is the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Atan2([Single](https://learn.microsoft.com/dotnet/api/system.single) y, [Single](https://learn.microsoft.com/dotnet/api/system.single) x)


**Summary:**
Returns the angle in radians whose tangent is the quotient of two specified numbers.

**Parameters:**

- `y` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `x` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Sinh([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the hyperbolic sine of the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Cosh([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the hyperbolic cosine of the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Tanh([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the hyperbolic tangent of the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Asinh([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the angle whose hyperbolic sine is the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Acosh([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the angle whose hyperbolic cosine is the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Single](https://learn.microsoft.com/dotnet/api/system.single) Atanh([Single](https://learn.microsoft.com/dotnet/api/system.single) f)


**Summary:**
Returns the angle whose hyperbolic tangent is the specified value.

**Parameters:**

- `f` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Sin([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the sine of the specified angle in radians.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Cos([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the cosine of the specified angle in radians.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Tan([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the tangent of the specified angle in radians.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Asin([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the angle in radians whose sine is the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Acos([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the angle in radians whose cosine is the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Atan([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the angle in radians whose tangent is the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Atan2([Double](https://learn.microsoft.com/dotnet/api/system.double) y, [Double](https://learn.microsoft.com/dotnet/api/system.double) x)


**Summary:**
Returns the angle in radians whose tangent is the quotient of two specified numbers.

**Parameters:**

- `y` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `x` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Sinh([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the hyperbolic sine of the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Cosh([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the hyperbolic cosine of the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Tanh([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the hyperbolic tangent of the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Asinh([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the angle whose hyperbolic sine is the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Acosh([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the angle whose hyperbolic cosine is the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) Atanh([Double](https://learn.microsoft.com/dotnet/api/system.double) f)


**Summary:**
Returns the angle whose hyperbolic tangent is the specified value.

**Parameters:**

- `f` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): 

---


---