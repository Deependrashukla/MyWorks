-- Define the maximum line length
local MAX_LINE = 1000

-- Function to reverse a string in place (Lua strings are immutable, so we use a table)
local function reverse(s)
    local chars = {}
    for i = 1, #s do
        chars[i] = s:sub(i, i)  -- Split the string into individual characters
    end

    -- Reverse the characters
    for i = 1, math.floor(#chars / 2) do
        local temp = chars[i]
        chars[i] = chars[#chars - i + 1]
        chars[#chars - i + 1] = temp
    end

    -- Rebuild the reversed string
    return table.concat(chars)
end

-- Function to read a line from input
local function get_line(limit)
    local s = io.read("*line")  -- Read a line from standard input
    if s then
        if #s > limit - 1 then
            s = s:sub(1, limit - 1)  -- Truncate if it exceeds the limit
        end
        return s .. "\n"  -- Append newline character
    else
        return ""  -- Return empty string on EOF
    end
end

-- Example usage
print("Enter a line of text:")
local line = get_line(MAX_LINE)
print("You entered:\n", line)

local reversed_line = reverse(line)
print("Reversed line:", reversed_line)
