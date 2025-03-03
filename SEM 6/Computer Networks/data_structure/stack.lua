Stack = {}


function Stack.is_empty(self)
    return #self.data == 0
end


-- Add an element to the stack
function Stack.push(self, value)
    self.data[#self.data + 1] = value
end


-- Remove and return the top element
function Stack.pop(self)
    if self:is_empty() then
        return nil, "stack is empty"
    end
    return table.remove(self.data)
end

-- Get the top element without removing it
function Stack.top(self)
    if self:is_empty() then
        return nil, "stack is empty"
    end
    return self.data[#self.data]
end

-- Display the current state of stack
function Stack.display(self)
    for i = 1, #self.data do 
        print(self.data[i])
    end
end

function Stack.init()
    local instance = {data = {}} -- Create a new table with `data`
    setmetatable(instance, {__index = Stack}) -- Set Stack as the metatable
    return instance
end




-- ############

local stack = Stack:init()
stack:push(10)
stack:push(20)
-- print(stack:pop())
-- print(stack:top())
stack:display()