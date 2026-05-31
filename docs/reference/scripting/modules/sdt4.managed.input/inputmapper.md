# InputMapper



## Definition

**Namespace:** `SDT4.Managed.Input`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
sealed class InputMapper
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **InputMapper**
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

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindButtonMapping&lt;TEnum&gt;(TEnum mapping, [KeyInput](./keyinput.md) input, [InputModifier](./inputmodifier.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) registerRepeat, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)

Maps a button binding to a key input.

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([KeyInput](./keyinput.md)): Key input

- `modifier` ([InputModifier](./inputmodifier.md)): Modifiers that must be held down for the input to trigger

- `registerRepeat` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Should repeatedly trigger when the key is held down?

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if <paramref name="strictModifier" /> is disabled!)


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindButtonMapping&lt;TEnum&gt;(TEnum mapping, [MouseInput](./mouseinput.md) input, [InputModifier](./inputmodifier.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)

Maps a button binding to a mouse input.

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([MouseInput](./mouseinput.md)): Mouse input

- `modifier` ([InputModifier](./inputmodifier.md)): Modifiers that must be held down for the input to trigger

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if <paramref name="strictModifier" /> is disabled!)


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindButtonMapping&lt;TEnum&gt;(TEnum mapping, [GamepadButtonInput](./gamepadbuttoninput.md) input, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) registerRepeat)

Maps a button binding to a gamepad input.

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([GamepadButtonInput](./gamepadbuttoninput.md)): Gamepad input

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): What gamepad to use

- `registerRepeat` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Should repeatedly trigger when the button is held down?


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindButtonMapping&lt;TEnum&gt;(TEnum mapping, [MouseMotionInput](./mousemotioninput.md) input)

Maps a button binding to a mouse movement/scroll.<br /> <strong>NOTE:</strong> This will only trigger upon <strong>POSITIVE</strong> values! <strong>ZERO</strong> values will <strong>NOT</strong> It is thus recommended to use this solely for things such as event triggers, as opposed to field values

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([MouseMotionInput](./mousemotioninput.md)): Mouse movement input


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindAxisMapping&lt;TEnum&gt;(TEnum mapping, [KeyInput](./keyinput.md) input, [Single](https://learn.microsoft.com/dotnet/api/system.single) value, [InputModifier](./inputmodifier.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)

Maps a button binding to a key input.

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([KeyInput](./keyinput.md)): Key input

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Value of the binding. 1 and -1 are recommended values.

- `modifier` ([InputModifier](./inputmodifier.md)): Modifiers that must be held down for the input to trigger

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if <paramref name="strictModifier" /> is disabled!)


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindAxisMapping&lt;TEnum&gt;(TEnum mapping, [MouseInput](./mouseinput.md) input, [Single](https://learn.microsoft.com/dotnet/api/system.single) value, [InputModifier](./inputmodifier.md) modifier, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) strictModifier)

Maps a button binding to a mouse input.

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([MouseInput](./mouseinput.md)): Mouse input

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Value of the binding. 1 and -1 are recommended values.

- `modifier` ([InputModifier](./inputmodifier.md)): Modifiers that must be held down for the input to trigger

- `strictModifier` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Does the binding require exact modifiers? 
            (If this is disabled, inputs <c>CTRL + A</c> and <c>A</c> will both be triggered if the user presses CTRL+A if <paramref name="strictModifier" /> is disabled!)


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindAxisMapping&lt;TEnum&gt;(TEnum mapping, [GamepadButtonInput](./gamepadbuttoninput.md) input, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex, [Single](https://learn.microsoft.com/dotnet/api/system.single) value)

Maps an axis binding to a joystick boolean input<br />

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([GamepadButtonInput](./gamepadbuttoninput.md)): Mouse movement input

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): What gamepad to use

- `value` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Value of the binding. 1 and -1 are recommended values.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindAxisMapping&lt;TEnum&gt;(TEnum mapping, [GamepadAnalogInput](./gamepadanaloginput.md) input, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex, [Single](https://learn.microsoft.com/dotnet/api/system.single) scale)

Maps an axis binding to a joystick movement (thumbstick or triggers).<br /> This will trigger upon all movement deltas

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([GamepadAnalogInput](./gamepadanaloginput.md)): Mouse movement input

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): What gamepad to use

- `scale` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Scale of the movement. This acts as a direct multiplier. Recommended to keep at 1


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) BindAxisMapping&lt;TEnum&gt;(TEnum mapping, [MouseMotionInput](./mousemotioninput.md) input, [Single](https://learn.microsoft.com/dotnet/api/system.single) sensitivity)

Maps an axis binding to a mouse movement/scroll.<br /> <strong>NOTE:</strong> This will only trigger upon <strong>POSITIVE</strong> values! <strong>ZERO</strong> values will <strong>NOT</strong> It is thus recommended to use this solely for things such as event triggers, as opposed to field values

**Parameters:**

- `mapping` (TEnum): What binding to map

- `input` ([MouseMotionInput](./mousemotioninput.md)): Mouse movement input

- `sensitivity` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): Scale of the movement. This acts as a direct multiplier


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindButtonMapping&lt;TEnum&gt;(TEnum mapping, [KeyInput](./keyinput.md) input, [InputModifier](./inputmodifier.md) modifier)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([KeyInput](./keyinput.md)): 

- `modifier` ([InputModifier](./inputmodifier.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindButtonMapping&lt;TEnum&gt;(TEnum mapping, [MouseInput](./mouseinput.md) input, [InputModifier](./inputmodifier.md) modifier)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([MouseInput](./mouseinput.md)): 

- `modifier` ([InputModifier](./inputmodifier.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindButtonMapping&lt;TEnum&gt;(TEnum mapping, [GamepadButtonInput](./gamepadbuttoninput.md) input, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([GamepadButtonInput](./gamepadbuttoninput.md)): 

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindButtonMapping&lt;TEnum&gt;(TEnum mapping, [MouseMotionInput](./mousemotioninput.md) input)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([MouseMotionInput](./mousemotioninput.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindAxisMapping&lt;TEnum&gt;(TEnum mapping, [KeyInput](./keyinput.md) input, [InputModifier](./inputmodifier.md) modifier)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([KeyInput](./keyinput.md)): 

- `modifier` ([InputModifier](./inputmodifier.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindAxisMapping&lt;TEnum&gt;(TEnum mapping, [MouseInput](./mouseinput.md) input, [InputModifier](./inputmodifier.md) modifier)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([MouseInput](./mouseinput.md)): 

- `modifier` ([InputModifier](./inputmodifier.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindAxisMapping&lt;TEnum&gt;(TEnum mapping, [GamepadButtonInput](./gamepadbuttoninput.md) input, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([GamepadButtonInput](./gamepadbuttoninput.md)): 

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindAxisMapping&lt;TEnum&gt;(TEnum mapping, [GamepadAnalogInput](./gamepadanaloginput.md) input, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) gamepadIndex)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([GamepadAnalogInput](./gamepadanaloginput.md)): 

- `gamepadIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnbindAxisMapping&lt;TEnum&gt;(TEnum mapping, [MouseMotionInput](./mousemotioninput.md) input)

**Parameters:**

- `mapping` (TEnum): 

- `input` ([MouseMotionInput](./mousemotioninput.md)): 


---


---