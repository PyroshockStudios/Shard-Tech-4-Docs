# RMLCanvas

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See `RunLater` on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
class RMLCanvas
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RMLCanvas**
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
| `public static get; PrimaryCanvas` | [RMLCanvas](./rmlcanvas.md) |  |
| `public get; Themes` | [RMLThemeQuery](./rmlthemequery.md) |  |
| `public get; Documents` | [RMLDocument[]](./rmldocument.md) | Retrieves all currently loaded documents |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DestroyDocument([RMLDocument](./rmldocument.md) document)


**Summary:**
Removes the document from the UI

**Parameters:**

- `document` ([RMLDocument](./rmldocument.md)): Document instance


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetDpi([Single](https://learn.microsoft.com/dotnet/api/system.single) dpiScale)


**Summary:**
Sets the ratio between the dp/px size

**Parameters:**

- `dpiScale` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Ratio. 1 is default


---
#### public T GetDataModel&lt;T&gt;()


**Summary:**
Retrieves the data model instantiated for this context

**Returns:**

- T: The exact data model instance

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---