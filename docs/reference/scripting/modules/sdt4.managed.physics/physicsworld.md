# PhysicsWorld



## Definition

**Namespace:** `SDT4.Managed.Physics`  
**Assembly:** `SDT4.Managed.Physics.dll`

```csharp
class PhysicsWorld
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **PhysicsWorld**
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
| `public get; set; Gravity` | [Float3](../sdt4.managed.core/math/float3.md) |  |


---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddPhysicsActor([Actor](../sdt4.managed.core/actor.md) actor)

**Parameters:**

- `actor` ([Actor](../sdt4.managed.core/actor.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) KillPhysicsActor([Actor](../sdt4.managed.core/actor.md) actor)

**Parameters:**

- `actor` ([Actor](../sdt4.managed.core/actor.md)): 


---
#### public [PhysicsVehicleBuilder](./vehicle/physicsvehiclebuilder.md) CreateVehicleActor()

**Returns:**

- [PhysicsVehicleBuilder](./vehicle/physicsvehiclebuilder.md): 

---
#### public [PhysicsRayHit](./physicsrayhit.md) RayCast([Float3](../sdt4.managed.core/math/float3.md) origin, [Float3](../sdt4.managed.core/math/float3.md) direction, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDistance, [PhysicsQueryFlags](./physicsqueryflags.md) flags, [PhysicsQueryFilterFlags](./physicsqueryfilterflags.md) filterFlags)

**Parameters:**

- `origin` ([Float3](../sdt4.managed.core/math/float3.md)): 

- `direction` ([Float3](../sdt4.managed.core/math/float3.md)): 

- `maxDistance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `flags` ([PhysicsQueryFlags](./physicsqueryflags.md)): 

- `filterFlags` ([PhysicsQueryFilterFlags](./physicsqueryfilterflags.md)): 


**Returns:**

- [PhysicsRayHit](./physicsrayhit.md): 

---
#### public [PhysicsRayHit[]](./physicsrayhit.md) RayCastAll([Float3](../sdt4.managed.core/math/float3.md) origin, [Float3](../sdt4.managed.core/math/float3.md) direction, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDistance, [PhysicsQueryFlags](./physicsqueryflags.md) flags, [PhysicsQueryFilterFlags](./physicsqueryfilterflags.md) filterFlags)

**Parameters:**

- `origin` ([Float3](../sdt4.managed.core/math/float3.md)): 

- `direction` ([Float3](../sdt4.managed.core/math/float3.md)): 

- `maxDistance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `flags` ([PhysicsQueryFlags](./physicsqueryflags.md)): 

- `filterFlags` ([PhysicsQueryFilterFlags](./physicsqueryfilterflags.md)): 


**Returns:**

- [PhysicsRayHit[]](./physicsrayhit.md): 

---
#### public [PhysicsSweepHit](./physicssweephit.md) Sweep([RigidShape](./rigidshape.md) shape, [Float3](../sdt4.managed.core/math/float3.md) direction, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDistance, [PhysicsQueryFlags](./physicsqueryflags.md) flags, [PhysicsQueryFilterFlags](./physicsqueryfilterflags.md) filterFlags)

**Parameters:**

- `shape` ([RigidShape](./rigidshape.md)): 

- `direction` ([Float3](../sdt4.managed.core/math/float3.md)): 

- `maxDistance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `flags` ([PhysicsQueryFlags](./physicsqueryflags.md)): 

- `filterFlags` ([PhysicsQueryFilterFlags](./physicsqueryfilterflags.md)): 


**Returns:**

- [PhysicsSweepHit](./physicssweephit.md): 

---
#### public [PhysicsSweepHit[]](./physicssweephit.md) SweepAll([RigidShape](./rigidshape.md) shape, [Float3](../sdt4.managed.core/math/float3.md) direction, [Single](https://learn.microsoft.com/dotnet/api/system.single) maxDistance, [PhysicsQueryFlags](./physicsqueryflags.md) flags, [PhysicsQueryFilterFlags](./physicsqueryfilterflags.md) filterFlags)

**Parameters:**

- `shape` ([RigidShape](./rigidshape.md)): 

- `direction` ([Float3](../sdt4.managed.core/math/float3.md)): 

- `maxDistance` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `flags` ([PhysicsQueryFlags](./physicsqueryflags.md)): 

- `filterFlags` ([PhysicsQueryFilterFlags](./physicsqueryfilterflags.md)): 


**Returns:**

- [PhysicsSweepHit[]](./physicssweephit.md): 

---
#### public [PhysicsOverlapHit](./physicsoverlaphit.md) Overlap([RigidShape](./rigidshape.md) shape, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) getShapeIndex, [PhysicsQueryFilterFlags](./physicsqueryfilterflags.md) filterFlags)

**Parameters:**

- `shape` ([RigidShape](./rigidshape.md)): 

- `getShapeIndex` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `filterFlags` ([PhysicsQueryFilterFlags](./physicsqueryfilterflags.md)): 


**Returns:**

- [PhysicsOverlapHit](./physicsoverlaphit.md): 

---
#### public [PhysicsOverlapHit[]](./physicsoverlaphit.md) OverlapAll([RigidShape](./rigidshape.md) shape, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) getShapeIndex, [PhysicsQueryFilterFlags](./physicsqueryfilterflags.md) filterFlags)

**Parameters:**

- `shape` ([RigidShape](./rigidshape.md)): 

- `getShapeIndex` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `filterFlags` ([PhysicsQueryFilterFlags](./physicsqueryfilterflags.md)): 


**Returns:**

- [PhysicsOverlapHit[]](./physicsoverlaphit.md): 

---


---