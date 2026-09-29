# AppInstance

## Summary
Represents the running application instance, providing system metadata, resource management, and service capabilities.

## Remarks
<para><b>Master Thread:</b> Operations on this type interact directly with engine and runtime subsystems, and must be executed exclusively on the Master Thread.</para>

## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class AppInstance
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **AppInstance**
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
| `public get; Build` | [InstanceBuild](./instancebuild.md) | Gets the target build configuration under which this instance was compiled. |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the name of the application or game title. |
| `public get; GameVersion` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the game or product version string. |
| `public get; EngineVersion` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the underlying engine runtime version string. |
| `public get; Platform` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the operating system or target platform identifier. |
| `public get; ResourceManager` | [ResourceManager](./resourcemanager.md) | Gets the primary resource manager responsible for asset and bundle resolution. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetCapability&lt;TCapability&gt;(out TCapability capability)


**Summary:**
Attempts to resolve an active capability service registered with the application instance.

**Parameters:**

- `capability` (TCapability): When this method returns, contains the resolved capability instance if found; otherwise, <see langword="null" />.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the capability is registered and was resolved; otherwise, <see langword="false" />.

---
#### public [IEnumerable&lt;ICapability&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateCapabilities()


**Summary:**
Enumerates all active capability services currently registered with the instance.

**Returns:**

- [IEnumerable&lt;ICapability&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): A sequence of registered [ICapability](./capabilities/icapability.md) instances.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a formatted string detailing instance metadata, engine versions, and registered capabilities.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string representation of the application instance.

---


---