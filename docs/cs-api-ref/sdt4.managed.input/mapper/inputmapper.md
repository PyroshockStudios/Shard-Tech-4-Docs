# InputMapper

## Summary




## Definition

**Namespace:** `SDT4.Managed.Input.Mapper`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
static class InputMapper
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **InputMapper**
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public static MaxInputId` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |



---

## Methods

#### public static [IInputReceiver](./iinputreceiver.md) RegisterInputReceiver([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, [IInputReceiver](./iinputreceiver.md) inputReceiver)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `inputReceiver` ([IInputReceiver](./iinputreceiver.md)): 


**Returns:**

- [IInputReceiver](./iinputreceiver.md): 

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnregisterInputReceiver([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, [IInputReceiver](./iinputreceiver.md) inputReceiver)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `inputReceiver` ([IInputReceiver](./iinputreceiver.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [KeyCode](../desktop/keycode.md) code, [InputModifiers](../desktop/inputmodifiers.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) registerRepeat, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)


**Summary:**
Maps an action binding to a physical keyboard key.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `code` ([KeyCode](../desktop/keycode.md)): Key input

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): Modifiers that must be held down for the input to trigger

- `registerRepeat` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Should repeatedly trigger when the key is held down?

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if `strictModifier` is disabled!)


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseButton](../desktop/mousebutton.md) input, [InputModifiers](../desktop/inputmodifiers.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)


**Summary:**
Maps an action binding to a mouse button.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([MouseButton](../desktop/mousebutton.md)): Mouse input

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): Modifiers that must be held down for the input to trigger

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if `strictModifier` is disabled!)


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [GamepadButton](../gamepad/gamepadbutton.md) input, [GamepadIdentifier](../gamepad/gamepadidentifier.md) gamepadIndex, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) registerRepeat)


**Summary:**
Maps an action binding to a gamepad button.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([GamepadButton](../gamepad/gamepadbutton.md)): Gamepad input

- `gamepadIndex` ([GamepadIdentifier](../gamepad/gamepadidentifier.md)): What gamepad to use

- `registerRepeat` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Should repeatedly trigger when the button is held down?


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseMotionInput](../desktop/mousemotioninput.md) input)


**Summary:**
Maps an action binding to a mouse movement/scroll.<br />
<strong>NOTE:</strong> This will only trigger upon <strong>POSITIVE</strong> values! <strong>ZERO</strong> values will <strong>NOT</strong>
It is thus recommended to use this solely for things such as event triggers, as opposed to field values

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([MouseMotionInput](../desktop/mousemotioninput.md)): Mouse movement input


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindCustomActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [Guid](https://learn.microsoft.com/dotnet/api/system.guid) sourceId, [String](https://learn.microsoft.com/dotnet/api/system.string) channel, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) deviceId)


**Summary:**
Maps a custom button/axis binding from a custom peripheral driver to an action.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `sourceId` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): Input mapper GUID. Provided by [IRawInputSource](../custom/irawinputsource.md)

- `channel` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Input mapper channel name. Provided by [IRawInputSource](../custom/irawinputsource.md)

- `deviceId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): Input device ID. Typically, if used, to designate multiple physical controllers.


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [KeyCode](../desktop/keycode.md) code, [Single](https://learn.microsoft.com/dotnet/api/system.single) value, [InputModifiers](../desktop/inputmodifiers.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)


**Summary:**
Maps an axis range binding to a keyboard key.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `code` ([KeyCode](../desktop/keycode.md)): Key input

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Value of the binding. 1 and -1 are recommended values.

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): Modifiers that must be held down for the input to trigger

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if `strictModifier` is disabled!)


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseButton](../desktop/mousebutton.md) input, [Single](https://learn.microsoft.com/dotnet/api/system.single) value, [InputModifiers](../desktop/inputmodifiers.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)


**Summary:**
Maps an axis range binding to a mouse button.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([MouseButton](../desktop/mousebutton.md)): Mouse input

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Value of the binding. 1 and -1 are recommended values.

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): Modifiers that must be held down for the input to trigger

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if `strictModifier` is disabled!)


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [GamepadButton](../gamepad/gamepadbutton.md) input, [GamepadIdentifier](../gamepad/gamepadidentifier.md) gamepadIndex, [Single](https://learn.microsoft.com/dotnet/api/system.single) value)


**Summary:**
Maps an axis range binding to a digital gamepad button.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([GamepadButton](../gamepad/gamepadbutton.md)): Mouse movement input

- `gamepadIndex` ([GamepadIdentifier](../gamepad/gamepadidentifier.md)): What gamepad to use

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Value of the binding. 1 and -1 are recommended values.


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [GamepadAxis](../gamepad/gamepadaxis.md) input, [GamepadIdentifier](../gamepad/gamepadidentifier.md) gamepadIndex, [Single](https://learn.microsoft.com/dotnet/api/system.single) scale)


**Summary:**
Maps an axis range binding to an analogue gamepad stick or trigger.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([GamepadAxis](../gamepad/gamepadaxis.md)): Mouse movement input

- `gamepadIndex` ([GamepadIdentifier](../gamepad/gamepadidentifier.md)): What gamepad to use

- `scale` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Scale of the movement. This acts as a direct multiplier. Recommended to keep at 1


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseMotionInput](../desktop/mousemotioninput.md) input, [Single](https://learn.microsoft.com/dotnet/api/system.single) sensitivity)


**Summary:**
Maps an axis range binding to continuous mouse movement or scrolling.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `input` ([MouseMotionInput](../desktop/mousemotioninput.md)): Mouse movement input

- `sensitivity` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Scale of the movement. This acts as a direct multiplier


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) BindCustomRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [Guid](https://learn.microsoft.com/dotnet/api/system.guid) sourceId, [String](https://learn.microsoft.com/dotnet/api/system.string) channel, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) deviceId, [Single](https://learn.microsoft.com/dotnet/api/system.single) scale)


**Summary:**
Maps a custom analog axis to a range binding.

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): What binding to map

- `sourceId` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): Input mapper GUID. Provided by [IRawInputSource](../custom/irawinputsource.md)

