# DebugConsole

## Summary




## Definition

**Namespace:** `SDT4.Managed.Debugging`  
**Assembly:** `SDT4.Managed.Debugging.dll`

```csharp
static class DebugConsole
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **DebugConsole**
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

#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) Print([String](https://learn.microsoft.com/dotnet/api/system.string) message, [ColorRgba](../sdt4.managed.core/math/colorrgba.md) textColor, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) printToConsole, [Double](https://learn.microsoft.com/dotnet/api/system.double) duration)


**Summary:**
Prints text to the screen and console, with a certain colour and duration.

**Parameters:**

- `message` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The message to print

- `textColor` ([ColorRgba](../sdt4.managed.core/math/colorrgba.md)): The colour of the printed text on screen

- `printToConsole` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Whether to log the message to the console (will show up in log files)

- `duration` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): How long the text should be visible on screen


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) Print([String](https://learn.microsoft.com/dotnet/api/system.string) message, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) printToConsole, [Double](https://learn.microsoft.com/dotnet/api/system.double) duration)


**Summary:**
Prints text to the screen and console, with a duration.

**Parameters:**

- `message` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The message to print

- `printToConsole` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Whether to log the message to the console (will show up in log files)

- `duration` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): How long the text should be visible on screen


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) Print([String](https://learn.microsoft.com/dotnet/api/system.string) message)


**Summary:**
Prints text to the screen anDebugConsole_PrintToDebugOverlayd console

**Parameters:**

- `message` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The message to print


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) Log([String](https://learn.microsoft.com/dotnet/api/system.string) message, [LogSeverity](./logseverity.md) severity)

**Parameters:**

- `message` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `severity` ([LogSeverity](./logseverity.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) LogReferenceHazard([Object](https://learn.microsoft.com/dotnet/api/system.object) disposed, [Object](https://learn.microsoft.com/dotnet/api/system.object) notifier, [String?](https://learn.microsoft.com/dotnet/api/system.string) additionalMsg)

**Parameters:**

- `disposed` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 

- `notifier` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 

- `additionalMsg` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) LogOwnershipHazard([Object](https://learn.microsoft.com/dotnet/api/system.object) disposed)

**Parameters:**

- `disposed` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


---


---