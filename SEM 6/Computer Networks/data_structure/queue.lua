-- Queue = {}

-- function Queue.is_empty(self)
--     return #self.data == 0
-- end

-- function Queue.enqueue(self, value)
--     self.data[#self.data + 1] = value
-- end

-- function Queue.dequeue(self)
--     if self:is_empty() then 
--         return nil, "queue is empty."
--     end
--     return table.remove(self.data, 1)
-- end

-- function Queue.front(self)
--     if self:is_empty() then 
--         return nil, "queue is empty."
--     end
--     return self.data[0]
-- end

-- function Queue.display(self)
--     if self:is_empty() then 
--         return nil
--     end
--     for i = 1, #self.data do
--         print(self.data[i])
--     end
-- end


-- function Queue.init()
--     local instance = {data = {}} -- Create a new table with `data`
--     setmetatable(instance, {__index = Queue}) -- Set Stack as the metatable
--     return instance
-- end


-- local queue = Queue:init()
-- queue:enqueue(1)
-- queue:enqueue(2)
-- queue:display()
-- queue:dequeue()
-- queue:display()



