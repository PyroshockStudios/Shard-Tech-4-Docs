# CameraComponent

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class CameraComponent
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Component](./component.md) ➔  **CameraComponent**
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
| `public get; set; ProjectionType` | [CameraProjection](../graphics/cameraprojection.md) | The projection type used when defining a camera |
| `public get; set; NearPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The near plane of the frustum. For perspective mode, valid numbers are exclusively positive numbers. Orthographic may assume any valid number |
| `public get; set; FarPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The far plane of the frustum. For perspective mode, this is often discarded to use infinite far planes instead. Orthographic may assume any valid number. |
| `public get; set; OrthoLeftPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The left plane of the frustum. Only valid in [CameraProjection.Orthographic](../graphics/cameraprojection.md#orthographic) mode |
| `public get; set; OrthoRightPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The right plane of the frustum. Only valid in [CameraProjection.Orthographic](../graphics/cameraprojection.md#orthographic) mode |
| `public get; set; OrthoTopPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The top plane of the frustum. Only valid in [CameraProjection.Orthographic](../graphics/cameraprojection.md#orthographic) mode |
| `public get; set; OrthoBottomPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The bottom plane of the frustum. Only valid in [CameraProjection.Orthographic](../graphics/cameraprojection.md#orthographic) mode |
| `public get; set; PerspectiveFov` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | The FOV (in radians) when using the [CameraProjection.Perspective](../graphics/cameraprojection.md#perspective) mode |
| `public get; set; AspectRatio` | [Nullable&lt;Single&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) | The aspect ratio (width / height) used in [CameraProjection.Perspective](../graphics/cameraprojection.md#perspective) mode When set to <em>null</em>, the aspect ratio is computed automatically based off of the viewport's resolution. |


##### `OrthoLeftPlane` Remarks
!!! note
    Shard Tech 4 assumes a left-handed coordinate system.

##### `OrthoRightPlane` Remarks
!!! note
    Shard Tech 4 assumes a left-handed coordinate system.

##### `OrthoTopPlane` Remarks
!!! note
    Shard Tech 4 assumes a left-handed coordinate system.

##### `OrthoBottomPlane` Remarks
!!! note
    Shard Tech 4 assumes a left-handed coordinate system.


---

## Methods

#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---


---