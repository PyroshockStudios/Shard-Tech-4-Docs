# Gamepad

## Summary




## Definition

**Namespace:** `SDT4.Managed.Input`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
sealed class Gamepad
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Gamepad**
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
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; Index` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public get; set; Deadzone` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Threshold as to when joystick movement is relevant. Not recommended to set to very low values, as minor stick drift is fairly common |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsButtonDown([GamepadButtonInput](./gamepadbuttoninput.md) button)

**Parameters:**

- `button` ([GamepadButtonInput](./gamepadbuttoninput.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Single](https://learn.microsoft.com/dotnet/api/system.single) GetAnalogAxis([GamepadAnalogInput](./gamepadanaloginput.md) analog, [Single](https://learn.microsoft.com/dotnet/api/system.single) deadzoneRange)

**Parameters:**

- `analog` ([GamepadAnalogInput](./gamepadanaloginput.md)): 

- `deadzoneRange` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


**Returns:**

- [Single](https://learn.microsoft.com/dotnet/api/system.single): 

---
#### public static [Gamepad[]](./gamepad.md) GetConnectedGamepads()

**Returns:**

- [Gamepad[]](./gamepad.md): 

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) SetGamepadStateCallback([GamepadConnectionStateDelegate](./gamepadconnectionstatedelegate.md) cb)

**Parameters:**

- `cb` ([GamepadConnectionStateDelegate](./gamepadconnectionstatedelegate.md)): 


---
#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsGamepadPresent([Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex)

**Parameters:**

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---