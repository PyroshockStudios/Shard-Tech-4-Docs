# GamepadInput

## Summary
Provides polling access, configuration settings, and event-driven dispatching 
for gamepad buttons and analogue axes across connected devices.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See `RunLater` on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Input.Gamepad`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
static class GamepadInput
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **GamepadInput**
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
| `public static get; set; RolloverTime` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the time window (in seconds) between initially holding the game press before the repeat event occurs. |
| `public static get; set; RepeatDelay` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the delay (in seconds) between repeated press events for buttons. |
| `public static get; set; InnerAxisDeadzone` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the inner deadzone threshold applied to all gamepad analog axes. Axis inputs below this magnitude are clamped to 0.0, and remaining values are rescaled accordingly. |
| `public static get; set; OuterAxisDeadzone` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets or sets the outer deadzone threshold applied to all gamepad analog axes. Axis inputs above this magnitude are clamped to 1.0, and remaining values are rescaled accordingly. |


##### `InnerAxisDeadzone` Remarks
Default is <c>0.1</c>. Valid values range from <c>[0.0, 1.0)</c>.

##### `OuterAxisDeadzone` Remarks
Default is <c>1.0</c>. Valid values range from <c>(0.0, 1.0]</c>.


---

## Methods

#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsButtonDown([GamepadIdentifier](./gamepadidentifier.md) deviceId, [GamepadButton](./gamepadbutton.md) button)


**Summary:**
Retrieves whether the specified button is currently held down on the target gamepad.

**Remarks:**
!!! note
    In the case of:
    - [GamepadButton.LeftStickUp](./gamepadbutton.md#leftstickup)
    - [GamepadButton.LeftStickRight](./gamepadbutton.md#leftstickright)
    - [GamepadButton.LeftStickDown](./gamepadbutton.md#leftstickdown)
    - [GamepadButton.LeftStickLeft](./gamepadbutton.md#leftstickleft)
    - [GamepadButton.RightStickUp](./gamepadbutton.md#rightstickup)
    - [GamepadButton.RightStickRight](./gamepadbutton.md#rightstickright)
    - [GamepadButton.RightStickDown](./gamepadbutton.md#rightstickdown)
    - [GamepadButton.RightStickLeft](./gamepadbutton.md#rightstickleft)
    - [GamepadButton.RightTrigger](./gamepadbutton.md#righttrigger)
    - [GamepadButton.LeftTrigger](./gamepadbutton.md#lefttrigger)
    The input is emulated by polling the axis until it passes the deadzone threshold.
    Emulated repeat triggers can be configured via [GamepadInput.RolloverTime](./gamepadinput.md#rollovertime) and [GamepadInput.RepeatDelay](./gamepadinput.md#repeatdelay).

**Parameters:**

- `deviceId` ([GamepadIdentifier](./gamepadidentifier.md)): The identifier representing the target gamepad device.

- `button` ([GamepadButton](./gamepadbutton.md)): The button to query state for.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the device is connected and the button is pressed; 
otherwise, <see langword="false" />.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) GetAxisValue([GamepadIdentifier](./gamepadidentifier.md) deviceId, [GamepadAxis](./gamepadaxis.md) axis)


**Summary:**
Retrieves the post-processed, deadzone-adjusted value of an analog axis on the target gamepad.

**Parameters:**

- `deviceId` ([GamepadIdentifier](./gamepadidentifier.md)): The identifier representing the target gamepad device.

- `axis` ([GamepadAxis](./gamepadaxis.md)): The analog axis to query.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The adjusted axis value (typically normalized between -1.0 and 1.0, or 0.0 and 1.0 for triggers), 
or <c>0.0</c> if the device is not connected.

---
#### public static [Double](https://learn.microsoft.com/dotnet/api/system.double) GetRawAxisValue([GamepadIdentifier](./gamepadidentifier.md) deviceId, [GamepadAxis](./gamepadaxis.md) axis)


**Summary:**
Queries the native layer directly for the raw, unmapped, and unfiltered hardware axis value.

**Parameters:**

- `deviceId` ([GamepadIdentifier](./gamepadidentifier.md)): The identifier representing the target gamepad device.

- `axis` ([GamepadAxis](./gamepadaxis.md)): The analog axis to query.


**Returns:**

- [Double](https://learn.microsoft.com/dotnet/api/system.double): The unmodified native axis value, or <c>0.0</c> if the device is not connected.

---


---