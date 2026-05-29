# WaypointComponent



## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class WaypointComponent
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [AbstractComponent](./abstractcomponent.md) ➔  **WaypointComponent**
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
| `public get; SplineLength` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; set; Granularity` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; set; Looping` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |
| `public get; Points` | [IReadOnlyList&lt;WaypointSplinePoint&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1) |  |


---

## Methods

#### public [WaypointSplinePathPoint](./waypointsplinepathpoint.md) GetPoint([Single](https://learn.microsoft.com/dotnet/api/system.single) t)

**Parameters:**

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [WaypointSplinePathPoint](./waypointsplinepathpoint.md): 

---
#### public [WaypointSplinePathPoint](./waypointsplinepathpoint.md) GetPointAlongDistance([Single](https://learn.microsoft.com/dotnet/api/system.single) d)

**Parameters:**

- `d` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [WaypointSplinePathPoint](./waypointsplinepathpoint.md): 

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) GetSegmentLength([Single](https://learn.microsoft.com/dotnet/api/system.single) tA, [Single](https://learn.microsoft.com/dotnet/api/system.single) tB, [Single](https://learn.microsoft.com/dotnet/api/system.single) dx)

**Parameters:**

- `tA` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `tB` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `dx` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public [WaypointSplinePathPoint](./waypointsplinepathpoint.md) GetNearestPoint([Float3](../math/float3.md) sourcePoint, out [Single](https://learn.microsoft.com/dotnet/api/system.single) t, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) maxKdTreeNeighbourChecks)

**Parameters:**

- `sourcePoint` ([Float3](../math/float3.md)): 

- `t` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 

- `maxKdTreeNeighbourChecks` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [WaypointSplinePathPoint](./waypointsplinepathpoint.md): 

---


---