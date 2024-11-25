# C# Source Generators

  * [Documentation and samples](#documentation-and-samples)
  * [Source Generators](#source-generators)
  * [Meta - libs and generators for other generators](#meta---libs-and-generators-for-other-generators)
  * [Tips & Tricks](#tips--tricks)
  * [Articles](#articles)
  * [Videos](#videos)
  * [Demo, PoC and excercise projects](#demo-poc-and-excercise-projects)
  * [Projects using custom Source Generators "internally"](#projects-using-custom-source-generators-internally)

---

A list of C# Source Generators (not necessarily awesome), because I haven't found a good list yet.

**C# Source Generators** is a Roslyn compiler feature introduced in C#9/.NET 5. It lets C# developers inspect user code and generate new C# source files that can be added to a compilation.

Add GitHub topic [`csharp-sourcegenerator`](https://github.com/topics/csharp-sourcegenerator) to your generator repo - let's get it started!

## Documentation and samples

- [docs.microsoft.com](https://docs.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview) official documentation.
- [dotnet/roslyn feature design document](https://github.com/dotnet/roslyn/blob/main/docs/features/source-generators.md) describing the compiler feature.
- [dotnet/roslyn cookbook](https://github.com/dotnet/roslyn/blob/main/docs/features/source-generators.cookbook.md) to help with generator creation.
- [dotnet/roslyn-sdk samples](https://github.com/dotnet/roslyn-sdk/tree/main/samples/CSharp/SourceGenerators) show how to implement a source generator and use features like external package references (*inside* generators). Includes AutoNotify, Csv, Maths, Mustache, and SettingsXml.
- [SourceGeneratorPlayground](https://wengier.com/SourceGeneratorPlayground) - an online Source Generator Playground to play with generator ideas 💡 without any setup noise. [Source repo](https://github.com/davidwengier/SourceGeneratorPlayground).
- [davidwengier/SourceGeneratorTemplate](https://github.com/davidwengier/SourceGeneratorTemplate) -![stars](https://img.shields.io/github/stars/davidwengier/SourceGeneratorTemplate?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/davidwengier/SourceGeneratorTemplate?style=flat-square&cacheSeconds=86400) A basic template for writing a C# source generator, from the Roslyn dev.

## Source Generators

<details open>
 <summary>Categories</summary>

- [Dependency Injection (IoC Container)](#dependency-injection-ioc-container)
- [Console / CLI](#console--cli)
- [Mappers](#mappers)
- [Communication](#communication)
- [Graphics / Drawing](#graphics--drawing)
- [Enums](#enums)
- [Functional Programming](#functional-programming)
  - [Value semantic / New Type Idiom](#value-semantic--new-type-idiom)
  - [Immutability](#immutability)
  - [Discriminated Unions](#discriminated-unions)
- [Serialization](#serialization)
  - [Json](#json)
- [Validation](#validation)
- [Localization](#localization)
- [Testing](#testing)
  - [Mocking](#mocking)
- [Patterns](#patterns)
  - [Mediator](#mediator)
  - [Command](#command)
  - [Builder](#builder)
  - [Proxy](#proxy)
  - [Visitor](#visitor)
  - [Adapter](#adapter)
- [Domain Driven Design (DDD)](#domain-driven-design-ddd)
- [Metaprogramming](#metaprogramming)
- [Webprogramming](#webprogramming)
  - [Open Api](#open-api)
  - [Razor / Blazor](#razor--blazor)
- [XAML / WPF / Avalonia](#xaml--wpf--avalonia)
  - [INotifyPropertyChanged](#inotifypropertychanged)
  - [Model View Viewmodel (MVVM)](#model-view-viewmodel-mvvm)
- [Database / ORM](#database--orm)
- [Statically typed resources / configurations](#statically-typed-resources--configurations)
- [Other](#other)

</details>

<!--
  Sorted alphabetically in each category. Template for entries:
- [REPO](https://github.com/REPO) - ![stars](https://img.shields.io/github/stars/REPO?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/REPO?style=flat-square&cacheSeconds=86400)
-->

### Dependency Injection (IoC Container)

- [AutoCtor](https://github.com/distantcam/AutoCtor) - ![stars](https://img.shields.io/github/stars/distantcam/AutoCtor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/distantcam/AutoCtor?style=flat-square&cacheSeconds=86400) AutoCtor is a Roslyn Source Generator that will automatically create a constructor for your class for use with constructor Dependency Injection.
- [AutoRegisterInject](https://github.com/patrickklaeren/AutoRegisterInject) - ![stars](https://img.shields.io/github/stars/patrickklaeren/AutoRegisterInject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/patrickklaeren/AutoRegisterInject?style=flat-square&cacheSeconds=86400) Automatically generate Microsoft Dependency Injection ServiceCollection registrations for your classes from attributes.
- [DependencyInjection.SourceGenerators](https://github.com/jimmy-mll/DependencyInjection.SourceGenerators) ![stars](https://img.shields.io/github/stars/jimmy-mll/Microsoft.Extensions.DependencyInjection.SourceGenerators?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jimmy-mll/Microsoft.Extensions.DependencyInjection.SourceGenerators?style=flat-square&cacheSeconds=86400) This project is a C# source generator designed to simplify and automate the registration of dependencies in Microsoft's Dependency Injection service collection. By using this package, developers can enhance the clarity and efficiency of their code by reducing the need for manual service registration.
- [DependencyManagement](https://github.com/essy-ecosystem/dependency-management) - ![stars](https://img.shields.io/github/stars/essy-ecosystem/dependency-management?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/essy-ecosystem/dependency-management?style=flat-square&cacheSeconds=86400) The Dependency Management is a very fast dependency injection and components container, with many interesting features, and without reflection.
- [GrpcInjection](https://github.com/juniorporfirio/grpcinjection) -![stars](https://img.shields.io/github/stars/juniorporfirio/grpcinjection?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/juniorporfirio/grpcinjection?style=flat-square&cacheSeconds=86400) - GrpcInjection is a tool  that allow you to inject Services and Interceptor in time of compilation inside of GRPC Projects using C# source generator.
- [Injectio](https://github.com/loresoft/Injectio) - ![stars](https://img.shields.io/github/stars/loresoft/Injectio?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/loresoft/Injectio?style=flat-square&cacheSeconds=86400) - Source generator that helps register discovered services in the dependency injection container
- [Jab](https://github.com/pakrym/jab) -![stars](https://img.shields.io/github/stars/pakrym/jab?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/pakrym/jab?style=flat-square&cacheSeconds=86400) - Compile Time Dependency Injection
- [lambdajection](https://github.com/cythral/lambdajection) -![stars](https://img.shields.io/github/stars/cythral/lambdajection?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/cythral/lambdajection?style=flat-square&cacheSeconds=86400) Framework for building AWS Lambdas using dependency injection and aspect-oriented programming.
- [MrMeeseeks.DIE](https://github.com/Yeah69/MrMeeseeks.DIE) - ![stars](https://img.shields.io/github/stars/Yeah69/MrMeeseeks.DIE?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Yeah69/MrMeeseeks.DIE?style=flat-square&cacheSeconds=86400) An unambigous, convenient, flexible and feature rich compile time dependency injection container.
- [Pure.DI](https://github.com/DevTeam/Pure.DI) - ![stars](https://img.shields.io/github/stars/DevTeam/Pure.DI?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DevTeam/Pure.DI?style=flat-square&cacheSeconds=86400) - dependency injection for .NET without any IoC/DI containers, frameworks, dependencies, and thus without any performance impact and side-effects.
- [SourceInject](https://github.com/giggio/sourceinject/) -![stars](https://img.shields.io/github/stars/giggio/sourceinject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/giggio/sourceinject?style=flat-square&cacheSeconds=86400) A source generator that allow you to generate your services for dependencies injection during compile time.
- [StrongInject](https://github.com/YairHalberstadt/stronginject) -![stars](https://img.shields.io/github/stars/YairHalberstadt/stronginject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/YairHalberstadt/stronginject?style=flat-square&cacheSeconds=86400) - compile time dependency injection for .NET.
- [Thunderboltloc](https://github.com/AlyElhaddad/ThunderboltIoc) - ![stars](https://img.shields.io/github/stars/AlyElhaddad/ThunderboltIoc?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/AlyElhaddad/ThunderboltIoc?style=flat-square&cacheSeconds=86400) One of the very first IoC frameworks for .Net that has no reflection.

### Console / CLI

- [AutoSpectre](https://github.com/jeppevammenkristensen/auto-spectre) - ![stars](https://img.shields.io/github/stars/jeppevammenkristensen/auto-spectre?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jeppevammenkristensen/auto-spectre?style=flat-square&cacheSeconds=86400) Generates a service for prompting and populating a class using the Spectre.Console library
- [docopt.net](https://github.com/docopt/docopt.net) - ![stars](https://img.shields.io/github/stars/docopt/docopt.net?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/docopt/docopt.net?style=flat-square&cacheSeconds=86400) generates C# source code that parses command-line arguments into a strong-typed arguments class (also generated), given _just_ the [POSIX-style usage in plain text](http://docopt.org/) as part of the CLI. In other words, write the help message for your program and get the entire parser generated for free!
- [Figgle](https://github.com/drewnoakes/figgle) - ![stars](https://img.shields.io/github/stars/drewnoakes/figgle?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/drewnoakes/figgle?style=flat-square&cacheSeconds=86400) - Generate ASCII banner text at compile time (or run time) using figlet fonts.

### Mappers

- [AutoDto](https://github.com/Ohorodnikov/AutoDto) -![stars](https://img.shields.io/github/stars/Ohorodnikov/AutoDto?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Ohorodnikov/AutoDto?style=flat-square&cacheSeconds=86400) - A source generator that generates DTO models from BL to avoid same BL and DTO models
- [Flattening](https://github.com/Kros-sk/Kros.Generators.Flattening) - ![stars](https://img.shields.io/github/stars/Kros-sk/Kros.Generators.Flattening?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Kros-sk/Kros.Generators.Flattening?style=flat-square&cacheSeconds=86400) - C# source generator for generating flattened classes from complex domain classes.
- [GraphQL.Tools](https://github.com/MoienTajik/GraphQL.Tools) -![stars](https://img.shields.io/github/stars/MoienTajik/GraphQL.Tools?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/MoienTajik/GraphQL.Tools?style=flat-square&cacheSeconds=86400) - A GraphQL to C# compiler (code-generator) which turns your GraphQL schema into a set of C# classes, interfaces, and enums.
- [Mapperly](https://github.com/riok/mapperly) -![stars](https://img.shields.io/github/stars/riok/mapperly?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/riok/mapperly?style=flat-square&cacheSeconds=86400) - A source generator for generating object mappings. Inspired by MapStruct.
- [MappingCloningExtensions](https://github.com/musictopia2/MappingCloningExtensions) - ![stars](https://img.shields.io/github/stars/musictopia2/MappingCloningExtensions?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/MappingCloningExtensions?style=flat-square&cacheSeconds=86400)  Generates extensions of objects for mapping and cloning using either attributes or fluent style.  Also, supports deep copying and specfiying whether it can do a deep copy and the possibility of doing so safely.
- [Mapster](https://github.com/MapsterMapper/Mapster) -![stars](https://img.shields.io/github/stars/MapsterMapper/Mapster?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/MapsterMapper/Mapster?style=flat-square&cacheSeconds=86400) - A fast, fun and performant object to object Mapper. Has better performance and is more memorry efficient than Automapper. Besides code generation, supports also Fluent API.
- [MapTo](https://github.com/mrtaikandi/MapTo) -![stars](https://img.shields.io/github/stars/mrtaikandi/mapto?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/mrtaikandi/mapto?style=flat-square&cacheSeconds=86400) - A convention based object to object mapper similar to Automapper.
- [NextGenMapper](https://github.com/DedAnton/NextGenMapper) - ![stars](https://img.shields.io/github/stars/DedAnton/NextGenMapper?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DedAnton/NextGenMapper?style=flat-square&cacheSeconds=86400) Easy-to-use mapper without configuration.
- [SourceMapper](https://github.com/alekshura/SourceMapper) - ![stars](http://img.shields.io/github/stars/alekshura/SourceMapper?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/alekshura/SourceMapper?style=flat-square&cacheSeconds=86400) - generates Mappers code based on attributes used on interfaces or abstract classes. It is inspired by Java [MapStruct](https://mapstruct.org/)
- [SourceMapper](https://github.com/paiden/SourceMapper/) -![stars](https://img.shields.io/github/stars/paiden/SourceMapper?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/paiden/SourceMapper?style=flat-square&cacheSeconds=86400) A source generator that creates extension methods for cloning and mapping.

### Communication

- [CoreWCF](https://github.com/CoreWCF/CoreWCF) -![stars](https://img.shields.io/github/stars/CoreWCF/CoreWCF?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/CoreWCF/CoreWCF?style=flat-square&cacheSeconds=86400) CoreWCF provides support of WCF server side code on .NET Core / .NET6. CoreWCF allows users to inject services into `OperationContract` implementation using a source generator to provide an `OperationContract` implementation that fits the expected `ServiceContract`. The supplied implementation fetch services from the DI container the same way the `[FromServices]` attribute works in ASP.NET core MVC Controllers. The source generator supports both a dedicated `[Injected]` attribute and the ASP.NET Core MVC `[FromServices]` attribute.
- [Imp.NET](https://github.com/DouglasDwyer/Imp.NET) -![stars](https://img.shields.io/github/stars/DouglasDwyer/Imp.NET?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DouglasDwyer/Imp.NET?style=flat-square&cacheSeconds=86400) - a fast, high-level, object-oriented C# networking library that supports the invocation of remote methods through proxy interface objects.
- [IoTHubClientGenerator](https://github.com/alonf/IoTHubClientGenerator) -  ![stars](https://img.shields.io/github/stars/alonf/IoTHubClientGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/alonf/IoTHubClientGenerator?style=flat-square&cacheSeconds=86400) Build a C# Azure IoT Device client program in seconds!

### Graphics / Drawing

- [ComputeSharp](https://github.com/Sergio0694/ComputeSharp) -![stars](https://img.shields.io/github/stars/Sergio0694/ComputeSharp?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Sergio0694/ComputeSharp?style=flat-square&cacheSeconds=86400) A .NET library to run C# code in parallel on the GPU through DX12 and dynamically generated HLSL compute shaders, which are transpiled from C# and precompiled at build-time using source generators.
- [Svg to C# Source Generators](https://github.com/wieslawsoltes/Svg.Skia) -![stars](https://img.shields.io/github/stars/wieslawsoltes/Svg.Skia?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/wieslawsoltes/Svg.Skia?style=flat-square&cacheSeconds=86400) SVGC compiles SVG drawing markup to C# using SkiaSharp as rendering engine. SVGC can be also used as codegen for upcoming C# 9 Source Generator feature.

### Enums

- [BetterEnums](https://github.com/Ceiridge/BetterEnums) - ![stars](https://img.shields.io/github/stars/Ceiridge/BetterEnums?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Ceiridge/BetterEnums?style=flat-square&cacheSeconds=86400) C# Enums with values and better performance as a source generator
- [Credfeto.Enumeration.Source.Generation](https://github.com/credfeto/credfeto-enum-source-generation) -![stars](https://img.shields.io/github/stars/credfeto/credfeto-enum-source-generation?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/credfeto/credfeto-enum-source-generation?style=flat-square&cacheSeconds=86400) Enum to text generator for enums - generates strongly typed enums for all enums in the assembly, and using `EnumText` attribute for third party enums.  Also includes an analyzer to ensure that all enum usages use the `.GetName` extension method rather than `.ToString`.
- [Enum.Source.Generator](https://github.com/EngRajabi/Enum.Source.Generator) - ![stars](https://img.shields.io/github/stars/EngRajabi/Enum.Source.Generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/EngRajabi/Enum.Source.Generator?style=flat-square&cacheSeconds=86400) A C# source generator to create an enumeration (enum) class from an enum type. With this package, you can work on enums very, very fast without using reflection.
- [EnumClass](https://github.com/ashenBlade/EnumClass) - ![stars](https://img.shields.io/github/stars/ashenBlade/EnumClass?style=flat-square&cacheSeconds=604800) ![last_commit](https://img.shields.io/github/last-commit/ashenBlade/EnumClass?style=flat-square&cacheSeconds=86400) Generate Kotlin's `enum class` from C# `enum` with additional features like Switch function (instead of `switch` statement). It also contains support libraries like generator for JsonConverter for generated classes
- [EnumerationClassGenerator](https://github.com/HamedFathi/EnumerationClassGenerator) -![stars](https://img.shields.io/github/stars/HamedFathi/EnumerationClassGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/HamedFathi/EnumerationClassGenerator?style=flat-square&cacheSeconds=86400) - A C# source generator to create an enumeration class from an enum type.
- [EnumFastToStringDotNet](https://github.com/Spinnernicholas/EnumFastToStringDotNet) -![stars](https://img.shields.io/github/stars/Spinnernicholas/EnumFastToStringDotNet?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Spinnernicholas/EnumFastToStringDotNet?style=flat-square&cacheSeconds=86400) - Automatically generates enum extension methods that implement a switch expression based ToString method.
- [EnumUtilitiesGenerator](https://github.com/leoformaggi/enum-utilities-generator) -![stars](https://img.shields.io/github/stars/leoformaggi/enum-utilities-generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/leoformaggi/enum-utilities-generator?style=flat-square&cacheSeconds=86400) - A source generator to generate compile-time mapping of enums and description attributes.
- [FastEnumGenerator](https://github.com/musictopia2/FastEnumGenerator) - ![stars](https://img.shields.io/github/stars/musictopia2/FastEnumGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/FastEnumGenerator?style=flat-square&cacheSeconds=86400)  An enum like generator where you create a partial class with private enum and it will generate an enum like record struct even including returning the words and a list.
- [JOS.Enumeration](https://github.com/joseftw/jos.enumeration) - Enumeration class powered by source generation

### Functional Programming

#### Value semantic / New Type Idiom

- [Generator.Equals](https://github.com/diegofrata/Generator.Equals) - ![stars](https://img.shields.io/github/stars/diegofrata/Generator.Equals?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/diegofrata/Generator.Equals?style=flat-square&cacheSeconds=86400) generates equality and hashing for classes and records, supports a number of strategies for comparing collections and properties.
- [RSCG_UtilityTypes](https://github.com/ignatandrei/RSCG_UtilityTypes) - ![stars](https://img.shields.io/github/stars/ignatandrei/RSCG_UtilityTypes?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ignatandrei/RSCG_UtilityTypes?style=flat-square&cacheSeconds=86400) Add Omit and Pick attributes to generate classes from existing class, like in TypeScript.
- [Strongly](https://github.com/lucasteles/Strongly) ![stars](https://img.shields.io/github/stars/lucasteles/Strongly?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/lucasteles/Strongly?style=flat-square&cacheSeconds=86400) - Easily generate serializable domain value types
- [ValueObjectGenerator](https://github.com/RyotaMurohoshi/ValueObjectGenerator) - ![stars](https://img.shields.io/github/stars/RyotaMurohoshi/ValueObjectGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RyotaMurohoshi/ValueObjectGenerator?style=flat-square&cacheSeconds=86400) C# source generator is for ValueObjects (ie.Wrapper classes).
- [Vogen](https://github.com/SteveDunn/Vogen) - ![stars](https://img.shields.io/github/stars/SteveDunn/Vogen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/SteveDunn/Vogen?style=flat-square&cacheSeconds=86400) C# source generator and code analyser that generates strongly typed domain identities.
- [WrapperValueObject](https://github.com/martinothamar/WrapperValueObject) - ![stars](https://img.shields.io/github/stars/martinothamar/WrapperValueObject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/martinothamar/WrapperValueObject?style=flat-square&cacheSeconds=86400) - for creating simple value objects wrapping primitive types.

#### Immutability

- [Immutype](https://github.com/DevTeam/Immutype) - ![stars](https://img.shields.io/github/stars/DevTeam/Immutype?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DevTeam/Immutype?style=flat-square&cacheSeconds=86400) - generates extension methods to support immutability.
- [Visor](https://github.com/leviysoft/Visor) - ![stars](https://img.shields.io/github/stars/leviysoft/Visor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/leviysoft/Visor?style=flat-square&cacheSeconds=86400) C# optics library with incremental code generator (maintained fork of [suspended Tinkoff project](https://github.com/Tinkoff/Visor))

#### Discriminated Unions

- [AnyOf](https://github.com/StefH/AnyOf) - ![stars](https://img.shields.io/github/stars/StefH/AnyOf?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/StefH/AnyOf?style=flat-square&cacheSeconds=86400) The Source Generator creates a `AnyOf<First, TSecond, ...>` type to handle multiple defined types as input parameters for methods.
- [dotVariant](https://github.com/mknejp/dotvariant) - ![stars](https://img.shields.io/github/stars/mknejp/dotvariant?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/mknejp/dotvariant?style=flat-square&cacheSeconds=86400) A type-safe and space-efficient sum type for C# (comparable to discriminated unions in C or C++).
- [Dunet](https://github.com/domn1995/dunet) - ![stars](https://img.shields.io/github/stars/domn1995/dunet?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/domn1995/dunet?style=flat-square&cacheSeconds=604800) A simple source generator for [discriminated unions](https://en.wikipedia.org/wiki/Tagged_union) in C#.
- [Funcky Discriminated Unions](https://github.com/polyadic/funcky-discriminated-union) - ![stars](https://img.shields.io/github/stars/polyadic/funcky-discriminated-union?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/polyadic/funcky-discriminated-union?style=flat-square&cacheSeconds=86400) A source generator that generates `Match` methods for all your discriminated unions needs. ✨ Can be used with or without the functional programming library Funcky.
- [N.SourceGenerators.UnionTypes](https://github.com/Ne4to/N.SourceGenerators.UnionTypes) - ![stars](https://img.shields.io/github/stars/Ne4to/N.SourceGenerators.UnionTypes?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Ne4to/N.SourceGenerators.UnionTypes?style=flat-square&cacheSeconds=86400) Discriminated union type source generator.
- [Unions](https://github.com/PaulBraetz/Unions) - ![stars](https://img.shields.io/github/stars/PaulBraetz/Unions?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/PaulBraetz/Unions?style=flat-square&cacheSeconds=86400) for generating meaningful, efficient union types.

### Serialization

- [AutoDeconstructable](https://github.com/nemesissoft/Nemesis.TextParsers/tree/master/Nemesis.TextParsers.CodeGen/Deconstructable) -![stars](https://img.shields.io/github/stars/nemesissoft/Nemesis.TextParsers?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/nemesissoft/Nemesis.TextParsers?style=flat-square&cacheSeconds=86400) Generator for efficient and automatic flat text serializer/deserializer using [Deconstructable aspect](https://github.com/nemesissoft/Nemesis.TextParsers/blob/master/Specification.md#deconstructables) in [NTP](https://github.com/nemesissoft/Nemesis.TextParsers) library.
- [Azura](https://github.com/Lucina/Azura) -![stars](https://img.shields.io/github/stars/Lucina/Azura?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Lucina/Azura?style=flat-square&cacheSeconds=86400) Generates binary [de]serializers on Streams at design time.
- [CSV-Parser-Generator](https://github.com/LokiMidgard/CSV-Parser-Generator) - ![stars](https://img.shields.io/github/stars/LokiMidgard/CSV-Parser-Generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/LokiMidgard/CSV-Parser-Generator?style=flat-square&cacheSeconds=86400) A Parser for CSV with support for uncommon line separators (e.g. Unicode) and instantiation of read-only objects and working nullable handling.
- [ProtobufSourceGenerator](https://github.com/ladeak/ProtobufSourceGenerator) -![stars](https://img.shields.io/github/stars/ladeak/ProtobufSourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ladeak/ProtobufSourceGenerator?style=flat-square&cacheSeconds=86400) - A source generator that generates partial helper classes where member properties are attributed with ProtoMember attribute.
- [SerdeDn (serde-sn)](https://github.com/agocke/serde-dn) -![stars](https://img.shields.io/github/stars/agocke/serde-dn?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/agocke/serde-dn?style=flat-square&cacheSeconds=86400) is a port of the popular [serde.rs](https://serde.rs/) Rust serialization/deserialization library to .NET. Basic cases are fully automated using a C# source generator.
- [SpreadCheetah](https://github.com/sveinungf/spreadcheetah) -![stars](https://img.shields.io/github/stars/sveinungf/spreadcheetah?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/sveinungf/spreadcheetah?style=flat-square&cacheSeconds=86400) Create Excel files with a C# Source Generator for generating the rows.
- [StackXML](https://github.com/ZingBallyhoo/StackXML) -![stars](https://img.shields.io/github/stars/ZingBallyhoo/StackXML?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ZingBallyhoo/StackXML?style=flat-square&cacheSeconds=86400) Stack based zero-allocation XML serializer and deserializer.
- [StructPacker](https://github.com/RudolfKurka/StructPacker) -![stars](https://img.shields.io/github/stars/RudolfKurka/StructPacker?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RudolfKurka/StructPacker?style=flat-square&cacheSeconds=86400) binary serializer that auto-generates C# serialization code to achieve peak runtime performance and efficiency.
- [Tinyhand](https://github.com/archi-Doc/Tinyhand) -![stars](https://img.shields.io/github/stars/archi-Doc/Tinyhand?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/archi-Doc/Tinyhand?style=flat-square&cacheSeconds=86400) - Tiny and simple data format/serializer using a source generator.

#### Json

- [GeneratedJsonConverters](https://github.com/aviationexam/json-converter-source-generator) -![stars](https://img.shields.io/github/stars/aviationexam/json-converter-source-generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/aviationexam/json-converter-source-generator?style=flat-square&cacheSeconds=86400) - generate json converters for polymorph contracts and string based enum serialization.
- [JsonByExampleGenerator](https://github.com/hermanussen/JsonByExampleGenerator) -![stars](https://img.shields.io/github/stars/hermanussen/JsonByExampleGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/hermanussen/JsonByExampleGenerator?style=flat-square&cacheSeconds=86400) - generate classes based on example json files in your project.
- [JsonDeserializeResourceSourceGenerator](https://github.com/musictopia2/JsonDeserializeResourceSourceGenerator) - ![stars](https://img.shields.io/github/stars/musictopia2/JsonDeserializeResourceSourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/JsonDeserializeResourceSourceGenerator?style=flat-square&cacheSeconds=86400)  Instead of having to do embedded resource, can instead have json as additional file and it will produce a c# string and will deserialize to a type specified.
- [JsonPolymorphicGenerator](https://github.com/surgicalcoder/JsonPolymorphicGenerator) - ![stars](https://img.shields.io/github/stars/surgicalcoder/JsonPolymorphicGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/surgicalcoder/JsonPolymorphicGenerator?style=flat-square&cacheSeconds=86400) - Source Code Generator for System.Text.Json JsonDerivedType attributes on polymorphic classes
- [JsonSerializerContextGenerator](https://github.com/musictopia2/JsonSerializerContextGenerator) - ![stars](https://img.shields.io/github/stars/musictopia2/JsonSerializerContextGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/JsonSerializerContextGenerator?style=flat-square&cacheSeconds=86400)  A source generator that produces nearly the same code as system.json.text but easier to use because you only have to put an attribute for a model class you want to produce for.  Also, produces a method to register to make it easy to use that source generator when serializing/deserializing json.
- [JsonSrcGen](https://github.com/trampster/JsonSrcGen) -![stars](https://img.shields.io/github/stars/trampster/JsonSrcGen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/trampster/JsonSrcGen?style=flat-square&cacheSeconds=86400) - compile time JSON serializer generation.
- [TeuJson](https://github.com/Terria-K/TeuJson) - ![stars](https://img.shields.io/github/stars/Terria-K/TeuJson?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Terria-K/TeuJson?style=flat-square&cacheSeconds=86400) A Reflection-less and Lightweight Json Library using source generator.

### Validation
- [Validly](https://github.com/Hookyns/validly) -![stars](https://img.shields.io/github/stars/Hookyns/validly?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Hookyns/validly?style=flat-square&cacheSeconds=86400) - A performant, zero-allocation, and highly customizable validation library that generates validation logic based on attributes, with usage similar to DataAnnotations.

### Localization

- [kli.Localize](https://github.com/kl1mm/localize) - ![stars](https://img.shields.io/github/stars/kl1mm/localize?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kl1mm/localize?style=flat-square&cacheSeconds=86400) - localize strings from json files via  source code generation
- [MrMeeseeks.ResXToViewModelGenerator](https://github.com/Yeah69/MrMeeseeks.ResXToViewModelGenerator) - ![stars](https://img.shields.io/github/stars/Yeah69/MrMeeseeks.ResXToViewModelGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Yeah69/MrMeeseeks.ResXToViewModelGenerator?style=flat-square&cacheSeconds=86400) Takes ResX files and generates localization ViewModels for a more convenient usage of localization in MVVM projects.
- [ResXGenerator](https://github.com/ycanardeau/ResXGenerator) -![stars](https://img.shields.io/github/stars/ycanardeau/ResXGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ycanardeau/ResXGenerator?style=flat-square&cacheSeconds=86400) Generates strongly-typed resource classes for looking up localized strings.

### Testing

- [Buildenator](https://github.com/progala2/Buildenator) -![stars](https://img.shields.io/github/stars/progala2/Buildenator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/progala2/Buildenator?style=flat-square&cacheSeconds=86400) Generate data builder classes for testing purposes (and not only) for your entities. Autofixture + Moq extensions.
- [FluentAssertions.Eventual](https://github.com/mazharenko/FluentAssertions.Eventual) - ![stars](https://img.shields.io/github/stars/mazharenko/FluentAssertions.Eventual?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/mazharenko/FluentAssertions.Eventual?style=flat-square&cacheSeconds=86400) - Generates a specialized waiting wrapper for `FluentAssertions` assertions, offering a syntax similar to plain `FluentAssertions`.
- [ScenarioTests](https://github.com/koenbeuk/ScenarioTests) -![stars](https://img.shields.io/github/stars/koenbeuk/ScenarioTests?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/koenbeuk/ScenarioTests?style=flat-square&cacheSeconds=86400) Test your code like you would write a notebook. Simply and effective

#### Mocking

- [GRPC-Mock-Server](https://github.com/cezarypiatek/GRPC-Mock-Server) -![stars](https://img.shields.io/github/stars/cezarypiatek/GRPC-Mock-Server?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/cezarypiatek/GRPC-Mock-Server?style=flat-square&cacheSeconds=86400) - A source generator for stubbing GRPC services.
- [InterfaceGenerator](https://github.com/daver32/InterfaceGenerator) - ![stars](https://img.shields.io/github/stars/daver32/InterfaceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/daver32/InterfaceGenerator?style=flat-square&cacheSeconds=86400) - Auto generate interface definition by implementation, for when you need an abstraction for the sake of mocking.
- [MockableStaticGenerator](https://github.com/HamedFathi/MockableStaticGenerator) - ![stars](https://img.shields.io/github/stars/HamedFathi/MockableStaticGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/HamedFathi/MockableStaticGenerator?style=flat-square&cacheSeconds=86400) A C# source generator to make an interface and a class wrapper to test static/extension methods.
- [MockGen](https://github.com/thomas-girotto/MockGen) - ![stars](https://img.shields.io/github/stars/thomas-girotto/MockGen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/thomas-girotto/MockGen?style=flat-square&cacheSeconds=86400) A C# mocking library based on source generators.
- [MockSourceGenerator](https://github.com/hermanussen/MockSourceGenerator) - ![stars](https://img.shields.io/github/stars/hermanussen/MockSourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/hermanussen/MockSourceGenerator?style=flat-square&cacheSeconds=86400) A C# mocking library that generates mocks at compile-time using a source generator.
- [ProxyInterfaceGenerator](https://github.com/StefH/ProxyInterfaceSourceGenerator) -![stars](https://img.shields.io/github/stars/StefH/ProxyInterfaceSourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/StefH/ProxyInterfaceSourceGenerator?style=flat-square&cacheSeconds=86400) generate an interface and a Proxy class for classes. This makes it possible to wrap external classes which do not have an interface, in a Proxy class which makes it easier to Mock and use DI.
- [Rocks](https://github.com/JasonBock/Rocks) - ![stars](https://img.shields.io/github/stars/JasonBock/Rocks?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/JasonBock/Rocks?style=flat-square&cacheSeconds=86400) A mocking library based on the Compiler APIs (Roslyn + Mocks).

### Patterns

- [Lombok.NET](https://github.com/CollinAlpert/Lombok.NET) - ![stars](https://img.shields.io/github/stars/CollinAlpert/Lombok.NET?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/CollinAlpert/Lombok.NET?style=flat-square&cacheSeconds=86400) Generates boilerplate code and common code patterns. As the name suggests, it is the .NET version of Java's Lombok.

#### Mediator

- [DumplingsDevs.Pipelines](https://github.com/DumplingsDevs/Pipelines) - ![stars](https://img.shields.io/github/stars/DumplingsDevs/Pipelines?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DumplingsDevs/Pipelines?style=flat-square&cacheSeconds=604800) The most flexible mediation implementation in the .NET ecosystem with your own types.
- [Immediate.Handlers](https://github.com/viceroypenguin/Immediate.Handlers) -![stars](https://img.shields.io/github/stars/viceroypenguin/Immediate.Handlers?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/viceroypenguin/Immediate.Handlers?style=flat-square&cacheSeconds=86400) An implementation of the Mediator pattern in .NET using source generators, without using a central mediator instance.
- [Mediator](https://github.com/martinothamar/Mediator) -![stars](https://img.shields.io/github/stars/martinothamar/Mediator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/martinothamar/Mediator?style=flat-square&cacheSeconds=86400) - a high performance implementation of Mediator pattern in .NET using source generators.
- [MediatR controllers generator](https://github.com/Burgyn/MMLib.MediatR.Generators) -![stars](https://img.shields.io/github/stars/Burgyn/MMLib.MediatR.Generators?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Burgyn/MMLib.MediatR.Generators?style=flat-square&cacheSeconds=86400) This generator generates controllers and their methods based on your [MediatR](https://github.com/jbogard/MediatR) requests.

#### Command

- [Plastic](https://github.com/sang-hyeon/Plastic) -![stars](https://img.shields.io/github/stars/sang-hyeon/Plastic?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/sang-hyeon/Plastic?style=flat-square&cacheSeconds=86400) This project provides encapsulation of things like Domain, Application Rules, Business Rules or Business Logic in Application.

#### Builder

- [Data Builder Generator](https://github.com/dasMulli/data-builder-generator) -![stars](https://img.shields.io/github/stars/dasMulli/data-builder-generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/dasMulli/data-builder-generator?style=flat-square&cacheSeconds=86400) Generate data builder patterns for your model classes.
- [FluentBuilder](https://github.com/StefH/FluentBuilder) - ![stars](https://img.shields.io/github/stars/StefH/FluentBuilder?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/StefH/FluentBuilder?style=flat-square&cacheSeconds=86400) - A project which uses Source Generation to create a FluentBuilder for a specified model or DTO.
- [M31.FluentAPI](https://github.com/m31coding/M31.FluentAPI) - ![stars](https://img.shields.io/github/stars/m31coding/M31.FluentAPI?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/m31coding/M31.FluentAPI?style=flat-square&cacheSeconds=86400) - Generate fluent APIs for your C# classes with ease.

#### Proxy

- [avatar](https://github.com/kzu/avatar) -![stars](https://img.shields.io/github/stars/kzu/avatar?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kzu/avatar?style=flat-square&cacheSeconds=86400) A modern compile-time generated interception/proxy library.
- [DudNet](https://github.com/jwshyns/DudNet) - ![stars](https://img.shields.io/github/stars/jwshyns/dudnet?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jwshyns/dudnet?style=flat-square&cacheSeconds=604800) A C# source generator for implementing a proxy pattern.

#### Visitor

- [MrMeeseeks.Visitor](https://github.com/Yeah69/MrMeeseeks.Visitor) - ![stars](https://img.shields.io/github/stars/Yeah69/MrMeeseeks.Visitor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Yeah69/MrMeeseeks.Visitor?style=flat-square&cacheSeconds=86400) Generates the boilerplate code for applications of the Visitor pattern.

#### Adapter

- [AutoInterface](https://github.com/beakona/AutoInterface) -![stars](https://img.shields.io/github/stars/beakona/AutoInterface?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/beakona/AutoInterface?style=flat-square&cacheSeconds=86400) interface-to-member source generator.

### Domain Driven Design (DDD)

- [AltaSoft.DomainPrimitives](https://github.com/altasoft/DomainPrimitives) - ![stars](https://img.shields.io/github/stars/altasoft/DomainPrimitives?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/altasoft/DomainPrimitives?style=flat-square&cacheSeconds=86400) - A C# toolkit purposefully designed to accelerate the development of domain-specific primitives within your applications. This streamlined solution empowers developers to efficiently encapsulate fundamental domain logic. Through this toolkit, you'll significantly reduce code complexity while improving the maintainability of your project.
- [Architect.DomainModeling](https://github.com/TheArchitectDev/Architect.DomainModeling) - ![stars](https://img.shields.io/github/stars/TheArchitectDev/Architect.DomainModeling?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/TheArchitectDev/Architect.DomainModeling?style=flat-square&cacheSeconds=86400) A complete Domain-Driven Design (DDD) toolset for implementing domain models, including base types and source generators for ValueObjects, WrapperValueObjects, Entities, and Identities.

### Metaprogramming

- [GenerateHelperLibraries](https://github.com/musictopia2/GenerateHelperLibraries) - ![stars](https://img.shields.io/github/stars/musictopia2/GenerateHelperLibraries?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/GenerateHelperLibraries?style=flat-square&cacheSeconds=86400)  A source generator where you can send any code to the client without having to do as a string.  Helper for custom classes a client has to override in order to have additional features for source generators.  Intended to be used from another source generator.
- [Gobie](https://github.com/GobieGenerator/Gobie) -![stars](https://img.shields.io/github/stars/GobieGenerator/Gobie?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/GobieGenerator/Gobie?style=flat-square&cacheSeconds=86400) - Allows developers define and use custom source generation without writing any generator code themselves or learning the Roslyn APIs. Instead, devs define the generator they want, in C#, and can then use that generator throughout their project.
- [Matryoshki](https://github.com/krasin-ga/matryoshki) - ![stars](https://img.shields.io/github/stars/krasin-ga/matryoshki?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/krasin-ga/matryoshki?style=flat-square&cacheSeconds=86400) Metaprogramming framework based on C# source generators. It allows you to define behaviours with adornments and generate decorators for arbitrary types.
- [SourceGeneratorQuery](https://github.com/roeibajayo/SourceGeneratorQuery) - ![stars](https://img.shields.io/github/stars/roeibajayo/SourceGeneratorQuery?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/roeibajayo/SourceGeneratorQuery?style=flat-square&cacheSeconds=86400) - C# SourceGenerator helper which helps you query your files, and adds LINQ support.

### Webprogramming

- [AjaxService.Gen](https://github.com/MrAliSalehi/AjaxService) - ![stars](https://img.shields.io/github/stars/MrAliSalehi/AjaxService?style=flat-square) ![last commit](https://img.shields.io/github/last-commit/MrAliSalehi/AjaxService?style=flat-square&cacheSeconds=86400) - Automatically Generate typescript Ajax calls based on your C# Api endpoints.
- [ApiClientGenerator](https://github.com/surgicalcoder/ApiClientGenerator) - ![stars](https://img.shields.io/github/stars/surgicalcoder/ApiClientGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/surgicalcoder/ApiClientGenerator?style=flat-square&cacheSeconds=86400) Generates a strongly typed HttpClient based off MVC's default routing. Can be used to output into multiple projects, like Blazor WebAssembly.
- [ControllerGenerator](https://github.com/cloud0259/ControllerGenerator) -![stars](https://img.shields.io/github/stars/cloud0259/ControllerGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/cloud0259/ControllerGenerator?style=flat-square&cacheSeconds=86400) Automatically generate controllers from services in a web application
- [HttpClientCodeGenerator](https://github.com/Jalalx/HttpClientCodeGenerator) -![stars](https://img.shields.io/github/stars/jalalx/HttpClientCodeGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jalalx/HttpClientCodeGenerator?style=flat-square&cacheSeconds=86400) - HttpClientGenerator is a tool that uses the Roslyn code generator feature to write boilerplate HttpClient code for you.
- [Ridge](https://github.com/Melchy/Ridge) -![stars](https://img.shields.io/github/stars/Melchy/Ridge?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Melchy/Ridge?style=flat-square&cacheSeconds=86400) Generates strongly-typed clients for API based on controller definition and internal application details.
- [Safe-Routing](https://github.com/daviddotcs/safe-routing) -![stars](https://img.shields.io/github/stars/daviddotcs/safe-routing?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/daviddotcs/safe-routing?style=flat-square&cacheSeconds=86400)  Analyses a project's razor pages and MVC controllers, producing strongly-typed representations of those routes as you type
- [TypedSignalR.Client](https://github.com/nenoNaninu/TypedSignalR.Client) -![stars](https://img.shields.io/github/stars/nenoNaninu/TypedSignalR.Client?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/nenoNaninu/TypedSignalR.Client?style=flat-square&cacheSeconds=86400) C# Source Generator to create strongly typed SignalR clients.

#### Open Api

- [H.NSwag.Generator](https://github.com/HavenDV/H.NSwag.Generator) -![stars](https://img.shields.io/github/stars/HavenDV/H.NSwag.Generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/HavenDV/H.NSwag.Generator?style=flat-square&cacheSeconds=86400) - C# Source Generator for NSwag.
- [SourceApi](https://github.com/alekshura/SourceApi) - ![stars](https://img.shields.io/github/stars/alekshura/SourceApi?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/alekshura/SourceApi?style=flat-square&cacheSeconds=86400) - API first Open API code generator based on json or yaml definitions. It generates base abstract controllers with docs, routes, that you inherit and implement in your controllers.
- [ST.NSwag.ServerSourceGenerator](https://github.com/s-tarasov/ST.NSwag.ServerSourceGenerator) -![stars](https://img.shields.io/github/stars/s-tarasov/ST.NSwag.ServerSourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/s-tarasov/ST.NSwag.ServerSourceGenerator?style=flat-square&cacheSeconds=86400) Generates Web API/ASP.NET Core controllers from a OpenAPI specification.

#### Razor / Blazor

- [BlazorInteropGenerator](https://github.com/surgicalcoder/BlazorInteropGenerator) -![stars](https://img.shields.io/github/stars/surgicalcoder/BlazorInteropGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/surgicalcoder/BlazorInteropGenerator?style=flat-square&cacheSeconds=86400) Generates Blazor -> Javascript strongly typed interop methods, by parsing the Javascript it self and generating extension methods for IJSRuntime.
- [BlazorOcticons](https://github.com/BlazorOcticons/BlazorOcticons) - ![stars](https://img.shields.io/github/stars/BlazorOcticons/BlazorOcticons?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/BlazorOcticons/BlazorOcticons?style=flat-square&cacheSeconds=86400) Github [Octicons](https://primer.style/octicons/) created as a `.razor` components using source generator. The generated components are available via the NuGet package, the generator itself is available as a separate NuGet package. The project [website](https://blazorocticons.net/) is an example using the generated components.
- [MiniRazor](https://github.com/Tyrrrz/MiniRazor) -![stars](https://img.shields.io/github/stars/Tyrrrz/MiniRazor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Tyrrrz/MiniRazor?style=flat-square&cacheSeconds=86400) Portable Razor compiler & code generator.
- [RazorPageRouteGenerator](https://github.com/surgicalcoder/RazorPageRouteGenerator) - ![stars](https://img.shields.io/github/stars/surgicalcoder/RazorPageRouteGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/surgicalcoder/RazorPageRouteGenerator?style=flat-square&cacheSeconds=86400) Generates methods with parameters for Razor and Blazor pages, so you can navigate without having to guess URLs or parameters.

### XAML / WPF / Avalonia

- [Avalonia.NameGenerator](https://github.com/AvaloniaUI/Avalonia.NameGenerator) -![stars](https://img.shields.io/github/stars/avaloniaui/Avalonia.NameGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/avaloniaui/Avalonia.NameGenerator?style=flat-square&cacheSeconds=86400) Generates typed references to named [Avalonia](https://github.com/avaloniaui) XAML controls.
- [boilerplatezero](https://github.com/IGood/boilerplatezero) -![stars](https://img.shields.io/github/stars/IGood/boilerplatezero?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/IGood/boilerplatezero?style=flat-square&cacheSeconds=86400) WPF Dependency Property and Routed Event generator.
- [DependencyPropertyGenerator](https://github.com/HavenDV/DependencyPropertyGenerator) - ![stars](https://img.shields.io/github/stars/HavenDV/DependencyPropertyGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/HavenDV/DependencyPropertyGenerator?style=flat-square&cacheSeconds=86400) Dependency property and routed event source generator for WPF/UWP/WinUI/Uno/Avalonia/MAUI platforms.
- [WinUI-ObservableSettings](https://github.com/JasonWei512/WinUI-ObservableSettings) -![stars](https://img.shields.io/github/stars/JasonWei512/WinUI-ObservableSettings?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/JasonWei512/WinUI-ObservableSettings?style=flat-square&cacheSeconds=86400) - Generate boilerplates to read and write settings in packaged WinUI 3 app.

#### INotifyPropertyChanged

- [PropertyChanged.SourceGenerator](https://github.com/canton7/PropertyChanged.SourceGenerator) -![stars](https://img.shields.io/github/stars/canton7/PropertyChanged.SourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/canton7/PropertyChanged.SourceGenerator?style=flat-square&cacheSeconds=86400) - Powerful INotifyPropertyChanged Source Generator, which generates INPC boilerplate for you as part of your build. Supports features such as automatic and manual dependencies between properties, notifications when specific properties change, and more.
- [ValueChangedGenerator](https://github.com/ufcpp/ValueChangedGenerator) -![stars](https://img.shields.io/github/stars/ufcpp/ValueChangedGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ufcpp/ValueChangedGenerator?style=flat-square&cacheSeconds=86400) for generating PropertyChanged from inner struct members.

#### Model View Viewmodel (MVVM)

- [DevExpress.Mvvm.CodeGenerators](https://github.com/DevExpress/DevExpress.Mvvm.CodeGenerators) - ![stars](https://img.shields.io/github/stars/DevExpress/DevExpress.Mvvm.CodeGenerators?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DevExpress/DevExpress.Mvvm.CodeGenerators?style=flat-square&cacheSeconds=86400) Generates boilerplate code for your View Models (INotifyPropertyChanged, Commands, IDataErrorInfo, DevExpress services). Compatible with the Prism and MVVM Light libraries.
- [Microsoft MVVM Toolkit](https://github.com/CommunityToolkit/dotnet) -![stars](https://img.shields.io/github/stars/CommunityToolkit/dotnet?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/CommunityToolkit/dotnet?style=flat-square&cacheSeconds=86400) A modular MVVM library with support for source generators to reduce boilrplate and improve performance.
- [MvvmGen](https://github.com/thomasclaudiushuber/mvvmgen) - ![stars](https://img.shields.io/github/stars/thomasclaudiushuber/MvvmGen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/thomasclaudiushuber/MvvmGen?style=flat-square&cacheSeconds=86400) A lightweight MVVM library for XAML applications that generates your ViewModels with a C# Source Generator.

### Database / ORM

- [AdaskoTheBeAsT.Identity.Dapper](https://github.com/AdaskoTheBeAsT/AdaskoTheBeAsT.Identity.Dapper) - ![stars](https://img.shields.io/github/stars/AdaskoTheBeAsT/AdaskoTheBeAsT.Identity.Dapper?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/AdaskoTheBeAsT/AdaskoTheBeAsT.Identity.Dapper?style=flat-square&cacheSeconds=86400) - Custom Dapper implementation for Microsoft.Extensions.Identity.Stores (part of ASP.NET Core Identity)
- [Breezy](https://github.com/Ludovicdln/Breezy) - ![stars](https://img.shields.io/github/stars/Ludovicdln/Breezy?style=flat-square&cacheSeconds=604800)	![last commit](https://img.shields.io/github/last-commit/ludovicdln/Breezy?style=flat-square&cacheSeconds=86400) Micro ORM with source generator.
- [MapDataReader](https://github.com/jitbit/MapDataReader) - ![stars](https://img.shields.io/github/stars/jitbit/mapdatareader?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jitbit/mapdatareader?style=flat-square&cacheSeconds=86400) - Fast mapping `IDataReader` to a custom class
- [SqlMarshal](https://github.com/kant2002/SqlMarshal) -![stars](https://img.shields.io/github/stars/kant2002/SqlMarshal?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kant2002/SqlMarshal?style=flat-square&cacheSeconds=86400) Native AOT friendly-performant mini-ORM. Generation of wrappers for accessing SQL using ADO.NET.

### Statically typed resources / configurations

- [dot-env-generator](https://github.com/RainwayApp/dot-env-generator) - ![stars](https://img.shields.io/github/stars/RainwayApp/dot-env-generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RainwayApp/dot-env-generator?style=flat-square&cacheSeconds=86400) A source generator for C# that turns `.env` files into runtime constants.
- [EnvVariablesGenerator](https://github.com/KAW0/EnvVariablesGenerator) - ![stars](https://img.shields.io/github/stars/KAW0/EnvVariablesGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/KAW0/EnvVariablesGenerator?style=flat-square&cacheSeconds=86400) Generate code from `.env` files that can be changed after build.
- [NotNot.AppSettings](https://github.com/jasonswearingen/NotNot.AppSettings) - ![stars](https://img.shields.io/github/stars/jasonswearingen/NotNot.AppSettings?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jasonswearingen/NotNot.AppSettings?style=flat-square&cacheSeconds=86400) Automatically create strongly typed C# settings objects from AppSettings.json.
- [SourceConfig](https://github.com/alekshura/SourceConfig) - ![stars](https://img.shields.io/github/stars/alekshura/SourceConfig?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/alekshura/SourceConfig?style=flat-square&cacheSeconds=86400) - Generates configuration POCO objects, lists, dictionaries in AOT based on *.json config files.
- [StronglyTypedEmbeddedResources](https://github.com/surgicalcoder/StronglyTypedEmbeddedResources) - ![stars](https://img.shields.io/github/stars/surgicalcoder/StronglyTypedEmbeddedResources?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/surgicalcoder/StronglyTypedEmbeddedResources?style=flat-square&cacheSeconds=86400) Generates strongly typed names for Embedded Resources automatically.
- [TxtToListGenerator](https://github.com/musictopia2/TxtToListGenerator) - ![stars](https://img.shields.io/github/stars/musictopia2/TxtToListGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/TxtToListGenerator?style=flat-square&cacheSeconds=86400)  A source generator where if you have a text file as additional file and you have a list ordered by return carriages, then it produces either a list of int or a list of string in c#.

### Text templating

- [Transplator](https://github.com/atifaziz/Transplator) - ![stars](https://img.shields.io/github/stars/atifaziz/Transplator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/atifaziz/Transplator?style=flat-square&cacheSeconds=86400) A simple C# source generator for text templates.
- [Weave](https://github.com/otac0n/Weave) - ![stars](https://img.shields.io/github/stars/otac0n/Weave?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/otac0n/Weave?style=flat-square&cacheSeconds=86400) Weave is a text templating engine for .NET that is all about attention to detail. Weave handles the tricky work of making your rendered text beautiful.

### Other

- [AutoConstructor](https://github.com/k94ll13nn3/AutoConstructor) - ![stars](https://img.shields.io/github/stars/k94ll13nn3/AutoConstructor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/k94ll13nn3/AutoConstructor?style=flat-square&cacheSeconds=86400) C# source generator that generates a constructor from readonly fields/properties in a class or struct.
- [AutoFilterer.Generators](https://github.com/enisn/AutoFilterer/blob/develop/docs/generators/AutoFilterer-Generators.md) - ![stars](https://img.shields.io/github/stars/enisn/AutoFilterer?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/enisn/AutoFilterer?style=flat-square&cacheSeconds=86400) AutoFilterer.Generators aims to generate filter DTOs from entities automatically via using dotnet source generators.
- [AutomaticInterface](https://github.com/codecentric/net_automatic_interface) - ![stars](https://img.shields.io/github/stars/codecentric/net_automatic_interface?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/codecentric/net_automatic_interface?style=flat-square&cacheSeconds=86400) Generate an Interface from a class.
- [AutoInvoke](https://github.com/LokiMidgard/AutoInvoke.Generator) -![stars](https://img.shields.io/github/stars/LokiMidgard/AutoInvoke.Generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/LokiMidgard/AutoInvoke.Generator?style=flat-square&cacheSeconds=86400) A generator that generates a method that invokes a specified generic method, for every Type in your project that satisfies a defined constraint.
- [BigMachines](https://github.com/archi-Doc/BigMachines) -![stars](https://img.shields.io/github/stars/archi-Doc/BigMachines?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/archi-Doc/BigMachines?style=flat-square&cacheSeconds=86400) BigMachines is State Machine library for .NET.
- [BitsKit](https://github.com/barncastle/BitsKit) - A C# library for efficient bit-level reading and writing also adding bit field support
- [CacheSourceGenerator](https://github.com/jeppevammenkristensen/cachesourcegenerator) -![stars](https://img.shields.io/github/stars/jeppevammenkristensen/cachesourcegenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jeppevammenkristensen/cachesourcegenerator?style=flat-square&cacheSeconds=86400) Generates an IMemoryCache wrapper around a method call. 
- [Cloneable](https://github.com/mostmand/Cloneable) -![stars](https://img.shields.io/github/stars/mostmand/Cloneable?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/mostmand/Cloneable?style=flat-square&cacheSeconds=86400) auto-generate Clone method.
- [Durian](https://github.com/piotrstenke/Durian) - ![stars](https://img.shields.io/github/stars/piotrstenke/Durian?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/piotrstenke/Durian?style=flat-square&cacheSeconds=86400) Extends the default capabilities of C# by mimicking features from other languages.
- [Fairy](https://github.com/hermanussen/Fairy) -![stars](https://img.shields.io/github/stars/hermanussen/Fairy?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/hermanussen/Fairy?style=flat-square&cacheSeconds=86400) generates C# code based on Sitecore Content Serialization (SCS) `.yml` files.
- [FastGenericNew](https://github.com/Nyrest/FastGenericNew) - ![stars](https://img.shields.io/github/stars/Nyrest/FastGenericNew?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Nyrest/FastGenericNew?style=flat-square&cacheSeconds=86400)  The ultimate fast alternative to `Activator.CreateInstance<T>` / `new T()`.  Built on SourceGenerator V2 (Incremental Generator).
- [GitBuildInfo.SourceGenerator](https://github.com/Elskom/GitBuildInfo.SourceGenerator) -![stars](https://img.shields.io/github/stars/Elskom/GitBuildInfo.SourceGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Elskom/GitBuildInfo.SourceGenerator?style=flat-square&cacheSeconds=86400) - for dumping the git information (commit hash, branch, the head description) into assembly level metadata attributes.
- [Hangfire.RecurringJob](https://github.com/IeuanWalker/Hangfire.RecurringJob) - ![stars](https://img.shields.io/github/stars/IeuanWalker/Hangfire.RecurringJob?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/IeuanWalker/Hangfire.RecurringJob?style=flat-square&cacheSeconds=86400) - Automatically generates the recurring job registration code.
- [IDisposableGenerator](https://github.com/Elskom/IDisposableGenerator) -![stars](https://img.shields.io/github/stars/Elskom/IDisposableGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Elskom/IDisposableGenerator?style=flat-square&cacheSeconds=86400) - a Source Generator for Generating the Dispose functions in Disposables. All you have to do is mark them with attributes and it will work from there.
- [Lazysh](https://github.com/B1Z0N/LazyshGen) - ![stars](https://img.shields.io/github/stars/B1Z0N/LazyshGen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/B1Z0N/LazyshGen?style=flat-square&cacheSeconds=86400) Lazy implementation of any interface.
- [LinqGen](https://github.com/cathei/LinqGen) - ![stars](https://img.shields.io/github/stars/cathei/LinqGen?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/cathei/LinqGen?style=flat-square&cacheSeconds=86400) Alloc-free and fast replacement for Linq, with code generation.
- [LoggingDecoratorGenerator](https://github.com/DavidFineboym/LoggingDecoratorGenerator) - ![stars](https://img.shields.io/github/stars/DavidFineboym/LoggingDecoratorGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/DavidFineboym/LoggingDecoratorGenerator?style=flat-square&cacheSeconds=86400) Generates logger decorator class for an interface. Uses Microsoft.Extensions.Logging.ILogger to log and requires it in decorator class constructor.
- [MemberAccessGenerator](https://github.com/ufcpp/MemberAccessGenerator) -![stars](https://img.shields.io/github/stars/ufcpp/MemberAccessGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ufcpp/MemberAccessGenerator?style=flat-square&cacheSeconds=86400) generates `GetMember(int)` and/or `GetMember(string)` methods that return property value for a given property name or index (e.g. in positional records).
- [MrMeeseeks.StaticDelegateGenerator](https://github.com/Yeah69/MrMeeseeks.StaticDelegateGenerator) - ![stars](https://img.shields.io/github/stars/Yeah69/MrMeeseeks.StaticDelegateGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Yeah69/MrMeeseeks.StaticDelegateGenerator?style=flat-square&cacheSeconds=86400) Makes static classes and members injectable as dependency by generating delegating interfaces and their implementing classes.
- [Navitski.Crystalized](https://github.com/AlexNav73/Navitski.Crystalized) - ![stars](https://img.shields.io/github/stars/AlexNav73/Navitski.Crystalized?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/AlexNav73/Navitski.Crystalized?style=flat-square&cacheSeconds=86400) Generates domain model based on schema files. Generated model supports undo/redo, saving to/loading from SQLite and Json files, precise changes tracking and more.
- [net_automatic_interface](https://github.com/codecentric/net_automatic_interface) -![stars](https://img.shields.io/github/stars/codecentric/net_automatic_interface?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/codecentric/net_automatic_interface?style=flat-square&cacheSeconds=86400) .Net Core Source Generator for Automatic Interfaces.
- [PolySharp](https://github.com/Sergio0694/PolySharp) -![stars](https://img.shields.io/github/stars/Sergio0694/PolySharp?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Sergio0694/PolySharp?style=flat-square&cacheSeconds=86400) Provides generated, source-only polyfills for C# language features, to easily use all runtime-agnostic features downlevel.
- [PrimaryConstructor](https://github.com/chaowlert/PrimaryConstructor) -![stars](https://img.shields.io/github/stars/chaowlert/PrimaryConstructor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/chaowlert/PrimaryConstructor?style=flat-square&cacheSeconds=86400) Generate primary constructor from readonly fields.
- [PrimitiveStaticDataGenerator](https://github.com/iiweis/PrimitiveStaticDataGenerator) -![stars](https://img.shields.io/github/stars/iiweis/PrimitiveStaticDataGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/iiweis/PrimitiveStaticDataGenerator?style=flat-square&cacheSeconds=86400) for creating methods that return optimized `ReadOnlySpan<T>` static data from primitive values.
- [PrintMembersGenerator](https://github.com/Youssef1313/PrintMembersGenerator) -![stars](https://img.shields.io/github/stars/Youssef1313/PrintMembersGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Youssef1313/PrintMembersGenerator?style=flat-square&cacheSeconds=86400) helps re-defining C# record's PrintMembers method to force include/exclude certain members.
- [QuickConstructor](https://github.com/flavien/QuickConstructor) - ![stars](https://img.shields.io/github/stars/flavien/QuickConstructor?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/flavien/QuickConstructor?style=flat-square&cacheSeconds=86400) A reliable and feature-rich source generator that can automatically emit a constructor from the fields and properties of a class. It can also generate null checks based on nullable reference types annotations.
- [SmallSharp](https://github.com/kzu/SmallSharp) -![stars](https://img.shields.io/github/stars/kzu/SmallSharp?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kzu/SmallSharp?style=flat-square&cacheSeconds=86400) Create, edit and run multiple C# 9.0 top-level programs in the same project by just selecting the startup program from the start button.
- [SmartAnnotations](https://github.com/fiseni/SmartAnnotations) -![stars](https://img.shields.io/github/stars/fiseni/SmartAnnotations?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/fiseni/SmartAnnotations?style=flat-square&cacheSeconds=86400) A library that uses source generators to automatically generate data annotations for your models. It provides a strongly-typed mechanism (fluent like API) to define your annotation rules.
- [StringLiteralGenerator](https://github.com/ufcpp/StringLiteralGenerator) -![stars](https://img.shields.io/github/stars/ufcpp/StringLiteralGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ufcpp/StringLiteralGenerator?style=flat-square&cacheSeconds=86400) for optimizing UTF-8 binaries.
- [SyncMethodGenerator](https://github.com/zompinc/sync-method-generator) -![stars](https://img.shields.io/github/stars/zompinc/sync-method-generator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/zompinc/sync-method-generator?style=flat-square&cacheSeconds=86400) - Generates a synchronized method from your async code.
- [ThisAssembly](https://github.com/kzu/ThisAssembly) -![stars](https://img.shields.io/github/stars/kzu/ThisAssembly?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/kzu/ThisAssembly?style=flat-square&cacheSeconds=86400) Exposes project and assembly level information as constants in the ThisAssembly class.
- [ToString](https://github.com/Burgyn/MMLib.ToString) -![stars](https://img.shields.io/github/stars/Burgyn/MMLib.ToString?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Burgyn/MMLib.ToString?style=flat-square&cacheSeconds=86400) - C# source generator for implementing `ToString` override like `record` type.
- [TupleOverloadGenerator](https://github.com/ProphetLamb/TupleOverloadGenerator) - ![stars](https://img.shields.io/github/stars/ProphetLamb/TupleOverloadGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/ProphetLamb/TupleOverloadGenerator?style=flat-square&cacheSeconds=86400) - Overload `params` array parameter with tuples avoiding heap allocations.
- [ValueLink](https://github.com/archi-Doc/ValueLink) -![stars](https://img.shields.io/github/stars/archi-Doc/ValueLink?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/archi-Doc/ValueLink?style=flat-square&cacheSeconds=86400) A C# Library for creating and managing multiple links between objects.

## Meta - libs and generators for other generators

<!--
  Sorted alphabetically. Template for entries:
- [REPO](https://github.com/REPO) - ![stars](https://img.shields.io/github/stars/REPO?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/REPO?style=flat-square&cacheSeconds=86400)
-->

- [AttributeFactoryGenerator](https://github.com/PaulBraetz/AttributeFactoryGenerator) - ![stars](https://img.shields.io/github/stars/PaulBraetz/AttributeFactoryGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/PaulBraetz/AttributeFactoryGenerator?style=flat-square&cacheSeconds=86400) - Generate factories to easily parse actual attribute instances from symbol data.
- [AttributesSourceGeneratorHelper](https://github.com/musictopia2/AttributesSourceGeneratorHelper) - ![stars](https://img.shields.io/github/stars/musictopia2/AttributesSourceGeneratorHelper?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/AttributesSourceGeneratorHelper?style=flat-square&cacheSeconds=86400)  A source generator to help another generator by producing attributes.  Anything that inherits from Attribute will be sent to the client so you don't have to build strings for attributes.
- [CommonSourceGeneratorsHelpers](https://github.com/musictopia2/CommonSourceGeneratorsHelpers) - ![stars](https://img.shields.io/github/stars/musictopia2/CommonSourceGeneratorsHelpers?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/musictopia2/CommonSourceGeneratorsHelpers?style=flat-square&cacheSeconds=86400)  A generator to create many helpers for source generators to use to make up that its very difficult to reference third party libraries in source generators including extensions and a source code string builder.
- [HotReload](https://github.com/andrzejolszak/BuilderGeneratorHotReload) - ![stars](https://img.shields.io/github/stars/andrzejolszak/BuilderGeneratorHotReload?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/andrzejolszak/BuilderGeneratorHotReload?style=flat-square&cacheSeconds=86400) - A simple hack to enable hot reload in Visual Studio Intellisense when developing a source generator project together with an example dependent client project inside a single solution.
- [SourceGeneratorUtils](https://github.com/thenameless314159/SourceGeneratorUtils) - ![stars](https://img.shields.io/github/stars/thenameless314159/SourceGeneratorUtils?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/thenameless314159/SourceGeneratorUtils?style=flat-square&cacheSeconds=86400)  An essential library equipped with utility functions and helpers to aid in writing source files for source generators or for general purposes. Based on the `System.Text.Json` source generator architecture for best-practices.
- [SourceGenerator.Helper.CopyCode](https://github.com/LokiMidgard/SourceGenerator.Helper.CopyCode) - ![stars](https://img.shields.io/github/stars/LokiMidgard/SourceGenerator.Helper.CopyCode?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/LokiMidgard/SourceGenerator.Helper.CopyCode?style=flat-square&cacheSeconds=86400) - A simple Generator that generates a string representation to an annotated Type.

## Tips & Tricks

Collection of tips and tricks (simple and brief to fit in Tweet):

[Tweeted](https://twitter.com/raboof/status/1397296571801288704) by [@raboof](https://twitter.com/raboof) on May 25 2021 at 23:00:

> TIL to debug a source generator in VS 16.10: upgrade [Microsoft.CodeAnalysis.CSharp to 3.10.\*](https://www.nuget.org/packages/Microsoft.CodeAnalysis.CSharp/3.10.0-3.final), add `<IsRoslynComponent>true</IsRoslynComponent>` to source generator project, select **Roslyn Component** for **Launch** in **Project Properties Debug** page, choose **Target** then <kbd>F5</kbd> :rocket:
>
> ![Source Generator debugger](https://docs.microsoft.com/en-us/visualstudio/releases/2019/media/16.10/16.10_p2_source_generators_debugger.png)

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

Build failed in WPF projects [microsoft/CsWin32#7](https://github.com/microsoft/CsWin32/issues/7):

> If your build failed in a *_wpftmp.csproj file you need to add following property to your (*.csproj) project file:
> ```xml
> <IncludePackageReferencesDuringMarkupCompilation>true</IncludePackageReferencesDuringMarkupCompilation>
> ```
>
> and use at least .NET 5.0.102 SDK

  [#SourceGenerators]: https://twitter.com/hashtag/SourceGenerators?src=hashtag_click
  [#sourcegenerators]: https://twitter.com/hashtag/sourcegenerators?src=hashtag_click
  [#roslyn]: https://twitter.com/hashtag/roslyn?src=hashtag_click
  [#csharp]: https://twitter.com/hashtag/csharp?src=hashtag_click
  [#dotnetcore]: https://twitter.com/hashtag/dotnetcore?src=hashtag_click
  [#analyzers]: https://twitter.com/hashtag/analyzers?src=hashtag_click

Reference local projects or embed NuGet packages to source generator assemblies [dotnet/roslyn#47517](https://github.com/dotnet/roslyn/discussions/47517#discussioncomment-64145):

⚠ Please be aware that this may result in crashes, when another generator or SDK component loads such an assembly with lower version. If you can, please avoid embedding additional DLLs/packages.

> You can add a dependency to a source generator in the same solution through three steps:
> 
> 1. Add a `<PackageReference>`, making sure to set both `GeneratePathProperty="true"` and `PrivateAssets="all"`
> 2. Add a build target to add `<TargetPathWithTargetPlatformMoniker>` elements as part of GetTargetPath, and add all the required dependency assemblies inside this target, making sure to set `IncludeRuntimeDependency="false"`
> 3. Update `<GetTargetPathDependsOn>` to ensure the target from the previous step is used
> 
> You can see an example of these steps here:
> https://github.com/dotnet/roslyn-sdk/blob/0313c80ed950ac4f4eef11bb2e1c6d1009b328c4/samples/CSharp/SourceGenerators/SourceGeneratorSamples/SourceGeneratorSamples.csproj#L13-L30

## Articles

<!--
  Sorted from newest. Please follow the template:
  - [Title](URL) (YYYY-MM-DD) short description.
-->
- [Series: Creating a source generator](https://andrewlock.net/series/creating-a-source-generator/) (2022-02-01) Complete series about how to create an incremental source generator, using the APIs introduced in .NET 6.
- [Mastering at Source Generators](https://medium.com/c-sharp-progarmming/mastering-at-source-generators-18125a5f3fca) (2022-01-15) Generating CRUD controller from DTO model using text template.
- [Using C# Source Generators to create an external DSL](https://devblogs.microsoft.com/dotnet/using-c-source-generators-to-create-an-external-dsl/) (2021-01-27) that shows how to implement a simple DSL.
- [4 ways to generate code in C# — Including Source Generators in .NET 5](https://levelup.gitconnected.com/four-ways-to-generate-code-in-c-including-source-generators-in-net-5-9e6817db425) (2021-01-19) demonstrates the comparison between Source Generators, T4 template and Reflection, etc.
- [.NET 5 Source Generators - MediatR - CQRS - OMG!](https://www.edument.se/en/blog/post/net-5-source-generators-mediatr-cqrs) (2020-12-16) explores how source generators can be used to automatically generate an API for a system using the MediatR library and the CQRS pattern.
- [Source Generators in .NET 5 with ReSharper](https://blog.jetbrains.com/dotnet/2020/11/12/source-generators-in-net-5-with-resharper/) (2020-11-20) introduces source generators and briefly mentions how they are being worked into the ReSharper product.
- [Source Generators - real world example](https://dominikjeske.github.io/source-generators) (2020-11-09) contains a rich and deep dive into a real world generator with lots of useful tips.
- [How to profile C# 9.0 Source Generators](https://jaylee.org/archive/2020/10/10/profiling-csharp-9-source-generators.html) (2020-10-10) demonstrates how to profile your source generator using the [performance profiling tools built into Visual Studio](https://docs.microsoft.com/en-us/visualstudio/profiling/?view=vs-2019).
- [How to Debug C# 9 Source Code Generators](https://nicksnettravels.builttoroam.com/debug-code-gen/) (2020-10-09) contains debugging tips.
- [How to generate code using Roslyn source generators in real world scenarios](https://www.cazzulino.com/source-generators.html) (2020-09-17) rich story of how ThisAssembly generator was written using Scriban templates.
- [.NET Blog 'New C# Source Generator Samples' post](https://devblogs.microsoft.com/dotnet/new-c-source-generator-samples/) (2020-08-25) that shows some simple samples.
- [.NET Blog 'Introducing C# Source Generators' post](https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/) (2020-04-29) that announces the feature.

## Videos

<!--
  Sorted from newest. Please follow the template:
  - [Title](URL) (YYYY-MM-DD) short description.
-->

- [C# Source Generators - Write code that writes code - David Wengier](https://www.youtube.com/watch?v=pqLs7X6Cr6s) (2020-11-13) Roslyn dev takes deep dive into the topic.
- [.NET Languages and Runtime Community Standup - Source Generators](https://www.youtube.com/watch?v=A4479Etdx4I) (2020-10-08) shows how Generators work and how they can be tested.
- [Channel 9 'Source Generators in C#'](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Source-Generators-in-CSharp) (2020-08-12) has Roslyn PMs discussing the feature.

## Demo, PoC and excercise projects

Maybe they can inspire you too!

- [RyanAlameddine/SourceGeneratorDemo](https://github.com/RyanAlameddine/SourceGeneratorDemo) - ![stars](https://img.shields.io/github/stars/RyanAlameddine/SourceGeneratorDemo?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/RyanAlameddine/SourceGeneratorDemo?style=flat-square&cacheSeconds=86400) contains 3 demos: hello world, INPC and OpCode class.
- [TMC-CSharp/CodeExerciseLibrary](https://github.com/TMC-CSharp/CodeExerciseLibrary) - ![stars](https://img.shields.io/github/stars/TMC-CSharp/CodeExerciseLibrary?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/TMC-CSharp/CodeExerciseLibrary?style=flat-square&cacheSeconds=86400) Library to help creating C# exercises. Generates missing methods and classes inside tests on the fly by using Source Generators.
- [DpdtInject](https://github.com/lsoft/DpdtInject) - ![stars](https://img.shields.io/github/stars/lsoft/DpdtInject?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/lsoft/DpdtInject?style=flat-square&cacheSeconds=86400) DI container based on C# Source Generators. Its goal is to remove everything possible from runtime and make resolving process as faster as we can. This is achieved by transferring huge piece of resolving logic to the compilation stage into the source generator.
- [jakubsturc/talk-csharp-source-generators](https://github.com/jakubsturc/talk-csharp-source-generators/tree/master/demo/SourceGeneratorSamples) - ![stars](https://img.shields.io/github/stars/jakubsturc/talk-csharp-source-generators?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/jakubsturc/talk-csharp-source-generators?style=flat-square&cacheSeconds=86400) contains 4 generators: AutoNotify, ConsoleWritelineHijack, HelloWorld and SettingsXml, plus nice presentation slides.
- [Compile Time Method Execution Generator](https://github.com/hermanussen/CompileTimeMethodExecutionGenerator) - ![stars](https://img.shields.io/github/stars/hermanussen/CompileTimeMethodExecutionGenerator?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/hermanussen/CompileTimeMethodExecutionGenerator?style=flat-square&cacheSeconds=86400) proof of concept that allows executing a method during compilation, so that it can be really fast during runtime.

## Projects using custom Source Generators "internally"

- [Elskom/Sdk](https://github.com/Elskom/Sdk) - ![stars](https://img.shields.io/github/stars/Elskom/Sdk?style=flat-square$cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/Elskom/Sdk?style=flat-square&cacheSeconds=86400) Dumps git repository data to assembly level metadata attributes that can be checked at runtime for things like trapping if a user is using an possibly unstable build of the libraries built in the repository and so the user can see a message about it (and optionally opt into running the possibly unstable code).
- [Heroicons.AspNetCore](https://github.com/tompazourek/Heroicons.AspNetCore) -![stars](https://img.shields.io/github/stars/tompazourek/Heroicons.AspNetCore?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/tompazourek/Heroicons.AspNetCore?style=flat-square&cacheSeconds=86400) [Heroicons](https://heroicons.com/) that are easy to use in ASP.NET Core MVC as TagHelpers.
- [NetFabric.Hyperlinq](https://github.com/NetFabric/NetFabric.Hyperlinq) - ![stars](https://img.shields.io/github/stars/NetFabric/NetFabric.Hyperlinq?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/NetFabric/NetFabric.Hyperlinq?style=flat-square&cacheSeconds=86400) generates overloads for its extension methods.
- [RestEase](https://github.com/canton7/RestEase) - ![stars](https://img.shields.io/github/stars/canton7/RestEase?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/canton7/RestEase?style=flat-square&cacheSeconds=86400) uses Source Generator to generate interface implementations on compile time instead of in runtime via Reflection.Emit.
- [WarHub/wham](https://github.com/WarHub/wham) - ![stars](https://img.shields.io/github/stars/WarHub/wham?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/WarHub/wham?style=flat-square&cacheSeconds=86400) generates code for immutable tree object graph based on red-green node approach used in Roslyn; generates custom XmlSerializer that supports C#9 records and ImmutableArray.
