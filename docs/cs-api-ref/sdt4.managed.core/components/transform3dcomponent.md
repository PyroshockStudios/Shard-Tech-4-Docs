# Transform3DComponent

## Summary
Represents a 3D transformation component attached to an actor, defining position, rotation, and scale in local and world space.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Transform3DComponent
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
| `public static get; ComponentId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | The unique identity of [Transform3DComponent](./transform3dcomponent.md). |
| `public get; Right` | [Vector3f](../math/vector3f.md) | Gets the normalise-length right direction vector in world space. |
| `public get; Up` | [Vector3f](../math/vector3f.md) | Gets the normalise-length upwards direction vector in world space. |
| `public get; Forward` | [Vector3f](../math/vector3f.md) | Gets the normalise-length forward direction vector in world space. |
| `public get; set; Translation` | [Vector3d](../math/vector3d.md) | Gets or sets the translation vector relative to the actor's parent. |
| `public get; set; Rotation` | [Quaternion](../math/quaternion.md) | Gets or sets the orientation quaternion relative to the actor's parent. |
| `public get; set; Scale` | [Vector3f](../math/vector3f.md) | Gets or sets the scale vector relative to the actor's parent. |
| `public get; set; WorldTranslation` | [Vector3d](../math/vector3d.md) | Gets or sets the absolute position vector in world space. |
| `public get; set; WorldRotation` | [Quaternion](../math/quaternion.md) | Gets or sets the absolute orientation quaternion in world space. |
| `public get; set; WorldScale` | [Vector3f](../math/vector3f.md) | Gets or sets the absolute scale vector in world space. |



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