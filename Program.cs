// Minimal ASP.NET Core example to serve modules.json
// Run with: dotnet new web -o WebApiExample (or place into a .NET 6+ project)
// This file is a minimal Program.cs sketch for reference.
using System.Text.Json;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapGet("/api/modules", async ctx =>
{
    var path = Path.Combine(AppContext.BaseDirectory, "modules.json");
    if (!File.Exists(path))
    {
        ctx.Response.StatusCode = 404;
        await ctx.Response.WriteAsync("modules.json not found");
        return;
    }
    var json = await File.ReadAllTextAsync(path);
    ctx.Response.ContentType = "application/json";
    await ctx.Response.WriteAsync(json);
});

app.MapGet("/", async ctx =>
{
    var path = Path.Combine(AppContext.BaseDirectory, "trade-with-suli.html");
    if (File.Exists(path)) await ctx.Response.SendFileAsync(path);
    else await ctx.Response.WriteAsync("trade-with-suli.html not found");
});

app.Run();
