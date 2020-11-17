# C# Source Generators

A list of C# Source Generators (not necessarily awesome), because I haven't found a good list yet.

**C# Source Generators** is a Roslyn compiler feature introduced in C#9/.NET 5. It lets C# developers inspect user code and generate new C# source files that can be added to a compilation.

Add GitHub topic [`csharp-sourcegenerator`](https://github.com/topics/csharp-sourcegenerator) to your generator repo - let's get it started!

<!--
Template for github repo links:
- [REPO](https://github.com/REPO)  - ![stars](https://img.shields.io/github/stars/REPO?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/REPO?style=flat-square&cacheSeconds=86400)
-->

## Documentation and samples

- [dotnet/roslyn feature design document](https://github.com/dotnet/roslyn/blob/master/docs/features/source-generators.md) describing the compiler feature.
- [dotnet/roslyn cookbook](https://github.com/dotnet/roslyn/blob/master/docs/features/source-generators.cookbook.md) to help with generator creation.
- [dotnet/roslyn-sdk samples](https://github.com/dotnet/roslyn-sdk/tree/master/samples/CSharp/SourceGenerators) show how to implement a source generator and use features like external package references (*inside* generators).
- [sourcegen.dev](https://sourcegen.dev) - an online Source Generator Playground to play with generator ideas 💡 without any setup noise. [Source repo](https://github.com/davidwengier/SourceGeneratorPlayground).
- [davidwengier/SourceGeneratorTemplate](https://github.com/davidwengier/SourceGeneratorTemplate)  - ![stars](https://img.shields.io/github/stars/davidwengier/SourceGeneratorTemplate?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/davidwengier/SourceGeneratorTemplate?style=flat-square&cacheSeconds=86400) A basic template for writing a C# source generator, from the Roslyn dev.

## Source Generators

- [AutoInterface](https://github.com/beakona/AutoInterface)  - ![stars](https://img.shields.io/github/stars/beakona/AutoInterface?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/beakona/AutoInterface?style=flat-square&cacheSeconds=86400) interface-to-member source generator.
- [avatar](https://github.com/kzu/avatar)  - ![stars](https://img.shields.io/github/stars/kzu/avatar?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kzu/avatar?style=flat-square&cacheSeconds=86400) A modern compile-time generated interception/proxy library.
- [Cloneable](https://github.com/mostmand/Cloneable)  - ![stars](https://img.shields.io/github/stars/mostmand/Cloneable?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/mostmand/Cloneable?style=flat-square&cacheSeconds=86400) auto-generate Clone method.
- [JsonSrcGen](https://github.com/trampster/JsonSrcGen)  - ![stars](https://img.shields.io/github/stars/trampster/JsonSrcGen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/trampster/JsonSrcGen?style=flat-square&cacheSeconds=86400) - compile time JSON serializer generation.
- [MemberAccessGenerator](https://github.com/ufcpp/MemberAccessGenerator)  - ![stars](https://img.shields.io/github/stars/ufcpp/MemberAccessGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ufcpp/MemberAccessGenerator?style=flat-square&cacheSeconds=86400) generates `GetMember(int)` and/or `GetMember(string)` methods that return property value for a given property name or index (e.g. in positional records).
- [net_automatic_interface](https://github.com/codecentric/net_automatic_interface)  - ![stars](https://img.shields.io/github/stars/codecentric/net_automatic_interface?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/codecentric/net_automatic_interface?style=flat-square&cacheSeconds=86400) .Net Core Source Generator for Automatic Interfaces.
- [PrimaryConstructor](https://github.com/chaowlert/PrimaryConstructor)  - ![stars](https://img.shields.io/github/stars/chaowlert/PrimaryConstructor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/chaowlert/PrimaryConstructor?style=flat-square&cacheSeconds=86400) Generate primary constructor from readonly fields.
- [PrintMembersGenerator](https://github.com/Youssef1313/PrintMembersGenerator)  - ![stars](https://img.shields.io/github/stars/Youssef1313/PrintMembersGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Youssef1313/PrintMembersGenerator?style=flat-square&cacheSeconds=86400) helps re-defining C# record's PrintMembers method to force include/exclude certain members.
- [SmallSharp](https://github.com/kzu/SmallSharp)  - ![stars](https://img.shields.io/github/stars/kzu/SmallSharp?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kzu/SmallSharp?style=flat-square&cacheSeconds=86400) Create, edit and run multiple C# 9.0 top-level programs in the same project by just selecting the startup program from the start button.
- [StringLiteralGenerator](https://github.com/ufcpp/StringLiteralGenerator)  - ![stars](https://img.shields.io/github/stars/ufcpp/StringLiteralGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ufcpp/StringLiteralGenerator?style=flat-square&cacheSeconds=86400) for optimizing UTF-8 binaries.
- [StrongInject](https://github.com/YairHalberstadt/stronginject)  - ![stars](https://img.shields.io/github/stars/YairHalberstadt/stronginject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/YairHalberstadt/stronginject?style=flat-square&cacheSeconds=86400) - compile time dependency injection for .NET.
- [StructPacker](https://github.com/RudolfKurka/StructPacker)  - ![stars](https://img.shields.io/github/stars/RudolfKurka/StructPacker?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RudolfKurka/StructPacker?style=flat-square&cacheSeconds=86400) binary serializer that auto-generates C# serialization code to achieve peak runtime performance and efficiency.
- [Svg to C# Source Generators](https://github.com/wieslawsoltes/SourceGenerators)  - ![stars](https://img.shields.io/github/stars/wieslawsoltes/SourceGenerators?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/wieslawsoltes/SourceGenerators?style=flat-square&cacheSeconds=86400) SVGC compiles SVG drawing markup to C# using SkiaSharp as rendering engine. SVGC can be also used as codegen for upcoming C# 9 Source Generator feature.
- [ThisAssembly](https://github.com/kzu/ThisAssembly)  - ![stars](https://img.shields.io/github/stars/kzu/ThisAssembly?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kzu/ThisAssembly?style=flat-square&cacheSeconds=86400) Exposes project and assembly level information as constants in the ThisAssembly class.
- [ValueObjectGenerator](https://github.com/RyotaMurohoshi/ValueObjectGenerator)  - ![stars](https://img.shields.io/github/stars/RyotaMurohoshi/ValueObjectGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RyotaMurohoshi/ValueObjectGenerator?style=flat-square&cacheSeconds=86400) C# source generator is for ValueObjects (ie.Wrapper classes).
- [WrapperValueObject](https://github.com/martinothamar/WrapperValueObject)  - ![stars](https://img.shields.io/github/stars/martinothamar/WrapperValueObject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/martinothamar/WrapperValueObject?style=flat-square&cacheSeconds=86400) - for creating simple value objects wrapping primitive types.

## Tips & Tricks

Collection of tips and tricks (simple and brief to fit in Tweet):

[Tweeted](https://twitter.com/raboof/status/1328426892882550784) by [@raboof](https://twitter.com/raboof) on Nov 16 2020 at 20:57:

> See files emitted by [#SourceGenerators] by adding these properties to your (*.csproj) project file:
>
> ```xml
> <EmitCompilerGeneratedFiles>true</EmitCompilerGeneratedFiles>
> <CompilerGeneratedFilesOutputPath>$(BaseIntermediateOutputPath)Generated</CompilerGeneratedFilesOutputPath>
> ```

[Tweeted](https://twitter.com/Chiser99/status/1301198611158499328) by [@Chiser99](https://twitter.com/Chiser99) on Sep 02 2020 at 06:41:

> I made a thing: https://github.com/chsienki/Kittitas
>
> If you're building Roslyn Source Generators or Analyzers check it out, it makes debugging them inside the compiler easier. #roslyn #csharp #dotnetcore #sourcegenerators #analyzers


  [#SourceGenerators]: https://twitter.com/hashtag/SourceGenerators?src=hashtag_click
  [#sourcegenerators]: https://twitter.com/hashtag/sourcegenerators?src=hashtag_click
  [#roslyn]: https://twitter.com/hashtag/roslyn?src=hashtag_click
  [#csharp]: https://twitter.com/hashtag/csharp?src=hashtag_click
  [#dotnetcore]: https://twitter.com/hashtag/dotnetcore?src=hashtag_click
  [#analyzers]: https://twitter.com/hashtag/analyzers?src=hashtag_click

## Articles

- [Source Generators in .NET 5 with ReSharper](https://blog.jetbrains.com/dotnet/2020/11/12/source-generators-in-net-5-with-resharper/) (2020-11-20) introduces source generators and briefly mentions how they are being worked into the ReSharper product
- [Source Generators - real world example](https://dominikjeske.github.io/source-generators) (2020-11-09) contains a rich and deep dive into a real world generator with lots of useful tips.
- [How to Debug C# 9 Source Code Generators](https://nicksnettravels.builttoroam.com/debug-code-gen/) (2020-10-09)
- [.NET Blog 'New C# Source Generator Samples' post](https://devblogs.microsoft.com/dotnet/new-c-source-generator-samples/) (2020-08-25) that shows some simple samples.
- [.NET Blog 'Introducing C# Source Generators' post](https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/) (2020-04-29) that announces the feature.

## Videos

- [.NET Languages and Runtime Community Standup - Source Generators](https://www.youtube.com/watch?v=A4479Etdx4I) (2020-10-08) shows how Generators work and how they can be tested.
- [Channel 9 'Source Generators in C#'](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Source-Generators-in-CSharp) (2020-08-12) has Roslyn PMs discussing the feature.

## Demo, PoC and excercise projects

Maybe they can inspire you too!

- [RyanAlameddine/SourceGeneratorDemo](https://github.com/RyanAlameddine/SourceGeneratorDemo) - ![stars](https://img.shields.io/github/stars/RyanAlameddine/SourceGeneratorDemo?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RyanAlameddine/SourceGeneratorDemo?style=flat-square&cacheSeconds=86400) contains 3 demos: hello world, INPC and OpCode class.
- [TMC-CSharp/CodeExerciseLibrary](https://github.com/TMC-CSharp/CodeExerciseLibrary) - ![stars](https://img.shields.io/github/stars/TMC-CSharp/CodeExerciseLibrary?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/TMC-CSharp/CodeExerciseLibrary?style=flat-square&cacheSeconds=86400) Library to help creating C# exercises. Generates missing methods and classes inside tests on the fly by using Source Generators.
- [DpdtInject](https://github.com/lsoft/DpdtInject)  - ![stars](https://img.shields.io/github/stars/lsoft/DpdtInject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/lsoft/DpdtInject?style=flat-square&cacheSeconds=86400) DI container based on C# Source Generators. Its goal is to remove everything possible from runtime and make resolving process as faster as we can. This is achieved by transferring huge piece of resolving logic to the compilation stage into the source generator.
- [jakubsturc/talk-csharp-source-generators](https://github.com/jakubsturc/talk-csharp-source-generators/tree/master/demo/SourceGeneratorSamples)  - ![stars](https://img.shields.io/github/stars/jakubsturc/talk-csharp-source-generators?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jakubsturc/talk-csharp-source-generators?style=flat-square&cacheSeconds=86400) contains 4 generators: AutoNotify, ConsoleWritelineHijack, HelloWorld and SettingsXml, plus nice presentation slides.
- [Compile Time Method Execution Generator](https://github.com/hermanussen/CompileTimeMethodExecutionGenerator)  - ![stars](https://img.shields.io/github/stars/hermanussen/CompileTimeMethodExecutionGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/hermanussen/CompileTimeMethodExecutionGenerator?style=flat-square&cacheSeconds=86400) proof of concept that allows executing a method during compilation, so that it can be really fast during runtime.

## Projects using custom Source Generators "internally"

- [NetFabric.Hyperlinq](https://github.com/NetFabric/NetFabric.Hyperlinq)  - ![stars](https://img.shields.io/github/stars/NetFabric/NetFabric.Hyperlinq?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/NetFabric/NetFabric.Hyperlinq?style=flat-square&cacheSeconds=86400) generates overloads for its extension methods.
- [RestEase](https://github.com/canton7/RestEase)  - ![stars](https://img.shields.io/github/stars/canton7/RestEase?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/canton7/RestEase?style=flat-square&cacheSeconds=86400) uses Source Generator to generate interface implementations on compile time instead of in runtime via Reflection.Emit.
- [WarHub/wham](https://github.com/WarHub/wham)  - ![stars](https://img.shields.io/github/stars/WarHub/wham?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/WarHub/wham?style=flat-square&cacheSeconds=86400) generates code for immutable tree object graph based on red-green node approach used in Roslyn; generates custom XmlSerializer that supports C#9 records and ImmutableArray.
