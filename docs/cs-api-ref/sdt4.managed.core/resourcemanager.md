# ResourceManager

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class ResourceManager
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **ResourceManager**
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

#### public [Task&lt;AssetLoadResult&lt;TResource&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) LoadAssetAsync&lt;TResource&gt;([AssetID](./asset/assetid.md) assetId)


**Summary:**
Returns an asynchronous task to an [AssetLoadResult&lt;&gt;](./asset/assetloadresult`1.md) containing <typeparamref name="TResource" />

**Parameters:**

- `assetId` ([AssetID](./asset/assetid.md)): A valid asset handle pointing to a resource described by <typeparamref name="TResource" />


**Returns:**

- [Task&lt;AssetLoadResult&lt;TResource&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1): A valid [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) holding the load result.

---
#### public static TResource FromControlBlock&lt;TResource&gt;([IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) block)


**Summary:**
Converts control block pointer to a proper asset handle. 

**Parameters:**

- `block` ([IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr)): Control block pointer.


**Returns:**

- TResource: If `block` is invalid then <strong>NULL</strong> is returned. 
If the underlying data does NOT match <typeparamref name="TResource" />, an [InvalidCastException](https://learn.microsoft.com/dotnet/api/system.invalidcastexception) is thrown, 
Otherwise a valid TResource is returned.

---


---