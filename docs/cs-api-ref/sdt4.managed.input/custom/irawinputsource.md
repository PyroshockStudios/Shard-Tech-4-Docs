# IRawInputSource

## Summary




## Definition

**Namespace:** `SDT4.Managed.Input.Custom`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
interface IRawInputSource
```
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
| `public get; SourceId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | A globally unique identifier for this input source. |
| `public get; ButtonChannels` | [String[]](https://learn.microsoft.com/dotnet/api/system.string) | An immutable list of available button inputs |
| `public get; AxisChannels` | [String[]](https://learn.microsoft.com/dotnet/api/system.string) | An immutable list of available axis inputs |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Initialize()


**Summary:**
Called by [RawInputIngestion](./rawinputingestion.md) when the input source is attached

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Poll([RawInputCommands](./rawinputcommands.md) commands)


**Summary:**
Called by [RawInputIngestion](./rawinputingestion.md) when polling is invoked by the engine

**Parameters:**

- `commands` ([RawInputCommands](./rawinputcommands.md)): Dispatch delegates provided


---


---