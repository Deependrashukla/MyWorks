local function check_Pminus(Pminus) -- check Pminus
    if ( not Pminus) then  return true end -- degenerate case
    --=======================
    assert(type(Pminus) == "table")
    for k, v in pairs(Pminus) do
      assert(type(v) == "string")
      assert(#v == 1)
    end
    local newP = assert(subtract_from(Pminus, game.P))
    return true
  end
  --=============================================================
    -- check that Wplus contains words not created before
  local function check_Wplus(Wplus)
    assert(type(Wplus) == "table")
    for k1, w1 in ipairs(Wplus) do
      assert(type(w1) == "string")
      -- check that word exists in dictionary
      assert(game.D[w1])
      -- check that word has not been made before
      for i = 1, #game.H do
        assert(game.H[i].word ~= w1)
      end
      -- check that word is not in play (argue why this is not needed)
      for i = 1, #game.W do
        -- print("Found " .. w1 .. " at location ", i)
        assert(game.W[i] ~= w1)
      end
      -- check no duplicates
      for k2, w2 in ipairs(Wplus) do
        if ( k1 ~= k2 ) then assert(w1 ~= w2) end
      end
    end
    return true
  end


--   ####### Here is my codde

local function check_Pminus(Pminus)
    if (not Pminus) then 
        return true
    end
    assert(type(Pminus) == "table")
    for k, v in ipairs(Pminus) do
        assert(type(v) == "string")
        assert(#v == 1)
    end
    --  No need to store it in newp?
    local newP = assert(subtract_from(Pminus, gmae.P))
    return true
end



