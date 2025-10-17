from fastmcp import FastMCP

mcp = FastMCP("MCP Calculator Server")

@mcp.tool()
async def add(a:int, b:int) -> int:
    return a+b


@mcp.tool()
async def subtract(a:int, b:int) -> int:
    return a - b


@mcp.tool()
async def multiply(a:int, b:int) -> int:
    return a * b


@mcp.tool()
async def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


@mcp.tool()
async def modulus(a:int, b:int) -> int:
    if b == 0:
        raise ValueError("Modulus by zero is not allowed")
    return a % b


@mcp.tool()
async def power(a:float, b:float) -> float:
    return a ** b


@mcp.tool()
async def sqrt(x:float) -> float:
    if x < 0:
        raise ValueError("Square root of a negative number is not allowed")
    return x ** 0.5


if __name__ == "__main__":
    mcp.run(transport="stdio")