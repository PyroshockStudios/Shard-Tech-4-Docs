# SceneScript

Since we've had an extensive look at the [Scene](../../../../cs-api-ref/sdt4.managed.core/scene.md) class, it is only natural to first make use of it.

## Making a SceneScript

Shard Tech 4 offers two methods of creating scene scripts:

- Written C# class
- Visual C# class

Both are perfectly valid methods of creating a class, the following is a [Visual Script](../../../editor/visualscript.md)

![Basic Scene Script](image.png)

Equivalent written C# class:

```csharp

using SDT4.Managed.Core;
using SDT4.Managed.Core.Script;

namespace MyGame;

public class MyScene : SceneScript 
{
    protected MyScene(SceneScriptToken token) : base(token) {}

    protected override void OnPreBegin() 
    {

    }
}

```

Once `Scene.Start[Async]()` is called, `OnPreBegin()` is the first method called. additionally, `On[...]Tick()` may be called before the scene finished loading (once `OnPostBegin()` is invoked);

!!! tip
    See the [SceneScript](../../../../cs-api-ref/sdt4.managed.core/script/scenescript.md) api reference for all possible overrides.


# ActorScript

[ActorScript](../../../../cs-api-ref/sdt4.managed.core/script/actorscript.md) is a script class that allows adding behaviour to a [Prefab](../../../editor/asset/prefab.md). This is very powerful and allows to create complex actors. 

## Making an ActorScript
Shard Tech 4 akin to SceneScript, offers two methods of creating actor scripts:

- Written C# class
- Visual C# class

[Visual Script](../../../editor/visualscript.md):

![Actor Script](image-1.png)

Written C# class:

```csharp

using SDT4.Managed.Core;
using SDT4.Managed.Core.Script;

namespace MyGame;

public class MyActor : ActorScript 
{
    protected MyActor(ActorScriptToken token) : base(token) {}

    protected override void OnCreate(ScriptPayload payload) 
    {

    }

    protected override void OnSpawn() 
    {

    }

    protected override void OnBegin() 
    {

    }
}

```

## OnCreate vs OnBegin vs OnSpawn

These three look very similar in functionality, and may be called in close situations, however the use in which they are called is very different.

Once `Scene.Start[Async]()` is called, `OnCreate()` is called together with `OnBegin()` for persistent scripts (e.g. Actors present in the scene before `Scene.Start[Async]()` was called). OnSpawn() is only called when `Scene.CreatePrefabActor()` or `Scene.InvokeProp()` is explicitly called to spawn a script.

!!! tip
    See the [ActorScript](../../../../cs-api-ref/sdt4.managed.core/script/actorscript.md) API reference for all possible overrides.
