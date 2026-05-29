# AppInstance



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
| `public get; Environment` | [InstanceEnvironment](./instanceenvironment.md) |  |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; Version` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; Platform` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; ResourceManager` | [IResourceManager](./iresourcemanager.md) |  |


---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetCapability&lt;TCapability&gt;(out TCapability capability)

**Parameters:**

- `capability` (TCapability): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---