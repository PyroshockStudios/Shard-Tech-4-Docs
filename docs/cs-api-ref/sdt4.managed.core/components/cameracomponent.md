# CameraComponent

## Summary
Represents a camera component attached to an actor, defining view and projection parameters for scene rendering.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct CameraComponent
```
**Implements:**

##### [IActorComponent](./iactorcomponent.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Owner` | [ActorHandle](../actorhandle.md) |  |
| `public static get; ComponentId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | The unique identity of [CameraComponent](./cameracomponent.md). |
| `public get; set; ProjectionType` | [ProjectionMode](./projectionmode.md) | Gets or sets the projection mode utilised by the camera. |
| `public get; set; NearPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the distance to the near clipping plane of the frustum. |
| `public get; set; FarPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the distance to the far clipping plane of the frustum. |
| `public get; set; OrthoLeftPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the coordinate of the left clipping plane of the frustum. Only applicable in `Orthographic` mode. |
| `public get; set; OrthoRightPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the coordinate of the right clipping plane of the frustum. Only applicable in `Orthographic` mode. |
| `public get; set; OrthoTopPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the coordinate of the top clipping plane of the frustum. Only applicable in `Orthographic` mode. |
| `public get; set; OrthoBottomPlane` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the coordinate of the bottom clipping plane of the frustum. Only applicable in `Orthographic` mode. |
| `public get; set; PerspectiveFov` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the field of view in radians when operating in `Perspective` mode. |
| `public get; set; AspectRatio` | [Nullable&lt;Single&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) | Gets or sets the aspect ratio (width divided by height) used in `Perspective` mode. |


##### `NearPlane` Remarks
In `Perspective` mode, this value must be strictly positive. In `Orthographic` mode, any valid real number may be specified.

##### `FarPlane` Remarks
In `Perspective` mode, this plane is frequently ignored when the renderer utilises infinite far planes. In `Orthographic` mode, any valid real number may be specified.

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

##### `AspectRatio` Remarks
When set to <see langword="null" />, the aspect ratio is derived automatically from the current viewport resolution.


---

## Methods

#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is equal to the current component.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with the current component.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the specified object is equivalent to this component; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this component.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a string representation of the component.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string representing the component instance.

---


---