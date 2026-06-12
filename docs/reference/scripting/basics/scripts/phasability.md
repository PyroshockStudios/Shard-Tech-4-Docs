# Phasability

Phasability defines the presence of a script in a scene.

## Non-Phasable

Non-phaseable scripts do not have a fixed presence in the scene, and reside purely within the C# script environment.
[PropScripts](../../modules/sdt4.managed.core/script/propscript.md) are a prime example, as they are merely *props* and do not *act* in the scene. They merely *set the stage* for the *actors*.

## Phasable

Phasable scripts have a fixed presence in the scene, and reside in both the C# script environment and the native C++ environment.
[ActorScripts](../../modules/sdt4.managed.core/script/actorscript.md) are a prime example, as they *act* in the scene.
