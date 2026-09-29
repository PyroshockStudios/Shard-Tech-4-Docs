# AxisAlignedBox

## Summary
Represents an axis-aligned bounding box (AABB) 3D space defined by minimum and maximum extents.



## Definition

**Namespace:** `SDT4.Managed.Core.Math`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct AxisAlignedBox
```
**Implements:**

##### [IEquatable&lt;AxisAlignedBox&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public Min` | [Vector3f](./vector3f.md) | The minimum corner point of the bounding box. |
| `public Max` | [Vector3f](./vector3f.md) | The maximum corner point of the bounding box. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; Infinite` | [AxisAlignedBox](./axisalignedbox.md) | Gets an infinite bounding box where minimum bounds exceed maximum bounds. |
| `public get; set; Extent` | [Vector3f](./vector3f.md) | Gets or sets the total size across all dimensions (<c>Max - Min</c>). |
| `public get; set; Position` | [Vector3f](./vector3f.md) | Gets or sets the centre position of the bounding box. |
| `public get; HalfExtent` | [Vector3f](./vector3f.md) | Gets the half-extents of the bounding box (<c>Extent * 0.5f</c>). |
| `public get; IsValid` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the bounding box is valid, meaning all components of [AxisAlignedBox.Min](./axisalignedbox.md#min) are less than or equal to [AxisAlignedBox.Max](./axisalignedbox.md#max). |


##### `Extent` Remarks
Modifying the extent scales the box symmetrically around its current centre position.

##### `Position` Remarks
Modifying the position translates the box while preserving its current dimensions.


---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Intersects([AxisAlignedBox](./axisalignedbox.md) other)


**Summary:**
Determines whether this bounding box intersects another bounding box.

**Parameters:**

- `other` ([AxisAlignedBox](./axisalignedbox.md)): The other bounding box to test against.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the boxes overlap or touch; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Intersect([AxisAlignedBox](./axisalignedbox.md) other, out [AxisAlignedBox](./axisalignedbox.md) result)


**Summary:**
Computes the intersection of this bounding box with another.

**Parameters:**

- `other` ([AxisAlignedBox](./axisalignedbox.md)): The bounding box to intersect with.

- `result` ([AxisAlignedBox](./axisalignedbox.md)): The resulting overlapping bounding box if an intersection occurs; otherwise, an infinite box.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the boxes intersect; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Contains([Vector3f](./vector3f.md) point)


**Summary:**
Determines whether a point lies within or on the boundaries of this bounding box.

**Parameters:**

- `point` ([Vector3f](./vector3f.md)): The 3D point to test.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the point is contained; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Contains([AxisAlignedBox](./axisalignedbox.md) other)


**Summary:**
Determines whether another bounding box is completely enclosed within this bounding box.

**Parameters:**

- `other` ([AxisAlignedBox](./axisalignedbox.md)): The bounding box to test for containment.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `other` is entirely inside; otherwise, <see langword="false" />.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Grow([Vector3f](./vector3f.md) point)


**Summary:**
Expands the bounding box to encapsulate the specified point.

**Parameters:**

- `point` ([Vector3f](./vector3f.md)): The point to include.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Grow([AxisAlignedBox](./axisalignedbox.md) other)


**Summary:**
Expands the bounding box to encapsulate another bounding box.

**Parameters:**

- `other` ([AxisAlignedBox](./axisalignedbox.md)): The bounding box to include.


---
#### public static [AxisAlignedBox](./axisalignedbox.md) Union([AxisAlignedBox](./axisalignedbox.md) a, [AxisAlignedBox](./axisalignedbox.md) b)


**Summary:**
Computes the union of two bounding boxes.

**Parameters:**

- `a` ([AxisAlignedBox](./axisalignedbox.md)): The first bounding box.

- `b` ([AxisAlignedBox](./axisalignedbox.md)): The second bounding box.


**Returns:**

- [AxisAlignedBox](./axisalignedbox.md): A new [AxisAlignedBox](./axisalignedbox.md) enclosing both inputs.

---
#### public [Vector3f](./vector3f.md) ClosestPoint([Vector3f](./vector3f.md) point)


**Summary:**
Clamps a point to the boundaries of the bounding box.

**Parameters:**

- `point` ([Vector3f](./vector3f.md)): The point to clamp.


**Returns:**

- [Vector3f](./vector3f.md): The closest point on or inside the bounding box.

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) DistanceSquared([Vector3f](./vector3f.md) point)


**Summary:**
Returns the squared distance from a point to the nearest point on the bounding box.

**Parameters:**

- `point` ([Vector3f](./vector3f.md)): The 3D point.


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): The squared distance.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) GetCorners([Span&lt;Vector3f&gt;](https://learn.microsoft.com/dotnet/api/system.span-1) corners)


**Summary:**
Populates an array of 8 vertices representing the corners of the box.

**Parameters:**

- `corners` ([Span&lt;Vector3f&gt;](https://learn.microsoft.com/dotnet/api/system.span-1)): A pre-allocated buffer of at least 8 elements to receive the corners.


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([AxisAlignedBox](./axisalignedbox.md) other)


**Summary:**
Determines whether the specified [AxisAlignedBox](./axisalignedbox.md) is equal to the current instance.

**Parameters:**

- `other` ([AxisAlignedBox](./axisalignedbox.md)): The bounding box to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if both boxes have equal bounds; otherwise, <see langword="false" />.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is equal to the current instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is an [AxisAlignedBox](./axisalignedbox.md) and matches bounds; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this bounding box.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Formats the bounding box as a readable string displaying minimum and maximum bounds.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string representation of the bounding box.

---


---