# RMLCanvas



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
| `public get; PrimaryCanvas` | [RMLCanvas](./rmlcanvas.md) |  |
| `public get; Themes` | [RMLThemeQuery](./rmlthemequery.md) |  |


---

## Methods

#### public T LoadDocument&lt;T&gt;([String](https://learn.microsoft.com/dotnet/api/system.string) document)

Loads the document from an rml source file

**Parameters:**

- `document` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Asset path of the RML document


**Returns:**

- T: Document instance

---
#### public [RMLDocument](./rmldocument.md) LoadDocument([String](https://learn.microsoft.com/dotnet/api/system.string) document)

Loads the document from an rml source file without any scripts attatched

**Parameters:**

- `document` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Asset path of the RML document


**Returns:**

- [RMLDocument](./rmldocument.md): Document instance

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DestroyDocument([RMLDocument](./rmldocument.md) document)

Removes the document from the UI

**Parameters:**

- `document` ([RMLDocument](./rmldocument.md)): Document instance


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetDpi([Single](https://learn.microsoft.com/dotnet/api/system.single) dpiScale)

Sets the ratio between the dp/px size

**Parameters:**

- `dpiScale` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Ratio. 1 is default


---
#### public T GetDataModel&lt;T&gt;()

Retrives the data model instantiated for this context

**Returns:**

- T: The exact data model instance

---
#### public [RMLDocument[]](./rmldocument.md) GetAllDocuments()

Retrives all currently loaded documents

**Returns:**

- [RMLDocument[]](./rmldocument.md): List of document instances.

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