- `channel` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Input mapper channel name. Provided by [IRawInputSource](../custom/irawinputsource.md)

- `deviceId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): Input device ID. Typically, if used, to designate multiple physical controllers.

- `scale` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Scale of the movement. This acts as a direct multiplier. Recommended to keep at 1


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [KeyCode](../desktop/keycode.md) code, [InputModifiers](../desktop/inputmodifiers.md) modifier)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `code` ([KeyCode](../desktop/keycode.md)): 

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseButton](../desktop/mousebutton.md) input, [InputModifiers](../desktop/inputmodifiers.md) modifier)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([MouseButton](../desktop/mousebutton.md)): 

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [GamepadButton](../gamepad/gamepadbutton.md) input, [GamepadIdentifier](../gamepad/gamepadidentifier.md) gamepadIndex)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([GamepadButton](../gamepad/gamepadbutton.md)): 

- `gamepadIndex` ([GamepadIdentifier](../gamepad/gamepadidentifier.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseMotionInput](../desktop/mousemotioninput.md) input)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([MouseMotionInput](../desktop/mousemotioninput.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindCustomActionMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [Guid](https://learn.microsoft.com/dotnet/api/system.guid) sourceId, [String](https://learn.microsoft.com/dotnet/api/system.string) channel, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) deviceId)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `sourceId` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): 

- `channel` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `deviceId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [KeyCode](../desktop/keycode.md) code, [InputModifiers](../desktop/inputmodifiers.md) modifier)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `code` ([KeyCode](../desktop/keycode.md)): 

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseButton](../desktop/mousebutton.md) input, [InputModifiers](../desktop/inputmodifiers.md) modifier)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([MouseButton](../desktop/mousebutton.md)): 

- `modifier` ([InputModifiers](../desktop/inputmodifiers.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [GamepadButton](../gamepad/gamepadbutton.md) input, [GamepadIdentifier](../gamepad/gamepadidentifier.md) gamepadIndex)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([GamepadButton](../gamepad/gamepadbutton.md)): 

- `gamepadIndex` ([GamepadIdentifier](../gamepad/gamepadidentifier.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [GamepadAxis](../gamepad/gamepadaxis.md) input, [GamepadIdentifier](../gamepad/gamepadidentifier.md) gamepadIndex)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([GamepadAxis](../gamepad/gamepadaxis.md)): 

- `gamepadIndex` ([GamepadIdentifier](../gamepad/gamepadidentifier.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [MouseMotionInput](../desktop/mousemotioninput.md) input)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `input` ([MouseMotionInput](../desktop/mousemotioninput.md)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindCustomRangeMapping&lt;TEnum&gt;([Int32](https://learn.microsoft.com/dotnet/api/system.int32) inputId, TEnum mapping, [Guid](https://learn.microsoft.com/dotnet/api/system.guid) sourceId, [String](https://learn.microsoft.com/dotnet/api/system.string) channel, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) deviceId)

**Parameters:**

- `inputId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `mapping` (TEnum): 

- `sourceId` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): 

- `channel` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `deviceId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---


---