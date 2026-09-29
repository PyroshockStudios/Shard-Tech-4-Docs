# RmlDataModel

## Summary




## Definition

**Namespace:** `SDT4.Managed.UI.Rml.Data`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
abstract class RmlDataModel
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RmlDataModel**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Context` | [RmlContext](../rmlcontext.md) | Returns the context that owns this data model |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Returns the name of the data model. |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) FlagDirty([String?](https://learn.microsoft.com/dotnet/api/system.string) variable)


**Summary:**
Marks the data model as dirty to rebuild (part of) the DOM.
If the `variable` is null, then the entire model is assumed dirty

**Remarks:**
!!! important
    Only top-level variables may be dirtied, i.e. members of this [RmlDataModel](./rmldatamodel.md) instance

**Parameters:**

- `variable` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): <em>Valid</em> name of the variable to specify, or null to dirty the entire document.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

**Remarks:**
!!! danger
    Do NOT call this manually. This will be called by the RmlContext when destroying the data model.
    Invoking this will result in undefined behaviour

---


---