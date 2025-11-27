# Python Syntax

## Understanding Indentation

Indentation is one of Python's most distinctive features. Unlike many other programming languages where indentation is just for readability, **Python uses indentation to define code blocks**.

### What is Indentation?

Indentation refers to the **spaces or tabs at the beginning of a code line**. It tells Python which lines of code belong together as a block.

### Why Indentation Matters

- **Mandatory syntax**: Python requires proper indentation to run correctly
- **Defines code structure**: It indicates which code belongs to loops, functions, conditionals, etc.
- **Prevents errors**: Missing or inconsistent indentation will cause syntax errors

## Indentation Rules

### Correct Indentation

When using conditional statements like `if`, the code inside the block **must be indented**:

```python
if 5 > 2:
    print("Five is greater than two!")
```

✅ **This works perfectly!** The `print` statement is indented, showing it's part of the `if` block.

### Incorrect Indentation - Missing Indent

```python
# ❌ This will cause an error:
if 5 > 2:
print("Five is greater than two!")
```

**Error reason**: The `print` statement is not indented, so Python doesn't know it belongs to the `if` block.

### Flexible Indentation Amount

Python allows flexibility in the **number of spaces**, but you must be **consistent** within the same block:

```python
# Both of these are valid:
if 5 > 2:
    print("Two spaces work fine!")

if 5 > 2:
        print("Eight spaces also work!")
```

✅ **Both examples work** because each maintains consistent indentation within their block.

### Inconsistent Indentation - Error

```python
# ❌ This will cause an error:
if 5 > 2:
    print("Five is greater than two!") 
        print("This has different indentation!")
```

**Error reason**: The two print statements have **different indentation levels** within the same code block.

## Best Practices

1. **Use 4 spaces** per indentation level (Python standard)
2. **Be consistent** throughout your code
3. **Don't mix tabs and spaces** - choose one and stick with it
4. Most code editors can be configured to automatically use spaces when you press Tab

## Key Takeaway

> In Python, indentation is not optional or just for style - it's **part of the language syntax** and determines how your code executes.
