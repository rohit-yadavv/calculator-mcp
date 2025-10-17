from fastmcp import FastMCP

mcp = FastMCP("MCP Calculator Server")

@mcp.tool()
def add(a:int, b:int) -> int:
    return a+b


@mcp.tool()
def subtract(a:int, b:int) -> int:
    return a - b


@mcp.tool()
def multiply(a:int, b:int) -> int:
    return a * b


@mcp.tool()
def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


@mcp.tool()
def modulus(a:int, b:int) -> int:
    if b == 0:
        raise ValueError("Modulus by zero is not allowed")
    return a % b


@mcp.tool()
def power(a:float, b:float) -> float:
    return a ** b


@mcp.tool()
def sqrt(x:float) -> float:
    if x < 0:
        raise ValueError("Square root of a negative number is not allowed")
    return x ** 0.5


if __name__ == "__main__":
    mcp.run()