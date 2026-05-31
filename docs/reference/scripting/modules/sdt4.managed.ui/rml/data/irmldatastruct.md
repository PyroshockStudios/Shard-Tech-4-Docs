# IRMLDataStruct

RML data structure containing members.
A class implementing this should contain members with the [<see cref="T:SDT4.Managed.UI.RML.Attributes.RMLDataVariableAttribute" />] attribute.

## Definition

**Namespace:** `SDT4.Managed.UI.RML.Data`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
interface IRMLDataStruct
```
**Implements:**

##### [IRMLData](./irmldata.md)
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

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) MemberSetEvent([String](https://learn.microsoft.com/dotnet/api/system.string) memberName)

Called when the data model updates the variable with name <paramref name="memberName" /> directly. This is <strong>NOT</strong> called when a member has its variable updated.

**Parameters:**

- `memberName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Name of the updated member variable


---


---