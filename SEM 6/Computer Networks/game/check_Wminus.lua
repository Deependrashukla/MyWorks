local function check_Wminus(Wminus) -- check Wminus
   if ( not Wminus ) then return true end  -- degenerate case
   assert(type(Wminus) == "table")
   for k1, w1 in ipairs(Wminus) do
     assert(type(w1) == "string")
     --if word is in W, it can't be in H becuase bot of them are mutually exclusive.
     -- check that word is in play
     local found = false
     for i = 1, #game.W do
          if ( game.W[i] == w1) then
            found = true
            break
          end
        end
        assert(found)
    -- check that word is not in history
    local found = false
    for i = 1, #game.H do
        if ( game.H[i].word == w1) then
            found = true
            break
        end
    end
        assert(not found)
        -- check no duplicates
        for k2, w2 in ipairs(Wminus) do
          if ( k1 ~= k2 ) then assert(w1 ~= w2) end
        end
      end
      return true
    end











-- my codestarts from here ############

local function check_Wminus(Wminus)
    if (not Wminus) then 
        return true
    end
    assert(type(Wminus) == "table")
    for k1, w1 ipairs(Wminus) do
        -- ? will letter can't be word
        assert(type(w1) == "string")
        -- check that word is in play
        found = false
        for i=1, #game.W do
            if game.W[i] == w1 then
                found = true
                break
            end
        end
        assert(found)
        --  WHY CHECKING AGAIN AS W AND H IS MUTUALLY EXCLUSIVE/
        -- check that word is not in history
        for i=1, #game.H do 
            assert(game.H[i].word ~= w1)
        end
        -- check no duplicates
        for k2, w2 ipairs(Wminus) do
            if k1 ~= k2 then
                assert(w1 ~= w2)
            end
        end
        return true
    end 