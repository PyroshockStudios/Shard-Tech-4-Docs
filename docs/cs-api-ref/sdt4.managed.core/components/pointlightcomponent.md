# PointLightComponent

## Summary
Represents an omnidirectional point light component attached to an actor.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct PointLightComponent
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
| `public static get; ComponentId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | The unique identity of [PointLightComponent](./pointlightcomponent.md). |
| `public get; set; Color` | [ColorRgba](../math/colorrgba.md) | Gets or sets the light's colour emission. The alpha component is ignored |
| `public get; set; Intensity` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the brightness intensity of the point light. |
| `public get; set; AttenuationRadius` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the maximum distance from the light source at which its illumination attenuates to zero. |



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